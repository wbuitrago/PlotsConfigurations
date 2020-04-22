import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

#mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'
mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6/'
mcDir_private='/eos/user/j/jixiao/HWWnano3/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction = 'Autumn18_102X_nAODv6_Full2018v6'
mcSteps = 'MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6{var}'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'SFweight'
mcCommonWeight = 'SFweight*PromptGenLepMatch4l'
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['B','Run2016B-Nano1June2019_ver2-v1'] ,
    ['C','Run2016C-Nano1June2019-v1'] ,
    ['D','Run2016D-Nano1June2019-v1'] ,
    ['E','Run2016E-Nano1June2019-v1'] ,
    ['F','Run2016F-Nano1June2019-v1'] ,
    ['G','Run2016G-Nano1June2019-v1'] ,
    ['H','Run2016H-Nano1June2019-v1'] ,
]
DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']
DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
    }
###########################################
############  Reducible Bkg  ##############
###########################################
### Signal
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
samples['WpWp_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### Interference
# need:
# WpWpJJ_Interference_TuneCUETP8M1_13TeV-madgraph-pythia8
# WLLJJ_WToLNu_Interference_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8
#files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_Interference')
#samples['WpWpJJ_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_Interference')
#samples['WLLJJ_WToLNu_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

### WW QCD
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### WZ QCD
files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet')
samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.2',
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_ext1')
samples['WZ_QCD_AMCNLO'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['WZ_QCD_mllmin01'] = {
    'name': files,
    'weight': mcCommonWeight+'*(Gen_ZGstar_mass > 4)',
    'FilesPerJob': 4
}

### ZZ
# need:
# ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8
# ZZJJTo4L_QCD_TuneCP5_13TeV-madgraph-pythia8
files = nanoGetSampleFiles(mcDirectory, 'ZZTo4L_AMCNLOFXFX')
samples['ZZ4L'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ggZZ2m2t') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2t') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2m') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4t') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4m') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4e')
samples['ggZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### TVX
# need:
# TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8

files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'TTZToQQ') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToQQ') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll_4f')
samples['TVX'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### Vg
# need: 
# LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# old: WGJJ Zg
files = nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        nanoGetSampleFiles(mcDirectory, 'Zg')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

files = nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['VgS1'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS1', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS1', 'Zg', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

### Wrong-sign
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluWWTo2L2Nu_MCFM')
samples['WW'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop')
samples['Top'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

# MIT: 
# DY0JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY1JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY2JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY3JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY0JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY1JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY2JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
# DY3JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50-LO_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50')
samples['DY'] = {
    'name': files,
    'weight': 'mcCommonWeight_os*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
        Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 17,
}
# need:
# # not found: VBFHToZZTo4L_M125_13TeV_powheg2_JHUGenV714_pythia8
# VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8
files = nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125') + \
        nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125') + \
        nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluHToZZTo4L_M125') + \
        nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125')
samples['Higgs'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}
# Others
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')
samples['DPS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW') + \
        nanoGetSampleFiles(mcDirectory, 'WWG') 
samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
################## FAKE ###################
###########################################
#1389 files
samples['Fake_lep'] = {
    'name': [],
    'weight': 'METFilter_DATA*fakeW',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        if not (pd=='MuonEG' and _=='E'):
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__fakeW/', pd + '_' + sd)
        else:
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__fakeW/', pd + '_Run2016E-Nano1June2019-v3')
        samples['Fake_lep']['name'].extend(files)
        samples['Fake_lep']['weights'].extend([DataTrig[pd]] * len(files))
###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        if not (pd=='MuonEG' and _=='E'):
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__l2tightOR2016v6/', pd + '_' + sd)
        else:
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__l2tightOR2016v6/', pd + '_Run2016E-Nano1June2019-v3')
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))