# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

supercut='nLepton>2'

## Signal regions

cuts['WZ_ee_mu'] = 'nMuon==1 && nElectron==2'

cuts['wzb_jetpt30_zlep'] ='nMuon==1 && nElectron==2 && wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
cuts['wzb_jetpt50_zlep'] ='nMuon==1 && nElectron==2 && wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt50 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
