# cuts

supercut = '   Lepton_pt[0]>30 \
            && Lepton_pt[1]>20 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && PuppiMET_pt > 60 \
            && detajj > 2.5 \
            && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
            && multiJet \
             && abs(mll-90)<15 \
            && mjj>200 && CleanJet_eta[0]<4.7 \
            && CleanJet_pt[0]>50 && CleanJet_pt[1]>30 \
           '
# supercut: && ptll>30 \


## Signal regions
cuts['Zjj_13TeV'] = {
   'expr': 'sr',
    # Define the sub-categorization of sr
   'categories' : {
      #
      #'em' : ' zeroJet  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && mth<60 && mll>40 && mll<80',
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
      #&& abs(mll-90)<15 \
      # && mjj>200 && Jet_eta[0]<4.7 \
      # && Jet_pt[0]>50 && Jet_pt[1]>30 
   }
}
