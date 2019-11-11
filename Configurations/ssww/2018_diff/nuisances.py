# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and skey != 'Fake_lep' and skey !='WZ_EWK' and skey !='Vg' and skey !='DPS']
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''
mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__'
from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2018',
#    'type': 'lnN',
#    'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top', 'DY'])
}
'''
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
'''
#### FAKES

## FIXME: check the 30% lnN
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst',
    'type': 'lnN',
    'samples': {
        'Fake_lep': '1.3'
    },
    #'cutspost': lambda self, cuts: [cut for cut in cuts if '20em' not in cut],
    #'perRecoBin': True
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake_lep': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m',
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

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_trigger',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': mcDirectory+'ElepTup'+'/',
    'folderDown': mcDirectory+'ElepTdo'+'/',
    #'AsLnN': '1'
}

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': mcDirectory+'MupTup'+'/',
    'folderDown': mcDirectory+'MupTdo'+'/',
    #'AsLnN': '1'
}

##### Jet energy scale

nuisances['jes'] = {
    'name': 'CMS_scale_j',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': mcDirectory+'JESup'+'/',
    'folderDown': mcDirectory+'JESdo'+'/',
    #'AsLnN': '1'
}

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': mcDirectory+'METup'+'/',
    'folderDown': mcDirectory+'METdo'+'/',
    #'AsLnN': '1'
}

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['puWeightUp/puWeight', 'puWeightDown/puWeight']) for skey in mc),
    #'AsLnN': '1',
}


##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)
# [0] is muR=0.50000E+00 muF=0.50000E+00
# [1] is muR=0.50000E+00 muF=0.10000E+01
# [2] is muR=0.50000E+00 muF=0.20000E+01
# [3] is muR=0.10000E+01 muF=0.50000E+00
# [4] is muR=0.10000E+01 muF=0.10000E+01
# [5] is muR=0.10000E+01 muF=0.20000E+01
# [6] is muR=0.20000E+01 muF=0.50000E+00
# [7] is muR=0.20000E+01 muF=0.10000E+01
# [8] is muR=0.20000E+01 muF=0.20000E+01

variations = ['LHEScaleWeight[%d]' % i for i in [0, 1, 3, 5, 7, 8]]


nuisances['QCDscale'] = {
    'name': 'QCDscale',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WpWp_EWK': variations,
        'WpWp_EWK_lep1pt_bin0': variations,
        'WpWp_EWK_lep1pt_bin1': variations,
        'WpWp_EWK_lep1pt_bin2': variations,
        'WpWp_EWK_lep1pt_out': variations,
        'WpWp_EWK_lep2pt_bin0': variations,
        'WpWp_EWK_lep2pt_bin1': variations,
        'WpWp_EWK_lep2pt_bin2': variations,
        'WpWp_EWK_lep2pt_out': variations,
        'WpWp_EWK_jet1pt_bin0': variations,
        'WpWp_EWK_jet1pt_bin1': variations,
        'WpWp_EWK_jet1pt_bin2': variations,
        'WpWp_EWK_jet1pt_out': variations,
        'WpWp_EWK_jet2pt_bin0': variations,
        'WpWp_EWK_jet2pt_bin1': variations,
        'WpWp_EWK_jet2pt_bin2': variations,
        'WpWp_EWK_jet2pt_out': variations,
        'WpWp_EWK_mll_bin0': variations,
        'WpWp_EWK_mll_bin1': variations,
        'WpWp_EWK_mll_bin2': variations,
        'WpWp_EWK_mll_bin3': variations,
        'WpWp_EWK_mll_out': variations,
        'WpWp_EWK_mjj_bin0': variations,
        'WpWp_EWK_mjj_bin1': variations,
        'WpWp_EWK_mjj_bin2': variations,
        'WpWp_EWK_mjj_bin3': variations,
        'WpWp_EWK_mjj_out': variations,
        'WpWp_QCD': variations,
    }
}

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))