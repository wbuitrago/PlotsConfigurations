# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

## Signal regions

supercut='nLepton>2'

cuts['SR_3l']    = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj>400 && zlep_wz'
cuts['SR_2e_mu'] = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj>400 && zlep_wz && 2e_mu'
cuts['SR_2mu_e'] = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj>400 && zlep_wz && 2mu_e'
cuts['SR_3e']    = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj>400 && zlep_wz && 3e'
cuts['SR_3mu']   = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj>400 && zlep_wz && 3mu'
cuts['CR']       = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj>100 && mjj<400 && zlep_wz'
