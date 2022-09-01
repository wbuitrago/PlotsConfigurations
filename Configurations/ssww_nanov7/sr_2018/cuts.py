# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>1 && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 &&\
    abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 &&\
    tauVeto_ww && zveto_ww && lep0eta && lep1eta'

## Signal regions
cuts['SR'] = 'bVeto && jetpt30 && leppt_30_30 && MET_PT>30 && zlep_ww && mjj>500 && abs(detajj)>2.5'
cuts['BTAG'] = '(!bVeto) && jetpt30 && leppt_30_30 && MET_PT>30 && zlep_ww && mjj>500 && abs(detajj)>2.5'
