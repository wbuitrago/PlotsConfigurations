import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2018
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
    'expr': '('+DYrew['2018']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2018']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
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
if btag_algo == "deepcsv": 
  aliases['bVeto'] = {
      'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0'
  }

  aliases['bReq'] = {
      'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1'
  }
elif btag_algo == "deepflav":
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0494) == 0'
    }        
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0494) >= 1'
    }

# Flavour definitions

aliases['SameFlav'] = {
    'expr': '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
    'samples': mc
}

aliases['DiffFlav'] = {
    'expr': 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'samples': mc
}

# CR definitions

aliases['topcr'] = {
    #'expr': 'mtw2>30 && mll>50 && ((zeroJet && !bVeto) || bReq)'
    'expr': '!bVeto'
}

aliases['wwcr'] = {
    'expr': 'bVeto && PuppiMET_pt>100'
}

aliases['dycr'] = {
    'expr': 'bVeto && PuppiMET_pt<=100 && detajj<3'
}
aliases['dypucr'] = {
    'expr': 'bVeto && PuppiMET_pt<=100 && detajj>=3 && ptll<60'
}



# SR definition

aliases['sr'] = {
    #'expr': 'mth>60 && mtw2>30 && bVeto'
    'expr': 'bVeto && PuppiMET_pt<=100 && detajj>=3 && ptll>60'
}
aliases['ZeppenfeldDilepton'] = {
    'expr' : '(0.5*((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1]))/TMath::Abs(CleanJet_eta[0] - CleanJet_eta[1]))'
}
aliases['ZeppenfeldLeadingLepton'] = {
    'expr' : '(Lepton_eta[0] - 0.5*(CleanJet_eta[0] + CleanJet_eta[1]))/abs(CleanJet_eta[0] - CleanJet_eta[1])'
}

aliases['LowZ'] = {
    'expr':  'abs(ZeppenfeldDilepton) < 0.5'        
}

aliases['HighZ'] = {
    'expr':  'abs(ZeppenfeldDilepton) >=1.5'
}

aliases['hardJets'] = {
    'expr':  'Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 25 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 25',
    'samples': ['DY']
}

aliases['PUJets'] = {
    'expr':  '!(Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 25 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 25)',
    'samples': ['DY']
}
aliases['Lepton_eta1'] = {
    'expr': 'Alt$(Lepton_eta[0],-9999.)'
}
aliases['Lepton_eta2'] = {
    'expr': 'Alt$(Lepton_eta[1],-9999.)'
}
aliases['deltaphill'] = {
    # 'expr': 'abs(Lepton_phi[0]-Lepton_phi[1])'
    'expr': 'TMath::Abs(Alt$(Lepton_phi[0],-9999.)-Alt$(Lepton_phi[1],-9999.))'
}
aliases['ZeppenfeldDilepton'] = {
    'expr' : '(0.5*((Lepton_eta[0] + Lepton_eta[1]) - (CleanJet_eta[0] + CleanJet_eta[1]))/abs(CleanJet_eta[0] - CleanJet_eta[1]))'
}

aliases['deltaetall'] = {
    # 'expr': 'abs(Lepton_eta[0]-Lepton_eta[1])' 
    'expr': 'TMath::Abs(Alt$(Lepton_eta[0],-9999.)-Alt$(Lepton_eta[1],-9999.))'
}

aliases['met'] = {
    'expr': 'PuppiMET_pt'
}

aliases['ptj1'] = {
    # 'expr': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99'
    'expr': 'Alt$(CleanJet_pt[0],-9999.)'
}

aliases['deltaphijj'] = {
    #'expr': 'abs(CleanJet_phi[0]-CleanJet_phi[1])'
    'expr': 'TMath::Abs(Alt$(CleanJet_phi[0],-9999.)-Alt$(CleanJet_phi[1],-9999.))'
}

aliases['R_j1l1'] = {
    'expr':  'TMath::Sqrt(TMath::Power(CleanJet_eta[0]-Lepton_eta[0],2)+TMath::Power(CleanJet_phi[0]-Lepton_phi[0],2))'
}
aliases['R_j2l1'] = {
    'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[0],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[0],2))'
}
aliases['R_j1l2'] = {
    'expr':  'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Lepton_phi[1],2))'
}
aliases['R_j2l2'] = {
    'expr': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[1],2))'
}
## DNN
model_notTop = "ovetrained_model/"
aliases['cut_index'] = {
    'expr': '(bVeto && multiJet && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)))'
}
folderpath = os.path.realpath(inspect.getfile(inspect.currentframe()))
folderpath =  os.path.dirname(folderpath)
#FIXME choose the correct model 
mva_reader_path = folderpath + '/mva/'
models_path = '/eos/home-g/gpizzati/SWAN_projects/ML_classification'

aliases['DNNoutput_notTop'] = {
    'class': 'MVAReader_notTop',
    'args': ( models_path + '/' + model_notTop, models_path + '/' + model_notTop + 'cumulative_signal_2018.root', False, 1),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mvareader_notTop.cc+', 
    ],
}
"""
aliases['DNNoutput_highZ'] = {
    'class': 'MVAReader_highZ',
    'args': ( models_path +'/sr/models/' + model_highZ, False, 1),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mvareader_highZ.cc+', 
    ],
}
"""
aliases['DNNoutput'] = {
     'expr': '(bVeto)*(DNNoutput_notTop)'
 }

# B tag scale factors
if btag_algo == "deepcsv":
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

elif btag_algo == "deepflav":
    btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepJet_102XSF_V2.csv' % os.getenv('CMSSW_BASE')
    aliases['Jet_btagSF_deepflav_shape'] = {
        'linesToAdd': [
            'gSystem->Load("libCondFormatsBTauObjects.so");',
            'gSystem->Load("libCondToolsBTau.so");',
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L %s/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+' % os.getenv('CMSSW_BASE') 
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
    'expr': ' * '.join(['SFweight2l', 'LepWPCut', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'btagSF', 'Jet_PUIDSF']),
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

# aliases['Weight2MINLO'] = {
#     'linesToAdd': ['.L %s/Differential/weight2MINLO.cc+' % configurations],
#     'class': 'Weight2MINLO',
#     'args': '%s/src/LatinoAnalysis/Gardener/python/data/powheg2minlo/NNLOPS_reweight.root' % os.getenv('CMSSW_BASE'),
#     'samples' : [skey for skey in samples if 'ggH_hww' in skey],
# }

# ## GGHUncertaintyProducer wasn't run for GluGluHToWWTo2L2Nu_Powheg_M125 
# thus = [
#     'ggH_mu',
#     'ggH_res',
#     'ggH_mig01',
#     'ggH_mig12',
#     'ggH_VBF2j',
#     'ggH_VBF3j',
#     'ggH_pT60',
#     'ggH_pT120',
#     'ggH_qmtop'
# ]

# for thu in thus:
#     aliases[thu+'_2'] = {
#         'linesToAdd': ['.L %s/Differential/gghuncertainty.cc+' % configurations],
#         'class': 'GGHUncertainty',
#         'args': (thu,),
#         'samples': ['ggH_hww']
#     }

aliases['lhe_mjj'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[4] * LHEPart_pt[5] * (TMath::CosH(LHEPart_eta[4] - LHEPart_eta[5]) - TMath::Cos(LHEPart_phi[4] - LHEPart_phi[5])))',
    'samples': ['Zjj']
}
