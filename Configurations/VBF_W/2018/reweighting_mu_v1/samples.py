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

mcDirectory = os.path.join(treeBaseDir,  mcProduction , mcSteps)
mcPrivateDirectory = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + skim)


############################# PROVA
treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
directory_data   = os.path.join(treeBaseDir_SMP, dataReco+ '_skim', dataSteps)

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(mcDirectory, 'Autumn18_102X_nAODv7_Full2018v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')
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
              'btagSF','PUJetIdSF'] #btagSF removed

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

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectory,'WLNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                    }

###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '

samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT70_100')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf'),
#				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
                        'weight': CommonWeight+'*' + Wjets_photon_filter +'* ewknloW',
			                	'FilesPerJob' : 15, 
                        'subsamples': {
                          'hardJets'  : 'hardJets',
                          'PUJets'    : 'PUJets'
                                    }
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

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectory,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectory,'ST_s-channel_ext1') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_antitop_ext1') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_top_ext1') 
                                 + nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic') 
                                 + nanoGetSampleFiles(mcDirectory,'TTZjets')
                                 + nanoGetSampleFiles(mcDirectory,'TTWjets'),
                                 #+ nanoGetSampleFiles(mcDirectory,'TTWJetsToLNu'), #also this is available (was commented)
                      'weight': CommonWeight,
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                      'FilesPerJob' : 16,
                      'EventsPerJob' : 70000,
#                     'suppressNegative' :['all'],
#                     'suppressNegativeNuisances' :['all'],
                }

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
#addSampleWeight(samples,'top','TTZjets','Top_pTrw')
#addSampleWeight(samples,'top','TTWjets','Top_pTrw')

#Not corrected in baseW, so we should correct the XS here
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


###############################################


############## VV ##################

samples['VV']  = { 'name' :  nanoGetSampleFiles(mcDirectory,'WmToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WmToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WmTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpTo2J_WmToLNu_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpToLNu_WpTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'ZTo2L_ZTo2J_QCD'),
                   'weight': CommonWeight,
#                   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, # still missing EWKnlowW 
                   'FilesPerJob' : 17,
                   'EventsPerJob' : 70000,
                }


###############################################

############ VBS ############

samples['VBS']  = { 'name' :  nanoGetSampleFiles(mcDirectory,'WmToLNu_ZTo2J') 
                              + nanoGetSampleFiles(mcDirectory,'WmTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectory,'WpTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectory,'WpToLNu_ZTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WpToLNu_WpTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WmToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WpToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WpTo2J_WmToLNu')
                              + nanoGetSampleFiles(mcDirectory,'ZTo2L_ZTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WWToLNuQQ'),
                    'weight': CommonWeight,
#                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' :16,
                    'EventsPerJob' : 70000,
                }

########################################


################ ggWW ##################

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(mcDirectory,'GluGluWWToLNuQQ'),
                    'weight': CommonWeight,
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }


##VBF-Z has an updated k-factor but w/ different sample files
##################################################

########### Higgs Related #############

samples['Higgs']  = {   'name'   :  nanoGetSampleFiles(mcDirectory,'GluGluHToWWToLNuQQ_M125')
                                    + nanoGetSampleFiles(mcDirectory,'HWminusJ_HToWW_LNu_M125')
                                    + nanoGetSampleFiles(mcDirectory,'HWplusJ_HToWW_LNu_M125')
                                    + nanoGetSampleFiles(mcDirectory,'VBFHToWWToLNuQQ_M125'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }


########### DY ############

DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY_M-50'] = {    'name'   :   nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50') #Don't use LO(_ext0)! DYMVA Training!
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_ext2')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf'),
                        'weight': CommonWeight+'*'+DY_photon_filter,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

#VBF-Z does use less sample (only M-50 and applies dome different weights (but uses signal at higher energies))
CombineBaseW(samples, 'DY_M-50', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext2'])
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50',               '(LHE_HT < 70)')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext2',          '(LHE_HT < 70)') 
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-70to100',    'DY_LO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-100to200',   'DY_LO_pTllrw * 1.000') #HT stitching correction
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-200to400',   'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-400to600',   'DY_LO_pTllrw * 0.990')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-600to800',   'DY_LO_pTllrw * 0.975')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-800to1200',  'DY_LO_pTllrw * 0.907')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-1200to2500', 'DY_LO_pTllrw * 0.833')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-2500toInf',  'DY_LO_pTllrw * 1.015')  




samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-10to50-LO_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-600toInf'),
                        'weight': CommonWeight+'*'+DY_photon_filter,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

addSampleWeight(samples,'DY_else','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw') 
addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-100to200','DY_LO_pTllrw') 
addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-200to400','DY_LO_pTllrw')
addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-400to600','DY_LO_pTllrw')
addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-600toInf','DY_LO_pTllrw')

################################

########## VBF - Z #############

samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcDirectory,'EWKZ2Jets_ZToLL_M-50'),
                        'weight': CommonWeight+ '*(lhe_mjj[0] > 120)',
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }

##VBF-Z --> slighly different weight
###############################


############ Vg ##############

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'ZGToLLG'),
                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 16,
                    'EventsPerJob' : 70000,
#                    'suppressNegative' :['all'],
#                    'suppressNegativeNuisances' :['all'],
                }

# the following baseW correction is needed in both v5 and v6 (for Zg, Not for ZGToLLG)
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

##VBF-Z has different weights (common)+genstar
###############################


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'ZGToLLG'),
                      'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 15,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                      # 'subsamples': {
                      #   'L': 'gstarLow',
                      #   'H': 'gstarHigh'
                      # }
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') # *0.448 XS correction for Zg
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'ZZZ')
                                + nanoGetSampleFiles(mcDirectory,'WZZ')
                                + nanoGetSampleFiles(mcDirectory,'WWZ')
                                + nanoGetSampleFiles(mcDirectory,'WWW'),
                    'weight': CommonWeight,
                                #+ nanoGetSampleFiles(mcDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 15,
                     'EventsPerJob' : 70000,
                  }


##########################################
############### VBS ###############
##########################################

#samples['WWewk'] = {
#    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop_dipoleRecoil_private'),
#    'weight': CommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
#     'FilesPerJob': 4
#}

# Then corrected
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
    # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
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
                FileTarget = nanoGetSampleFiles(dataDirectory,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


#samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}