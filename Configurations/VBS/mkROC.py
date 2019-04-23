#!/usr/bin/env python

import sys
from math import *
from collections import namedtuple
import ROOT
import cuts
import variables
import samples
import plot

#structures
curves = namedtuple('curves', ['nvar', 'roc', 'signif', 'signif_cut'], verbose=True)
multicurves2 = namedtuple('multicurves2', ['roc', 'signif'], verbose=True)

#structure creation
def create_graphs (number):
    return curves(number, ROOT.TGraph(), ROOT.TGraph(), ROOT.TGraph())

#canva creation
def create_canva (name):
    return ROOT.TCanvas('{}'.format(name), "", 100, 200, 700, 500)

#ROC and Significance curves builder
#it creates one ROC, one Signif and Signif_cut as many as len(sig) i.e. number of variables
def mk_RS (sig, bkg, bname):
    #colour series
    colours = [ROOT.kBlue+2, ROOT.kRed+1, ROOT.kGreen+2, ROOT.kPink, ROOT.kOrange+1, \
            ROOT.kSpring-8, ROOT.kAzure+1, ROOT.kViolet-5, ROOT.kCyan-1, ROOT.kYellow-2, \
                ROOT.kYellow+4, ROOT.kRed-9, ROOT.kCyan-6, ROOT.kOrange-5, ROOT.kOrange]
    if len(sig) > len(colours):
        for c in range(0, len(sig)-len(colours)):
            colours.append(880-20*c)
    
    mymulticurves2 = multicurves2(ROOT.TMultiGraph(), ROOT.TMultiGraph())
    mycurves = []
    for i in range(0, len(sig)):
        mycurves.append(create_graphs(i))
    for curve in mycurves:
        Nbin = sig[curve.nvar].GetNbinsX() #sig histo bin = bkg histo bin
        sTot = sig[curve.nvar].Integral()
        bTot = bkg[curve.nvar].Integral()
        for bi in range(1, Nbin+1): #1 = 1st bin index, Nbin = last bin index
            try:
                ind = sys.argv.index('--right')
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
        mymulticurves2.roc.Add(curve.roc)
        mymulticurves2.signif.Add(curve.signif)
        canva = create_canva('Signif_{}_{}'.format(bname,variables.variables.keys()[curve.nvar]))
        canva.cd()
        try:
            ind = sys.argv.index('--line')
            curve.signif_cut.Draw('APL')
        except:
            curve.signif_cut.Draw('AP')
        canva.SaveAs('Signif_{}_{}.png'.format(bname,variables.variables.keys()[curve.nvar]))
    canvaRoc = create_canva('ROC_{}'.format(bname))
    canvaRoc.cd()
    try:
        ind = sys.argv.index('--line')
        mymulticurves2.roc.Draw('APL')
    except:
        mymulticurves2.roc.Draw('AP')
    canvaRoc.SaveAs('ROC_{}.png'.format(bname))
    canvaSignif = create_canva('Signif_{}'.format(bname))
    canvaSignif.cd()
    try:
        ind = sys.argv.index('--line')
        mymulticurves2.signif.Draw('APL')
    except:
        mymulticurves2.signif.Draw('AP')
    canvaSignif.SaveAs('Signif_{}.png'.format(bname))
        

#signal and background list of histograms creator
def create_histo_list_RS(rootfile, signame, bkgnames):
    
    file_in = ROOT.TFile(rootfile)
    ROOT.gDirectory.cd('signals')
    hsig = []
    for vn in variables.variables.keys():
        hsig.append(ROOT.gDirectory.Get('{}_{}'.format(signame, vn)))

    if os.path.exists('RS_curves') == False:
        os.makedir('RS_curves/')    
    i = 0
    hbkg = []
    for bn in bkgnames:
        if i == 0:
            ROOT.gDirectory.cd('../backgrounds/'+bn)
        else:
            ROOT.gDirectory.cd('../'+bn)
        for vn in variables.variables.keys():
            hbkg.append(ROOT.gDirectory.Get('{}_{}'.format(bn, vn)))
        mk_RS(hsig, hbkg, bkgnames[i]) #creation of ROC and Significance curves
        del hbkg[:]
        i += 1

samples_sig_keys = []
samples_bkg_keys = []
bkg_names = []

for gk in plot.groupPlot.keys():
    if plot.groupPlot[gk]['isSignal'] == 0:
        samples_bkg_keys.append(plot.groupPlot[gk]['samples'])
        bkg_names.append(plot.groupPlot[gk]['nameHR'])
    elif plot.groupPlot[gk]['isSignal'] == 1:
        sig_name = plot.groupPlot[gk]['nameHR']
        for j in plot.groupPlot[gk]['samples']:
            samples_sig_keys.append(j)

output_name = 'signals_backgrounds.root' #default name
for argument in sys.argv:
    try:
        if argument[:13] == '--outputFile=' and argument[(len(argument)-5):] == '.root':
            output_name = argument[13:]
    except Exception:
        pass

try:
    ind = sys.argv.index('--mode=buildTFile')
    print '''
   ----------------------------------------------------------------------------
           __       ______   _____
           __ \       _   |     _ |       \  |         |
          |__\ |    |   | |   |          |\/ |   _` |  |  /   _ \   __|
           ___ \    | _ | |   | _        |   |  (   |    <    __/  |
         _|   \_\  _______|  _____|     _|  _| \__,_| _|\_\ \___| _| 

   ----------------------------------------------------------------------------
    '''

    sig_chain = ROOT.TChain('latino')
    for s in samples_sig_keys:
        name = samples.samples[s]['name']
        for n in name:
            sig_chain.Add(n[3:])

    bkg_chain = []        
    for i in range(0, len(samples_bkg_keys)):
        bkg_chain.append(ROOT.TChain('latino'))
        for b in samples_bkg_keys[i]:
            name = samples.samples[b]['name']
            for n in name:
                bkg_chain[i].Add(n[3:])
    
    F = ROOT.TFile (output_name, 'RECREATE')
    F.mkdir('signals')
    F.mkdir('backgrounds')
    ROOT.gDirectory.cd('signals')

    var_names = variables.variables.keys()
    
    count = 0
    for vk in var_names:
        var_name = var_names[count]
        sig_chain.Draw(variables.variables[vk]['name']+'>>{}_{}'.format(sig_name,var_name), cuts.supercut)
        if count+1 == 1:
            ap = 'st'
        elif count+1 == 2:
            ap = 'nd'
        elif count+1 == 3:
            ap = 'rd'
        else:
            ap = 'th'
        h_sig = ROOT.gDirectory.Get('{}_{}'.format(sig_name,var_name))
        h_sig.Write()
        print count+1, ap+' signal histogram saved in TFile'
        count += 1

    ROOT.gDirectory.cd('../backgrounds')

    n_count = 0
    for c in bkg_chain: #it could be slow if the number of background entries is large
        count = 0
        if n_count == 0:
            ROOT.gDirectory.mkdir(bkg_names[n_count])
            ROOT.gDirectory.cd(bkg_names[n_count])
        else:
            ROOT.gDirectory.cd("..")
            ROOT.gDirectory.mkdir(bkg_names[n_count])
            ROOT.gDirectory.cd(bkg_names[n_count])
        for vk in var_names:
            var_name = var_names[count]
            c.Draw(variables.variables[vk]['name']+'>>{}_{}'.format(bkg_names[n_count],var_name), cuts.supercut)
            number = len(var_names)*n_count+count+1
            if number == 1:
                ap = 'st'
            elif number == 2:
                ap = 'nd'
            elif number == 3:
                ap = 'rd'
            else:
                ap = 'th'
            h_bkg = ROOT.gDirectory.Get('{}_{}'.format(bkg_names[n_count],var_name))
            h_bkg.Write()
            print number, ap+' background histogram saved in TFile'
            count += 1
        n_count += 1

    F.Close()
except:
    try:
        ind = sys.argv.index('--mode=drawCurves')
        print '''
   ----------------------------------------------------------------------------
           __       ______   _____
           __ \       _   |     _ |       \  |         |
          |__\ |    |   | |   |          |\/ |   _` |  |  /   _ \   __|
           ___ \    | _ | |   | _        |   |  (   |    <    __/  |
         _|   \_\  _______|  _____|     _|  _| \__,_| _|\_\ \___| _| 

   ----------------------------------------------------------------------------
        '''

        create_histo_list_RS(output_name, sig_name, bkg_names) 

    except:
        print '''
    *************************************************************************
    *************************************************************************

    ERROR: choose an option beetween --mode=buildTFile and --mode=drawCurves

    *************************************************************************
    *************************************************************************
        '''

try:
    ind = sys.argv.index('--mode=buildTFile')
    print '''

    *************************************************************************
    *************************************************************************
    
    Signals and backgrounds histograms are saved in {}
    
    *************************************************************************
    *************************************************************************
    '''.format(output_name)
except:
    try:
        ind = sys.argv.index('--mode=drawCurves')
        print '''
        
    *************************************************************************
    *************************************************************************
    
        '''

        try:
            ind = sys.argv.index('--expanded')
            print '''
            Significance calculated by means of expanded formula:
                Z0 = sqrt{2*[(s+b)*ln(1+s/b)-s]}
            '''
        except:
            print '''
            Significance calculated by means of approximate formula:
                Z0 = s/sqrt(b)
            '''
            
        try:
            ind = sys.argv.index('--right')
            print '''
            Values to the RIGHT of the cut are REJECTED
            '''
        except:
            print '''
            Values to the LEFT of the cut are REJECTED
            '''
            
        try:
            ind_line = sys.argv.index('--line')
            print '''
            Points are connected with a line
            '''
        except Exception:
            pass

    except Exception:
        pass
    
        