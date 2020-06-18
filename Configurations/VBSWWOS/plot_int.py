import sys
import os
import argparse
from ROOT import gROOT, gStyle
from ROOT import TFile, TCanvas, TH1F,THStack, TLegend, TF1, TColor



def doIntPerYear( data, canvas, output,debug=False):
    xmin=500
    xmax=3000
    #hqcd= TH1F("hsum",";Gen_mjj; Events ",10,500,3000)
    #hewk= TH1F()
    #htot= TH1F("hsig",";Gen_mjj; Events ",10,500,3000)

    gStyle.SetOptFit(0)
    gStyle.SetOptStat(0)
    gROOT.SetBatch(1)
    hs = THStack()
    hqcd_hewk = THStack()
    leg = TLegend(0.58,0.75,0.89,0.89);

    for isample in data:
      if not os.path.exists(isample['ipath']): 
        print "Can't find this file :", isample['ipath'], " --> Skipping"
        sys.stdout.flush()
        return 0
      print '>>> Opening File :' , isample['ipath']
      sys.stdout.flush()
      inFile = TFile.Open ( isample['ipath'] ," READ ")

      c1 = inFile.Get(canvas)
      
      if 'hewk_qcd' in isample['obj']: htot = c1.GetListOfPrimitives().FindObject(isample['obj'])
      if 'ewk' not in isample['obj']: hqcd = c1.GetListOfPrimitives().FindObject(isample['obj'])
      if 'qcd' not in isample['obj']: hewk = c1.GetListOfPrimitives().FindObject(isample['obj'])

    hsig=hewk.Clone()
    hsig.SetName("hsig")
    hsum=hewk.Clone()
    hsum.Add(hqcd)
    hint=htot.Clone()
    hint.SetName("hint")
    hint.Add(hint,hsum,1,-1)
    
    c = TCanvas()
    c.SetName("c1")
    c.cd() 

    hint.SetLineColor(1)
    hqcd.SetLineColor(2)
    hsig.SetLineColor(3)
    htot.SetLineColor(4)
    hs.Add(hint)
    hs.Add(htot)
    hqcd_hewk.Add(hsig)
    hqcd_hewk.Add(hqcd)
    #hsig.Draw("pe")
    #hint.Draw("pe, same")

    leg.AddEntry(hsig,"WpWmJJ_EWK_noTop")
    leg.AddEntry(hqcd,"WpWmJJ_QCD_noTop")
    leg.AddEntry(htot,"WpWmJJ_EWK_QCD_noTop")
    leg.AddEntry(hint,"Interference")


    xtitle=hewk.GetXaxis().GetTitle()
    ytitle=hewk.GetYaxis().GetTitle()

    #print xtitle
    #print ytitle
    hs.SetTitle(";"+xtitle+";"+ytitle)

    hs.Draw("pe nostack")
    hqcd_hewk.Draw("pe same")

    line1 = TF1("line1","pol0",-100,4000)
    line1.FixParameter(0,0)
    line1.SetLineWidth(2)
    line1.SetLineStyle(2)
    line1.SetLineColor(2)
    line1.Draw("same")
    

    #leg.SetNColumns(2)
    leg.SetBorderSize(0)
    leg.Draw("same")
    c.SaveAs(output+".png")
    c.SaveAs(output+".pdf")
    c.SaveAs(output+".root")

def doCombination( file_list, output,debug=False):
    xmin=500
    xmax=3000
    hsig16= TH1F("hsig16",";Gen_mjj; Events ",10,500,3000)
    hsig17= TH1F("hsig17",";Gen_mjj; Events ",10,500,3000)
    hsig18= TH1F("hsig18",";Gen_mjj; Events ",10,500,3000)

    hint16= TH1F("hint16",";Gen_mjj; Events ",10,500,3000)
    hint17= TH1F("hint17",";Gen_mjj; Events ",10,500,3000)
    hint18= TH1F("hint18",";Gen_mjj; Events ",10,500,3000)




    gStyle.SetOptFit(0)
    gStyle.SetOptStat(0)
    gROOT.SetBatch(1)
    hs = THStack()
    leg = TLegend(0.58,0.75,0.89,0.89);

    for ifile in file_list:
      if not os.path.exists(ifile): 
        print '>>> This file does not exist :' , ifile, "  --> Check path..."
        continue
      print '>>> Opening File :' , ifile
      inFile = TFile.Open ( ifile," READ ")

      c1 = inFile.Get("c1")
      
      if '2018' in ifile: 
        hint18 = c1.GetListOfPrimitives().FindObject('hint')
        hsig18 = c1.GetListOfPrimitives().FindObject('hsig')
        print "Extract 2018"
      if '2017' in ifile:
        hint17 = c1.GetListOfPrimitives().FindObject('hint')
        hsig17= c1.GetListOfPrimitives().FindObject('hsig')
        print "Extract 2017"

      if '2016' in ifile: 
        hint16 = c1.GetListOfPrimitives().FindObject('hint')
        hsig16 = c1.GetListOfPrimitives().FindObject('hsig')
        print "Extract 2016"


    hsigcomb=hsig16.Clone()
    hsigcomb.SetName("hsigcomb")
    hsigcomb.Add(hsig17)
    hsigcomb.Add(hsig18)

    hintcomb=hint16.Clone()
    hintcomb.SetName("hintcomb")
    hintcomb.Add(hint17)
    hintcomb.Add(hint18)


    
    c = TCanvas()
    c.cd() 

    hintcomb.SetLineColor(1)
    hsigcomb.SetLineColor(4)
    hs.Add(hintcomb)
    hs.Add(hsigcomb)

    leg.AddEntry(hsigcomb,"WpWmJJ_EWK_noTop")
    leg.AddEntry(hintcomb,"Interference")



    hs.SetTitle("; Gen mjj [GeV]; Events")
    hs.Draw("pe nostack")

    line1 = TLine(xmin,0.0,xmax,0.0)
    line1.SetLineWidth(2)
    line1.SetLineStyle(2)
    line1.SetLineColor(2)
    line1.Draw("same")
    

    #leg.SetNColumns(2)
    leg.SetBorderSize(0)
    leg.Draw("same")
    c.SaveAs(output+".png")
    c.SaveAs(output+".pdf")
    c.SaveAs(output+".root")

#Main
#parse arguments --> From command line options: 1. Debug mode , 2. Run on nAOD or latinos post processed ntuples, 3.  input-output fold (that from interference.py)
parser = argparse.ArgumentParser()
parser.add_argument('--debug',          action='store_true',             dest='debug',          default=False,      help='debugging mode')
parser.add_argument('--donAOD',          action='store_true',             dest='donaod',          default=False,      help='run on nAOD')
parser.add_argument('--doPerYear',          action='store_true',             dest='dopery',          default=False,      help='interference plot per year')
parser.add_argument('--doComb',          action='store_true',             dest='docomb',          default=False,      help='2016/17/18 combination')
parser.add_argument('-o', '--outdir'   ,  dest='outdir',    default="/eos/user/f/fcetorel/www/VBS_OS/test/interference_ewkqcdfix_080620/",      type=str,      help='output base folder')
parser.add_argument('-y', '--year'   , nargs='+' ,   help='Choose the year you want to run on. Default is all.')

args = parser.parse_args()


donAOD=args.donaod
DEBUG=args.debug
doPerYear=args.dopery
doComb=args.docomb
fold=args.outdir
output=fold
years=[]
years = args.year

#FIXME select the years and if you want to run on latinos or nAOD and the variables
#years=["2016","2017","2018"]
#years=["2017"]
variables=["mjj","detajj","pt_1j","pt_2j","eta_1j","eta_2j","mll","pt_1l","pt_2l","eta_1l","eta_2l"]

if donAOD :
  tag="nAOD"
else :
  tag="latinos"


if doPerYear:
  for var in variables:
    for year in years:
      ewk = {
        'obj' :'hewk_notop',
        'ipath' : fold+tag+"_"+var+"_ewk_notop_"+year+".root",

           }
      qcd = {
 
        'obj' :'hqcd_notop',
        'ipath' : fold+tag+"_"+var+"_qcd_notop_"+year+".root",

           }
      ewk_qcd = {
        'obj' :'hewk_qcd_notop',
        'ipath' : fold+tag+"_"+var+"_ewk_qcd_notop_"+year+".root",
           }

      file_list = [ewk,qcd, ewk_qcd]
      doIntPerYear(file_list, "c1",output+tag+"_"+var+"_interference_"+str(year))

if doComb:

  file_combination= [output+tag+"_interference_2016.root",output+tag+"_interference_2017.root",output+tag+"_interference_2018.root"]
  doCombination(file_combination, output+tag+"_interference_combination")
    

