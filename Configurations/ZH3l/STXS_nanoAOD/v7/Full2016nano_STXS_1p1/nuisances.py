# nuisances
# name of samples here must match keys in samples.py    

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []

#### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc if skey not in ['WZ'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc if skey not in ['WZ'])
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WZ'])
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in ['WZ'])
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WZ'])
}

#### Theoretical Systematics

# Scale
from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_VH']  = {
  'name'  : 'QCDscale_VH',
  'samples'  : {
    'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
    #'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
    'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
    'ZH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm')
  },
  'type'  : 'lnN'
}

#nuisances['QCDscale_ggZH']  = {
#  'name'  : 'QCDscale_ggZH', 
#  'samples'  : {
#    'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm'),                  
#  },
#  'type'  : 'lnN'
#}

nuisances['QCDscale_ttH']  = {
  'name'  : 'QCDscale_ttH', 
  'samples'  : {
    'ttH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm'),                  
  },
  'type'  : 'lnN'
}

variations = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[5],1)', 'Alt$(LHEScaleWeight[7],1)', 'Alt$(LHEScaleWeight[8],1)']

nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'DY': variations},
    'AsLnN': '1'
}

nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WW'      : variations,
        'Zg'      : variations,
        'ZgS'     : variations,
        'WZ'      : variations,
        'ZZ'      : variations
    }
}

nuisances['QCDscale_WWewk'] = {
    'name': 'QCDscale_WWewk',
    'samples': {
        'WWewk': '1.11',
    },
    'type': 'lnN'
}


# ggww and interference
nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    }
}

nuisances['QCDscale_qqbar_ACCEPT']  = {
  'name'  : 'QCDscale_qqbar_ACCEPT', 
  'type'  : 'lnN',
  'samples'  : {
    'WH_hww'  : '1.010',
    #'ZH_hww'  : '1.015',
    'WH_htt'  : '1.010',
    'ZH_htt'  : '1.015',
  }
}

nuisances['QCDscale_gg_ACCEPT']  = {
  'name'  : 'QCDscale_gg_ACCEPT', 
  'samples'  : {
    #'ggZH_hww': '1.012',                   
    'ggWW'    : '1.012'
  },
  'type'  : 'lnN',
}

# pdf
#nuisances['pdf_Higgs_gg']  = {
#               'name'  : 'pdf_Higgs_gg', 
#               'samples'  : {
#                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm'), 
#                   },
#               'type'  : 'lnN'
#              }

nuisances['pdf_Higgs_qqbar']  = {
               'name'  : 'pdf_Higgs_qqbar', 
               'type'  : 'lnN',
               'samples'  : {
                   'WH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   #'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   'WH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'ZH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   },
              }

nuisances['pdf_Higgs_ttH'] = {
               'name': 'pdf_Higgs_ttH',
               'type': 'lnN',
               'samples': {
                   'ttH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')
                   },
              }

nuisances['pdf_qqbar'] = {
              'name': 'pdf_qqbar',
              'type': 'lnN',
              'samples': {
                  'Zg':  '1.04',
                  'ZgS': '1.04',
                  'WZ':  '1.04',
                  'ZZ':  '1.04',
                  },
              }

#nuisances['pdf_Higgs_gg_ACCEPT']  = {
#               'name'  : 'pdf_Higgs_gg_ACCEPT', 
#               'samples'  : {
#                   'ggZH_hww': '1.006', 
#                   },
#               'type'  : 'lnN',
#              }

nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   'WH_hww'  : '1.003',
#                   'ZH_hww'  : '1.002',
                   'WH_htt'  : '1.003',
                   'ZH_htt'  : '1.002',
                   },
              }

nuisances['pdf_qqbar_ACCEPT']  = {
               'name'  : 'pdf_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   'WZ'      : '1.001',
                   'ZZ'      : '1.001',
                   },
              }

nuisances['pdf_gg_ACCEPT'] = {
    'name': 'pdf_gg_ACCEPT',
    'samples': {
        'ggWW': '1.006',
    },
    'type': 'lnN',
}

#To be updated for v7
nuisances['PS_ISR'] = {
   'name': 'PS_ISR',
   'kind': 'weight',
   'type': 'shape',
   'samples': {
       'ggZH_hww': ['1.066107*(nCleanGenJet==0) + 1.047857*(nCleanGenJet==1) + 1.030005*(nCleanGenJet==2) + 1.005028*(nCleanGenJet>=3)', '0.921874*(nCleanGenJet==0) + 0.941939*(nCleanGenJet==1) + 0.962282*(nCleanGenJet==2) + 0.991580*(nCleanGenJet>=3)'],
       'ZH_hww': ['1.000684*(nCleanGenJet==0) + 1.000924*(nCleanGenJet==1) + 1.001683*(nCleanGenJet==2) + 1.002104*(nCleanGenJet>=3)', '0.999150*(nCleanGenJet==0) + 0.998821*(nCleanGenJet==1) + 0.997859*(nCleanGenJet==2) + 0.997316*(nCleanGenJet>=3)'],
       'WZ': ['1.002552*(nCleanGenJet==0) + 1.010286*(nCleanGenJet==1) + 1.014420*(nCleanGenJet==2) + 1.006226*(nCleanGenJet>=3)', '0.996802*(nCleanGenJet==0) + 0.987227*(nCleanGenJet==1) + 0.982005*(nCleanGenJet==2) + 0.992030*(nCleanGenJet>=3)'],
       'ZZ': ['1.003210*(nCleanGenJet==0) + 1.005480*(nCleanGenJet==1) + 1.004674*(nCleanGenJet==2) + 0.987845*(nCleanGenJet>=3)', '0.995997*(nCleanGenJet==0) + 0.993056*(nCleanGenJet==1) + 0.993659*(nCleanGenJet==2) + 1.014695*(nCleanGenJet>=3)'],
              },
}

#To be updated for v7
nuisances['PS_FSR'] = {
   'name': 'PS_FSR',
   'kind': 'weight',
   'type': 'shape',
   'samples': {
       'ggZH_hww': ['0.987316*(nCleanGenJet==0) + 0.986764*(nCleanGenJet==1) + 0.996498*(nCleanGenJet==2) + 1.004161*(nCleanGenJet>=3)', '1.019871*(nCleanGenJet==0) + 1.013853*(nCleanGenJet==1) + 1.005229*(nCleanGenJet==2) + 0.998573*(nCleanGenJet>=3)'],
       'ZH_hww': ['0.992867*(nCleanGenJet==0) + 0.992845*(nCleanGenJet==1) + 0.999470*(nCleanGenJet==2) + 1.007245*(nCleanGenJet>=3)', '1.012465*(nCleanGenJet==0) + 1.012743*(nCleanGenJet==1) + 1.003215*(nCleanGenJet==2) + 0.991286*(nCleanGenJet>=3)'],
       'WZ': ['0.992987*(nCleanGenJet==0) + 0.993725*(nCleanGenJet==1) + 1.000617*(nCleanGenJet==2) + 1.010869*(nCleanGenJet>=3)', '1.011267*(nCleanGenJet==0) + 1.010097*(nCleanGenJet==1) + 0.999445*(nCleanGenJet==2) + 0.983609*(nCleanGenJet>=3)'],
       'ZZ': ['0.997245*(nCleanGenJet==0) + 0.998689*(nCleanGenJet==1) + 1.004475*(nCleanGenJet==2) + 1.011440*(nCleanGenJet>=3)', '1.004482*(nCleanGenJet==0) + 1.002081*(nCleanGenJet==1) + 0.992617*(nCleanGenJet==2) + 0.981314*(nCleanGenJet>=3)'],
             },
}

#To be updated for v7
nuisances['PU'] = { 
   'name': 'CMS_PU_2016',
   'kind': 'weight',
   'type': 'shape',
   'samples': {
       'WZ': ['1.0016149*(puWeightUp/puWeight)', '0.99841193*(puWeightDown/puWeight)'],
       'ZZ': ['1.00189618*(puWeightUp/puWeight)', '0.99814883*(puWeightDown/puWeight)'],
       'ZH_hww': ['1.00098808*(puWeightUp/puWeight)', '0.99923369*(puWeightDown/puWeight)'],
       'ggZH_hww': ['1.00267652*(puWeightUp/puWeight)', '0.99739938*(puWeightDown/puWeight)'],
   },
   'AsLnN': '1',
}

nuisances['UE_CUET']  = {
                'name'  : 'UE_CUET',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples'  : {
                   'WH_hww'   : '1.015',
                   #'ZH_hww'   : '1.015',
                   #'ggZH_hww' : '1.015',
                   'WH_htt'   : '1.015',
                   'ZH_htt'   : '1.015',
               },
}

nuisances['WZ3l2jnorm']  = {
               'name'  : 'CMS_hww_WZ3l2jnorm',
               'samples'  : {
                   'WZ'       : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [cut for cut in cuts if '2j' in cut]
              }

nuisances['WZ3l1jnorm']  = {
               'name'  : 'CMS_hww_WZ3l1jnorm',
               'samples'  : {
                   'WZ'       : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [cut for cut in cuts if '1j' in cut]
              }

### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}

#### FAKES

fakeW_EleUp       = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lElUp       / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_EleDown     = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lElDown     / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_MuUp        = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lMuUp       / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_MuDown      = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lMuDown     / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statEleUp   = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatElUp   / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statEleDown = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatElDown / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statMuUp    = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatMuUp   / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statMuDown  = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatMuDown / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'

nuisances['fake_syst_e']  = {
               'name'  : 'CMS_fake_syst_e',
               'type'  : 'lnN',
               'samples'  : {
                   'Fake_e' : '1.30',
               },
}

nuisances['fake_syst_m']  = {
               'name'  : 'CMS_fake_syst_m',
               'type'  : 'lnN',
               'samples'  : {
                   'Fake_m' : '1.30',
               },
}

nuisances['fake_ele']  = {
                'name'  : 'CMS_fake_e_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_stat_e_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'CMS_fake_m_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}

nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_stat_m_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
}

###### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

#### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_3l_u)/(TriggerEffWeight_3l))*(TriggerEffWeight_3l>0.02) + (TriggerEffWeight_3l<=0.02)', '(TriggerEffWeight_3l_d)/(TriggerEffWeight_3l)']

nuisances['trigg']  = {
                'name'  : 'CMS_eff_hwwtrigger_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, trig_syst) for skey in mc),
}

##### Prefiring correction

prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples'  : dict((skey, prefire_syst) for skey in mc),
}

##### Electron Efficiency and energy scale

id_syst_ele = [ 'SFweightEleUp', 'SFweightEleDown']

nuisances['eff_e']  = {
                'name'  : 'CMS_eff_e_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_ele) for skey in mc),
}

nuisances['electronpt']  = {
                'name'  : 'CMS_scale_e_2016',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp' : 'ElepTup',
                'mapDown' : 'ElepTdo',
                'samples'  : dict((skey, ['1', '1']) for skey in mc if skey is not 'ZZ'), #TEMP
                'folderUp'   : treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__ElepTup_suffix', 
                'folderDown' : treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__ElepTdo_suffix', 
                'AsLnN' : '1',
}

###### Muon Efficiency and energy scale

id_syst_mu = [ 'SFweightMuUp', 'SFweightMuDown']

nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc),
}

nuisances['muonpt']  = {
                'name'  : 'CMS_scale_m_2016',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp' : 'MupTup',
                'mapDown' : 'MupTdo',
                'samples'  : dict((skey, ['1', '1']) for skey in mc if skey is not 'ZZ'), #TEMP
                'folderUp'   : treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__MupTup_suffix', 
                'folderDown' : treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__MupTdo_suffix', 
                'AsLnN' : '1',
}

####### Jet energy scale

jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']
folderup = ""
folderdo = ""

for js in jes_systs:
 if 'Absolute' in js:
    folderup = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESAbsoluteup_suffix' 
    folderdo = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESAbsolutedo_suffix' 
 elif 'BBEC1' in js:
    folderup = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESBBEC1up_suffix' 
    folderdo = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESBBEC1do_suffix' 
 elif 'EC2' in js:
    folderup = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESEC2up_suffix' 
    folderdo = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESEC2do_suffix' 
 elif 'HF' in js:
    folderup = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESHFup_suffix' 
    folderdo = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESHFdo_suffix' 
 elif 'Relative' in js:
    folderup = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESRelativeup_suffix' 
    folderdo = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESRelativedo_suffix' 
 elif 'FlavorQCD' in js:
    folderup = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESFlavorQCDup_suffix' 
    folderdo = treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__JESFlavorQCDdo_suffix' 

 nuisances[js] = {
                'name': 'CMS_scale_'+js,
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': js+'up',
                'mapDown': js+'do',
                'samples': dict((skey, ['1', '1']) for skey in mc),
		'folderUp': folderup,
		'folderDown': folderdo,
                'AsLnN': '1',
  }

##### MET energy scale

nuisances['met']  = {
                'name'  : 'CMS_scale_met_2016',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp' : 'METup',
                'mapDown' : 'METdo',
                'samples'  : dict((skey, ['1', '1']) for skey in mc),
                'folderUp'   : treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__METup_suffix', 
                'folderDown' : treeBaseDir+'Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__METdo_suffix', 
                'AsLnN' : '1',
}

# Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {},
             }

for n in nuisances.values():
    n['skipCMS'] = 1
