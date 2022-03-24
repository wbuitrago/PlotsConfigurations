# cuts

supercut = '   Lepton_pt[0]>30 \
            && Lepton_pt[1]>20 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
            && multiJet \
            && mjj>200 && abs(CleanJet_eta[0])<4.7 && abs(CleanJet_eta[1])<4.7 \
            && CleanJet_pt[0]>50 && CleanJet_pt[1]>30 \
            && mll>50 \
           '
# supercut: && ptll>30
#&& abs(mll-90)<15



#aliases['sr'] = {
    #'expr': 'bVeto'
#}


#aliases['multiJet'] = {
    #'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
#}





## Control regions
cuts['Top_13TeV_2j'] = {
   'expr': 'topcr',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'eemm' : '((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13))\
            && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
            && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
            && mll > 105 \
            ',
      #
   }
}


cuts['WW_13TeV_2j'] = {
   'expr': 'wwcr',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'eemm' : '((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13))\
            && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
            && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
            && PuppiMET_pt>100 \
            ',
      #
   }
}




cuts['DY_13TeV_2j'] = {
   'expr': 'dycr',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'eemm' : '((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13))\
            && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
            && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
            && PuppiMET_pt<100 \
            && detajj<2.0 \
            ',
      #
   }
}





## Signal regions
cuts['Zjj_13TeV_2j'] = {
   'expr': 'sr',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'eemm-high'     : '((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
                       && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
                       && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
                       && (CleanJet_pt[1]>50) \
                       ',
      #
      'eemm-low'      : '((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
                       && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
                       && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
                       && (CleanJet_pt[1]<=50) \
                       ',
      #
   }
}







## Signal regions
cuts['Optimization_13TeV_2j'] = {
   'expr': 'sr',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'eemm' : '((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
                       && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
                       && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
                       ',
      #
   }
}






