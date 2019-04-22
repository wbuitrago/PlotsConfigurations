import ROOT
from math import *
from collections import namedtuple
import sys


#structures

curves = namedtuple("curves", ["nvar", "roc1", "signif1", "signif11", "legf11", "legf22"], verbose=True)
multicurves = namedtuple("multicurves", ["roc1", "signif1", "leg1", "leg2"], verbose=True)

#create structure

def create_curves (number):
    return curves(number, ROOT.TGraph(), ROOT.TGraph(), ROOT.TGraph(), ROOT.TLegend(0.1,0.8,0.2,0.9), ROOT.TLegend(0.1,0.8,0.2,0.9))

#create canvas

def create_canva (num):
    return ROOT.TCanvas("signif{}".format(3 + num), "", 100, 200, 700, 500)

#roc and significance curves generator

def roc_curve (sig, bkg, namevar, mycurves , mymulticurves):

    mycurves.roc1.SetMarkerStyle(20)
    mycurves.signif1.SetMarkerStyle(20)
    mycurves.signif11.SetMarkerStyle(20)
    
    colours = [ROOT.kBlue+2, ROOT.kRed+1, ROOT.kGreen+2, ROOT.kPink, ROOT.kOrange+1, \
            ROOT.kSpring-8, ROOT.kAzure+1, ROOT.kViolet-5, ROOT.kCyan-1, ROOT.kYellow-2, \
                ROOT.kYellow+4, ROOT.kRed-9, ROOT.kCyan-6, ROOT.kOrange-5, ROOT.kOrange]
    
    if mycurves.nvar < len(colours):
        colour1 = colours[mycurves.nvar]
    else:
        colour1 = 880 - (mycurves.nvar)*20
            
    N_sig = sig.Integral() #Number of events (signal)
    N_bkg = bkg.Integral() #Number of events (background)
    Nbin = sig.GetNbinsX() #Nbin_sig = Nbin_bkg

    for i in range(1, Nbin+1):
        try:
            ind = sys.argv.index('--right')
            s = sig.Integral(1,i)
            b = bkg.Integral(1,i)
        except:
            s = sig.Integral(i,Nbin)
            b = bkg.Integral(i,Nbin)
        eff_sig = float(s) / N_sig
        eff_bkg = float(b) / N_bkg
        try:
            try:
                ind = sys.argv.index('--expanded')
                Z = sqrt(2*((s+b)*log(1+float(s)/b)-s))
            except:
                Z = float(s)/sqrt(b)
        except Exception:
            pass
        mycurves.roc1.SetPoint(i, eff_bkg, eff_sig)
        mycurves.signif1.SetPoint(i-1, eff_sig, Z)
        mycurves.signif11.SetPoint(i-1, sig.GetBinCenter(i), Z)

    
    #mycurves.roc1.SetMarkerStyle(20)
    mycurves.roc1.SetMarkerSize(0.9) #0.75
    mycurves.roc1.SetMarkerColor(colour1)
           
    #mycurves.signif1.SetMarkerStyle(20)
    mycurves.signif1.SetMarkerSize(0.9)
    mycurves.signif1.SetMarkerColor(colour1)  
        
    #mycurves.signif11.SetMarkerStyle(20)
    mycurves.signif11.SetMarkerSize(0.9)
    mycurves.signif11.SetMarkerColor(colour1)
    mycurves.signif11.GetXaxis().SetTitleSize(0.05)
    mycurves.signif11.GetXaxis().SetLabelSize(0.05)
    mycurves.signif11.GetYaxis().SetTitleSize(0.05)
    mycurves.signif11.GetYaxis().SetLabelSize(0.05)
    mycurves.signif11.GetXaxis().SetTitleOffset(0.85)
    mycurves.signif11.GetYaxis().SetTitleOffset(0.85)
    mycurves.legf11.AddEntry(mycurves.signif11, namevar, "lp")

    mymulticurves.roc1.Add(mycurves.roc1)
    mymulticurves.leg1.AddEntry(mycurves.roc1, namevar, "lp")
       
    mymulticurves.signif1.Add(mycurves.signif1)
    mymulticurves.leg2.AddEntry(mycurves.signif1, namevar, "lp")
    
    if mycurves.nvar == 0:
    
        mymulticurves.roc1.SetTitle(" ; #varepsilon_{bkg}; #varepsilon_{sig} ")
        mymulticurves.roc1.GetXaxis().SetTitleSize(0.05)
        mymulticurves.roc1.GetXaxis().SetLabelSize(0.05)
        mymulticurves.roc1.GetYaxis().SetTitleSize(0.05)
        mymulticurves.roc1.GetYaxis().SetLabelSize(0.05)
        mymulticurves.roc1.GetXaxis().SetTitleOffset(0.85)
        mymulticurves.roc1.GetYaxis().SetTitleOffset(0.85)
        
        mymulticurves.signif1.SetTitle(" ; #varepsilon_{sig}; Z_{0} ")
        mymulticurves.signif1.GetXaxis().SetTitleSize(0.05)
        mymulticurves.signif1.GetXaxis().SetLabelSize(0.05)
        mymulticurves.signif1.GetYaxis().SetTitleSize(0.05)
        mymulticurves.signif1.GetYaxis().SetLabelSize(0.05)
        mymulticurves.signif1.GetXaxis().SetTitleOffset(0.85)
        mymulticurves.signif1.GetYaxis().SetTitleOffset(0.85)
            
# mkROC macro
   
file_in = "plots_VBS_SS_test.root"
subdirectory = "VBS_13TeV_BaseCut"
    
variables = []
v_curves = []

c1 = ROOT.TCanvas("roc1", "", 100, 200, 700, 500)
c3 = ROOT.TCanvas("signif1", "", 100, 200, 700, 500)

f = ROOT.TFile(file_in)
    
ansv = "y"

# variables cycle
    
while True:
    variable = raw_input('Insert variable name: ')
    variables.append(variable)
    ansv = raw_input('Do you want to insert any other variable (y/n)? ')
    if ansv != "y":
        break
        
# structures cycle

i = 0
while True:
    v_curves.append(create_curves(i))
    i += 1
    if i >= len(variables):
        break

ROOT.gDirectory.cd(subdirectory)           #subdirectory
    
namesgn1 = "histo_WpWp_EWK"
namesgn2 = "histo_WmWm_EWK"

namebkg = []
bkg = 'y'
while True:
    name_b = raw_input('Insert bkg histo to analyze: ')
    namebkg.append(name_b)
    bkg = raw_input('Do you want to group any other bkg histo (y/n)? ')
    if bkg == "n":
        break

mymulticurves = multicurves(ROOT.TMultiGraph(), ROOT.TMultiGraph(), ROOT.TLegend(0.1,0.8,0.2,0.9), ROOT.TLegend(0.1,0.8,0.2,0.9))
        
# cycle on the variables
    
for i1 in range(0, len(variables)):
    if (i1 != 0):
        ROOT.gDirectory.cd("../")
    ROOT.gDirectory.cd(variables[i1])
            
    histosgn = ROOT.gDirectory.Get(namesgn1)
    histosgn2 = ROOT.gDirectory.Get(namesgn2)
    histosgn.Add(histosgn2)
    
    for i2 in range(0, len(namebkg)):
        histobkg = ROOT.gDirectory.Get(namebkg[i2])
        if i2 == 0:
	    histobkgTot = histobkg
	else:
            histobkgTot.Add(histobkg)
               
    roc_curve(histosgn,histobkgTot, variables[i1], v_curves[i1], mymulticurves)
    
#l = ROOT.TLine(0,0,1,1)
l = ROOT.TF1('l', 'x', 0., 1.)
l.SetLineStyle(7)
l.SetLineWidth(2)
l.SetLineColor(ROOT.kBlack)
        
c1.cd()
try:
    ind_line = sys.argv.index('--line')
    mymulticurves.roc1.Draw("APL")
except:
    mymulticurves.roc1.Draw("AP")
mymulticurves.leg1.Draw("SAME")
l.Draw("SAME")
c1.SaveAs("roc1.png")
       
c3.cd()
try:
    ind_line = sys.argv.index('--line')
    mymulticurves.signif1.Draw("APL")
except:
    mymulticurves.signif1.Draw("AP")
mymulticurves.leg2.Draw("SAME")
c3.SaveAs("signif1.png")

for j in range(0, len(variables)):
    varname = variables[j]
        
    c11 = create_canva(j)
    c11.cd()
    v_curves[j].signif11.GetXaxis().SetTitle(varname)
    v_curves[j].signif11.GetYaxis().SetTitle("Z_{0}")
    try:
        ind_line = sys.argv.index('--line')
        v_curves[j].signif11.Draw("APL")
    except:
        v_curves[j].signif11.Draw("AP")
    v_curves[j].legf11.Draw("SAME")
    c11.SaveAs("signif1_{}".format(varname)+".png")
        



print '''
-------------------------------------------------------------------------------
 _____      _______    _____
|  __ \    |  ___  |  |  ___|       \  |         |
| |__\ |   | |   | |  | |          |\/ |   _` |  |  /   _ \   __|
|  ___ \   | |___| |  | |___       |   |  (   |    <    __/  |
| |   \ \  |_______|  |_____|     _|  _| \__,_| _|\_\ \___| _| 

-------------------------------------------------------------------------------
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
