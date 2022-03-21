import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2018
configurations = os.path.dirname(configurations) # VBF_W
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, getBaseWnAOD, addSampleWeight

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
################# SKIMS ########################
################################################

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'

dataReco = 'Run2018_102X_nAODv7_Full2018v7'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2018v7__MCCorr2018v7' 

#from VBS
dataSteps = 'DATAl1loose2018v7__DATACombJJLNu2018'

skim = '2Jets1leptonW'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

mcDirectory = os.path.join(treeBaseDir,  mcProduction , mcSteps + '__' + skim)
mcPrivateDirectory = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps + '__' + skim)
dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + skim)


################################################
############ NUMBER OF LEPTONS #################
################################################

#Nlep='1'
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
#corrected trigger efficiency

XSWeight   = 'XSWeight'
SFweight1l = [ 'puWeight', 'SingleLepton_trigEff_corrected[0]',
              'Lepton_RecoSF[0]',LepWPWeight_1l, LepWPCut_1l,
              'PUJetIdSF']  #btagSF removed

SFweight = '*'.join(SFweight1l)

GenLepMatch   = 'Lepton_genmatched[0]'


################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

CommonWeight = XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch

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


#########################################
############### SIGNAL ##################
#########################################
###### W + jj EWK #######

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcPrivateDirectory,'WLNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                    }

###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########

samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu-LO')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT70_100')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT100_200')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT200_400')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT400_600')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT600_800')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT800_1200')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT1200_2500')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT2500_inf'),
#				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
                        'weight': CommonWeight+'* ewknloW',
			                	'FilesPerJob' : 15,   
        # 'subsamples': {
        #     "res_1": '(VBS_category==1) && (w_lep_pt < 100)',
        #     "res_2": '(VBS_category==1) && (w_lep_pt >= 100 && w_lep_pt < 200)',
        #     "res_3": '(VBS_category==1) && (w_lep_pt >= 200 && w_lep_pt < 300)',
        #     "res_4": '(VBS_category==1) && (w_lep_pt >= 300 && w_lep_pt < 400)',
        #     "res_5": '(VBS_category==1) && (w_lep_pt >= 400 && w_lep_pt < 500)',
        #     "res_6": '(VBS_category==1) && (w_lep_pt >= 500)',
        #     "boost_1": '(VBS_category==0) && (w_lep_pt < 75)',
        #     "boost_2": '(VBS_category==0) && (w_lep_pt >= 75 && w_lep_pt < 150)',
        #     "boost_3": '(VBS_category==0) && (w_lep_pt >= 150 && w_lep_pt < 250)',
        #     "boost_4": '(VBS_category==0) && (w_lep_pt >= 250 && w_lep_pt < 400)',
        #     "boost_5": '(VBS_category==0) && (w_lep_pt >= 400)',
        # }
		                 }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
############
# HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70_100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100_200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200_400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400_600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600_800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800_1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200_2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500_inf',  '2.7948') 

###############################################



############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcPrivateDirectory,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_s-channel_ext1') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_tW_antitop_ext1') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_tW_top_ext1') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'TTToSemiLeptonic') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'TTZjets')
                                 + nanoGetSampleFiles(mcPrivateDirectory,'TTWjets')
                                 +  nanoGetSampleFiles(mcPrivateDirectory,'TTWJetsToLNu'), #also this is available (was commented)
                      'weight': CommonWeight,
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                      'FilesPerJob' : 16,
                      'EventsPerJob' : 70000,
#                     'suppressNegative' :['all'],
#                     'suppressNegativeNuisances' :['all'],
                }

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw') #correzione NNLO in cui correggo pt_(2top) 
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','TTZjets','Top_pTrw')
addSampleWeight(samples,'top','TTWjets','Top_pTrw')

#Not corrected in baseW, so we should correct the XS here
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


###############################################


############## VV ##################

samples['VV']  = { 'name' :  nanoGetSampleFiles(mcPrivateDirectory,'WmToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'WmToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'WmTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'WpTo2J_WmToLNu_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'WpTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_WpTo2J_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcPrivateDirectory,'ZTo2L_ZTo2J_QCD'),
                   'weight': CommonWeight,
#                   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, # still missing EWKnlowW 
                   'FilesPerJob' : 17,
                   'EventsPerJob' : 70000,
                }


###############################################

#29
############ VBS ############

samples['VBS']  = { 'name' :  nanoGetSampleFiles(mcPrivateDirectory,'WmToLNu_ZTo2J') 
                              + nanoGetSampleFiles(mcPrivateDirectory,'WmTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_ZTo2J')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_WpTo2J')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WmToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpTo2J_WmToLNu')
                              + nanoGetSampleFiles(mcPrivateDirectory,'ZTo2L_ZTo2J')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WWToLNuQQ'),
                    'weight': CommonWeight,
#                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' :16,
                    'EventsPerJob' : 70000,
                }

########################################


################ ggWW ##################

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(mcPrivateDirectory,'GluGluWWToLNuQQ'),
                    'weight': CommonWeight,
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }

##################################################

########### Higgs Related #############

samples['Higgs']  = {   'name'   :  nanoGetSampleFiles(mcPrivateDirectory,'GluGluHToWWToLNuQQ_M125')
                                    + nanoGetSampleFiles(mcPrivateDirectory,'HWminusJ_HToWW_LNu_M125')
                                    + nanoGetSampleFiles(mcPrivateDirectory,'HWplusJ_HToWW_LNu_M125')
                                    + nanoGetSampleFiles(mcPrivateDirectory,'VBFHToWWToLNuQQ_M125'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }


########### DY ############

DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY'] = {    'name'   :   #nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50') #Don't use LO(_ext0)! DYMVA Training!
                                  nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_ext2')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-10to50-LO_ext1')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-4to50_HT-100to200')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-4to50_HT-200to400')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-4to50_HT-600toInf'),
                        'weight': CommonWeight+'*'+DY_photon_filter,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

#CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext2'])
addSampleWeight(samples,'DY','DYJetsToLL_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw') 
addSampleWeight(samples,'DY','DYJetsToLL_M-50',               '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',          '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1',   '(LHE_HT < 100)')   
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100',    'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',   'DY_LO_pTllrw * 1.000') #HT stitching correction
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',   'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600',   'DY_LO_pTllrw * 0.990')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',   'DY_LO_pTllrw * 0.975')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',  'DY_LO_pTllrw * 0.907')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500', 'DY_LO_pTllrw * 0.833')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',  'DY_LO_pTllrw * 1.015')  
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200','DY_LO_pTllrw') 
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf','DY_LO_pTllrw')

################################
#58
########## VBF - Z #############

samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcPrivateDirectory,'EWKZ2Jets_ZToLL_M-50'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }

###############################


############ Vg ##############

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcPrivateDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ZGToLLG'),
                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 16,
                    'EventsPerJob' : 70000,
#                    'suppressNegative' :['all'],
#                    'suppressNegativeNuisances' :['all'],
                }

# the following baseW correction is needed in both v5 and v6 (for Zg, Not for ZGToLLG)
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

###############################


############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcPrivateDirectory,'ZZZ')
                                + nanoGetSampleFiles(mcPrivateDirectory,'WZZ')
                                + nanoGetSampleFiles(mcPrivateDirectory,'WWZ')
                                + nanoGetSampleFiles(mcPrivateDirectory,'WWW'),
                    'weight': CommonWeight,
                                #+ nanoGetSampleFiles(mcPrivateDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 15,
                     'EventsPerJob' : 70000,
                  }


#65
############ VgS ############

#samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcPrivateDirectory,'Wg_MADGRAPHMLM')
#                                 + nanoGetSampleFiles(mcPrivateDirectory,'ZGToLLG')
#                                 + nanoGetSampleFiles(mcPrivateDirectory,'WZTo3LNu_mllmin01'),
#                      'weight' : '1',
#                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#                      'FilesPerJob' : 15,
#                      'EventsPerJob' : 70000,
#                      'suppressNegative' :['all'],
#                      'suppressNegativeNuisances' :['all'],
                      # 'subsamples': {
                      #   'L': 'gstarLow',
                      #   'H': 'gstarHigh'
                      # }
#                   }

#addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') # *0.448 XS correction for Zg
#addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')






# Then corrected
#fakeW = 'fakeWeight_35'

### Fakes
#samples['Fake'] = {
#  'name': [],
#  'weight': METFilter_DATA+'*'+fakeW,
#  'weights': [],
#  'isData': ['all'],
#  'FilesPerJob' : 40
#}

#for _, sd in DataRun:
#  for pd in DataSets:
#    # BE Careful --> we use dataDirectory because the Lepton tight cut was not applied in post-processing
#    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
#    samples['Fake']['name'].extend(files)
#    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


#########################################
################ DATA ###################
#########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 40,         
            }

for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(dataPrivateDirectory,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


#samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}