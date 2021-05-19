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

################################################
############ PRIVATE SAMPLES ###################
################################################

mcDirectory = '/eos/user/e/evernazz/nanoAOD_PostProc_ntuple_WZin/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
treeBaseDir = '/eos/user/e/evernazz/nanoAOD_PostProc_ntuple_WZin'
mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))


### WZ EWK
files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK_off'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 3,
}

files = nanoGetSampleFiles(mcDirectory, 'WZin_SM')
samples['WZ_EWK_priv'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 10,
}

### WZ QCD
files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu')
samples['WZ_QCD_off'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZQCD_SM')
samples['WZ_QCD_priv'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 10,
}
