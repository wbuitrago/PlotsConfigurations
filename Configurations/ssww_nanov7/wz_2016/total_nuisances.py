# nuisances
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')
# charge flip mc
CFMC=['WW','ggWW','top','DY','higgs']
try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

#### Luminosity
nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc if skey not in CFMC)
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc if skey not in CFMC)
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in CFMC)
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in CFMC)
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in CFMC)
}
#### FAKES

## FIXME: check the 30% lnN
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
    #'perRecoBin': True
}

nuisances['fake_ele'] = {
   'name': 'CMS_fake_e_2016',
   'kind': 'weight',
   'type': 'shape',
   'samples': {
       'Fake': ['fakeWEleUp', 'fakeWEleDown'],
   },
}

nuisances['fake_ele_stat'] = {
   'name': 'CMS_fake_stat_e_2016',
   'kind': 'weight',
   'type': 'shape',
   'samples': {
       'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
   },
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    },
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    },
}

##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc if skey not in CFMC),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc if skey not in CFMC),
}

##### prefire
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc if skey not in CFMC)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
   'name': 'CMS_eff_e',
   'kind': 'weight',
   'type': 'shape',
   'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc if skey not in CFMC),
}
nuisances['electronpt'] = {
   'name': 'CMS_scale_e',
   'kind': 'suffix',
   'type': 'shape',
   'mapUp': 'ElepTup',
   'mapDown': 'ElepTdo',
   'samples': dict((skey, ['1', '1']) for skey in mc if (skey not in CFMC and skey not in ['ggZZ'])),
   'folderUp': makeMCDirectory('ElepTup_suffix'),
   'folderDown': makeMCDirectory('ElepTdo_suffix'),
}


##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc if skey not in CFMC),
}
nuisances['muonpt'] = {
    'name': 'CMS_scale_m',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if (skey not in CFMC and skey not in ['ggZZ'])),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
}
##### charge flip
#cf_syst = ['cf_wgt_up/cf_wgt', 'cf_wgt_down/cf_wgt']
#
#nuisances['ChargeFlip'] = {
#	'name': 'ChargeFlip_2016',
#	'kind': 'weight',
#	'type': 'shape',
#	'samples': dict((skey, cf_syst) for skey in mc if skey in CFMC)
#}

### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc if skey not in CFMC)
}

##### Jet energy scale
nuisances['jes'] = {
    'name': 'CMS_scale_j_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JESup',
    'mapDown': 'JESdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in CFMC),
    'folderUp': makeMCDirectory('JESTotalup_suffix'),
    'folderDown': makeMCDirectory('JESTotaldo_suffix'),
}
#jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']
#
#for js in jes_systs:
#  if 'Absolute' in js: 
#    folderup = makeMCDirectory('JESAbsoluteup_suffix')
#    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
#  elif 'BBEC1' in js:
#    folderup = makeMCDirectory('JESBBEC1up_suffix')
#    folderdo = makeMCDirectory('JESBBEC1do_suffix')
#  elif 'EC2' in js:
#    folderup = makeMCDirectory('JESEC2up_suffix')
#    folderdo = makeMCDirectory('JESEC2do_suffix')
#  elif 'HF' in js:
#    folderup = makeMCDirectory('JESHFup_suffix')
#    folderdo = makeMCDirectory('JESHFdo_suffix')
#  elif 'Relative' in js:
#    folderup = makeMCDirectory('JESRelativeup_suffix')
#    folderdo = makeMCDirectory('JESRelativedo_suffix')
#  elif 'FlavorQCD' in js:
#    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
#    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')
#
#  nuisances[js] = {
#      'name': 'CMS_scale_'+js,
#      'kind': 'suffix',
#      'type': 'shape',
#      'mapUp': js+'up',
#      'mapDown': js+'do',
#      'samples': dict((skey, ['1', '1']) for skey in mc if skey not in CFMC), # if skey not in ['VZ','Vg','VgS','VgS_L','VgS_H']),
#      'folderUp': folderup,
#      'folderDown': folderdo,
#      'AsLnN': '1'
#  }

##### Jet energy resolution
#nuisances['JER'] = {
#    'name': 'CMS_res_j_2016',
#    'kind': 'suffix',
#    'type': 'shape',
#    'mapUp': 'JERup',
#    'mapDown': 'JERdo',
#    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in CFMC),
#    'folderUp': makeMCDirectory('JERup_suffix'),
#    'folderDown': makeMCDirectory('JERdo_suffix'),
#}
##### MET energy scale
nuisances['met'] = {
    'name': 'CMS_scale_met_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in CFMC),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
}
##### Pileup
nuisances['PU'] = {
    'name': 'CMS_PU',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['(puWeightUp/puWeight)', '(puWeightDown/puWeight)']) for skey in mc if skey not in CFMC),
}
## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
nuisances['scale_SSWW_EW'] = {
    'name': 'scale_SSWW_EW',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples':{
        'SSWW_EW': variations,
    },
    #'AsLnN': 1,
}
nuisances['scale_WZ_EW'] = {
    'name': 'scale_WZ_EW',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples':{
        'WZ_EW': variations,
    },
    #'AsLnN': 1,
}
variations = ['LHEPdfWeight[%d]' % i for i in range(0,33)]
nuisances['pdf_SSWW_EW'] = {
    'name': 'pdf_SSWW_EW',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples':{
        'SSWW_EW': variations,
    },
    # 'AsLnN': 1,
}
variations = ['LHEPdfWeight[%d]' % i for i in range(0,101)]
nuisances['pdf_WZ_EW'] = {
    'name': 'pdf_WZ_EW',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples':{
        'WZ_EW': variations,
    },
    # 'AsLnN': 1,
}

### NLO correction
nlo_syst = ['EW_weight_up/EW_weight', 'EW_weight_do/EW_weight']
nuisances['NLOcorr_SSWW_EW'] = {
    'name': 'CMS_NLOcorr_SSWW_EW',
    'kind': 'weight',
    'type': 'shape',
    'samples':{
        'SSWW_EW': nlo_syst,
    },
}
nuisances['NLOcorr_WZ_EW'] = {
    'name': 'CMS_NLOcorr_WZ_EW',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WZ_EW': nlo_syst,
    },
}

#nuisances['SSWWNorm2016']  = {
#    'name'  : 'SSWWNorm2016',
#    'samples'  : {
#        'SSWW_EW' : '1.00',    # change sample name
#    },
#    'type'  : 'rateParam',
#}
nuisances['tZqNorm2016']  = {
    'name'  : 'tZqNorm2016',
    'samples'  : {
        'tZq' : '1.00',    # change sample name
    },
    'type'  : 'rateParam',
}
nuisances['WZNorm2016']  = {
    'name'  : 'WZNorm2016',
    'samples'  : {
        'WZ_QCD_powheg' : '1.00',    # change sample name
    },
    'type'  : 'rateParam',
}
# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
# Use the following if you want to apply the automatic combine MC stat nuisances->Faster than bin-by-bin
nuisances['stat']  = {
    'type'  : 'auto',
    'maxPoiss'  : '10',
    'includeSignal'  : '1',
    'samples' : {}
}
# Differnt type of uncentainties: type->ln N: (modify only event yeld) use a lognorm distributions with sigma = uncertainty. For normalization rateParam
# can be used--> use a uniform distribution;
# Shape: modify not only the events yelds but the event selection too (the shape) will run the varied shapes
# according to the following two possible kinds
# kind-> weight: Use the specified weight to reweight events;
# tree: uses the provided alternative trees;
# The MC statistics is a particular uncertainty: is caused by our finite statistics used to elaborate the template fits. Two approach: unfied and bin-by-bin (bbb)
for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))