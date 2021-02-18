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
samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5,
}

# EFTNeg cqq11 
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_QU')
samples['sm_lin_quad_cqq11'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq11_QU')
samples['quad_cqq11'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

# EFTNeg cqq1
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_QU')
samples['sm_lin_quad_cqq1'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq1_QU')
samples['quad_cqq1'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

# EFTNeg cqq31
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_QU')
samples['sm_lin_quad_cqq31'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq31_QU')
samples['quad_cqq31'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

# EFTNeg cqq3
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_QU')
samples['sm_lin_quad_cqq3'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cqq3_QU')
samples['quad_cqq3'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

# EFTNeg cqq3
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cW_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cW_QU')
samples['sm_lin_quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cW_QU')
samples['quad_cW'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

# EFTNeg cHl3
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_QU')
samples['sm_lin_quad_cHl3'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHl3_QU')
samples['quad_cHl3'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

# EFTNeg cHq3
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_QU')
samples['sm_lin_quad_cHq3'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cHq3_QU')
samples['quad_cHq3'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

# EFTNeg cll1
files = nanoGetSampleFiles(mcDirectory, 'WZeu_SM') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_LI') + \
        nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_QU')
samples['sm_lin_quad_cll1'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

files = nanoGetSampleFiles(mcDirectory, 'WZeu_cll1_QU')
samples['quad_cll1'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 5
}

#Mixing
