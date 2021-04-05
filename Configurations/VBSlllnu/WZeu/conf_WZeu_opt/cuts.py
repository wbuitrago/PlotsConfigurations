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

cuts['wz_jetpt30_zlep'] = 'wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj)>2.5 && mjj>500 && zlep_wz'
cuts['wz_jetpt50_zlep'] = 'wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt50 && abs(detajj)>2.5 && mjj>500 && zlep_wz'

cuts['cut_1'] = 'wzinc1 && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj)>2.5 && mjj>500 && zlep_wz'
cuts['cut_2'] = 'wzinc && bVeto && tauVeto_wz && jetpt30 && abs(detajj)>2.5 && mjj>500 && zlep_wz'
cuts['cut_3'] = 'wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj)>1.5 && mjj>500 && zlep_wz'
cuts['cut_4'] = 'wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj)>2.5 && mjj>300 && zlep_wz'
cuts['cut_5'] = 'wzinc && bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj)>2.5 && mjj>500'
cuts['cut_6'] = 'wzinc && bVeto && MET_pt>30 && tauVeto_wz && firstjetpt50 && abs(detajj)>2.5 && mjj>500'

cuts['wzb_jetpt30_zlep'] = 'wzinc && !bVeto && MET_pt>30 && tauVeto_wz && jetpt30 && abs(detajj)>2.5 && mjj>500 && zlep_wz'
