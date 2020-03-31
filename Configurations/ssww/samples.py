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

mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'
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
mcCommonWeight = 'SFweight*PromptGenLepMatch2l'
mcCommonWeight_os = mcCommonWeight+'*chargeflip_w'
mcCommonWeight += '*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0)'

################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['A','Run2018A-Nano25Oct2019-v1'] ,
    ['B','Run2018B-Nano25Oct2019-v1'] ,
    ['C','Run2018C-Nano25Oct2019-v1'] ,
    ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,
]
DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}
###########################################
############  Reducible Bkg  ##############
###########################################
######## DY ########
# chargeflip
ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useDYtt = True

files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')


samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight_os + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                     Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 17,
}
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1',ptllDYW_LO)
# chargeflip
######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        nanoGetSampleFiles(mcDirectory, 'Zg')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}
addSampleWeight(samples, 'Vg', 'Zg', '0.448')

######## VgS ########
files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
        nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 15,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0)*0.448')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')
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
addSampleWeight(samples, 'VgS1', 'Zg', '(Gen_ZGstar_mass > 0)*0.448')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

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
addSampleWeight(samples, 'VgS2', 'Zg', '(Gen_ZGstar_mass > 0)*0.448')
######### VV #########
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')
#nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
#nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')

samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight+ '*1.11',
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')
samples['WZTo2L2Q'] = {
    'name': files,
    'weight': mcCommonWeight+ '*1.11',
    'FilesPerJob': 4
}
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
files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_powheg')
samples['WZ_QCD_powheg'] = {
    'name': files,
    'weight': mcCommonWeight,
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

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')# + \
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
########## VVV #########

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

########## TTV #########

files = nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
        nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

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
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
###########################################
#############   SIGNALS  ##################
###########################################
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK_madgraph')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['WpWp_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDir_private, 'VBS_SSWW_LL')

samples['ll'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}
files = nanoGetSampleFiles(mcDir_private, 'VBS_SSWW_LT')

samples['lt'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}
files = nanoGetSampleFiles(mcDir_private, 'VBS_SSWW_TT')

samples['tt'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}
files = nanoGetSampleFiles(mcDir_private, 'VBS_SSWW_TL')

samples['tl'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 25
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
    'FilesPerJob': 17
}

for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__fakeW/', pd + '_' + sd)
        samples['Fake_lep']['name'].extend(files)
        samples['Fake_lep']['weights'].extend([DataTrig[pd]] * len(files))
###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 17
}

for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6/', pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
