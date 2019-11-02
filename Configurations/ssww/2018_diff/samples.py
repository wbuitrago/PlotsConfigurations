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

mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5/'

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################
'''
eleWP='cut_WP_Tight80X_SS'
muWP='cut_Tight80x'

LepWPCut_2016       = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight_2016     = '35.92*LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

fakeW_2016 = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
'''


################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC*59.74'
#mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*59.74'
mcCommonWeight = 'SFweight*59.74'
################################################
############### B-Tag  WP ######################
################################################

# Definitions in aliases.py

#SFweight += '*btagSF'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'
METFilter_FAKE = 'METFilter_FAKE'

################################################
############ DATA DECLARATION ##################
################################################
DataRun_2016 = [
    ['B','Run2016B-Nano14Dec2018_ver2-v1'] ,
    ['C','Run2016C-Nano14Dec2018-v1'] ,
    ['D','Run2016D-Nano14Dec2018-v1'] ,
    ['E','Run2016E-Nano14Dec2018-v1'] ,
    ['F','Run2016F-Nano14Dec2018-v1'] ,
    ['G','Run2016G-Nano14Dec2018-v1'] ,
    ['H','Run2016H-Nano14Dec2018-v1'] ,
]


DataSets_2016 = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig_2016 = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
}

DataRun_2017 = [
    ['B','Run2017B-Nano14Dec2018-v1'] ,
    ['C','Run2017C-Nano14Dec2018-v1'] ,
    ['D','Run2017D-Nano14Dec2018-v1'] ,
    ['E','Run2017E-Nano14Dec2018-v1'] ,
    ['F','Run2017F-Nano14Dec2018-v1'] ,
]

DataSets_2017 = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']


DataTrig_2017 = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu &&  Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu &&  Trigger_sngMu' ,
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu &&  Trigger_dblEl' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl &&  Trigger_sngEl' ,
}

DataRun_2018 = [
    ['A','Run2018A-Nano1June2019-v1'] ,
    ['B','Run2018B-Nano1June2019-v1'] ,
    ['C','Run2018C-Nano1June2019-v1'] ,
    ['D','Run2018D-Nano1June2019_ver2-v1'] ,
]

DataSets_2018 = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig_2018 = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}
###########################################
############  Reducible Bkg  ##############
###########################################

# charge flip
'''
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

samples['ChMisId']=	{  	'name'	:getSampleFiles(chargeFlipDir,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'DYJetsToLL_M-50',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToENEN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToENMN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToENTN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToMNEN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToMNMN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToMNTN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToTNEN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToTNMN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'GluGluToWWToTNTN',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'WWTo2L2Nu',False,'nanoLatino_')
    ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*ChargeFlipW_vbs',
                            'FilesPerJob' : 15 ,
                            }
addSampleWeight(samples,'ChMisId','DYJetsToLL_M-10to50-LO'	,ptllDYW_LO)
addSampleWeight(samples,'ChMisId','DYJetsToLL_M-50'   	,ptllDYW_NLO)

###### TopAntiTop#######
Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'

samples['ttbar'] = 	{ 	'name'  :getSampleFiles(chargeFlipDir,'TTTo2L2Nu',False,'nanoLatino_')
                                    +getSampleFiles(chargeFlipDir,'ST_s-channel',False,'nanoLatino_')
                                    +getSampleFiles(chargeFlipDir,'ST_t-channel_antitop',False,'nanoLatino_')
                                    +getSampleFiles(chargeFlipDir,'ST_t-channel_top',False,'nanoLatino_')
                                    +getSampleFiles(chargeFlipDir,'ST_tW_antitop',False,'nanoLatino_')
                                    +getSampleFiles(chargeFlipDir,'ST_tW_top',False,'nanoLatino_')
    ,
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*ChargeFlipW_vbs',
                           'FilesPerJob' : 15 ,
                           }
addSampleWeight(samples,'ttbar','TTTo2L2Nu',Top_pTrw)
'''
######## Vgamma ########

files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeight, #mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)',
    'FilesPerJob': 4
}
#addSampleWeight(samples, 'Vg', 'Zg', '(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')

######### VV #########
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext1')
        #nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
        #nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')

samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
        #nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_ext1')
samples['WZ'] = {
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
        nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10')
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

samples['WW_strong'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
###########################################
#############   SIGNALS  ##################
###########################################
'''
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['WW_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
'''
mjj="sqrt(2*Alt$(GenJet_pt[0],-9999.)*Alt$(GenJet_pt[1],-9999.)*(cosh(Alt$(GenJet_eta[0],-9999.)-Alt$(GenJet_eta[1],-9999.))-cos(Alt$(GenJet_phi[0],-9999.)-Alt$(GenJet_phi[1],-9999.))))"
mll="sqrt(2*Alt$(LeptonGen_pt[0],-9999.)*Alt$(LeptonGen_pt[1],-9999.)*(cosh(Alt$(LeptonGen_eta[0],-9999.)-Alt$(LeptonGen_eta[1],-9999.))-cos(Alt$(LeptonGen_phi[0],-9999.)-Alt$(LeptonGen_phi[1],-9999.))))"

#mjj
#wwjj_bin0="("+mjj+"<1000)"
#wwjj_bin1="("+mjj+">=1000 && "+mjj+"<1500)"
#wwjj_bin2="("+mjj+">=1500)"

# mll

#wwjj_bin0="("+mll+"<95)"
#wwjj_bin1="("+mll+">=95 && "+mll+"<190)"
#wwjj_bin2="("+mll+">=190)"
#
#Dressed lepton pt 1 [30, 55, 90, 130, 180, 240, 320]
wwjj_bin0 = "(GenDressedLepton_pt[0]<55 && GenDressedLepton_pt[0]>=30)"
wwjj_bin1 = "(GenDressedLepton_pt[0]>=55 && GenDressedLepton_pt[0]<90)"
wwjj_bin2 = "(GenDressedLepton_pt[0]>=90 && GenDressedLepton_pt[0]<130)"
wwjj_bin3 = "(GenDressedLepton_pt[0]>=130 && GenDressedLepton_pt[0]<180)"
wwjj_bin4 = "(GenDressedLepton_pt[0]>=180)"

#dressed lepton pt2 2
#wwjj_bin0  = "(std_vector_dressedLeptonGen_pt[1]<50)"
#wwjj_bin1 = "(std_vector_dressedLeptonGen_pt[1]>=50 && std_vector_DressedLeptonGen_pt[1]<100)"
#wwjj_bin2 ="(std_vector_dressedLeptonGen_pt[1]>=100)"
#wwjj_bin3 ="(std_vector_dressedLeptonGen_pt[0]>=150)"
#A dressed lepton is a system formed of a charged lepton and nearby photons-> should be dressedLeptonGen used insted of the normal lepGen?

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')

samples['Signal_bin0'] = {
    'name': files,
    'weight':mcCommonWeight+'*'+wwjj_bin0,
    'FilesPerJob' : 6,
}

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')

samples['Signal_bin1'] = {
    'name': files,
    'weight':mcCommonWeight+'*'+wwjj_bin1,
    'FilesPerJob' : 6,
}

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')

samples['Signal_bin2'] = {
    'name': files,
    'weight':mcCommonWeight+'*'+wwjj_bin2,
    'FilesPerJob' : 6,
}

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')

samples['Signal_bin3'] = {
    'name': files,
    'weight':mcCommonWeight+'*'+wwjj_bin3,
    'FilesPerJob' : 6,
}

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')

samples['Signal_bin4'] = {
    'name': files,
    'weight':mcCommonWeight+'*'+wwjj_bin4,
    'FilesPerJob' : 6,
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
    'FilesPerJob': 47
}

for _, sd in DataRun_2018:
    for pd in DataSets_2018:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv5_Full2018v5/DATAl1loose2018v5__l2loose__fakeW/', pd + '_' + sd)
        samples['Fake_lep']['name'].extend(files)
        samples['Fake_lep']['weights'].extend([DataTrig_2018[pd]] * len(files))
###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun_2018:
    for pd in DataSets_2018:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv5_Full2018v5/DATAl1loose2018v5__l2loose__l2tightOR2018v5/', pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig_2018[pd]] * len(files))
