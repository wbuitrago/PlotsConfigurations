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

def makeMCDirectory(var=''):
    if var:
        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
        return '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6__{var}'.format(var=var)
    else:
        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR'

# samples
try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6/'

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction = 'Summer16_102X_nAODv5_Full2016v6'
mcSteps = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6{var}'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'SFweight'
mcCommonWeight = 'SFweight*PromptGenLepMatch3l'
#mcCommonWeight = 'XSWeight*SFweight*41.53'

################################################
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

######## Vg ########
files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(!(Gen_ZGstar_mass > 0))',
    'FilesPerJob': 4
}

######## VgS ########
files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
        nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass < 4)')

files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
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
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass < 4)')

files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['VgS2'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS2', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS2', 'Zg', '(Gen_ZGstar_mass > 0)')
######### VV #########
# ZZTo2L2Nu_EWK 9.85733 -> 0.002971/0.0003014
# ZZTo2L2Q_AMCNLOFXFX 1.25248 -> 4.033/3.22
# ZZTo4L_AMCNLOFXFX 0.9934 -> 1.204/1.212000
# WZTo2L2Q 1.0020 -> 5.606/5.5950
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_EWK') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q_AMCNLOFXFX') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L_AMCNLOFXFX')
samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
addSampleWeight(samples, 'ZZ', 'ZZTo2L2Nu_EWK', '9.85733')
addSampleWeight(samples, 'ZZ', 'ZZTo2L2Q_AMCNLOFXFX', '1.25248')

files = nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['WZTo2L2Q'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 7
}
files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet')

samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.2',
    'FilesPerJob': 7
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_ext1')
samples['WZ_QCD_powheg'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 7
}
files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_AMCNLO')
samples['WZ_QCD_AMCNLO'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.056',
    'FilesPerJob': 7
}

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 7
}

#addSampleWeight(samples,'WZ_EWK','WLLJJ_WToLNu_EWK', '(Gen_ZGstar_mass>=0.1)')
########## VVV #########
# WWW 1.138 -> 0.2086/0.18331
files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
addSampleWeight(samples, 'VVV', 'WWW', '1.138')

########## TTV #########

files = nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToQQ') + \
        nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10_ext3') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll_4f')

samples['TTV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
########## DPS #########
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['DPS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
###########################################
#######  IRREDUCIBLE BACKGROUNDS  #########
###########################################
# WpWpJJ_QCD 0.02612/0.02474
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.0558',
    'FilesPerJob': 4
}
###########################################
#############   SIGNALS  ##################
###########################################
# WpWpJJ_EWK 0.02695/0.02526
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['WpWp_EWK'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.067',
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
