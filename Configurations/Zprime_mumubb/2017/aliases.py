import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2017
configurations = os.path.dirname(configurations) # VBF_Zjj 
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA', 'Dyemb')]
mc_emb = [skey for skey in samples if skey not in ('Fake', 'DATA')]
btag_algo="deepflav"#deepcsv


eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW_tthmva_80'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc_emb + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

aliases['embedtotal'] = {
    'expr': 'embed_total_WP90V1',  # wrt. eleWP
    'samples': 'Dyemb'
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/Differential/ngenjet.cc+' % configurations],
    'class': 'CountGenJet',
    'samples': mc
}

##### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'getGenZpt',
    'samples': ['DY']
}
handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2017']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2017']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

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

if btag_algo=="deepcsv":
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
    }
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'
    }
  
elif btag_algo=="deepflav":
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0521) == 0'
    }
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0521) >= 1'
    }


# CR definitions

aliases['topcr'] = {
    'expr': 'mll>50 && ((zeroJet && !bVeto) || bReq)'
}

aliases['dycr'] = {
    'expr': 'bVeto && abs(mll-90)<15'

}

aliases['wwcr'] = {
    'expr': 'mth>60 && mtw2>30 && mll>100 && bVeto'
}

# SR definition

aliases['sr'] = {
    'expr': '(bVeto) && PuppiMET_pt<100 && detajj>2.0 && (abs(mll-90)<15)'
}

aliases['LowZ'] = {
    'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) < 1',
}

aliases['HighZ'] = {
    'expr':  '0.5*abs((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1])) >= 1',
}

aliases['hardJets'] = {
    'expr':  'Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 25 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 25', 
    'samples': ['DY']
}

aliases['PUJets'] = {
    'expr':  '!(Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 25 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 25)',
    'samples': ['DY']
}

# B tag scale factors
if btag_algo=="deepcsv":

    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['btagSF'] = {
        'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
        'samples': mc
    }
    
    for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
        for targ in ['bVeto', 'bReq']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_up_%s' % shift)
    
            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_down_%s' % shift)
    
        aliases['btagSF%sup' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
            'samples': mc
        }
    
        aliases['btagSF%sdown' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
            'samples': mc
        }

elif btag_algo=="deepflav":
    btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepFlavour_94XSF_V4_B_F.csv' % os.getenv('CMSSW_BASE')  # ---> dove e'???? #FIXME
    #btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepFlavour_94XSF_V3_B_F.csv' % os.getenv('CMSSW_BASE')
    #cd PhysicsTools/NanoAODTools/data/btagSF/
    #wget https://twiki.cern.ch/twiki/pub/CMS/BtagRecommendation94X/DeepFlavour_94XSF_V4_B_F.csv
    #cp /afs/cern.ch/user/g/gpizzati/public/btagSF/DeepFlavour_94XSF_V4_B_F.csv .
    
    aliases['Jet_btagSF_deepflav_shape'] = {
        'linesToAdd': [
            'gSystem->Load("libCondFormatsBTauObjects.so");',
            'gSystem->Load("libCondToolsBTau.so");',
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L %s/patches/btagsfpatch.cc+' % configurations
        ],
        'class': 'BtagSF',
        'args': (btagSFSource,'central','deepjet'),
        'samples': mc
    }
    
    
    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['btagSF'] = {
        'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
        'samples': mc
    }
    
    for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
        aliases['Jet_btagSF_deepflav_shape_up_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'up_' + shift,'deepjet'),
            'samples': mc
        }
        aliases['Jet_btagSF_deepflav_shape_down_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'down_' + shift,'deepjet'),
            'samples': mc
        }
    
        for targ in ['bVeto', 'bReq']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_up_%s' % shift)
    
            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_down_%s' % shift)
    
        aliases['btagSF%sup' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
            'samples': mc
        }
    
        aliases['btagSF%sdown' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
            'samples': mc
        }

aliases['Jet_PUIDSF'] = { 
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
  'samples': mc
}

aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
  'samples': mc
}

aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
  'samples': mc
}


# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepWPCut', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'btagSF', 'PrefireWeight','Jet_PUIDSF']),
    'samples': mc
}

# Muon ttHMVA SF needed for tau embedded samples
aliases['Muon_ttHMVA_SF'] = {
    'expr': '( (abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_cut_Tight_HWWW_tthmva_80_IdIsoSF[0]/Lepton_tightMuon_cut_Tight_HWWW_IdIsoSF[0])+(abs(Lepton_pdgId[0]) == 11) )*( (abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_cut_Tight_HWWW_tthmva_80_IdIsoSF[1]/Lepton_tightMuon_cut_Tight_HWWW_IdIsoSF[1])+ (abs(Lepton_pdgId[1]) == 11) )',
    'samples' : ['Dyemb']
}

# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc_emb
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc_emb
}

# Needed for top QCD scale uncertainty
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

aliases['lhe_mjj'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[4] * LHEPart_pt[5] * (TMath::CosH(LHEPart_eta[4] - LHEPart_eta[5]) - TMath::Cos(LHEPart_phi[4] - LHEPart_phi[5])))',
    'samples': ['Zjj']
}
