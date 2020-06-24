import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}
bAlgo = 'DeepB'
bWP = '0.4184'

mc = [skey for skey in samples if skey not in ('Fake_lep','DATA')]
# DNN reader
#dnn_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/ssww/sr2018_DNN/dnn/'
#models_path = '/eos/user/j/jixiao/latino/FullRun2/'
#aliases['DNNScore'] = {
#    'class': 'DNNScore',
#    'args': ( models_path +'ssww_leppt1_jetpt30/models/v31/', False),
#    'linesToAdd':[
#        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#        'gSystem->Load("libDNNEvaluator.so")',
#        '.L ' + dnn_reader_path + 'dnn_score.cc+',
#],
#}

# tau veto
aliases['tauVeto_ww'] = {
    'expr': '(Sum(Tau_pt > 18 && AbsVec(Tau_eta)<2.3 && (Tau_idMVAoldDM2017v2 >= 3) && Tau_idDecayMode &&sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(AbsVec(AbsVec(Tau_phi - Lepton_phi[0])-3.14159)-3.14159, 2) ) >= 0.4 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(AbsVec(AbsVec(Tau_phi - Lepton_phi[1])-3.14159)-3.14159, 2) ) >= 0.4) == 0)'
}
aliases['softmuon_veto']={
    'expr':'(Sum(AbsVec(Muon_dxy)<0.02 && AbsVec(Muon_dz)<0.1 && Muon_softId && Muon_pt>5 && AbsVec(Muon_eta)<2.4 && sqrt( pow(Muon_eta - Lepton_eta[0], 2) + pow(AbsVec(AbsVec(Muon_phi - Lepton_phi[0])-3.14159)-3.14159, 2) ) >= 0.4 && sqrt( pow(Muon_eta - Lepton_eta[1], 2) + pow(AbsVec(AbsVec(Muon_phi - Lepton_phi[1])-3.14159)-3.14159, 2) ) >= 0.4)==0)'
}
# chargeflip
#aliases['chargeflip_w'] = {
#    'linesToAdd': ['.L %s/ssww/l2_2018/mischarge_sf.cc+' % configurations],
#    'class': 'misID_sf',
#    'samples': mc,
#}
# chargeflip
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': ['VgS','VgS1','VgS2']
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': ['VgS','VgS1','VgS2']
}
# lepton sf
eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP = 'cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    #'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l',
    'samples': ['Fake_lep']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake_lep']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake_lep']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake_lep']
}
# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]',
    'samples': mc
}

#bjet
# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'CleanJet_pt[0] < 30.'
}

# ==1 jet with pt > 30 GeV
aliases['oneJet'] = {
    'expr': 'CleanJet_pt[0] >= 30. && CleanJet_pt[1] < 30.'
}

# ==2 jets with pt > 30 GeV
aliases['twoJet'] = {
    'expr': 'CleanJet_pt[0] >= 30. && CleanJet_pt[1] >= 30. && CleanJet_pt[2] < 30.'
}

# >=2 jets with pt > 30 GeV
aliases['twoJetOrMore'] = {
    'expr': 'CleanJet_pt[0] >= 30. && CleanJet_pt[1] >= 30.'
}


aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.4941) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.4941) >= 1'
}

aliases['btag0'] = {
    'expr': 'zeroJet && !bVeto'
}

aliases['btag1'] = {
    'expr': 'oneJet && bReq'
}

aliases['btag2'] = {
    'expr': 'twoJet && bReq'
}

# lepton eta range
aliases['lep0eta']={
    'expr': '((abs(Lepton_pdgId[0])==11 && abs(Lepton_eta[0]) <2.5) || (abs(Lepton_pdgId[0])==13 && abs(Lepton_eta[0]) <2.4))'
}
aliases['lep1eta']={
    'expr': '((abs(Lepton_pdgId[1])==11 && abs(Lepton_eta[1]) <2.5) || (abs(Lepton_pdgId[1])==13 && abs(Lepton_eta[1]) <2.4))'
}
aliases['jetpt30']={
    'expr': 'CleanJet_pt[0] >30 && CleanJet_pt[1]>30'
}
aliases['jetpt50']={
    'expr': 'CleanJet_pt[0] >50 && CleanJet_pt[1]>50'
}
aliases['leppt0']={
    'expr': 'Lepton_pt[0] >25 && Lepton_pt[1]>20'
}
aliases['leppt1']={
    'expr': 'Lepton_pt[0]>30 && Lepton_pt[1] >30'
}
# ssww region
aliases['zlep_ww']={
    'expr': 'abs((Lepton_eta[0] - (CleanJet_eta[0]+CleanJet_eta[1])/2)/detajj) < 0.75 && abs(Lepton_eta[1]-CleanJet_eta[0]+CleanJet_eta[1])/2)/detajj) < 0.75'
}
aliases['zveto_ww']={
    'expr': '(abs(Lepton_pdgId[0]) * abs(Lepton_pdgId[1]) != 11*11 || abs(mll - 91.1876) > 15)'
}
#aliases['ssww_region']={
#    'expr': 'nLepton>1 && nCleanJet >1 && Alt(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && AbsVec(Alt(CleanJet_eta[0],-9999.)) < 4.7&& AbsVec(Alt(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && zveto_ww && lep0eta && lep1eta'  # pt zlep mjj detajj
#}

# B tag scale factors

#btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')
#
#aliases['Jet_btagSF_shapeFix'] = {
#    'linesToAdd': [
#        'gSystem->Load("libCondFormatsBTauObjects.so");',
#        'gSystem->Load("libCondToolsBTau.so");',
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        '.L %s/patches/btagsfpatch.cc+' % configurations
#    ],
#    'class': 'BtagSF',
#    'args': (btagSFSource,),
#    'samples': mc
#}
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<20 || AbsVec(CleanJet_eta)>2.5))))',
    'samples': mc
}

#aliases['btag0SF'] = {
#    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && CleanJet_pt<30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<20 || CleanJet_pt>30 || AbsVec(CleanJet_eta)>2.5))))',
#    'samples': mc
#}
#
#aliases['btagnSF'] = {
#    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx) + (CleanJet_pt<30 || AbsVec(CleanJet_eta)>2.5))))',
#    'samples': mc
#}
#aliases['btagSF'] = {
#    'expr': 'bVetoSF*bVeto + btag0SF*btag0 + btagnSF*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)',
#    'samples': mc
#}
aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=30 || AbsVec(CleanJet_eta)>=2.5))))',
    'samples': mc
}
aliases['btagSF'] = {
    'expr': '(bVeto*bVetoSF + bReq*bReqSF + ( (!bVeto) && (!bReq) ))',
    'samples': mc
}
#for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
#    #aliases['Jet_btagSF_shape_up_%s' % shift] = {
#    #    'class': 'BtagSF',
#    #    'args': (btagSFSource, 'up_' + shift),
#    #    'samples': mc
#    #}
#    #aliases['Jet_btagSF_shape_down_%s' % shift] = {
#    #    'class': 'BtagSF',
#    #    'args': (btagSFSource, 'down_' + shift),
#    #    'samples': mc
#    #}
#
#    for targ in ['bVeto', 'btag0', 'btagn']:
#        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)
#
#        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)
#
#    aliases['btagSF%sup' % shift] = {
#        'expr': 'bVetoSF{shift}up*bVeto + btag0SF{shift}up*btag0 + btagnSF{shift}up*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
#        'samples': mc
#    }
#
#    aliases['btagSF%sdown' % shift] = {
#        'expr': 'bVetoSF{shift}down*bVeto + btag0SF{shift}down*btag0 + btagnSF{shift}down*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
#        'samples': mc
#    }
#
## data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l','LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','XSWeight','METFilter_MC','btagSF']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    #'expr': 'LepWPCut',
    'samples': mc
}
#aliases['mcCommonWeight_os'] = {
#    'expr': 'SFweight*PromptGenLepMatch2l*chargeflip_w*(Alt(Lepton_pdgId[0],-9999) * Alt(Lepton_pdgId[1],-9999) < 0)',#
#    'samples':mc
#}
## variations
#aliases['SFweightEleUp'] = {
#    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
#    'samples': mc
#}
#aliases['SFweightEleDown'] = {
#    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
#    'samples': mc
#}
#aliases['SFweightMuUp'] = {
#    'expr': 'LepSF2l__mu_'+muWP+'__Up',
#    'samples': mc
#}
#aliases['SFweightMuDown'] = {
#    'expr': 'LepSF2l__mu_'+muWP+'__Do',
#    'samples': mc
#}