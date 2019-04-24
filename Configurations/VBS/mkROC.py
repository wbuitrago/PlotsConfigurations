#!/usr/bin/env python

import sys
argv = sys.argv
sys.argv = argv[:1]
import os
import os.path
import optparse
import logging
from array import array
from math import *
from collections import namedtuple
from collections import OrderedDict
import ROOT
import LatinoAnalysis.Gardener.hwwtools as hwwtools

#structures
curves = namedtuple('curves', ['nvar', 'roc', 'signif', 'signif_cut'], verbose=True)
multicurves = namedtuple('multicurves', ['roc', 'signif', 'roc_leg', 'signif_leg'], verbose=True)

#structure creation
def create_graphs (number):
    return curves(number, ROOT.TGraph(), ROOT.TGraph(), ROOT.TGraph())

#canva creation
def create_canva (name):
    return ROOT.TCanvas('{}'.format(name), "", 100, 200, 700, 500)

#ROC and Significance curves creator
#it creates one ROC, one Signif and Signif_cut as many as len(sig) i.e. number of variables
def mk_RS (sig, bkg, bname):
    #colour series
    colours = [ROOT.kBlue+2, ROOT.kRed+1, ROOT.kGreen+2, ROOT.kPink, ROOT.kOrange+1, \
            ROOT.kSpring-8, ROOT.kAzure+1, ROOT.kViolet-5, ROOT.kCyan-1, ROOT.kYellow-2, \
                ROOT.kYellow+4, ROOT.kRed-9, ROOT.kCyan-6, ROOT.kOrange-5, ROOT.kOrange]
    if len(sig) > len(colours):
        for c in range(0, len(sig)-len(colours)):
            colours.append(880-20*c)
    
    mymulticurves = multicurves(ROOT.TMultiGraph(), ROOT.TMultiGraph(), \
        ROOT.TLegend(0.1,0.5,0.4,0.9), ROOT.TLegend(0.1,0.5,0.4,0.9))
    mymulticurves.roc.SetTitle(' ; #varepsilon_{bkg}; #varepsilon_{sig}')
    mymulticurves.signif.SetTitle(' ; #varepsilon_{sig}; Z_{0}')
    mycurves = []
    for i in range(0, len(sig)):
        mycurves.append(create_graphs(i))
    for curve in mycurves:
        Nbin = sig[curve.nvar].GetNbinsX() #sig histo bin = bkg histo bin
        sTot = sig[curve.nvar].Integral()
        bTot = bkg[curve.nvar].Integral()
        for bi in range(1, Nbin+1): #1 = 1st bin index, Nbin = last bin index
            try:
                if variables[variables.keys()[curve.nvar]]['SignalOnRight'] == 1:
                    s = sig[curve.nvar].Integral(bi,Nbin)
                    b = bkg[curve.nvar].Integral(bi,Nbin)
                else:
                    s = sig[curve.nvar].Integral(1,bi)
                    b = bkg[curve.nvar].Integral(1,bi)
            except:
                s = sig[curve.nvar].Integral(bi,Nbin)
                b = bkg[curve.nvar].Integral(bi,Nbin)
            eff_s = float(s)/sTot
            eff_b = float(b)/bTot
            try: #in order to avoid ZeroDivisionError
                if opt.expanded == 1:
                    Z = sqrt(2*((s+b)*log(1+float(s)/b)-s))
                else:
                    Z = float(s)/sqrt(b)
                curve.roc.SetPoint(bi-1,eff_b,eff_s)
                curve.signif.SetPoint(bi-1,eff_s,Z)
                curve.signif_cut.SetPoint(bi-1,sig[curve.nvar].GetBinCenter(bi),Z)
            except Exception:
                pass
        curve.roc.SetMarkerColor(colours[curve.nvar])
        curve.signif.SetMarkerColor(colours[curve.nvar])
        curve.signif_cut.SetMarkerColor(colours[curve.nvar])
        curve.roc.SetMarkerStyle(20)
        curve.roc.SetMarkerSize(opt.markerSize)
        curve.signif.SetMarkerStyle(20)
        curve.signif.SetMarkerSize(opt.markerSize)
        curve.signif_cut.SetMarkerStyle(20)
        curve.signif_cut.SetMarkerSize(opt.markerSize)
        mymulticurves.roc.Add(curve.roc)
        mymulticurves.roc_leg.AddEntry(curve.roc, variables.keys()[curve.nvar], 'LP')
        mymulticurves.signif.Add(curve.signif)
        mymulticurves.signif_leg.AddEntry(curve.signif, variables.keys()[curve.nvar], 'LP')
        curve.signif_cut.GetXaxis().SetTitle(variables.keys()[curve.nvar])
        curve.signif_cut.GetXaxis().SetTitleSize(0.05)
        curve.signif_cut.GetXaxis().SetTitleOffset(0.85)
        curve.signif_cut.GetYaxis().SetTitle('Z_{0}')
        curve.signif_cut.GetYaxis().SetTitleSize(0.05)
        curve.signif_cut.GetYaxis().SetTitleOffset(0.9)
        canva = create_canva('Signif_{}_{}'.format(bname,variables[variables.keys()[curve.nvar]]['xaxis']))
        canva.cd()
        if opt.line == 1:
            curve.signif_cut.Draw('APL')
        else:
            curve.signif_cut.Draw('AP')
        if opt.grid == 1:
            canva.SetGrid()
        canva.SaveAs('RS_curves/Signif_{}_{}.png'.format(bname,variables.keys()[curve.nvar]))
        canva.SaveAs('RS_curves/Signif_{}_{}.root'.format(bname,variables.keys()[curve.nvar]))
    canvaRoc = create_canva('ROC_{}'.format(bname))
    bisector = ROOT.TLine(0,0,1,1)
    bisector.SetLineColor(ROOT.kBlack)
    bisector.SetLineStyle(7)
    #bisector.SetLineWidth(2)
    p1 = ROOT.TGraph()
    p1.SetPoint(0,0,0)
    p2 = ROOT.TGraph()
    p2.SetPoint(0,1,1)
    mymulticurves.roc.Add(p1)
    mymulticurves.roc.Add(p2)
    canvaRoc.cd()
    if opt.line == 1:
        mymulticurves.roc.Draw('APL')
    else:
        mymulticurves.roc.Draw('AP')
    mymulticurves.roc_leg.SetNColumns(2)
    mymulticurves.roc_leg.SetLineColorAlpha(0,0)
    mymulticurves.roc_leg.SetFillColorAlpha(0,0)
    mymulticurves.roc_leg.SetTextSize(0.06)
    mymulticurves.roc_leg.Draw('SAME')
    bisector.Draw('L SAME')
    mymulticurves.roc.GetXaxis().SetLabelSize(0.045)
    mymulticurves.roc.GetXaxis().SetTitleSize(0.055)
    mymulticurves.roc.GetXaxis().SetTitleOffset(0.8)
    mymulticurves.roc.GetYaxis().SetLabelSize(0.045)
    mymulticurves.roc.GetYaxis().SetTitleSize(0.055)
    mymulticurves.roc.GetYaxis().SetTitleOffset(0.8)
    if opt.grid == 1:
        canvaRoc.SetGrid()
    canvaRoc.Modified()
    canvaRoc.Update()
    canvaRoc.SaveAs('RS_curves/ROC_{}.png'.format(bname))
    canvaRoc.SaveAs('RS_curves/ROC_{}.root'.format(bname))
    canvaSignif = create_canva('Signif_{}'.format(bname))
    canvaSignif.cd()
    if opt.line == 1:
        mymulticurves.signif.Draw('APL')
    else:
        mymulticurves.signif.Draw('AP')
    mymulticurves.signif_leg.SetNColumns(2)
    mymulticurves.signif_leg.SetLineColorAlpha(0,0)
    mymulticurves.signif_leg.SetFillColorAlpha(0,0)
    mymulticurves.signif_leg.SetTextSize(0.06)
    mymulticurves.signif_leg.Draw('SAME')
    mymulticurves.signif.GetXaxis().SetLabelSize(0.045)
    mymulticurves.signif.GetXaxis().SetTitleSize(0.055)
    mymulticurves.signif.GetXaxis().SetTitleOffset(0.8)
    mymulticurves.signif.GetYaxis().SetLabelSize(0.045)
    mymulticurves.signif.GetYaxis().SetTitleSize(0.055)
    mymulticurves.signif.GetYaxis().SetTitleOffset(0.8)
    if opt.grid == 1:
        canvaSignif.SetGrid()
    canvaSignif.Modified()
    canvaSignif.Update()
    canvaSignif.SaveAs('RS_curves/Signif_{}.png'.format(bname))
    canvaSignif.SaveAs('RS_curves/Signif_{}.root'.format(bname))



if __name__ == '__main__':
    
    sys.argv = argv
    
    print '''
-------------------------------------------------------------------------------
     __       ______   _____
     __ \       _   |     _ |       \  |         |
    |__\ |    |   | |   |          |\/ |   _` |  |  /   _ \   __|
     ___ \    | _ | |   | _        |   |  (   |    <    __/  |
   _|   \_\  _______|  _____|     _|  _| \__,_| _|\_\ \___| _| 

-------------------------------------------------------------------------------
    ''' 

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFile' , dest='inputFile'  , help='input file with histograms'                             , default='input.root')
    parser.add_option('--line'      , dest='line'       , help='connects points with a line'                            , default=0 , type=float)
    parser.add_option('--grid'      , dest='grid'       , help='draws grid on canva'                                    , default=0 , type=float)
    parser.add_option('--expanded'  , dest='expanded'   , help='significance calculated by means of expanded formula'   , default=0 , type=float)
    parser.add_option('--markerSize', dest='markerSize' , help='set marker size'                                        , default=1., type=float)

    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()
    
    ROOT.gROOT.SetBatch()
    
    
    print '          configuration file =', opt.pycfg
    print '                  input file =', opt.inputFile
    if opt.expanded == 1:
        print '''
            Significance calculated by means of expanded formula:
                 ____________________________________
                |                                    |
                |  Z0 = sqrt{2*[(s+b)*ln(1+s/b)-s]}  |
                |____________________________________|
            '''
    else:
        print '''
            Significance calculated by means of approximate formula:
                         ___________________
                        |                   |
                        |   Z0 = s/sqrt(b)  |
                        |___________________|
        '''
    if opt.grid == 1:
        print '''
    - grid is drawn on canvas'''
    if opt.line == 1:
        print '''
    - points are connected with a line'''
    
    print '''
    '''

    if opt.inputFile[(len(opt.inputFile)-5):] != '.root':
        print '''
    *************************************************************************
    *************************************************************************
        
        ERROR: insert the path where rootFile produced by
                mkShapes is saved (as an option of mkROC.py)
            
    *************************************************************************    
    *************************************************************************
        '''

    samples = OrderedDict()
    if os.path.exists(opt.samplesFile):
        handle = open(opt.samplesFile,'r')
        exec(handle)
        handle.close()
   
    cuts = {}
    if os.path.exists(opt.cutsFile):
        handle = open(opt.cutsFile,'r')
        exec(handle)
        handle.close()

    variables = {}
    if os.path.exists(opt.variablesFile):
        handle = open(opt.variablesFile,'r')
        exec(handle)
        handle.close()
        
    groupPlot = OrderedDict()
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile):
        handle = open(opt.plotFile,'r')
        exec(handle)
        handle.close()

        
    samples_sig_keys = []
    samples_bkg_keys = []
    bkg_names = []
    for gk in groupPlot.keys():
        if groupPlot[gk]['isSignal'] == 0:
            samples_bkg_keys.append(groupPlot[gk]['samples'])
            bkg_names.append(gk)
        elif groupPlot[gk]['isSignal'] == 1:
            sig_name = gk
            for j in groupPlot[gk]['samples']:
                samples_sig_keys.append(j)
        
    histos_sig = []
    histo_file = ROOT.TFile(opt.inputFile)
    cut = cuts.keys()[0] #default
    for ck in cuts.keys():
        if cuts[ck] == '1': #only supercut
            cut = ck
    ROOT.gDirectory.cd(cut)
    nv = 0
    for vk in variables.keys():
        if nv == 0:
            ROOT.gDirectory.cd(vk)
        else:
            ROOT.gDirectory.cd('../'+vk)
        hs = ROOT.gDirectory.Get('histo_'+samples_sig_keys[0])
        for sn in range(1, len(samples_sig_keys)):
            hs.Add(ROOT.gDirectory.Get('histo_'+samples_sig_keys[sn]))
        hs.SetName(sig_name+'_'+vk)
        hs.SetTitle(sig_name+'_'+vk)
        histos_sig.append(hs)
        nv += 1
    ROOT.gDirectory.cd('..')
    histos_bkg = []
    for nbkg in range(0,len(samples_bkg_keys)):
        nv = 0
        for vk in variables.keys():
            if nv == 0:
                ROOT.gDirectory.cd(vk)
            else:
                ROOT.gDirectory.cd('../'+vk)
            hb = ROOT.gDirectory.Get('histo_'+samples_bkg_keys[nbkg][0])
            for bn in range(1, len(samples_bkg_keys[nbkg])):
                hb.Add(ROOT.gDirectory.Get('histo_'+samples_bkg_keys[nbkg][bn]))
            hb.SetName(bkg_names[nbkg]+'_'+vk)
            hb.SetTitle(bkg_names[nbkg]+'_'+vk)
            histos_bkg.append(hb)
            nv += 1
        mk_RS(histos_sig, histos_bkg, bkg_names[nbkg]) #creation of ROC and Significance curves
        del histos_bkg[:]
        ROOT.gDirectory.cd('..')
    histo_file.Close()
    if os.path.exists('RS_curves') == False:
        os.makedirs('RS_curves/')
    
    print '... and now closing ...'
        