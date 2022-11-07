import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

############################################
############ MORE MC STAT ##################
############################################

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(directory_bkg, 'Autumn18_102X_nAODv7_Full2018v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')

##############################################
###### Tree Directory according to site ######
##############################################

samples={}


# Steps
mcSteps   = 'MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018' 
dataSteps = 'DATAl1loose2018v7__DATACombJJLNu2018'

SITE=os.uname()[1]
xrootdPath=''
if  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'

directory_bkg    = treeBaseDir + 'Autumn18_102X_nAODv7_Full2018v7/' + mcSteps
directory_signal = treeBaseDir_SMP + 'Autumn18_102X_nAODv7_Full2018v7/' + mcSteps
directory_data   = treeBaseDir + 'Run2018_102X_nAODv7_Full2018v7/'  + dataSteps

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='1'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight   = 'XSWeight'
SFweight1l = 'puWeight*\
              TriggerEffWeight_1l*\
              Lepton_RecoSF[0]'
SFweight  = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l
SFweight += '* btagSF *  PUJetIdSF * BoostedWtagSF_nominal'

GenLepMatch   = 'Lepton_genmatched[0]'

####
# NVTX reweighting
# SFweight += '*nvtx_reweighting'


################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['SingleMuon','EGamma']

DataTrig = {
            'SingleMuon' : 'Trigger_sngMu' ,
            'EGamma'     : '!Trigger_sngMu && Trigger_sngEl' 
}
###########################################
#############  BACKGROUNDS  ###############
##########################################


samples['Wjets_LO'] = { 'name' :   
            nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }


samples['Wjets_HT_70_100'] = { 'name' :   
            nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT70_100'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW * 1.21',### Added k-factor
        'FilesPerJob' : 15,
       }


samples['Wjets_HT_100_200'] = { 'name' :  
          nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }

samples['Wjets_HT_200_400'] = { 'name' :   
            nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }

samples['Wjets_HT_400_600'] = { 'name' :   
           nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }



samples['Wjets_HT_600_800'] = { 'name' :   
           nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }


samples['Wjets_HT_800_1200'] = { 'name' :   
           nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }


samples['Wjets_HT_1200_2500'] = { 'name' :   
           nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }


samples['Wjets_HT_2500_inf'] = { 'name' :   
           nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
        'FilesPerJob' : 15,
       }


addSampleWeight(samples,'Wjets_HT_100_200', 'WJetsToLNu-HT100_200', '0.993') 
addSampleWeight(samples,'Wjets_HT_200_400', 'WJetsToLNu-HT200_400', '1.002') 
addSampleWeight(samples,'Wjets_HT_400_600', 'WJetsToLNu-HT400_600', '1.009') 
addSampleWeight(samples,'Wjets_HT_600_800', 'WJetsToLNu-HT600_800', '1.120') 
addSampleWeight(samples,'Wjets_HT_800_1200', 'WJetsToLNu-HT800_1200', '1.202') 
addSampleWeight(samples,'Wjets_HT_1200_2500', 'WJetsToLNu-HT1200_2500', '1.332') 
addSampleWeight(samples,'Wjets_HT_2500_inf', 'WJetsToLNu-HT2500_inf', '4.200') 