# # nuisances
# #FIXME: TO BE UPDATED FOR 2018!

# # name of samples here must match keys in samples.py 

mc =["DY", "top", "VV", "VVV", "VBF-V", "top","Vg", "VgS", "VBS","Wjets_HT"]


# phase_spaces_boost = []
# phase_spaces_res = []

# for d in ["all","high","low", "all_lowvtx", "all_loweta", "all_higheta"]:
#     for cat in ["sig", "wjetcr", "topcr"]:
#         phase_spaces_boost.append("boost_{}_dnn{}".format(cat, d))
#         phase_spaces_res.append("res_{}_dnn{}".format(cat, d))


# phase_spaces_res_ele = [ ph+"_ele" for ph in phase_spaces_res]
# phase_spaces_res_mu = [ ph+"_mu" for ph in phase_spaces_res]
# phase_spaces_boost_ele = [ ph+"_ele" for ph in phase_spaces_boost]
# phase_spaces_boost_mu = [ ph+"_mu" for ph in phase_spaces_boost]

# phase_spaces_tot_ele = phase_spaces_res_ele + phase_spaces_boost_ele
# phase_spaces_tot_mu = phase_spaces_res_mu + phase_spaces_boost_mu
# phase_spaces_tot_res = phase_spaces_res_ele + phase_spaces_res_mu
# phase_spaces_tot_boost = phase_spaces_boost_ele + phase_spaces_boost_mu

# phase_spaces_dict = {"boost": phase_spaces_boost, "res": phase_spaces_res}
# phase_spaces_tot = phase_spaces_tot_ele + phase_spaces_tot_mu


# ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# #### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['top', "Wjets_HT"])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['top',"Wjets_HT"])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['top',"Wjets_HT"])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['top',"Wjets_HT"])
}



# #### FAKES

# if Nlep == '2' :
#   # already divided by central values in formulas !
#   fakeW_EleUp       = fakeW+'_EleUp'
#   fakeW_EleDown     = fakeW+'_EleDown'
#   fakeW_MuUp        = fakeW+'_MuUp'
#   fakeW_MuDown      = fakeW+'_MuDown'
#   fakeW_statEleUp   = fakeW+'_statEleUp'
#   fakeW_statEleDown = fakeW+'_statEleDown'
#   fakeW_statMuUp    = fakeW+'_statMuUp'
#   fakeW_statMuDown  = fakeW+'_statMuDown'

# else:
#   fakeW_EleUp       = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
#   fakeW_EleDown     = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
#   fakeW_MuUp        = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
#   fakeW_MuDown      = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
#   fakeW_statEleUp   = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
#   fakeW_statEleDown = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
#   fakeW_statMuUp    = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
#   fakeW_statMuDown  = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'

nuisances['fake_syst']  = {
               'name'  : 'CMS_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
               }

# nuisances['fake_ele']  = {
#                 'name'  : 'hww_fake_ele_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     : [ fakeW_EleUp , fakeW_EleDown ],
#                              },
# }

# nuisances['fake_ele_stat']  = {
#                 'name'  : 'hww_fake_ele_stat_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_statEleUp , fakeW_statEleDown ],
#                              },
# }

# nuisances['fake_mu']  = {
#                 'name'  : 'hww_fake_mu_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     : [ fakeW_MuUp , fakeW_MuDown ],
#                              },
# }


# nuisances['fake_mu_stat']  = {
#                 'name'  : 'hww_fake_mu_stat_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     : [ fakeW_statMuUp , fakeW_statMuDown ],
#                              },
# }

##### Btag nuisances

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]
   
    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }


####### Fatjet uncertainties
# fatjet_eff = ['Wtagging_SF_up/Wtagging_SF_nominal', 'Wtagging_SF_down/Wtagging_SF_nominal']
# nuisances['Wtagging_eff'] = {
#                 'name': 'CMS_eff_fatjet_2018',
#                 'kind' : 'weight', 
#                 'type' : 'shape',
#                 'samples': dict( (skey, fatjet_eff) for skey in mc)
# }

# ##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_'+Nlep+'l_u)/(TriggerEffWeight_'+Nlep+'l))*(TriggerEffWeight_'+Nlep+'l>0.02) + (TriggerEffWeight_'+Nlep+'l<=0.02)', '(TriggerEffWeight_'+Nlep+'l_d)/(TriggerEffWeight_'+Nlep+'l)']

nuisances['trigg']  = {
                'name'  : 'CMS_eff_trigger_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :   dict((skey, trig_syst) for skey in mc)
}


# ##### Electron Efficiency and energy scale

ele_id_syst_up = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Up[0])/\
                    (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
ele_id_syst_do = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Down[0])/\
                    (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
mu_id_syst_up = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Up[0])/\
                    (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'
mu_id_syst_do = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Down[0])/\
                    (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'

id_syst_ele = [ ele_id_syst_up, ele_id_syst_do ]
id_syst_mu = [ mu_id_syst_up, mu_id_syst_do ]

nuisances['eff_e']  = {
                'name'  : 'CMS_eff_e_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :   dict((skey, id_syst_ele) for skey in mc),
}

# nuisances['electronpt']  = {
#                 'name'  : 'CMS_scale_e_2018',
#                 'kind'  : 'tree',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['1', '1']) for skey in mc if skey not in ["Vg", "VgS"]),
#                 'folderUp'   :  directory_bkg +"_ElepTup",
#                 'folderDown' : directory_bkg +"_ElepTdo"
# }



# ##### Muon Efficiency and energy scale


# nuisances['eff_m']  = {
#                 'name'  : 'CMS_eff_m_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, id_syst_mu) for skey in mc)

# nuisances['muonpt']  = {
#                 'name'  : 'CMS_scale_m_2018',
#                 'kind'  : 'tree',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['1', '1']) for skey in mc),
#                 'folderUp'   : directory_bkg +"_MupTup",
#                 'folderDown' : directory_bkg +"_MupTdo"
# }


##### Jet energy scale

# nuisances['jes']  = {
#                 'name'  : 'CMS_scale_j_2018',
#                 'kind'  : 'tree',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['1', '1']) for skey in mc if skey not in ["Vg", "VgS"]),
#                 'folderUp'   : directory_bkg +"_JESup",
#                 'folderDown' : directory_bkg +"_JESdo",
# }



# nuisances['fatjet_jes']  = {
#                 'name'  : 'CMS_scale_fatj_2018',
#                 'kind'  : 'tree',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['1', '1']) for skey in mc if skey not in ["Vg", "VgS"]),
#                 'folderUp'   : directory_bkg +"_fatjet_JESup",
#                 'folderDown' : directory_bkg +"_fatjet_JESdo",
# }

# nuisances['fatjet_jms']  = {
#                 'name'  : 'CMS_mass_fatj_2018',
#                 'kind'  : 'tree',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['1', '1']) for skey in mc if skey not in ["Vg", "VgS"]),
#                 'folderUp'   : directory_bkg +"_fatjet_JMSup",
#                 'folderDown' : directory_bkg +"_fatjet_JMSdo",
# }



# ##### MET energy scale

# nuisances['met']  = {
#                 'name'  : 'CMS_scale_met_2018',
#                 'kind'  : 'tree',
#                 'type'  : 'shape',
#                  'samples'  : dict((skey, ['1', '1']) for skey in mc if skey not in ["Vg", "VgS"] ),
#                 'folderUp'   : directory_bkg +"_METup",
#                 'folderDown' : directory_bkg +"_METdo",
# }

######################
# Theory nuisance

# nuisances['QCD_scale_wjets'] = {
#      'name'  : 'QCDscale_wjets',
#      'kind'  : 'weight',
#      'type'  : 'shape',
#      'samples'  :   {
#          "Wjets" :         ["LHEScaleWeight[0]", "LHEScaleWeight[8]"],
#          "Wjets_HT" :      ["LHEScaleWeight[0]", "LHEScaleWeight[8]"],
#          "Wjets_njetsLO" : ["LHEScaleWeight[0]", "LHEScaleWeight[8]"],
#          "Wjets_NLO" :     ["LHEScaleWeight[0]", "LHEScaleWeight[8]"], 
#          "Wjets_LO" :      ["LHEScaleWeight[0]", "LHEScaleWeight[8]"], 
#      }
# }


# nuisances['QCD_scale_top'] = {
#      'name'  : 'QCDscale_top',
#      'kind'  : 'weight',
#      'type'  : 'shape',
#      'samples'  :   {
#         "top" : ["LHEScaleWeight[0]", "LHEScaleWeight[8]"], 
#      }
# }

# nuisances['QCD_scale_DY'] = {
#      'name'  : 'QCDscale_DY',
#      'kind'  : 'weight',
#      'type'  : 'shape',
#      'samples'  :   {
#         "DY_NLO" : ["LHEScaleWeight[0]", "LHEScaleWeight[8]"], 
#         "DY" : ["LHEScaleWeight[0]", "LHEScaleWeight[8]"],
#      }
# }

# nuisances['QCD_scale_VV'] = {
#      'name'  : 'QCDscale_VV',
#      'kind'  : 'weight',
#      'type'  : 'shape',
#      'samples'  :   {
#         "VV" : ["LHEScaleWeight[0]", "LHEScaleWeight[8]"], 
#      }
# }

# nuisances['QCD_scale_VBF-V'] = {
#      'name'  : 'QCDscale_VBF-V',
#      'kind'  : 'weight',
#      'type'  : 'shape',
#      'samples'  :   {
#         "VBF-V" : ["LHEScaleWeight[0]", "LHEScaleWeight[8]"], 
#      }
# }

# nuisances['QCD_scale_VBS'] = {
#      'name'  : 'QCDscale_VBS',
#      'kind'  : 'weight',
#      'type'  : 'shape',
#      'samples'  :   {
#          "VBS" : ["LHEScaleWeight[0]", "LHEScaleWeight[8]"], 
#      }
# }
##################################
#### Custom nuisances



# if useEmbeddedDY: del nuisances['prefire']['samples']['DY']

# #
# # PS and UE
# #
# nuisances['PS']  = {
#                 'name'  : 'PS',
#                 'skipCMS' : 1,
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                   'WW'      : ['PSWeight[0]', 'PSWeight[3]'],
#                   },
#                 }

# nuisances['UE']  = {
#                 'name'  : 'UE', 
#                 'skipCMS' : 1,
#                 'kind'  : 'tree',
#                 'type'  : 'shape',
#                 'samples'  : {
# #                  'WW'      : ['1.12720771849', '1.13963144574'],
#                   'ggH_hww' : ['1.00211385568', '0.994966378288'], 
#                   'qqH_hww' : ['1.00367895901', '0.994831373195']
#                 },
#                 'folderUp'   : treeBaseDir+'Fall2018_nAOD_v1_Full2018v2/MCl1loose2018v2__MCCorr2018__btagPerEvent__l2loose__l2tightOR2018__UEup',
#                 'folderDown' : treeBaseDir+'Fall2018_nAOD_v1_Full2018v2/MCl1loose2018v2__MCCorr2018__btagPerEvent__l2loose__l2tightOR2018__UEdo',
#                 'AsLnN'      : '1',
# }


# nuisances['PU']  = {
#                 'name'  : 'CMS_PU_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                   'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
#                   'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
#                   'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
#                   'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
#                   'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
#                 },
#                 'AsLnN'      : '1',
# }

## Top pT reweighting uncertainty

# nuisances['singleTopToTTbar'] = {
#     'name': 'singleTopToTTbar',
#     'skipCMS': 1,
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': { 
#        'top': [
#         'isSingleTop * 1.0816 + isTTbar',
#         'isSingleTop * 0.9184 + isTTbar']
#       }
# }

## Top pT reweighting uncertainty

# nuisances['TopPtRew'] = {
#     'name': 'CMS_topPtRew',   # Theory uncertainty
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': {'top': ["1.", "1./Top_pTrw"]},
#     'symmetrize': True
# }


#################
## Samples normalizations
# nuisances['Top_norm']  = {
#                'name'  : 'CMS_Top_norm_2018',
#                'samples'  : {
#                    'top' : '1.00',
#                    },
#                'type'  : 'rateParam',
#                'cuts'  : phase_spaces_tot
#               }


# for wjbin in Wjets_lptbins:
#     for fl in ["ele", "mu"]:
#         for phs in ["res", "boost"]:
#             nuisances["{}_norm_{}_{}_2018".format(wjbin, fl, phs )] = {
#                 'name'  : 'CMS{}_norm_{}_{}_2018'.format(wjbin, fl, phs),
#                 'samples'  : { wjbin: '1.00' },
#                 'type'  : 'rateParam',
#                 'cuts'  : [f+"_"+fl for f in phase_spaces_dict[phs]]
#             }


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }



for n in nuisances.values():
    n['skipCMS'] = 1

   
#print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))
