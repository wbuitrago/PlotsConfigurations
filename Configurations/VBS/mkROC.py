#!/usr/bin/env python

import sys
import os
from math import *
from collections import namedtuple
import ROOT

variables = {}
print opt.variablesFile
if os.path.exists(opt.variablesFile) :
    handle = open(opt.variablesFile,'r')
    exec(handle)
    handle.close()
    #in case some variables need a compiled function
    for variableName, variable in variables.iteritems():
        if variable.has_key('linesToAdd'):
            linesToAdd = variable['linesToAdd']
            for line in linesToAdd:
                ROOT.gROOT.ProcessLineSync(line)
samples = {}
if os.path.exists(opt.samplesFile) :
    handle = open(opt.samplesFile,'r')
    exec(handle)
    handle.close()
    #in case some samples need a compiled function
    for sampleName, sample in samples.iteritems():
        if sample.has_key('linesToAdd'):
            linesToAdd = sample['linesToAdd']
            for line in linesToAdd:
                ROOT.gROOT.ProcessLineSync(line)

cuts = {}
if os.path.exists(opt.cutsFile) :
    handle = open(opt.cutsFile,'r')
    exec(handle)
    handle.close()

groupPlot = OrderedDict()
plot = {}
legend = {}
if os.path.exists(opt.plotFile) :
    handle = open(opt.plotFile,'r')
    exec(handle)
    handle.close()

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
                if variables.variables[variables.variables.keys()[curve.nvar]]['SignalOnRight'] == 1:
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
                try:
                    ind == sys.argv.index('--expanded')
                    Z = sqrt(2*((s+b)*log(1+float(s)/b)-s))
                except:
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
        curve.signif.SetMarkerStyle(20)
        curve.signif_cut.SetMarkerStyle(20)
        mymulticurves.roc.Add(curve.roc)
        mymulticurves.roc_leg.AddEntry(curve.roc, variables.variables.keys()[curve.nvar], 'LP')
        mymulticurves.signif.Add(curve.signif)
        mymulticurves.signif_leg.AddEntry(curve.signif, variables.variables.keys()[curve.nvar], 'LP')
        curve.signif_cut.GetXaxis().SetTitle(variables.variables.keys()[curve.nvar])
        curve.signif_cut.GetXaxis().SetTitleSize(0.05)
        curve.signif_cut.GetXaxis().SetTitleOffset(0.85)
        curve.signif_cut.GetYaxis().SetTitle('Z_{0}')
        curve.signif_cut.GetYaxis().SetTitleSize(0.05)
        curve.signif_cut.GetYaxis().SetTitleOffset(0.9)
        canva = create_canva('Signif_{}_{}'.format(bname,variables.variables[variables.variables.keys()[curve.nvar]]['xaxis']))
        canva.cd()
        try:
            ind = sys.argv.index('--line')
            curve.signif_cut.Draw('APL')
        except:
            curve.signif_cut.Draw('AP')
        try:
            ind = sys.argv.index('--grid')
            canva.SetGrid()
        except Exception:
            pass
        canva.SaveAs('RS_curves/Signif_{}_{}.png'.format(bname,variables.variables.keys()[curve.nvar]))
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
    try:
        ind = sys.argv.index('--line')
        mymulticurves.roc.Draw('APL')
    except:
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
    try:
        ind = sys.argv.index('--grid')
        canvaRoc.SetGrid()
    except Exception:
        pass
    canvaRoc.Modified()
    canvaRoc.Update()
    canvaRoc.SaveAs('RS_curves/ROC_{}.png'.format(bname))
    canvaSignif = create_canva('Signif_{}'.format(bname))
    canvaSignif.cd()
    try:
        ind = sys.argv.index('--line')
        mymulticurves.signif.Draw('APL')
    except:
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
    try:
        ind = sys.argv.index('--grid')
        canvaSignif.SetGrid()
    except Exception:
        pass
    canvaSignif.Modified()
    canvaSignif.Update()
    canvaSignif.SaveAs('RS_curves/Signif_{}.png'.format(bname))
        
isInput = False
for arg in sys.argv:
    if arg[:12] == '--inputFile=' and arg[(len(arg)-5):] == '.root':
        inputFile = arg[12:]
        isInput = True
if isInput == True:
    print '''
-------------------------------------------------------------------------------
     __       ______   _____
     __ \       _   |     _ |       \  |         |
    |__\ |    |   | |   |          |\/ |   _` |  |  /   _ \   __|
     ___ \    | _ | |   | _        |   |  (   |    <    __/  |
   _|   \_\  _______|  _____|     _|  _| \__,_| _|\_\ \___| _| 

-------------------------------------------------------------------------------
    '''    
    print ' --> Histograms used to generate curves are in', inputFile
    try:
        ind = sys.argv.index('--expanded')
        print '''
        * Significance calculated by means of expanded formula:
                ____________________________________
               |                                    |
               |  Z0 = sqrt{2*[(s+b)*ln(1+s/b)-s]}  |
               |____________________________________|
        '''
    except:
        print '''
        * Significance calculated by means of approximate formula:
                        ___________________
                       |                   |
                       |   Z0 = s/sqrt(b)  |
                       |___________________|
             
         - Use the option --expanded if you want Z0 calculated
           by means of expanded formula
        '''
    try:
        ind = sys.argv.index('--grid')
        print '''
        * Grid is drawn on canvas
        '''
    except Exception:
        pass
                        
    try:
        ind_line = sys.argv.index('--line')
        print '''
        * Points are connected with a line
        '''
    except Exception:
        pass
    
    samples_sig_keys = []
    samples_bkg_keys = []
    bkg_names = []
    for gk in plot.groupPlot.keys():
        if plot.groupPlot[gk]['isSignal'] == 0:
            samples_bkg_keys.append(plot.groupPlot[gk]['samples'])
            bkg_names.append(gk)
        elif plot.groupPlot[gk]['isSignal'] == 1:
            sig_name = gk
            for j in plot.groupPlot[gk]['samples']:
                samples_sig_keys.append(j)
    
    histos_sig = []
    histo_file = ROOT.TFile(inputFile)
    cut = cuts.cuts.keys()[0] #default
    for ck in cuts.cuts.keys():
        if cuts.cuts[ck] == '1': #only supercut
            cut = ck
    ROOT.gDirectory.cd(cut)
    nv = 0
    for vk in variables.variables.keys():
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
        for vk in variables.variables.keys():
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

else:
    print '''
  *************************************************************************
  *************************************************************************
    
      ERROR: insert the path where rootFile produced by
               mkShapes is saved (as an option of mkROC.py)
               
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
      Example: mkROC.py --inputFile=rootFile_test/plots_VBS_SS_test.root
        
  *************************************************************************    
  *************************************************************************
    '''