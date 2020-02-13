# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py
basedir='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv5_Full2018v5/'
################################ EXPERIMENTAL UNCERTAINTIES  #################################
try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''
#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2018',
#    'type': 'lnN',
#    'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES

## FIXME: check the 30% lnN
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst',
    'type': 'lnN',
    'samples': {
        'Fake_lep': '1.3'
    },
    #'perRecoBin': True
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWStatMuUp', 'fakeWStatMuDown'],
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

# ##### Trigger Efficiency (duplicate??)

# trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

# nuisances['trigg'] = {
#     'name': 'CMS_eff_hwwtrigger_2018',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': dict((skey, trig_syst) for skey in mc)
# }

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'linear', 'quadratic']),
    'folderUp': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__ElepTup',
    'folderDown': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__ElepTdo',
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
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'linear', 'quadratic']),
    #'folderUp': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__MupTup_suffix',
    'folderUp': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__MupTup',
    #'folderDown': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__MupTdo_suffix',
    'folderDown': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__MupTdo',
}

##### Jet energy scale

nuisances['jes'] = {
    'name': 'CMS_scale_j_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'linear', 'quadratic']),
    'folderUp': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__JESup',
    #'folderDown': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__JESdo_suffix',
    'folderDown': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__JESdo',
    'AsLnN': '1'
}

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['sm', 'linear', 'quadratic']),
    'folderUp': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__METup',
    #'folderDown': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__METdo_suffix',
    'folderDown': basedir+'MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__METdo',
}

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['(puWeightUp/puWeight)', '(puWeightDown/puWeight)']) for skey in mc),
    'AsLnN': '1',
}

nuisances['QCDscale'] = {
    'name': 'QCDscale',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WpWp_EWK': ['LHEScaleWeight[8]', 'LHEScaleWeight[0]'],
        'WpWp_QCD': ['LHEScaleWeight[8]', 'LHEScaleWeight[0]'],
    }
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