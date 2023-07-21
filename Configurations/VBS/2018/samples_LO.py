import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # WWSS
configurations = os.path.dirname(configurations) # 2018
configurations = os.path.dirname(configurations) # VBS
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseWnAOD, addSampleWeight

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

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
MCDir = os.path.join(treeBaseDir,  mcProduction , mcSteps)


# MCDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'


################################################
################### WEIGHTS ####################
################################################

# ---------------------------------------- Basic MC weights
mcCommonWeightNoMatch = 'SFweight_mod'
mcCommonWeight = 'SFweight_mod*PromptGenLepMatch4l'

# ---------------------------------------- Number of leptons
#Nlep='2'
#Nlep='3'
Nlep='4'

# ---------------------------------------- Lepton WP
eleWP = 'mvaFall17V1Iso_WP90_SS_tthmva_70'
# eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP  = 'cut_Tight_HWWW_tthmva_80'
#muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

# ---------------------------------------- MET filters
METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

# ---------------------------------------- fake weights
#fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
#fakeW = 'fakeW_ele_mvaFall17V1Iso_WP90_SS_tthmva_70_mu_cut_Tight_HWWW_2l2j'
#fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2j'
# ---------------------------------------- Basic MC weights
XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'

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


################################################
################ MC SAMPLES ####################
################################################

samples['ggZZ4L'] = {  'name'  :  nanoGetSampleFiles(MCDir,'ggZZ4m')
                             + nanoGetSampleFiles(MCDir,'ggZZ4m_ext1')
                             + nanoGetSampleFiles(MCDir,'ggZZ4t')
                             + nanoGetSampleFiles(MCDir,'ggZZ4e')
                             + nanoGetSampleFiles(MCDir,'ggZZ2e2t')
                             + nanoGetSampleFiles(MCDir,'ggZZ2m2t')
                             + nanoGetSampleFiles(MCDir,'ggZZ2e2m'),
                    'weight' :  mcCommonWeight,
                    'FilesPerJob' : 15,
                 }

ggZZbaseW   = getBaseWnAOD(MCDir,'Autumn18_102X_nAODv7_Full2018v7',['ggZZ4m',        'ggZZ4m_ext1'])

addSampleWeight(samples,'ggZZ4L','ggZZ2e2t',      "1.68") ## The NLO/LO k-factor, cited from https://arxiv.org/abs/1509.06734v1
addSampleWeight(samples,'ggZZ4L','ggZZ2m2t',      "1.68")
addSampleWeight(samples,'ggZZ4L','ggZZ2e2m',      "1.68")
addSampleWeight(samples,'ggZZ4L','ggZZ4m',        "1.68*"+ggZZbaseW+"/baseW")
addSampleWeight(samples,'ggZZ4L','ggZZ4m_ext1',   "1.68*"+ggZZbaseW+"/baseW")
addSampleWeight(samples,'ggZZ4L','ggZZ4t',        "1.68")
addSampleWeight(samples,'ggZZ4L','ggZZ4e',        "1.68")

# ---------------------------------------- ZZEWK
files = nanoGetSampleFiles(MCDir, 'EWKZZjjTo4L')
samples['ZZ4L_VBS_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 15
}

# ---------------------------------------- ZZQCD

files = nanoGetSampleFiles(MCDir, 'ZZjjTo4L_QCD')
samples['qqZZjj4L_VBS_QCD'] = {
    'name': files,
    'weight': mcCommonWeight ,
    'FilesPerJob': 15
}

###########################################
################## DATA ###################
###########################################

samples['DATA']  = 	{  'name': [ ] ,
                       'weight' :METFilter_DATA + '*' + LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
					}

for Run in DataRun :
  #DataDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv4_14Dec_Full2018v4/DATAl1loose2018__l2loose__l2tightOR2018v4/'
  DataDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(DataDir,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])


# samples = {k:i for k, i in sampes.items() if k in ["VBSSSWW, DATA, Fake"]}
