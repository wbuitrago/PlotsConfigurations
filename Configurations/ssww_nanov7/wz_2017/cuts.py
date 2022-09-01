# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>2 && Alt$(Lepton_pt[3],-9999)<10'

## WZ regions

cuts['WZ'] ='(wzinc>0.5) && bVeto && MET_PT>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'
cuts['WZb'] ='(wzinc>0.5) && !bVeto && MET_PT>30 && tauVeto_wz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_wz'