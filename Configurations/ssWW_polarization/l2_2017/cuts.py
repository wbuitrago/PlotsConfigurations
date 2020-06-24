# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>1 && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 &&\
    abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 &&\
    tauVeto_ww && zveto_ww && lep0eta && lep1eta && \
    mll > 20 && mjj > 100'

## Signal regions

#cuts['ssww_leppt0_jetpt30'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
cuts['ssww_leppt1_jetpt30'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['ssww_leppt1_jetpt30_alleta'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt1_jetpt30_softmuon_veto'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude && softmuon_veto'
#cuts['ssww_leppt0_jetpt50'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['ssww_leppt0_jetpt50_alleta'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt0_jetpt50_softmuon_veto'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto && jeteta_exclude'
cuts['ssww_leppt1_jetpt50'] = 'METFixEE2017_pt>30 && zlep_ww && bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'

#cuts['ssww_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['ssww_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['ssww_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['ssww_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'

#cuts['nonprompt_leppt0_jetpt30'] = 'METFixEE2017_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
cuts['nonprompt_leppt1_jetpt30'] = 'METFixEE2017_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['nonprompt_leppt1_jetpt30_softmuon_veto'] = 'METFixEE2017_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude && softmuon_veto'
#cuts['nonprompt_leppt0_jetpt50'] = 'METFixEE2017_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['nonprompt_leppt0_jetpt50_softmuon_veto'] = 'METFixEE2017_pt>30 && zlep_ww && (!softmuon_veto || !bVeto) && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
cuts['nonprompt_leppt1_jetpt50'] = 'METFixEE2017_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'

#cuts['nonprompt_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['nonprompt_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['nonprompt_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'
#cuts['nonprompt_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5 && jeteta_exclude'

#cuts['loosedijet_leppt0_jetpt30'] = 'METFixEE2017_pt>30 && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'
#cuts['loosedijet_leppt1_jetpt30'] = 'METFixEE2017_pt>30 && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'
#uts['loosedijet_leppt1_jetpt30_softmuon_veto'] = 'METFixEE2017_pt>30 && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude && softmuon_veto'
#cuts['loosedijet_leppt0_jetpt50'] = 'METFixEE2017_pt>30 && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'
#cuts['loosedijet_leppt0_jetpt50_softmuon_veto'] = 'METFixEE2017_pt>30 && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && softmuon_veto && jeteta_exclude'
#cuts['loosedijet_leppt1_jetpt50'] = 'METFixEE2017_pt>30 && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'

#cuts['loosedijet_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'
#cuts['loosedijet_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'
#cuts['loosedijet_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'
#cuts['loosedijet_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && jeteta_exclude'

#cuts['lowmjj_leppt0_jetpt30'] = 'MET_pt>30 && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt1_jetpt30'] = 'MET_pt>30 && zlep_ww && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt0_jetpt50'] = 'MET_pt>30 && zlep_ww && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt0_jetpt50_softmuon_veto'] = 'MET_pt>30 && zlep_ww && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && softmuon_veto'
#cuts['lowmjj_leppt1_jetpt50'] = 'MET_pt>30 && zlep_ww && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'

#cuts['lowmjj_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
