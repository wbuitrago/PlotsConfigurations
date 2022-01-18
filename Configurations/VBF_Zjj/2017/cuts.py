# cuts

supercut = '   Lepton_pt[0]>30 \
            && Lepton_pt[1]>20 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && detajj > 2.5 \
            && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
            && multiJet \
            && mjj>200 && abs(CleanJet_eta[0])<4.7 && abs(CleanJet_eta[1])<4.7 \
            && CleanJet_pt[0]>50 && CleanJet_pt[1]>30 \
           '
# supercut: && ptll>30
#&& abs(mll-90)<15



#aliases['sr'] = {
    #'expr': 'bVeto'
#}


#aliases['multiJet'] = {
    #'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
#}


## Signal regions
cuts['Zjj_13TeV_2j'] = {
   'expr': 'sr',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'ee' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
            && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
            && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
            ',
      #
      'mm' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
            && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 \
            && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
            ',
   }
}



