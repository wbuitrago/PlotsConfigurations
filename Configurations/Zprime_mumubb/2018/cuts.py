# cuts
supercut = '   Lepton_pt[0]>30 \
            && Lepton_pt[1]>20 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
            && multiJet \
            && mjj>200 && abs(CleanJet_eta[0])<4.7 && abs(CleanJet_eta[1])<4.7 \
            && CleanJet_pt[0]>50 && CleanJet_pt[1]>30 \
            && mll>50 \
            && PuppiMET_pt < 100 \
           '
## Control regions
cuts['Zprime_mumu_bb'] = {
   'expr': 'Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'loose_mm' : '((zeroJet && !bVeto) || bReq)',
      'tight_mm' : '((zeroJet && !bVeto) || bReqTight)',
      #
   }
}

cuts['Zprime_ee_bb'] = {
   'expr': 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'loose_ee' : '((zeroJet && !bVeto) || bReq)',
      'tight_ee' : '((zeroJet && !bVeto) || bReqTight)',
      #
   }
}

   
   
   