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

mcDirectory1 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

treeBaseDir1 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction1 = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps1 = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir1, mcProduction1, mcSteps1.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir1, mcProduction1, mcSteps1.format(var=''))

################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'SFweight'
mcCommonWeight = 'SFweight*PromptGenLepMatch3l'

################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['A','Run2018A-02Apr2020-v1'] ,
    ['B','Run2018B-02Apr2020-v1'] ,
    ['C','Run2018C-02Apr2020-v1'] ,
    ['D','Run2018D-02Apr2020-v1'] ,
]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}

mcDirectory = '/eos/user/e/evernazz/nanoAOD_PostProc_ntuple/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
treeBaseDir = '/eos/user/e/evernazz/nanoAOD_PostProc_ntuple'
mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM')
samples['SM'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_LI')
samples['cqq1_LI'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_QU')
samples['cqq1_QU'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

###########################################
############  Reducible Bkg  ##############
###########################################
### Signal

files = nanoGetSampleFiles(mcDirectory1, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
################## FAKE ###################
###########################################
#1389 files

fkDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__fakeW'

samples['Fake'] = {
    'name': [],
    'weight': 'METFilter_DATA*fakeW',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}
for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles(fkDirectory, pd + '_' + sd)
        samples['Fake']['name'].extend(files)
        samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################

dtDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7'

samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles(dtDirectory, pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
