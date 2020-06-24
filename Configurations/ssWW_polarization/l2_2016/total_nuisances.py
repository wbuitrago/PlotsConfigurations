
# nuisances
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and skey!='ll' and skey!='tl' and skey!='tt' and skey!='lt' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2016',
#    'type': 'lnN',
#    'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
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
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2016',
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
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc)
}
##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}
nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2016',
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
    'name': 'CMS_eff_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2016',
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
    'name': 'CMS_scale_j_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JESup',
    'mapDown': 'JESdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('JESup_suffix'),
    'folderDown': makeMCDirectory('JESdo_suffix'),
}
##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2016',
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
    'name': 'CMS_PU_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['(puWeightUp/puWeight)', '(puWeightDown/puWeight)']) for skey in mc),
}
# EW corrections
nuisances['EW_correction'] = {
    'name': 'EW_correction',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'LL': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'TL': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'TT': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'LL_fid': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'TL_fid': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'TT_fid': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'LL_o_fid': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'TL_o_fid': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
        'TT_o_fid': ['(EW_weight_up/EW_weight)', '(EW_weight_do/EW_weight)'],
    },
}
# qcd scale
nuisances['QCDscale_LL'] = {
    'name': 'QCDscale_LL',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'LL': ['ScaleW_up', 'ScaleW_do'],
        'LL_fid': ['ScaleW_up', 'ScaleW_do'],
        'LL_o_fid': ['ScaleW_up', 'ScaleW_do'],
        'LL2': ['ScaleW_up', 'ScaleW_do'],
    },
}
nuisances['QCDscale_TL'] = {
    'name': 'QCDscale_TL',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'TL': ['ScaleW_up', 'ScaleW_do'],
        'LL_fid': ['ScaleW_up', 'ScaleW_do'],
        'LL_o_fid': ['ScaleW_up', 'ScaleW_do'],
        'TL2': ['ScaleW_up', 'ScaleW_do'],
    },
}
nuisances['QCDscale_TT'] = {
    'name': 'QCDscale_TT',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'TT': ['ScaleW_up', 'ScaleW_do'],
        'LL_fid': ['ScaleW_up', 'ScaleW_do'],
        'LL_o_fid': ['ScaleW_up', 'ScaleW_do'],
        'TT2': ['ScaleW_up', 'ScaleW_do'],
    },
}
# pdf scale
nuisances['pdfscale_LL'] = {
    'name': 'pdfscale_LL',
    'type': 'lnN',
    'samples': {
        'LL': '1.00028',
        'LL_fid': '1.00028',
        'LL_o_fid': '1.00028',
        'LL2': '1.00028',
    },
}
nuisances['pdfscale_TL'] = {
    'name': 'pdfscale_TL',
    'type': 'lnN',
    'samples': {
        'TL': '1.00035',
        'LL_fid': '1.00035',
        'LL_o_fid': '1.00035',
        'TL2': '1.00035',
    },
}
nuisances['pdfscale_TT'] = {
    'name': 'pdfscale_TT',
    'type': 'lnN',
    'samples': {
        'TT': '1.0012',
        'LL_fid': '1.0012',
        'LL_o_fid': '1.0012',
        'TT2': '1.0012',
    },
}
#variations = ['LHEScaleWeight[%d]' % i for i in [4,9,14,19,29,39]]
#
#nuisances['QCDscale_WZ'] = {
#    'name': 'QCDscale_WZ',
#    'skipCMS': 1,
#    'kind': 'weight_envelope',
#    'type': 'shape',
#    'samples': {
#        'WZ_LL_EWK': variations,
#        'WZ_TL_EWK': variations,
#        'WZ_LT_EWK': variations,
#        'WZ_TT_EWK': variations,
#    },
#}
#
#variations = ['LHEPdfWeight[%d]' % i for i in range(0,33)]
#
#nuisances['pdf_WZ'] = {
#    'name': 'pdf_WZ',
#    'skipCMS': 1,
#    'kind': 'weight_envelope',
#    'type': 'shape',
#    'samples': {
#        'WZ_LL_EWK': variations,
#        'WZ_TL_EWK': variations,
#        'WZ_LT_EWK': variations,
#        'WZ_TT_EWK': variations,
#    },
#}

variations = ['LHEScaleWeight[%d]' % i for i in [0,1,3,5,7,8]]

nuisances['QCDscale'] = {
    'name': 'QCDscale',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WpWp_QCD': variations,
        'WZ_QCD': variations,
    },
}

variations = ['LHEPdfWeight[%d]' % i for i in range(0,101)]

nuisances['pdf'] = {
    'name': 'pdf',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WpWp_QCD': variations,
        'WZ_QCD': variations,
    },
}
#nuisances['TLscale2016']  = {
#    'name'  : 'TLscale2016',
#    'samples'  : {
#        'TL' : '1.00',    # change sample name
#    },
#    'type'  : 'rateParam',
#}
#nuisances['TTscale2016']  = {
#    'name'  : 'TTscale2016',
#    'samples'  : {
#        'TT' : '1.00',    # change sample name
#    },
#    'type'  : 'rateParam',
#}
nuisances['WZscale2016']  = {
    'name'  : 'WZscale2016',
    'samples'  : {
        'WZ_QCD' : '1.00',    # change sample name
    },
    'type'  : 'rateParam',
}
nuisances['tZqscale2016']  = {
    'name'  : 'tZqscale2016',
    'samples'  : {
        'tZq' : '1.00',    # change sample name
    },
    'type'  : 'rateParam',
}
nuisances['ZZscale2016']  = {
    'name'  : 'ZZscale2016',
    'samples'  : {
        'ZZ4L' : '1.00',    # change sample name
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
