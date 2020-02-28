# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

supercut='mjj > 150'

## Signal regions
cuts['lowmjj_total'] = 'ssww_region2 && jetpt30 && leppt30 && mjj < 500 && bVeto && softmuon_veto'
cuts['lowmjj_EE'] = 'ssww_region2 && jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11 && softmuon_veto'
cuts['lowmjj_MM'] = 'ssww_region2 && jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13 && softmuon_veto'
cuts['lowmjj_ME'] = 'ssww_region2 && jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11 && softmuon_veto'
cuts['lowmjj_EM'] = 'ssww_region2 && jetpt30 && leppt30 && mjj < 500 && bVeto && abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13 && softmuon_veto'


cuts['top_total'] = 'ssww_region2 && zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto)'
cuts['top_EE'] = 'ssww_region2 && zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto) && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11'
cuts['top_MM'] = 'ssww_region2 && zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto) && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13'
cuts['top_ME'] = 'ssww_region2 && zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto)&& abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11'
cuts['top_EM'] = 'ssww_region2 && zlep_ww && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && (!bVeto||!softmuon_veto)&& abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13'

cuts['ssww_total'] = 'ssww_region2 && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto'
cuts['ssww_EE'] = 'ssww_region2 && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11 && softmuon_veto'
cuts['ssww_MM'] = 'ssww_region2 && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11 && softmuon_veto'
cuts['ssww_ME'] = 'ssww_region2 && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11 && softmuon_veto'
cuts['ssww_MM'] = 'ssww_region2 && zlep_ww && bVeto && jetpt30 && leppt30 && mjj > 500 && abs(detajj)>2.5 && abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13 && softmuon_veto'
