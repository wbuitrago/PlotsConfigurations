# cuts

supercut = 'mll>60 && mll<120 && Lepton_pt[0]>25 && Lepton_pt[1]>13 && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5'

# cuts['Zee_incl']  = '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11) '

# cuts['Zmm_incl']  = '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13) '

cuts['Zee_1j']  = '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11) && oneJet'
cuts['Zmm_1j']  = '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13) && oneJet'
