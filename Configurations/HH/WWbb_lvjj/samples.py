import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

##############################################
###### Tree Directory according to site ######
##############################################

samples={}

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
directory_MC = treeBaseDir + 'Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1'
directory_data = treeBaseDir + 'Run2017_102X_nAODv4_Full2017v5/'

#############################################
########### Definition of weights ###########
#############################################
eleWP = 'mvaFall17V1Iso_WP90'
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

ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'

#############################################
################# SAMPLES ###################
#############################################


##SIGNAL##
samples['HH'] = {       'name' : getSampleFiles(directory_MC, 'GluGluToHHTo2B2WToLNu2J', True, 'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                        'FilesPerJob' : 2,
                }
## tt->WWbb->bblvjj ##
samples['TT_semilep']  = {    'name'   : getSampleFiles(directory_MC, 'TTToSemiLeptonic', True, 'nanoLatino_') ,
                      'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 3,
                 }
## W+jets -> lv +jets ##
samples['Wjets'] = { 'name' :   
          getSampleFiles(directory_MC, 'WJetsToLNu-LO', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu-LO_ext1', True, 'nanoLatino_')#
          + getSampleFiles(directory_MC, 'WJetsToLNu_HT100_200', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT100_200_ext1', True, 'nanoLatino_')#
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT100_200_ext2', True, 'nanoLatino_')#
          + getSampleFiles(directory_MC, 'WJetsToLNu_HT200_400', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT200_400_ext1', True, 'nanoLatino_')#
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT200_400_ext2', True, 'nanoLatino_')#
          + getSampleFiles(directory_MC, 'WJetsToLNu_HT400_600', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT400_600_ext1', True, 'nanoLatino_')#
          + getSampleFiles(directory_MC, 'WJetsToLNu_HT600_800', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT600_800_ext1', True, 'nanoLatino_')#
          + getSampleFiles(directory_MC, 'WJetsToLNu_HT800_1200', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT800_1200_ext1', True, 'nanoLatino_')#
          + getSampleFiles(directory_MC, 'WJetsToLNu_HT1200_2500', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT1200_2500_ext1', True, 'nanoLatino_')#
          + getSampleFiles(directory_MC, 'WJetsToLNu_HT2500_inf', True, 'nanoLatino_')
          #+ getSampleFiles(directory_MC, 'WJetsToLNu_HT2500_inf_ext1', True, 'nanoLatino_')#
          ,
				'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC ,
				'FilesPerJob' : 3,
		   }
addSampleWeight(samples,'Wjets', 'WJetsToLNu-LO', 'LHE_HT < 100')
addSampleWeight(samples,'Wjets', 'WJetsToLNu-LO_ext1', 'LHE_HT < 100')

#### other tt samples ####
samples["ttbar"] =  {  'name': getSampleFiles(directory_MC,'TTTo2L2Nu',True,'nanoLatino_' ) 
                            +  getSampleFiles(directory_MC,'TTWjets',True,'nanoLatino_' )
                            #+  getSampleFiles(directory_MC,'TTWjets_ext1',True,'nanoLatino_' )#
                            +  getSampleFiles(directory_MC,'TTZjets',True,'nanoLatino_' )
                            #+  getSampleFiles(directory_MC,'TTZjets_ext1',True,'nanoLatino_' )#
                            #+  getSampleFiles(directory_MC,'TTWJetsToLNu',True,'nanoLatino_' )#
                            ,
                        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC,
                        'FilesPerJob': 3,
}
addSampleWeight(samples,'TT_semilep','TTToSemiLeptonic',Top_pTrw)
addSampleWeight(samples,'ttbar','TTTo2L2Nu',Top_pTrw)
addSampleWeight(samples,'ttbar','TTWjets',Top_pTrw)
addSampleWeight(samples,'ttbar','TTWjets_ext1',Top_pTrw)
addSampleWeight(samples,'ttbar','TTZjets',Top_pTrw)
addSampleWeight(samples,'ttbar','TTZjets_ext1',Top_pTrw)

##### Single Top ####
samples['singleTop'] = {    
                         'name'   :  getSampleFiles(directory_MC,'ST_s-channel',True,'nanoLatino_') 
                                   + getSampleFiles(directory_MC,'ST_t-channel_antitop',True,'nanoLatino_') 
                                   + getSampleFiles(directory_MC,'ST_t-channel_top',True,'nanoLatino_') 
                                   + getSampleFiles(directory_MC,'ST_tW_antitop',True,'nanoLatino_') 
                                   + getSampleFiles(directory_MC,'ST_tW_top',True,'nanoLatino_') ,
                         'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                         'FilesPerJob' : 3,
                         }

###### Drell-Yan #### 
samples['DY'] = {    'name'   :   getSampleFiles(directory_MC,'DYJetsToLL_M-5to50-LO',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-4to50_HT-100to200',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-4to50_HT-200to400',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-4to50_HT-400to600',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-4to50_HT-600toInf',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50_HT-100to200',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50_HT-200to400',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50_HT-400to600_ext1',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50_HT-600to800',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50_HT-800to1200',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50_HT-1200to2500',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'DYJetsToLL_M-50_HT-2500toInf',True,'nanoLatino_')
                                ,
                      'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                      'FilesPerJob' : 6,
                  }
addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO +'*(LHE_HT<100)')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50-LO',ptllDYW_LO +'*(LHE_HT<100)')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_ext1',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',ptllDYW_LO)


samples['VV']  = { 'name' :  
               getSampleFiles(directory_MC,'WmTo2J_ZTo2L_QCD',   True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'WmToLNu_WmTo2J_QCD', True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'WmToLNu_ZTo2J_QCD',  True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'WpTo2J_WmToLNu_QCD', True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'WpTo2J_ZTo2L_QCD',   True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'WpToLNu_WmTo2J_QCD', True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'WpToLNu_WpTo2J_QCD', True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'WpToLNu_ZTo2J_QCD',  True, 'nanoLatino_') +
               getSampleFiles(directory_MC,'ZTo2L_ZTo2J_QCD',    True, 'nanoLatino_') ,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC,
        'FilesPerJob' : 3,
}
samples['VVV']  = {  'name'   :   getSampleFiles(directory_MC,'ZZZ',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'WZZ',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'WWZ',True,'nanoLatino_')
                                + getSampleFiles(directory_MC,'WWW',True,'nanoLatino_'),
                                #+ getSampleFiles(directory_MC,'WWG',True,'nanoLatino_'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC ,
                    'FilesPerJob' : 3,
                  }





###########################
###### DATA (2017) ########
###########################
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
'''
samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20,
                  }

for Run in DataRun :
        directory = treeBaseDir+'Run2017_102X_nAODv4_Full2017v5/DATAl1loose2017v5__HHbblnuSkim2017v1' 
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:
                        print(iFile)
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
'''