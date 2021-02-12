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

################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'SFweight'
mcCommonWeight = 'SFweight*PromptGenLepMatch3l'

mcDirectory_off = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
mcProduction_off = 'Autumn18_102X_nAODv7_Full2018v7'
treeBaseDir_off = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcSteps_off = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

def makeMCDirectory_off(var=''):
    if var:
        return os.path.join(treeBaseDir_off, mcProduction_off, mcSteps_off.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir_off, mcProduction_off, mcSteps_off.format(var='')) 

files = nanoGetSampleFiles(mcDirectory_off, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
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
    'FilesPerJob': 5,
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_LI')
samples['cqq11_LI'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_QU')
samples['cqq11_QU'] = {
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

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_LI')
samples['cqq31_LI'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_QU')
samples['cqq31_QU'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_LI')
samples['cqq3_LI'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_QU')
samples['cqq3_QU'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_LI')
samples['cHl3_LI'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_QU')
samples['cHl3_QU'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_LI')
samples['cHq3_LI'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_QU')
samples['cHq3_QU'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_LI')
samples['cll1_LI'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_QU')
samples['cll1_QU'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

