# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


cuts["supercut"] ={
    'expr'   : '(\
        nLepton>0 && nCleanJet >3 && Alt(Lepton_pt,1,-999.)<10 &&\
        abs(jet1_eta) < 4.7&& abs(jet2_eta) < 4.7 &&\
        tauVeto_ww && \
        ((abs(Lepton_pdgId[0])==11 && abs(Lepton_eta[0]) <2.5) || (abs(Lepton_pdgId[0])==13 && abs(Lepton_eta[0]) <2.4)) && \
        abs(bjet_eta) <2.5 && \
        mlb > 20 && mj1j2 > 100 && \
        (abs(jet1_eta) < 2.65 || abs(jet1_eta)>3.139) && (abs(jet2_eta) < 2.65 || abs(jet2_eta)>3.139)\
    )',
    'parent' : None,
    'doVars' : False,
    'doNumpy': False
}
## Signal regions
cuts['ssww_leppt1_jetpt30']={
    'expr'   : '(\
        METFixEE2017_pt>30 && bReq && \
        jet1_pt >30 && jet2_pt >30 && \
        Lepton_pt[0] >30 && bjet_pt >30 && \
        mj1j2 > 500 && abs(detaj1j2)>2.5\
    )',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
}
#cuts['ssww_leppt0_jetpt30'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt0_jetpt30'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto'
#cuts['ssww_leppt1_jetpt30'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt1_jetpt30_softmuon_veto'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto'
#cuts['ssww_leppt0_jetpt50'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt0_jetpt50_softmuon_veto'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto'
#cuts['ssww_leppt0_jetpt50_HEM'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5 && !HEM'
#cuts['ssww_leppt1_jetpt50'] = 'MET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5'

#cuts['ssww_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['ssww_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5'

#cuts['nonprompt_leppt0_jetpt30'] = 'MET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt0_jetpt30_softmuon_veto'] = 'MET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto'
#cuts['nonprompt_leppt1_jetpt30'] = 'MET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt1_jetpt30_softmuon_veto'] = 'MET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5 && softmuon_veto'
#cuts['nonprompt_leppt0_jetpt50'] = 'MET_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt0_jetpt50_softmuon_veto'] = 'MET_pt>30 && zlep_ww && (!softmuon_veto || !bVeto) && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt0_jetpt50_HEM'] = 'MET_pt>30 && zlep_ww && !HEM && !bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt1_jetpt50'] = 'MET_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5'

#cuts['nonprompt_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt30 && leppt1 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt0 && mjj > 500 && abs(detajj)>2.5'
#cuts['nonprompt_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && !bVeto && jetpt50 && leppt1 && mjj > 500 && abs(detajj)>2.5'

#cuts['loosedijet_leppt0_jetpt30'] = 'MET_pt>30 && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['loosedijet_leppt1_jetpt30'] = 'MET_pt>30 && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['loosedijet_leppt0_jetpt50'] = 'MET_pt>30 && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['loosedijet_leppt0_jetpt50_softmuon_veto'] = 'MET_pt>30 && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && softmuon_veto'
#cuts['loosedijet_leppt0_jetpt50_HEM'] = 'MET_pt>30 && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && !HEM'
#cuts['loosedijet_leppt1_jetpt50'] = 'MET_pt>30 && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'

#cuts['loosedijet_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['loosedijet_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['loosedijet_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['loosedijet_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'

#cuts['lowmjj_leppt0_jetpt30'] = 'MET_pt>30 && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt1_jetpt30'] = 'MET_pt>30 && zlep_ww && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt0_jetpt50'] = 'MET_pt>30 && zlep_ww && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt0_jetpt50_softmuon_veto'] = 'MET_pt>30 && zlep_ww && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww) && softmuon_veto'
#cuts['lowmjj_leppt1_jetpt50'] = 'MET_pt>30 && zlep_ww && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'

#cuts['lowmjj_leppt0_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt30 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt1_jetpt30_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt30 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt0_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt50 && leppt0 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
#cuts['lowmjj_leppt1_jetpt50_PuppiMET'] = 'PuppiMET_pt>30 && zlep_ww && jetpt50 && leppt1 && mjj > 500 && !(abs(detajj)>2.5 && zlep_ww)'
