# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


cuts["supercut"] ={
    'expr'   : '(\
        nLepton>1 && nCleanJet >1 && Alt(Lepton_pt,2,-999.)<10 &&\
        abs(Alt(CleanJet_eta,0,999)) < 4.7&& abs(Alt(CleanJet_eta,1,999)) < 4.7 &&\
        tauVeto_ww && \
        (abs(Lepton_pdgId[0]) * abs(Lepton_pdgId[1]) != 11*11 || abs(mll - 91.1876) > 15) && \
        ((abs(Lepton_pdgId[0])==11 && abs(Lepton_eta[0]) <2.5) || (abs(Lepton_pdgId[0])==13 && abs(Lepton_eta[0]) <2.4)) && \
        ((abs(Lepton_pdgId[1])==11 && abs(Lepton_eta[1]) <2.5) || (abs(Lepton_pdgId[1])==13 && abs(Lepton_eta[1]) <2.4)) && \
        mll > 20 && mjj > 100\
    )',
    'parent' : None,
    'doVars' : False,
    'doNumpy': False
}
## Signal regions
cuts['ssww_leppt1_jetpt30']={
    'expr'   : '(\
        MET_pt>30 && bVeto && \
        Alt(CleanJet_pt,0,-999.) >30 && Alt(CleanJet_pt,1,-999.) >30 && \
        Lepton_pt[0] >30 && Lepton_pt[1] >30 && \
        mjj > 500 && abs(detajj)>2.5\
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
