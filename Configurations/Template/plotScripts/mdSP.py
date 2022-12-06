#!/usr/bin/env python

import re
from sys import argv
import os.path
from optparse import OptionParser
from math import sqrt,fabs
from collections import OrderedDict
import CMS_lumi, tdrstyle


tdrstyle.setTDRStyle()


parser = OptionParser()
parser.add_option("-s", "--stat",   dest="stat",          default=False, action="store_true")  # ignore systematic uncertainties to consider statistical uncertainties only
parser.add_option("-v", "--verbose",   dest="verbose",          default=False, action="store_true")
#parser.add_option("-S", "--force-shape", dest="shape",    default=False, action="store_true")  # ignore systematic uncertainties to consider statistical uncertainties only
#parser.add_option("-a", "--asimov", dest="asimov",  default=False, action="store_true")
#parser.add_option("-m", "--mass", dest="mass",  default=125, type="float")
#from DatacardParser import *

parser.add_option("--plotFile",   dest="plotFile",          default="" )

(options, args) = parser.parse_args()
options.bin = True # fake that is a binary output, so that we parse shape lines
options.noJMax = False
options.nuisancesToExclude = ''


plot = {}
legend = {}
if os.path.exists(options.plotFile) :
   handle = open(options.plotFile,'r')
   exec(handle)
   handle.close()


import ROOT
#ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")

from HiggsAnalysis.CombinedLimit.DatacardParser import *


DC = parseCard(file(args[0]), options)

signals     = DC.list_of_signals()
signals = [i for i in signals if i != "VBS_qcd"]

#if "H_htt"  in signals: signals.remove("H_htt")
#if "ggH_htt" in signals: signals.remove("ggH_htt")
#if "qqH_htt" in signals: signals.remove("qqH_htt")
#if "WH_htt" in signals: signals.remove("WH_htt")
#if "ZH_htt" in signals: signals.remove("ZH_htt")

#combChannels = ['0 jet ggH-tagged','1 jet ggH-tagged','2 jet ggH-tagged','2 jet VBF-tagged','2 jet VH-tagged']
#combChannels = ['4-lepton ZH-tagged','3-lepton WH-tagged','2-jet VH-tagged','2-jet VBF-tagged high mjj','2-jet VBF-tagged low mjj','2-jet VBF-tagged','2-jet ggH-tagged','1-jet SF ggH-tagged','1-jet ggH-tagged','0-jet SF ggH-tagged','0-jet ggH-tagged']

combChannels = ['WVlnujj','OS','SS','WZ','ZZ','ZZ2l2nu','ZV']
overallSignalRate = OrderedDict()
overallTotalSignal = OrderedDict()

for c in combChannels:
  overallSignalRate[c] = OrderedDict() 
  overallSignalRate[c]['ewk_SSWW'] = 0.
  overallSignalRate[c]['ewk_OSWW'] = 0.
  overallSignalRate[c]['ewk_WZ'] = 0.
  overallSignalRate[c]['ewk_ZZ'] = 0.

  overallTotalSignal[c] = 0.

splitVBF=False

print(overallSignalRate)
for channel in DC.exp:

  print " channel = ", channel

  #if 'of0j' in channel: c='0-jet ggH-tagged'
  #elif 'of_0j' in channel: c='0-jet ggH-tagged' 
  #elif 'of1j' in channel: c='1-jet ggH-tagged'
  #elif 'of_1j' in channel: c='1-jet ggH-tagged'
  #elif 'of2j' in channel and not ('vbf' in channel or 'vh' in channel): c='2-jet ggH-tagged'
  #elif 'of_2j' in channel and not ('vbf' in channel or 'vh' in channel): c='2-jet ggH-tagged'
  #elif 'vbf' in channel:
  #  if splitVBF:
  #    if 'lowmjj'  in channel: c='2-jet VBF-tagged low mjj'
  #    elif 'highmjj'  in channel: c='2-jet VBF-tagged high mjj'
  #  else:
  #    c='2-jet VBF-tagged'
  #elif 'vh' in channel: c='2-jet VH-tagged'
  #elif 'sf0j' in channel: c='0-jet SF ggH-tagged'
  #elif 'sf1j' in channel: c='1-jet SF ggH-tagged'
  #elif 'wh3l' in channel: c='3-lepton WH-tagged'
  #elif 'zh4l' in channel: c='4-lepton ZH-tagged'
  #else:
  #  print "UNKNOWN CHANNEL"
  #  break 
  if 'WVlnujj' in channel: c='WVlnujj'
  elif 'OS' in channel: c = "OS"
  elif "SS_WZ" in channel: c = channel
  elif "ZZ" in channel and "ZZ2l2nu" not in channel: c = "ZZ"
  elif "ZZ2l2nu" in channel: 
     c = "ZZ2l2nu"
     print(c, channel)
  elif "ZV" in channel: c = "ZV"
  #else:
  #   print "channel {} not found, continue".format(channel)
  #   continue
  print("--> new channel " +c ) 
  for s in signals :
    if s in DC.exp[channel].keys(): # possible that some backgrounds/signals appear only in some channels
      if s == 'ggH_htt':
        overallSignalRate[c]['ggH_hww'] +=  DC.exp[channel][s]
      elif s == 'qqH_htt':
        overallSignalRate[c]['qqH_hww'] +=  DC.exp[channel][s]
      elif s == 'WH_htt':
        overallSignalRate[c]['WH_hww'] +=  DC.exp[channel][s]
      elif s == 'ZH_htt':
        overallSignalRate[c]['ZH_hww'] +=  DC.exp[channel][s]
      elif s == 'ggZH_hww': # put ggZH together with ZH
        overallSignalRate[c]['ZH_hww'] +=  DC.exp[channel][s]
      else:
        if "SS_WZ" in c:
           if s == "ewk_WW_SS"  : 
              overallSignalRate["SS"]["ewk_SSWW"] +=  DC.exp[channel][s] 
              overallTotalSignal["SS"] += DC.exp[channel][s]
           if s == "ewk_WZ"     : 
              overallSignalRate["WZ"]["ewk_WZ"] +=  DC.exp[channel][s] 
              overallTotalSignal["WZ"] += DC.exp[channel][s]
        
        else:
           if s == "ewk_WpWp" or s == "ewk_WmWm": overallSignalRate[c]["ewk_SSWW"] +=  DC.exp[channel][s] 
           if s == "ewk_WpWm": overallSignalRate[c]["ewk_OSWW"] +=  DC.exp[channel][s]
           if s == "ewk_WpZ" or s == "ewk_WmZ": overallSignalRate[c]["ewk_WZ"] +=  DC.exp[channel][s]
           if s == "ewk_ZZ": overallSignalRate[c]["ewk_ZZ"] +=  DC.exp[channel][s]
           
           #overallSignalRate[c][s] +=  DC.exp[channel][s]
           overallTotalSignal[c] += DC.exp[channel][s]
        
        if c == "ZZ2l2nu": print("ZZ2l2nu ", DC.exp[channel][s])

stack = ROOT.THStack()
histos = {}
leg = ROOT.TLegend(0.82,0.45,0.99,0.8)
color = 0.

ncat=0
combChannelsToConsider = []
for k in combChannels:
  if overallTotalSignal[k] == 0: continue
  ncat+=1
  combChannelsToConsider.append(k)
  print k

print("combChannels: " , combChannels)

for s in ["ewk_SSWW", "ewk_OSWW", "ewk_WZ", "ewk_ZZ"]:
  histos[s] = ROOT.TH1F(s,s,ncat,0,ncat)

frame = histos['ewk_SSWW'].Clone()
frame.GetYaxis().SetRangeUser(0,1)
frame.GetYaxis().SetTitle("Signal fraction")
frame.GetXaxis().SetLabelSize(0.05)
frame.GetYaxis().SetLabelSize(0.05)
frame.GetYaxis().SetTitleSize(0.05)
frame.GetYaxis().SetTitleOffset(1.1)
frame.SetTitle("")
frame.SetStats(0)

events = {}

for i,c in enumerate(combChannelsToConsider):
#  if overallTotalSignal[c] == 0: continue
  frame.GetXaxis().SetBinLabel(i+1,c)
  print(i, c)
  for s in overallSignalRate[c]:
    print(s, overallSignalRate[c].keys(), histos.keys())
    histos[s].SetBinContent(i+1,overallSignalRate[c][s]/overallTotalSignal[c])
    histos[s].SetFillColor(int(format(plot[s]['color'], "d")))
    histos[s].SetLineColor(int(format(plot[s]['color'], "d")))
    histos[s].SetBarWidth(0.5)
    histos[s].SetBarOffset(0.25)
    print "category ", c," ", " signal ",s," signal fraction = ",overallSignalRate[c][s]/overallTotalSignal[c], " events = ", overallSignalRate[c][s]

for s in overallSignalRate['WVlnujj']: #used just to preserve the order of the signals
  stack.Add(histos[s])
  leg.AddEntry(histos[s],plot[s]['nameHR'],"f")



#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.lumi_13TeV = "35.9 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"

#iPos = 33
iPos = 0

H_ref = 1000
W_ref = 1400
W = W_ref
H  = H_ref

# references for T, B, L, R
T = 0.08*H_ref
B = 0.12*H_ref
L = 0.25*W_ref
R = 0.20*W_ref

canvas = ROOT.TCanvas("c2","c2",50,50,W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(0)
canvas.SetTicky(0)
#canvas.SetGrid()


frame.Draw("hbars")

stack.Draw("hbars same")
leg.SetBorderSize(0)
leg.Draw()

CMS_lumi.CMS_lumi(canvas, 4, iPos)


events = ROOT.TLatex()
events.SetTextSize(0.033)
events.SetTextAngle(0)
events.SetTextAlign(22)

for i,c in enumerate(combChannelsToConsider):
#  if overallTotalSignal[c] == 0: continue
  x = ROOT.gPad.GetUxmin() + 0.15*frame.GetXaxis().GetBinWidth(i+1)
  y = frame.GetXaxis().GetBinCenter(i+1)
  events.DrawLatex(x,y,"#color[10]{ "+" {0:.1f}".format(overallTotalSignal[c])+" events}")

ROOT.gPad.RedrawAxis()

canvas.Print("prova.pdf")
canvas.Print("prova.png")


