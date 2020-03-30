# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

supercut='mjj > 100'

## Signal regions
cuts['ssww_total'] = 'ssww_region && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto'
cuts['ssww_EE'] = 'ssww_region && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11 && softmuon_veto'
cuts['ssww_MM'] = 'ssww_region && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13 && softmuon_veto'
cuts['ssww_ME'] = 'ssww_region && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11 && softmuon_veto'
cuts['ssww_EM'] = 'ssww_region && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13 && softmuon_veto'
