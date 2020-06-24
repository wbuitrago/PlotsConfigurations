# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>2'

## Signal regions

#cuts['loosewz'] ='wzinc && bVeto && MET_pt>30 && tauVeto_wz'
#cuts['loosewz_HEM'] ='wzinc && bVeto && MET_pt>30 && tauVeto_wz && !HEM'
#cuts['loosewz_PuppiMET'] ='wzinc && bVeto && PuppiMET_pt>30 && tauVeto_wz'

#cuts['wz_jetpt30'] ='wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'
#cuts['wz_jetpt30_PuppiMET'] ='wzinc && bVeto && PuppiMET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'

cuts['wz_jetpt30_zlep'] ='wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
cuts['wz_jetpt50_zlep'] ='wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt50 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
#cuts['wz_jetpt30_zlep_HEM'] ='wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && !HEM'
#cuts['wz_jetpt30_PuppiMET_zlep'] ='wzinc && bVeto && PuppiMET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'

#cuts['wzb_jetpt30'] ='wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'
#cuts['wzb_jetpt30_PuppiMET'] ='wzinc && !bVeto && PuppiMET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500'

cuts['wzb_jetpt30_zlep'] ='wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
cuts['wzb_jetpt50_zlep'] ='wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt50 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
#cuts['wzb_jetpt30_zlep_HEM'] ='wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz && !HEM'
#cuts['wzb_jetpt30_PuppiMET_zlep'] ='wzinc && !bVeto && PuppiMET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
