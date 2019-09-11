import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

##############################################
###### Tree Directory according to site ######
##############################################

samples={}

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
directory_MC = treeBaseDir + 'Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5'
directory_data = treeBaseDir + 'Run2017_102X_nAODv4_Full2017v5'

#############################################
########### Definition of weights ###########
#############################################
eleWP = 'mvaFall17V2Iso_WP90'
muWP  = 'cut_Tight_HWWW'

LepWPCut_1l    =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l =  'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                  Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l

XSWeight   =   'XSWeight'
SFweight1l =   'puWeight*\
                TriggerEffWeight_1l*\
                Lepton_RecoSF[0]*\
                EMTFbug_veto'

SFweight      = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l+'*PrefireWeight'

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'


#############################################
################# SAMPLES ###################
#############################################

samples['HH'] = {       'name' : getSampleFiles(directory_MC, 'GluGluToHHTo2B2WToLNu2J', True, 'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                        'FilesPerJob' : 3,
                }
 """                                                                                                                                                                                                1,1           Top
samples['Wjets'] = { 'name' :   
          getSampleFiles(directory, 'WJetsToLNu-LO', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu-LO_ext1', True, 'nanoLatino_')
          + getSampleFiles(directory, 'WJetsToLNu_HT100_200', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT100_200_ext1', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT100_200_ext2', True, 'nanoLatino_')
          + getSampleFiles(directory, 'WJetsToLNu_HT200_400', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT200_400_ext1', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT200_400_ext2', True, 'nanoLatino_')
          + getSampleFiles(directory, 'WJetsToLNu_HT400_600', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT400_600_ext1', True, 'nanoLatino_')
          + getSampleFiles(directory, 'WJetsToLNu_HT600_800', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT600_800_ext1', True, 'nanoLatino_')
          + getSampleFiles(directory, 'WJetsToLNu_HT800_1200', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT800_1200_ext1', True, 'nanoLatino_')
          + getSampleFiles(directory, 'WJetsToLNu_HT1200_2500', True, 'nanoLatino_')
          #+ getSampleFiles(directory, 'WJetsToLNu_HT1200_2500_ext1', True, 'nanoLatino_')
          + getSampleFiles(directory, 'WJetsToLNu_HT2500_inf', True, 'nanoLatino_'),
          #+ getSampleFiles(directory, 'WJetsToLNu_HT2500_inf_ext1', True, 'nanoLatino_'),
				'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC ,
				'FilesPerJob' : 2,
		   }



samples['TT_semilep']  = {    'name'   : getSampleFiles(directory_MC, 'TTToSemiLeptonic', True) ,
                      'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 3,
                 }

###### Drell-Yan #### 
samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-5to50-LO',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-4to50_HT-100to200',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-4to50_HT-200to400',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-4to50_HT-400to600',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-4to50_HT-600toInf',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_HT-100to200',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_HT-200to400',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_HT-400to600_ext1',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_HT-600to800',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_HT-800to1200',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_HT-1200to2500',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_HT-2500toInf',False,'nanoLatino_')
                                ,
                      'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 6,
                  }

##### Single Top ####
samples['singleTop'] = {    
            'name'   :  getSampleFiles(directory,'ST_s-channel',False,'nanoLatino_') 
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_') 
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_') 
                      + getSampleFiles(directory,'ST_tW_antitop',False,'nanoLatino_') 
                      + getSampleFiles(directory,'ST_tW_top',False,'nanoLatino_') ,
            'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC ,
            'FilesPerJob' : 3,
                 }

#### TT leptonic ####
samples['TT_leptonic']  = {    'name'   : getSampleFiles(directory_MC, 'TTTo2L2Nu',True),
                               'weight' :   XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                               'FilesPerJob' : 3,
                          }
##### WW #####
samples['WW']  = {    'name'   : getSampleFiles(directory_MC, 'WWTo2L2Nu',True),
                      'weight' :   XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 3,
                 }

#### WWW ####
samples['WWW']  = {    'name'   : getSampleFiles(directory_MC, 'WWW',True),
                      'weight' :    XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 3,
                 }

samples['WWZ']  = {   'name'   : getSampleFiles(directory_MC, 'WWZ',True),
                      'weight' :    XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 3,
                 }

#### WZ #### 
samples['WZ']  = {    'name'   : getSampleFiles(directory_MC, 'WZTo1L1Nu2Q',True)\
                                         +getSampleFiles(directory_MC, 'WZTo1L3Nu',True) \
                                         +getSampleFiles(directory_MC, 'WZTo2L2Q',True),
                      'weight' :   XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 3,
                 }
                                                                                                                                                                                                 141,1         67%
#### ZZ #### 
samples['ZZ']  = {   'name'   : getSampleFiles(directory_MC, 'ZZTo2L2Q',True)\
                               +getSampleFiles(directory_MC, 'ZZTo2L2Nu',True),
                      'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 3,
                 }

####################
###### DATA ########
####################
DataRun = [
            ['B','Run2017B-Nano14Dec2018-v1'] ,
            ['C','Run2017C-Nano14Dec2018-v1'] ,
            ['D','Run2017D-Nano14Dec2018-v1'] ,
            ['E','Run2017E-Nano14Dec2018-v1'] ,
            ['F','Run2017F-Nano14Dec2018-v1']
          ]

DataSets = ['SingleMuon','SingleElectron']

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl' 
}

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20,
                  }

for Run in DataRun :
        directory = treeBaseDir+'Run2017_102X_nAODv4_Full2017v5/DATAl1loose2017v5/DATAl1loose2017v5' #???????
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:
                        print(iFile)
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
"""
