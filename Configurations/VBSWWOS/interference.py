
import sys
import os
import argparse
from math import sqrt, cos, cosh, pi
from ROOT import gROOT, gStyle
from ROOT import TFile, TCanvas, TH1F, THStack, TLegend, TChain, TLorentzVector, TMath

def DeltaEta(eta1, eta2):

  return abs( eta1 - eta2 )


def DeltaPhi(phi1, phi2):

  dphi = abs( phi1 - phi2 )
  if( dphi > pi ): dphi = 2*pi - dphi
  return dphi;

def DeltaR(eta1, phi1,
           eta2, phi2):

  return sqrt( DeltaEta(eta1,eta2)*DeltaEta(eta1,eta2) + 
               DeltaPhi(phi1,phi2)*DeltaPhi(phi1,phi2) )

def FillHisto(sample, donAOD=False, DEBUG=True ):

  gStyle.SetOptFit(0)
  gStyle.SetOptStat(0)
  gROOT.SetBatch(1)

  #Clean Jet Var
  hpt_1j =  TH1F("pt_1j", ";Pt 1st clean gen jet [GeV]; Events", 20, 0., 200)
  hpt_2j =  TH1F("pt_2j", ";Pt 2st clean gen jet [GeV]; Events", 20, 0., 200)
  heta_1j =  TH1F("eta_1j", ";Eta 1st clean  gen jet;Events", 20, -5., 5.)
  heta_2j = TH1F("eta_2j", ";Eta 2nd clean gen jet;Events", 20, -5., 5.)
  hmjj= TH1F("mjj",";Gen_mjj [GeV]; Events ",10,500,3000)
  hdetajj= TH1F("detajj",";Gen_detajj; Events ",10,3.5,10.5)
 
  #Lepton VAr
  hpt_1l =  TH1F("pt_1l", ";Pt 1st lepton gen [Gev]; Events", 20, 0., 200)
  hpt_2l =  TH1F("pt_2l", ";Pt 2nd lepton gen [GeV]; Events", 20, 0., 200)
  heta_1l =  TH1F("eta_1l", ";Eta 1st lepton gen; Events", 10, -2.5, 2.5)
  heta_2l = TH1F("eta_2l", ";Eta 2nd lepton gen; Events", 10, -2.5, 2.5)
  hmll = TH1F("mll","; Gen_mll[GeV]; Events; ", 10, 0, 400)
  
  hlist=[  hmjj,
  hdetajj,
  hpt_1j,
  hpt_2j,
  heta_1j,
  heta_2j,
  hpt_1l,
  hpt_2l,
  heta_1l,
  heta_2l,
  hmll]

  for h in hlist:
    h.Sumw2()

    
  Events=TChain("Events")
  Runs=TChain("Runs")

  if donAOD:
    print "Opening the File: ", sample['nAODpath']
    for ifile in sample['nAODpath']:
      Events.Add(ifile)
      Runs.Add(ifile)
    Events.SetBranchStatus("*",0)
    Events.SetBranchStatus("GenDressedLepton_pt",1)
    Events.SetBranchStatus("GenDressedLepton_eta",1)
    Events.SetBranchStatus("GenDressedLepton_phi",1) 
    Events.SetBranchStatus("GenDressedLepton_mass",1)
    Events.SetBranchStatus("nGenDressedLepton",1)

  else:
    Events.SetBranchStatus("*",0)
    print "Opening the File: ", sample['path']
    Events.Add(sample['path'])
    Runs.Add(sample['path'])
    Events.SetBranchStatus("nLeptonGen",1)
    Events.SetBranchStatus("LeptonGen_pt",1)
    Events.SetBranchStatus("LeptonGen_eta",1)
    Events.SetBranchStatus("LeptonGen_phi",1) 
    Events.SetBranchStatus("LeptonGen_mass",1)


  Events.SetBranchStatus("nGenJet",1)
  Events.SetBranchStatus("GenJet_pt",1)
  Events.SetBranchStatus("GenJet_eta",1)
  Events.SetBranchStatus("GenJet_phi",1) 
  Events.SetBranchStatus("GenJet_mass",1)
  Events.SetBranchStatus("LHEPart_pt",1)
  Events.SetBranchStatus("LHEPart_eta",1)
  Events.SetBranchStatus("LHEPart_phi",1) 
  Events.SetBranchStatus("GenPart_pdgId",1)
  Events.SetBranchStatus("genWeight",1)
  #Events.SetBranchStatus("XSWeight",1)

  Runs.SetBranchStatus("*",0)
  Runs.SetBranchStatus("genEventSumw_",1)

  #Get the correct weights, xsec and lumi
  sumGenW=0
  for ir in range(Runs.GetEntries()):
    Runs.GetEntry(ir)
    print "#", ir, "genEventSumw", Runs.genEventSumw_
    sumGenW+= Runs.genEventSumw_
  print "So sumGenW is ", sumGenW
  xsec = sample['xsec']
  lumi = sample['lumi']

  #Xsec for 2016
  if "2016" in sample['year']: 
    xsec = sample['xsec_2016']

  print "Year: ", sample['year'], "Lumi ",lumi, "using this xsec: ", xsec

  
  print "Filling the Histo ... "
  print ">> Starting the Loop on Events "

  #Starting the loop on Events to fill the histo
  for ev in range(Events.GetEntries()):

    jets_clean = [] #the list containing the 2 jets clean with pT > 30 GeV

    if DEBUG:
      if ev%1==0: 
        if ev > 50: break
        print "\n\n----------------------------------------------------\n" \
            "Processing event " , ev , " out of " ,Events.GetEntries() ,"\n" \
            "----------------------------------------------------\n" 
        sys.stdout.flush()
    else:
      if ev%10000==0: 
        print "Processing event " , ev , " out of " ,Events.GetEntries()  
        sys.stdout.flush()
    nCleanJet=0

    Events.GetEntry(ev)
    if donAOD:
      nLep=Events.nGenDressedLepton
    else:
      nLep=Events.nLeptonGen

    if nLep < 2:  #requiring at least 2 leptons
      if DEBUG: 
        print nLep,"Skipping:: Not enough Leptons, continue ..."     
      continue

    if donAOD:
      pt_leading=Events.GenDressedLepton_pt[0]
      pt_subleading=Events.GenDressedLepton_pt[1]
    else:
      pt_leading=Events.LeptonGen_pt[0]
      pt_subleading=Events.LeptonGen_pt[1]


    #Asking for two leptons: over the treshold
    if( pt_leading < 20 or pt_subleading < 10 ):
      if DEBUG: 
        print  pt_leading , pt_subleading ,"Skipping:: Lepton Not Over the pt Threshold, continue ..."
     
      continue
    #Cleaning the Jets (pT > 30, no Leptons with pt>10 in dR < 0.4)
    if Events.nGenJet==0: 
      if DEBUG: print "  Skipping No Jets: ", Events.nGenJet
      continue
    
    if DEBUG: print ">>>> Starting the Loop on Jets --> # of Jets: ", Events.nGenJet
    for iJ in range(Events.nGenJet):
      jet = TLorentzVector()
      jpt=Events.GenJet_pt[iJ]
      jeta=Events.GenJet_eta[iJ]
      jphi=Events.GenJet_phi[iJ]
      jmass=Events.GenJet_mass[iJ]
      
      CleanJet = True
      if DEBUG:
        print "    iJets", iJ+1,"# of Jets: ", Events.nGenJet," # of CleanJet", nCleanJet
        print "    Jet Pt ", jpt

      if jpt<30 : 
        CleanJet=False
        if DEBUG: print "    Pt < 30, So Not a CleanJet  ", CleanJet, " Exit the Jet Loop"
        break 
      if DEBUG: print ">>>>>> Starting the Loop on Leptons --> # of Leptons: ", nLep
      for iLep in range(nLep):
        if donAOD:
          lpt =Events.GenDressedLepton_pt[iLep]
          leta=Events.GenDressedLepton_eta[iLep]
          lphi=Events.GenDressedLepton_phi[iLep]
        else:
          lpt =Events.LeptonGen_pt[iLep]
          leta=Events.LeptonGen_eta[iLep]
          lphi=Events.LeptonGen_phi[iLep]



        if DEBUG:
          print "         iLepton ", iLep+1," # of Leptons: ", nLep
          print "         Lepton Pt ",lpt
          print "         deltaR  ",DeltaR(jeta,jphi,leta,lphi)
        
        if lpt < 10: 
          if DEBUG: 
            print "         Pt < 10, So CleanJet is ", CleanJet, "--> Quit the Lepton Loop ..."
          break
        
        if DeltaR(jeta,jphi,leta,lphi) < 0.4 : 
          CleanJet=False
          if DEBUG:
            print "         DeltaR < 0.4, So CleanJet is ", CleanJet, "--> Quit the Lepton Loop ..."
          break
          
      if DEBUG: print "<<<<<< Ended Loop on Leptons "

      if CleanJet :
        nCleanJet += 1
        jet.SetPtEtaPhiM(jpt,jeta,jphi,jmass)
        jets_clean.append(jet)
        
        if DEBUG: 
          print ">>>>>> !!! So We Have a CleanJet ", CleanJet, "And # of CleanJet is " , nCleanJet
          print " jets clean: Pt   ,   Eta    ,  Phi    , Mass \n" \
          "            ",jets_clean[nCleanJet-1].Pt(),jets_clean[nCleanJet-1].Eta(), jets_clean[nCleanJet-1].Phi(), jets_clean[nCleanJet-1].M()

      if nCleanJet==2 : 
        if DEBUG: 
          print ">>>>>> Found at least ", nCleanJet, "CleanJets with pT > 30 GeV --> Quit the Jet loop ..." 
          break

    if DEBUG: print "<<<< Ended Loop on Jets "

    #At least 2 CleanJet
    if nCleanJet < 2 : 
      if DEBUG: print " --- We dont have enough CleanJet ... continue ... ---"
      continue
    if DEBUG: 
      print "  Found ", nCleanJet, " CleanJet with pT > 30 GeV"  


    
    noTop_noHiggs=0 # excluding the top and the Higgs
    for ipart in range(0,len(Events.GenPart_pdgId)):
      noTop_noHiggs += (abs(Events.GenPart_pdgId[ipart])==6 or abs(Events.GenPart_pdgId[ipart])==25)
    if noTop_noHiggs>0: 
      if DEBUG: print "find an Higgs:   ", noTop_noHiggs
    

    #VBS Phase Space Cut
    mjj = (jets_clean[0]+jets_clean[1]).M()
    detajj = abs(jets_clean[0].Eta()-jets_clean[1].Eta())
    #print "            ",jets_clean[0].Pt(),jets_clean[0].Eta(), jets_clean[0].Phi(), jets_clean[0].M()
    #print "            ",jets_clean[1].Pt(),jets_clean[1].Eta(), jets_clean[1].Phi(), jets_clean[1].M()
    if DEBUG: print "Invariant mass of the jets: " , mjj, "and gap in eta : ", detajj
    if mjj <= 500 or detajj <= 3.5 : 
      if DEBUG: "Not in the VBS phase space"
      continue
   
    #Save the var of the 2 first lepton
    lepton1 = TLorentzVector()
    lepton2 = TLorentzVector()
    if donAOD:
      leppt = getattr (Events ,"GenDressedLepton_pt")
      lepeta = getattr (Events ,"GenDressedLepton_eta")
      lepphi = getattr (Events ,"GenDressedLepton_phi")
      lepmass = getattr (Events ,"GenDressedLepton_mass")
    else:
      leppt = getattr (Events ,"LeptonGen_pt")
      lepeta = getattr (Events ,"LeptonGen_eta")
      lepphi = getattr (Events ,"LeptonGen_phi")
      lepmass = getattr (Events ,"LeptonGen_mass")

    lepton1.SetPtEtaPhiM (leppt[0] , lepeta[0] , lepphi[0] , lepmass[0])
    lepton2.SetPtEtaPhiM (leppt[1] , lepeta[1] , lepphi[1] , lepmass[1])
    mll = (lepton1+lepton2).M()
    if DEBUG: 
      print "             ,lepton Pt(),      Eta(),        Phi(),         M()"
      print "            ",lepton1.Pt(),lepton1.Eta(), lepton1.Phi(), lepton1.M()
      print "            ",lepton2.Pt(),lepton2.Eta(), lepton2.Phi(), lepton2.M() 
      print "             and mlll is: ", mll

    #To Cut at LHE level W Mass to fix 2016 bug
    part0 = TLorentzVector () 
    part1 = TLorentzVector ()
    part2 = TLorentzVector ()
    part3 = TLorentzVector ()
    pt = getattr (Events ,"LHEPart_pt")
    eta = getattr (Events ,"LHEPart_eta")
    phi = getattr (Events ,"LHEPart_phi")

    part0.SetPtEtaPhiM (pt[0] , eta[0] , phi[0] , 0)
    part1.SetPtEtaPhiM (pt[1] , eta[1] , phi[1] , 0)
    part2.SetPtEtaPhiM (pt[2] , eta[2] , phi[2] , 0)
    part3.SetPtEtaPhiM (pt[3] , eta[3] , phi[3] , 0)
    
    LHE_mW1 = (part0+part1).M()
    LHE_mW2 = (part2+part3).M()

    xsec = sample['xsec']
    lumi = sample['lumi']

    massRange = True 

    #Remove the bug from 2016
    if "2016" in sample['year']: 
      xsec = sample['xsec_2016']
      if DEBUG:
        print "LHE_mW1,   LHEmW2"
        print LHE_mW1, LHE_mW2
      if (LHE_mW1 < 63 or LHE_mW2 < 63 or LHE_mW1 > 100 or LHE_mW2 >100):
        if DEBUG: 
          print "So massRange should be false"
          #print "LHE_mW1,   LHEmW2"
          #print LHE_mW1, LHE_mW2
          #print "So massRange should be false"
        massRange = False
      if DEBUG:
        print "Mass Range is ", massRange

    

    if DEBUG: 
      print "Year: ", sample['year'], "Lumi ",lumi, "using this xsec: ", xsec
      print "So sumGenW is ", sumGenW
      print "So genWeight is ", Events.genWeight
      print "Mass Range is ", massRange

    weight = (1000*xsec*lumi*Events.genWeight) / sumGenW

    if massRange: #always True for 2017-2018
      if DEBUG: 
        print "!!! The Event passed the Selections !!!"    
        print "!!! So I Can Finally Fill the Histo  !!! "
        print "mjj ---> ", mjj
        print "detajj ---> ", detajj
        print "pt 1 j ---> ", jets_clean[0].Pt()
        print "pt 2 j ---> ", jets_clean[1].Pt()
        print "eta 1 j ---> ", jets_clean[0].Eta()
        print "eta 2 j ---> ", jets_clean[1].Eta()
        print "mll ---> ", mll
        print "pt 1 lep ---> ", lepton1.Pt()
        print "pt 2 lep ---> ", lepton2.Pt()
        print "eta 1 lep ---> ", lepton1.Eta()
        print "eta 2 lep ---> ", lepton2.Eta()

      hmjj.Fill(mjj, weight)
      hdetajj.Fill(detajj, weight)
      hpt_1j.Fill(jets_clean[0].Pt(), weight)
      hpt_2j.Fill(jets_clean[1].Pt(), weight)
      heta_1j.Fill(jets_clean[0].Eta(), weight)
      heta_2j.Fill(jets_clean[1].Eta(), weight)
      hpt_1l.Fill(lepton1.Pt(), weight)
      hpt_2l.Fill(lepton2.Pt(), weight)
      heta_1l.Fill(lepton1.Eta(), weight)
      heta_2l.Fill(lepton2.Eta(), weight)
      hmll.Fill(mll, weight)



  
     
  print "<< Ended Loop on Events "
  print "Filled Histos "
  if DEBUG: "Now returning the histo: "

  return hlist



#FIXME insert the correct paths to samples
gStyle.SetOptFit(0)
gStyle.SetOptStat(111)
gROOT.SetBatch(1)
y2018={    'nAOD_ewk' : ['/tmp/fcetorel/2A89B2D0-7762-6E42-915F-A0333FFAD09C.root','/tmp/fcetorel/1FF1C9ED-2992-1B46-802C-3FB73AA7439D.root'],
          'nAOD_qcd' : ['/tmp/fcetorel/E8D773D8-4D92-C84A-B0FA-8AC593718BEE.root'],
          'nAOD_ewkqcd' : ['/tmp/fcetorel/E3C54B11-5A91-D140-B9F5-907BC6A08EA4.root','/tmp/fcetorel/79ED660B-C08B-8544-A0B7-DD63DC16A478.root','/tmp/fcetorel/74066BC5-F858-D94A-9160-DD84C43F61C6.root'],
         'directory':"/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/",
         'year':"2018",
          'lumi': 59.7
}
y2017={ 'nAOD_ewk' : ['/tmp/fcetorel/92C04F7F-95C6-8A48-8B42-54552B25ED5F.root'],
          'nAOD_qcd' : ['/tmp/fcetorel/4FDDD108-CBDC-2B4F-83C5-8D0D911DC088.root'],
          'nAOD_ewkqcd' : ['/tmp/fcetorel/7E7A4504-10AB-3944-8F9F-AB408C071B50.root','/tmp/fcetorel/FAA86043-6044-094C-8E40-FCEAFA10EC27.root'],
         'directory': "/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6/",
         'year':"2017",
          'lumi': 41.2

}
y2016={ 'nAOD_ewk' : ['/tmp/fcetorel/2DA8F372-E3C6-E34E-9F37-63CE076D9413.root'],
          'nAOD_qcd' : ['/tmp/fcetorel/DC59416B-18CC-E143-A5AB-3D51F0E8AB7E.root','/tmp/fcetorel/DF8BC857-1FAC-D347-B48B-4735CEBCB679.root','/tmp/fcetorel/BAE08180-3591-4444-A2DC-5DDFD0327E07.root'],
          'nAOD_ewkqcd' : ['/tmp/fcetorel/D041682E-9625-F948-B63C-49E0A912403B.root','/tmp/fcetorel/A3275165-6A93-384F-891D-9728E8F425BE.root'],
        'directory': "/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6/",
         'year':"2016",
          'lumi': 35.9
}


#FIXME select the year 
#Also remember to change MANUALLY genEventSumw in genEventSumw_ in the code, if you run on 2018
year=y2018


#dir2017="/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/";
ewk_notop = {
        'path' : year['directory']+'nanoLatino_WpWmJJ_EWK_noTop__part*.root',
        'nAODpath': year['nAOD_ewk'],
        'xsec' : 0.08875,
        'xsec_2016': 0.3452, 
        'year' : year['year'],
        'lumi' : year['lumi'],
        'name' : 'ewk_notop',
        'color' : 633,
           }

qcd_notop = {
        'path' : year['directory']+'nanoLatino_WpWmJJ_QCD_noTop__part*.root',
        'nAODpath': year['nAOD_qcd'],
        'xsec' : 2.160,
        'xsec_2016': 2.423, 
        'year' : year['year'],
        'lumi' : year['lumi'],
        'name' : 'qcd_notop',
        'color' : 633,
           }

ewk_qcd_notop = {
        'path' : year['directory']+'nanoLatino_WpWmJJ_EWK_QCD_noTop__part*.root',
        #'path16' : year['directoryAlt']+'nanoLatino_WpWmJJ_EWK_QCD_noTop__part*.root',
        'nAODpath': year['nAOD_ewkqcd'],
        'xsec' : 2.251,
        'xsec_2016': 2.663, 
        'year' : year['year'],
        'lumi' : year['lumi'],
        'name' : 'ewk_qcd_notop',
        'color' : 633,
           }


c= TCanvas()

#parse arguments --> From command line options: 1. Debug mode , 2. Run on nAOD or latinos post processed ntuples, 3. date, 4. outdir base fold
parser = argparse.ArgumentParser()
parser.add_argument('--debug',          action='store_true',      default=False,      help='debugging mode')
parser.add_argument('--donAOD',          action='store_true',    default=False,      help='run on nAOD')
parser.add_argument('-d', '--date'    , type=str   ,   help='date')
parser.add_argument('-o', '--outdir'   ,   default="/eos/user/f/fcetorel/www/VBS_OS/test/",      type=str,      help='output base folder')
args = parser.parse_args()

outdir=args.outdir
date=args.date
donAOD=args.donAOD
DEBUG=args.debug

try: 
    os.mkdir(outdir+"interference_ewkqcdfix_"+date) 
except OSError as error: 
    print(error) 

if (DEBUG):
  print "Entering Debugging Mode ...  "
  print "Created the out dir"
  print "Not Saving in debugging mode, but the output directory is set to: "+outdir+"interference_ewkqcdfix_"+date



hlist=[]

sample= [ewk_notop, qcd_notop, ewk_qcd_notop]
#sample = [ewk_notop]
for isample in sample:

  hlist = FillHisto(isample,donAOD, DEBUG)
  for h in hlist: 
    var= h.GetName()
    h.SetName("h"+isample['name'])
    h.Draw("")

  
    if DEBUG: continue #debugging mode doesnt save
    if donAOD:   
      c.SaveAs(outdir+"interference_ewkqcdfix_"+date+"/nAOD_"+var+"_"+isample['name']+"_"+isample['year']+".png") 
      c.SaveAs(outdir+"interference_ewkqcdfix_"+date+"/nAOD_"+var+"_"+isample['name']+"_"+isample['year']+".root")
    else:
      c.SaveAs(outdir+"interference_ewkqcdfix_"+date+"/latino_"+var+"_"+isample['name']+"_"+isample['year']+".png") 
      c.SaveAs(outdir+"interference_ewkqcdfix_"+date+"/latino_"+var+"_"+isample['name']+"_"+isample['year']+".root")
  


