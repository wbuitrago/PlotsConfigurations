import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2018
configurations = os.path.dirname(configurations) # VBF_Zjj
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

# embedReco = 'Embedding2018_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'

# embedSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
mcPrivateDirectory = os.path.join(treeBaseDirPrivate, mcProduction, mcSteps.format(var=''))
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90'
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l

################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight1l =       'puWeight*\
                   TriggerEffWeight_1l*\
                   Lepton_RecoSF[0]*\
                   EMTFbug_veto'
SFweight      = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l+'*PrefireWeight'
     
#GenLepMatch   = 'Lepton_genmatched[0]'



################################################
############## FAKE WEIGHTS ####################
################################################

# if Nlep == '2' :
#   fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
# else:
   fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

#FIXME b-tagging to be optimized
# Definitions in aliases.py

# Not using any btagging yet
#SFweight += '*btagSF'

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

DataSets = ['SingleMuon','SingleElectron']

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl' 
}

#########################################
############ SIGNAL ##################
#########################################
###### W + jj EWK #######

files = nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK')

samples['VBF_WLNu'] = {
        'name': files,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC,
       'suppressNegative' :['all'],
       'suppressNegativeNuisances' :['all'],
       'FilesPerJob' : 3,
        }

###########################################
#############  BACKGROUNDS  ###############
###########################################

############ DY ############
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useEmbeddedDY = False
useDYtt = False

embed_tautauveto = ''

files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

samples['DY'] = {
        'name': files,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC ,
        'FilesPerJob' : 5,
                }

addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)



############ Top ############

Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'

files = nanoGetSampleFiles(mcDirectory,'ST_s-channel' )+\
        nanoGetSampleFiles(mcDirectory,'ST_t-channel_antitop') +\
        nanoGetSampleFiles(mcDirectory 'ST_t-channel_top') +\
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop')+\
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['singleTop'] = {    
            'name'   :  files
            'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC ,
            'FilesPerJob' : 3,
                 }

files = nanoGetSampleFiles(mcDirectory, 'TTToSemiLeptonic') +\
        nanoGetSampleFiles(mcDirectory, 'TTWjets')
    
samples["ttbar"] =  {  'name': files
                        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC,
                        'FilesPerJob': 3,
}

addSampleWeight(samples,'ttbar','TTToSemiLeptonic',Top_pTrw)
addSampleWeight(samples,'ttbar','TTWjets',Top_pTrw)

files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO')+\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') +\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') +\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') +\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') +\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') +\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') +\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf')

samples['Wjets'] = { 'name' :  files
				'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC ,
				'FilesPerJob' : 2,
		   }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets', 'WJetsToLNu-LO', 'LHE_HT < 100')

#
files = nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J_QCD') +\
        nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J_QCD') +\
        nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu_QCD') +\
        nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J_QCD') +\
        nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J_QCD') +\
        nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J_QCD')

samples['VV']  = { 'name' :  files
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC,
        'FilesPerJob' : 3,
}

#samples["FakeQCD"] = { 'name':
#        getSampleFiles(directory, 'QCD_Pt-15to20_MuEnrichedPt5', True, 'nanoLatino_') + 
#        getSampleFiles(directory, 'QCD_Pt-20to30_MuEnrichedPt5', True, 'nanoLatino_') +
#        getSampleFiles(directory, 'QCD_Pt-30to50_MuEnrichedPt5', True, 'nanoLatino_') +
#        getSampleFiles(directory, 'QCD_Pt-50to80_MuEnrichedPt5', True, 'nanoLatino_') +
#        getSampleFiles(directory, 'QCD_Pt-80to120_MuEnrichedPt5', True, 'nanoLatino_') +
#        getSampleFiles(directory, 'QCD_Pt-120to170_MuEnrichedPt5', True, 'nanoLatino_') +
#        getSampleFiles(directory, 'QCD_Pt-170to300_MuEnrichedPt5', True, 'nanoLatino_') +
        #getSampleFiles(directory, 'QCD_Pt-15to20_EMEnriched', True, 'nanoLatino_') + # missing sample (don't need this)
#        getSampleFiles(directory, 'QCD_Pt-20to30_EMEnriched', True, 'nanoLatino_') +
#        getSampleFiles(directory, 'QCD_Pt-30to50_EMEnriched', True, 'nanoLatino_') +
#        getSampleFiles(directory, 'QCD_Pt-50to80_EMEnriched', True, 'nanoLatino_'),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC,
#        'FilesPerJob' :10,
#}

# Filter efficiency for FakeQCD (https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns)
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-15to20_MuEnrichedPt5', '0.0022')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-20to30_MuEnrichedPt5', '0.0045')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-30to50_MuEnrichedPt5', '0.00974')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-50to80_MuEnrichedPt5', '0.0196')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-80to120_MuEnrichedPt5', '0.0322')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-120to170_MuEnrichedPt5', '0.04518')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-170to300_MuEnrichedPt5', '0.0598')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-15to20_EMEnriched', '0.0096')  #missing sample
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-20to30_EMEnriched', '0.0088')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-30to50_EMEnriched', '0.0470')
#addSampleWeight(samples, 'FakeQCD', 'QCD_Pt-50to80_EMEnriched', '0.100')


###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  #'suppressNegative' :['all'],
  #'suppressNegativeNuisances' :['all'],
   'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake']['subsamples'] = {
  'e': 'abs(Lepton_pdgId[1]) == 11',
  'm': 'abs(Lepton_pdgId[1]) == 13'
}

##########################################
################# DATA ###################
##########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))