# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>2'

## Signal regions

#cuts['loosewz'] ='wzinc && bVeto && METFixEE2017_pt>30 && tauVeto_wz && jeteta_exclude'
#cuts['loosewz_PuppiMET'] ='wzinc && bVeto && PuppiMET_pt>30 && tauVeto_wz && jeteta_exclude'

#cuts['wz_jetpt30'] ='wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'
#cuts['wz_jetpt30_PuppiMET'] ='wzinc && bVeto && PuppiMET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'

cuts['wz_jetpt30_zlep'] ='wzinc && bVeto && METFixEE2017_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && jeteta_exclude'
cuts['wz_jetpt50_zlep'] ='wzinc && bVeto && METFixEE2017_pt>30 && tauVeto_wz && jetpt50 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && jeteta_exclude'
#cuts['wz_jetpt30_PuppiMET_zlep'] ='wzinc && bVeto && PuppiMET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && jeteta_exclude'

#cuts['wzb_jetpt30'] ='wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'
#cuts['wzb_jetpt30_PuppiMET'] ='wzinc && !bVeto && PuppiMET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'

cuts['wzb_jetpt30_zlep'] ='wzinc && !bVeto && METFixEE2017_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && jeteta_exclude'
cuts['wzb_jetpt50_zlep'] ='wzinc && !bVeto && METFixEE2017_pt>30 && tauVeto_wz && jetpt50 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && jeteta_exclude'
#cuts['wzb_jetpt30_PuppiMET_zlep'] ='wzinc && !bVeto && PuppiMETFixEE2017_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && jeteta_exclude'
