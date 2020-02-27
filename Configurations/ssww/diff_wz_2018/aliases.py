import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}
bAlgo = 'DeepB'
bWP = '0.4184'

aliases['wzinc'] = {
    'linesToAdd': ['.L %s/ssww/diff_wz_2018/wzinc.cc+' % configurations],
    'class': 'Wzinc',
}
aliases['zz'] = {
    'linesToAdd': ['.L %s/ssww/diff_wz_2018/zz.cc+' % configurations],
    'class': 'Zz',
}
mc = [skey for skey in samples if skey not in ('Fake_lep_2016','Fake_lep_2017','Fake_lep_2018','Fake_lep','DATA_2016', 'DATA_2017', 'DATA_2018','DATA')]

aliases['softmuon_veto']={
    'expr':'(Sum$(abs(Muon_dxy)<0.02 && abs(Muon_dz)<0.1 && Muon_softId && Muon_pt>5 && abs(Muon_eta)<2.4 && sqrt( pow(Muon_eta - Lepton_eta[0], 2) + pow(abs(abs(Muon_phi - Lepton_phi[0])-pi)-pi, 2) ) >= 0.4 && sqrt( pow(Muon_eta - Lepton_eta[1], 2) + pow(abs(abs(Muon_phi - Lepton_phi[1])-pi)-pi, 2) ) >= 0.4 && sqrt( pow(Muon_eta - Lepton_eta[2], 2) + pow(abs(abs(Muon_phi - Lepton_phi[2])-pi)-pi, 2) ) >= 0.4)==0)'
}
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': ['VgS','VgS1','VgS2']
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': ['VgS','VgS1','VgS2']
}
# lepton sf
#eleWP = 'mvaFall17V2Iso_WP90_SS'
eleWP = 'mvaFall17V1Iso_WP90_SS'

muWP = 'cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut3l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}
# Fake leptons transfer factor
aliases['fakeW'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l',
    'samples': ['Fake_lep']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElUp',
    'samples': ['Fake_lep']
}
aliases['fakeWEleDown'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElDown',
    'samples': ['Fake_lep']
}
aliases['fakeWMuUp'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWMuDown'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleUp'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatEleDown'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElDown',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuUp'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuUp',
    'samples': ['Fake_lep']
}
aliases['fakeWStatMuDown'] = {
    #'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuDown',
    'samples': ['Fake_lep']
}
# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch3l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]*Lepton_promptgenmatched[2], 0)',
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

# ==1 jet with pt > 30 GeV
aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) < 30.'
}

# ==2 jets with pt > 30 GeV
aliases['twoJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) >= 30. && Alt$(CleanJet_pt[2], 0) < 30.'
}

# >=2 jets with pt > 30 GeV
aliases['twoJetOrMore'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) >= 30.'
}


aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.7527) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.7527) >= 1'
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
    'expr': '((abs(Alt$(Lepton_pdgId[0],-9999))==11 && abs(Alt$(Lepton_eta[0],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[0],-9999))==13 && abs(Alt$(Lepton_eta[0],-9999.)) <2.4))'
}
aliases['lep1eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[1],-9999))==11 && abs(Alt$(Lepton_eta[1],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[1],-9999))==13 && abs(Alt$(Lepton_eta[1],-9999.)) <2.4))'
}
aliases['lep2eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[2],-9999))==11 && abs(Alt$(Lepton_eta[2],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[2],-9999))==13 && abs(Alt$(Lepton_eta[2],-9999.)) <2.4))'
}
aliases['lep3eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[3],-9999))==11 && abs(Alt$(Lepton_eta[3],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[3],-9999))==13 && abs(Alt$(Lepton_eta[3],-9999.)) <2.4))'
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
aliases['leppt25_wz']={
    'expr': 'Alt$(Lepton_pt[0],-9999.) >25 && Alt$(Lepton_pt[1],-9999.) >20 && Alt$(Lepton_pt[2],-9999.) >10 && Alt$(Lepton_pt[3],-9999.) <10'#Alt$(Lepton_pt[2],-9999.) >10'
}
aliases['leppt30_wz']={
    'expr': 'Alt$(Lepton_pt[0],-9999.) >30 && Alt$(Lepton_pt[1],-9999.) >30 && Alt$(Lepton_pt[2],-9999.) >10 && Alt$(Lepton_pt[3],-9999.) <10'#Alt$(Lepton_pt[2],-9999.) >10'
}
aliases['jet_cuts']={
    'expr': 'nCleanJet >1 && abs(detajj) > 2.5 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7'
}
aliases['EEE']={
    'expr': 'abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==11*11*11'
}
aliases['MEE']={
    'expr': 'abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*11*11'
}
aliases['MME']={
    'expr': 'abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*11'
}
aliases['MMM']={
    'expr': 'abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*13'
}
# wz region
aliases['ztag_wz']={
    'expr': '((Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999)==0 && abs(mll-91.1876)<15)||(Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[2],-9999)==0 && abs(mllOneThree-91.1876)<15)||(Alt$(Lepton_pdgId[1],-9999) + Alt$(Lepton_pdgId[2],-9999)==0 && abs(mllTwoThree-91.1876)<15))'  # bjet pt zlep
}
aliases['mll_cut_wz']={
    'expr': '((Alt$(Lepton_pdgId[0],-9999)*Alt$(Lepton_pdgId[1],-9999)>0 || mll>4)&&(Alt$(Lepton_pdgId[0],-9999)*Alt$(Lepton_pdgId[2],-9999)>0 || mllOneThree>4)&&(Alt$(Lepton_pdgId[1],-9999)*Alt$(Lepton_pdgId[2],-9999)>0|| mllTwoThree>4))'  # bjet pt zlep
}
aliases['pid_wz']={
    'expr': 'abs(Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999)+Alt$(Lepton_pdgId[2],-9999)) < 33'
}
aliases['zlep_wz']={
    'expr': 'abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75 && abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75'# && abs((Alt$(Lepton_eta[2],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) <0.5'
}
aliases['wz_region']={
    'expr': 'nLepton>2 && MET_pt>30 && lep0eta && lep1eta && lep2eta && ztag_wz && softmuon_veto'  # bjet pt
}
# B tag scale factors

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')

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
    #'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btag0SF'] = {
    #'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5))))',
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagnSF'] = {
    #'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': 'bVetoSF*bVeto + btag0SF*btag0 + btagnSF*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)',
    'samples': mc
}

for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
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

    for targ in ['bVeto', 'btag0', 'btagn']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        #alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        #alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': 'bVetoSF{shift}up*bVeto + btag0SF{shift}up*btag0 + btagnSF{shift}up*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': 'bVetoSF{shift}down*bVeto + btag0SF{shift}down*btag0 + btagnSF{shift}down*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
        'samples': mc
    }

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight3l','LepSF3l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','XSWeight','METFilter_MC','btagSF']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    #'expr': 'LepWPCut',
    'samples': mc
}
# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Do',
    'samples': mc
}
