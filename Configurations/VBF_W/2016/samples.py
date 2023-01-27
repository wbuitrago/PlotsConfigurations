import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2016
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

mcProduction = 'Summer16_102X_nAODv7_Full2016v7'

dataReco = 'Run2016_102X_nAODv7_Full2016v7'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2016v7__MCCorr2016v7' 

#from VBS
dataSteps = 'DATAl1loose2016v7__DATACombJJLNu2016'

skim = '2Jets1leptonW2016'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

# def makeMCDirectory(var=''):
#   if var:
#       return os.path.join(treeBaseDir, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
#   else:
#       return os.path.join(treeBaseDir, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectory = os.path.join(treeBaseDir,  mcProduction , mcSteps)
mcPrivateDirectory = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + skim)


############################# PROVA
treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
directory_data   = os.path.join(treeBaseDir_SMP, dataReco+ '_skim', dataSteps)

# def CombineBaseW(samples, proc, samplelist):
#   newbaseW = getBaseWnAOD(mcPrivateDirectory, 'Autumn18_102X_nAODv7_Full2018v7', samplelist)
#   for s in samplelist:
#     addSampleWeight(samples, proc, s, newbaseW+'/baseW')
################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='1'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################
#corrected trigger efficiency

XSWeight      = 'XSWeight'
SFweight1l =       'puWeight*\
                   TriggerEffWeight_1l*\
                   Lepton_RecoSF[0]*\
                   EMTFbug_veto'
# SFweight      = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l+'* PrefireWeight * btagSF * PUJetIdSF * Wtagging_SF_nominal'
SFweight      = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l+'* PrefireWeight * btagSF * PUJetIdSF'
     
GenLepMatch   = 'Lepton_genmatched[0]'


################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

# CommonWeight = XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch
CommonWeight = XSWeight

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2016B-02Apr2020_ver2-v1'],
    ['C','Run2016C-02Apr2020-v1'],
    ['D','Run2016D-02Apr2020-v1'],
    ['E','Run2016E-02Apr2020-v1'],
    ['F','Run2016F-02Apr2020-v1'],
    ['G','Run2016G-02Apr2020-v1'],
    ['H','Run2016H-02Apr2020-v1']
]

DataSets = ['SingleMuon','SingleElectron']


DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl',
}


#########################################
############### SIGNAL ##################
#########################################
###### W + jj EWK #######

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcPrivateDirectory,'EWK_LNuJJ'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                    }

###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########
# Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
# Total_correction = 'WJets_reweight'

samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu-LO_ext2')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT100_200_ext2')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT200_400_ext2')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT400_600_ext1')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT600_800_ext1')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT800_1200_ext1')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT1200_2500_ext1')
                                   + nanoGetSampleFiles(mcPrivateDirectory, 'WJetsToLNu_HT2500_inf_ext1'),
                        'weight': CommonWeight,
			                	'FilesPerJob' : 1, 
                        'subsamples': {
                          'hardJets'  : 'hardJets',
                          'PUJets'    : 'PUJets'
                                    }
		                 }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO_ext2', '(LHE_HT < 100)') # to be add ewknloW here!

###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcPrivateDirectory,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcPrivateDirectory,'ST_tW_top') 
                                #  + nanoGetSampleFiles(mcPrivateDirectory,'TTToSemiLeptonic') to be add (not present in pvt)
                                 + nanoGetSampleFiles(mcPrivateDirectory,'TTZjets')
                                 + nanoGetSampleFiles(mcPrivateDirectory,'TTWJetsToLNu_ext1')
                                 + nanoGetSampleFiles(mcPrivateDirectory,'TTWJetsToLNu_ext2')
                                 + nanoGetSampleFiles(mcPrivateDirectory,'TTWJetsToQQ'),
                                 #+ nanoGetSampleFiles(mcPrivateDirectory,'TTWJetsToLNu'), #also this is available (was commented)
                      'weight': CommonWeight,
                      'FilesPerJob' : 16,
                      'EventsPerJob' : 70000,
                }

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

############ VBS ############

samples['VBS']  = { 'name' :  nanoGetSampleFiles(mcPrivateDirectory,'WmToLNu_ZTo2J') 
                              + nanoGetSampleFiles(mcPrivateDirectory,'WmTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_ZTo2J')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_WpTo2J')
                              + nanoGetSampleFiles(mcPrivateDirectory,'WmToLNu_WmTo2J')
#                             + nanoGetSampleFiles(mcPrivateDirectory,'WpToLNu_WmTo2J') solo QCD
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


##VBF-Z has an updated k-factor but w/ different sample files
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

# DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY_M-50'] = {    'name'   : nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-70to100')
#                                 + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50') non presente
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-100to200_ext1')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-50_HT-2500toInf'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }


samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-5to50_HT-70to100') #Don't use LO(_ext0)! DYMVA Training!
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-5to50_HT-100to200')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-5to50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-5to50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-5to50_HT-600toinf_ext1')
                                  + nanoGetSampleFiles(mcPrivateDirectory,'DYJetsToLL_M-10to50'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

########## VBF - Z #############

samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcPrivateDirectory,'EWK_LLJJ_MLL-50_MJJ-120'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }

##VBF-Z --> slighly different weight
###############################


############ Vg ##############

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcPrivateDirectory,'Wg_MADGRAPHMLM'),
                                #  + nanoGetSampleFiles(mcPrivateDirectory,'ZGToLLG'),
                    # 'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
                    'weight': CommonWeight,
                    'FilesPerJob' : 16,
                    'EventsPerJob' : 70000,
#                    'suppressNegative' :['all'],
#                    'suppressNegativeNuisances' :['all'],
                }



############ VgS ############

# samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcPrivateDirectory,'Wg_MADGRAPHMLM'),
#                       # 'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#                       'weight' : CommonWeight,
#                       'FilesPerJob' : 15,
#                       'EventsPerJob' : 70000,
#                       'suppressNegative' :['all'],
#                       'suppressNegativeNuisances' :['all'],
#                       # 'subsamples': {
#                       #   'L': 'gstarLow',
#                       #   'H': 'gstarHigh'
#                       # }
#                    }

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


# Then corrected
# fakeW = 'fakeWeight_35'
fakeW = 'fakeWeight_35'

### Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+fakeW,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 40,
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataPrivateDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

    

#########################################
################ DATA ###################
#########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 60,         
            }

for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(dataPrivateDirectory,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


#samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}


# mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s 2Jets1leptonW2016 -i MCl1loose2016v7__MCCorr2016v7 -b -Q workday -T EWK_LNuJJ,WJetsToLNu-LO_ext2,WJetsToLNu_HT100_200_ext2,WJetsToLNu_HT200_400_ext2,WJetsToLNu_HT400_600_ext1,WJetsToLNu_HT600_800_ext1,WJetsToLNu_HT800_1200_ext1,WJetsToLNu_HT1200_2500_ext1,WJetsToLNu_HT2500_inf_ext1,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTZjets,TTWJetsToLNu_ext1,TTWJetsToLNu_ext2,TTWJetsToQQ,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWW_LNu_M125,HWplusJ_HToWW_LNu_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200_ext1,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600_ext1,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-5to50_HT-70to100,DYJetsToLL_M-5to50_HT-100to200,DYJetsToLL_M-5to50_HT-200to400_ext1,DYJetsToLL_M-5to50_HT-400to600_ext1,DYJetsToLL_M-5to50_HT-600toinf_ext1,DYJetsToLL_M-10to50,EWK_LLJJ_MLL-50_MJJ-120,Wg_MADGRAPHMLM,ZZZ,WZZ,WWZ,WWW
