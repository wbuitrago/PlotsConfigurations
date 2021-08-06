# nuisances
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

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
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc)
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc)
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc)
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'Top', 'DY', 'Higgs'])
}

# nuisances['lumi'] = {
#     'name': 'lumi_13TeV_2018',
#     'type': 'lnN',
#     'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
# }

#### FAKES

## FIXME: check the 30% lnN
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

##### B-tagger

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

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
}

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
}

##### Jet energy scale

nuisances['jes'] = {
    'name': 'CMS_scale_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JESup',
    'mapDown': 'JESdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['tZq']),
    'folderUp': makeMCDirectory('JESTotalup_suffix'),
    'folderDown': makeMCDirectory('JESTotaldo_suffix'),
}

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
}
##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['(puWeightUp/puWeight)', '(puWeightDown/puWeight)']) for skey in mc),
}

# variations_priv = ['LHEScaleWeight[%d]' % i for i in [0,1,3,5,7,8]]
variations_off_EWK  = ['LHEScaleWeight[%d]' % i for i in range(0,44)]
variations_off_QCD  = ['LHEScaleWeight[%d]' % i for i in range(0,9)]

nuisances['QCDscale_offEWK'] = {
    'name': 'QCDscale_offEWK',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WZ_EWK_off' : variations_off_EWK,
    },
}

nuisances['QCDscale_offQCD'] = {
    'name': 'QCDscale_offQCD',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WZ_QCD_off' : variations_off_QCD,
    },
}

nuisances['QCDscale_privEWK'] = {
    'name': 'QCDscale_privEWK',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WZ_EWK_priv': ['1.065+0.00009321*CleanJet_pt[0]', '0.7443-0.0001092*CleanJet_pt[0]'],
    },
}

nuisances['QCDscale_privQCD'] = {
    'name': 'QCDscale_privQCD',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WZ_QCD_priv': ['1.089+0.000106*CleanJet_pt[0]', '0.9269-0.00008684*CleanJet_pt[0]'],
    },
}

# variations_off = ['LHEPdfWeight[%d]' % i for i in range(0,33)]
# variations_priv = ['LHEPdfWeight[%d]' % i for i in range(0,101)]

# nuisances['pdf'] = {
#     'name': 'pdf',
#     'skipCMS': 1,
#     'kind': 'weight_envelope',
#     'type': 'shape',
#     'samples': {
#         'WZ_EWK_priv': variations_priv,
#         'WZ_QCD_priv': variations_priv,
#         'WZ_EWK_off' : variations_off,
#         'WZ_QCD_off' : variations_off,
#     },
# }

nuisances['pdf'] = {
    'name': 'pdf',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc)
}


variations = ['PSWeight[%d]' % i for i in range(0,4)]

nuisances['PS_off'] = {
    'name': 'PS_off',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WZ_EWK_off' : variations,
        'WZ_QCD_off' : variations,
    },
}

nuisances['PS_priv'] = {
    'name': 'PS_priv',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WZ_EWK_priv': variations,
        'WZ_QCD_priv': variations,
    },
}

nuisances['QCDnorm']  = {
   'name'  : 'QCDnorm',
   'samples'  : {
       'WZ_QCD_priv' : '1.00',
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
