# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

## Signal regions

supercut='nLepton>2 && \
          (abs(Alt$(Lepton_pdgId[0],9999))==11 && abs(Alt$(Lepton_pdgId[1],9999))==11 && abs(Alt$(Lepton_pdgId[2],9999))==13)  || \
          (abs(Alt$(Lepton_pdgId[0],9999))==13 && abs(Alt$(Lepton_pdgId[1],9999))==11 && abs(Alt$(Lepton_pdgId[2],9999))==11) || \
          (abs(Alt$(Lepton_pdgId[0],9999))==11 && abs(Alt$(Lepton_pdgId[1],9999))==13 && abs(Alt$(Lepton_pdgId[2],9999))==11)'

## Signal regions

cuts['SR'] = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj>400 && zlep_wz'
cuts['CR'] = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj<400 && zlep_wz'
# cuts['CR_200'] = 'wzinc && bVeto && MET_pt>20 && tauVeto_wz && jetpt_opt && abs(detajj)>1.5 && mjj<400 && mjj>200 && zlep_wz'
