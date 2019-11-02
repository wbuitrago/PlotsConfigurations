import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}
bAlgo = 'DeepB'
bWP = '0.4941'

mc = [skey for skey in samples if skey not in ('Fake_lep_2016','Fake_lep_2017','Fake_lep_2018','Fake_lep','DATA_2016', 'DATA_2017', 'DATA_2018','DATA')]
# tau veto
aliases['tauVeto_ww'] = {
    'expr': '(Sum$(Tau_pt > 18 && Tau_rawIso >=1 && sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-pi)-pi, 2) ) >= 0.3) == 0)'
}
aliases['tauVeto_wz'] = {
    'expr': '(Sum$(Tau_pt > 18 && Tau_rawIso >=1 && sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Tau_eta - Lepton_eta[2], 2) + pow(abs(abs(Tau_phi - Lepton_phi[2])-pi)-pi, 2) ) >= 0.3) == 0)'
}
aliases['tauVeto_zz'] = {
    'expr': '(Sum$(Tau_pt > 18 && Tau_rawIso >=1 && sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Tau_eta - Lepton_eta[2], 2) + pow(abs(abs(Tau_phi - Lepton_phi[2])-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Tau_eta - Lepton_eta[3], 2) + pow(abs(abs(Tau_phi - Lepton_phi[3])-pi)-pi, 2) ) >= 0.3) == 0)'
}
# lepton sf
#eleWP = 'mvaFall17V2Iso_WP90_SS'
eleWP = 'mvaFall17Iso_WP90_SS'

muWP = 'cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}
# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    #'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_4l',
    'samples': ['Fake_lep']
}
# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}
aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

#bjet
# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}

# B tagging

aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'
}


# lepton eta range
aliases['lep0eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[0],-9999))==11 && abs(Alt$(Lepton_eta[0],-9999.)) <=2.5) || (abs(Alt$(Lepton_pdgId[0],-9999))==13 && abs(Alt$(Lepton_eta[0],-9999.)) <=2.4))'
}
aliases['lep1eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[1],-9999))==11 && abs(Alt$(Lepton_eta[1],-9999.)) <=2.5) || (abs(Alt$(Lepton_pdgId[1],-9999))==13 && abs(Alt$(Lepton_eta[1],-9999.)) <=2.4))'
}
aliases['lep2eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[2],-9999))==11 && abs(Alt$(Lepton_eta[2],-9999.)) <=2.5) || (abs(Alt$(Lepton_pdgId[2],-9999))==13 && abs(Alt$(Lepton_eta[2],-9999.)) <=2.4))'
}
aliases['lep3eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[3],-9999))==11 && abs(Alt$(Lepton_eta[3],-9999.)) <=2.5) || (abs(Alt$(Lepton_pdgId[3],-9999))==13 && abs(Alt$(Lepton_eta[3],-9999.)) <=2.4))'
}
aliases['jetpt30']={
    'expr': 'Alt$(CleanJet_pt[0],-9999.) >30 && Alt$(CleanJet_pt[1],-9999.) >30'
}
aliases['jetpt50']={
    'expr': 'Alt$(CleanJet_pt[0],-9999.) >50 && Alt$(CleanJet_pt[1],-9999.) >50'
}
aliases['leppt0']={
    'expr': 'Alt$(Lepton_pt[0],-9999.) >25 && Alt$(Lepton_pt[1],-9999.) >20'
}
aliases['leppt30']={
    'expr': 'Alt$(Lepton_pt[0],-9999.) >30 && Alt$(Lepton_pt[1],-9999.) >30'
}

# ssww region
aliases['zlep_ww']={
    'expr': 'abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75 && abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75'
}
aliases['zveto_ww']={
    'expr': '(abs(Alt$(Lepton_pdgId[0],-9999)) * abs(Alt$(Lepton_pdgId[1],-9999)) != 11*11 || abs(mll - 91.1876) > 15)'
}
aliases['ssww_region']={
    #'expr': 'nLepton>1 && nCleanJet >1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0 && Alt$(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(detajj) > 2.5 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && zveto_ww && lep0eta && lep1eta && zlep_ww'  # pt zlep
    #'expr': 'nLepton>1 && nCleanJet >1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0 && Alt$(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && zveto_ww && lep0eta && lep1eta'  # pt zlep
    'expr': 'nLepton>1 && nCleanJet >1 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0 && Alt$(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && zveto_ww && lep0eta && lep1eta'  # pt zlep
}
# wz region
aliases['ztag_wz']={
    'expr': '((Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999)==0 && abs(mll-91.1876)<15)||(Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[2],-9999)==0 && abs(mllOneThree-91.1876)<15)||(Alt$(Lepton_pdgId[1],-9999) + Alt$(Lepton_pdgId[2],-9999)==0 && abs(mllTwoThree-91.1876)<15))'  # bjet pt zlep
}
aliases['pid_wz']={
    'expr': '(abs(Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999)+Alt$(Lepton_pdgId[2],-9999)) == 11||abs(Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999)+Alt$(Lepton_pdgId[2],-9999)) == 13)'
}
aliases['zlep_wz']={
    'expr': 'abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 1 && abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 1 && abs((Alt$(Lepton_eta[2],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) <1'
}
aliases['wz_region']={
    'expr': 'nLepton>2 && nCleanJet >1 && MET_pt>30 && WH3l_mlll>100 && mjj > 500 && abs(detajj) > 2.5 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_wz && ztag_wz && pid_wz && zlep_wz && lep0eta && lep1eta && lep2eta'  # bjet pt
}
# zz region
aliases['ztag_zz']={
    'expr': 'abs(z0Mass_zh4l-91.1876) < 15 && abs(z1Mass_zh4l-91.1876) < 15'
}
aliases['zlep_zz']={
    'expr': 'abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75 && abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75 && abs((Alt$(Lepton_eta[2],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) <0.75 && abs((Alt$(Lepton_eta[3],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) <0.75'
}
aliases['zz_region']={
    'expr': 'nLepton>3 && nCleanJet >1 && MET_pt>30 && mjj > 500 && abs(detajj) > 2.5 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && lep0eta && lep1eta && lep2eta && lep3eta && ztag_zz && zlep_zz'  # pt
}

# B tag scale factors

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/btagsfpatch.cc+' % configurations
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
    'samples': mc
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto || zeroJet)*bVetoSF + (!zeroJet)*bReqSF',
    #'expr': '(bVeto || (ssww_region && zeroJet))*bVetoSF + (ssww_region && !zeroJet)*bReqSF',
    #'expr': '(bVeto || (wz_region && zeroJet))*bVetoSF + (wz_region && !zeroJet)*bReqSF',
    #'expr': '(bVeto || (zz_region && zeroJet))*bVetoSF + (zz_region && !zeroJet)*bReqSF',
    'samples': mc
}

for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + shift),
        'samples': mc
    }
    aliases['Jet_btagSF_shapeFix_down_%s' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + shift),
        'samples': mc
    }

    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF', 'PrefireWeight']),
    #'expr': 'LepWPCut',
    'samples': mc
}
