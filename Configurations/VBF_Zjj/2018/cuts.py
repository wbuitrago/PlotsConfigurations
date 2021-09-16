# cuts

supercut = '   Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 60 \
            && mjj > 300 \
            && detajj > 2.5 \
            && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
           '

## Signal regions
cuts['Zjj_13TeV'] = {
   'expr': 'SR',
    # Define the sub-categorization of sr
   'categories' : {
      #
      #'em' : ' zeroJet  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && mth<60 && mll>40 && mll<80',
      #
      'ee' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && mjj>500 && detajj>2.5 && multijet',
      #
      'mm' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && mjj>500 && detajj>2.5 && multijet', 
      #
   }
}


