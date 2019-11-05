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
mcCommonWeightNoMatch = 'SFweight'
#mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*59.74'
mcCommonWeight = 'SFweight*PromptGenLepMatch2l'
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

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 4
}
#addSampleWeight(samples, 'Vg', 'Zg', '(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')

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
'''
files = nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')
#nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
#nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_ext1')
samples['WZTo2L2Q'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
'''
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
files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-60_EWK_4F')# + \
#nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To60_EWK_4F')
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
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['WpWp_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?
# gen pt lep1 bin
lep1pt_bin0='Alt$(GenDressedLepton_pt[0],-9999.)>30 && Alt$(GenDressedLepton_pt[0],-9999.)<=85'
lep1pt_bin1='Alt$(GenDressedLepton_pt[0],-9999.)>85 && Alt$(GenDressedLepton_pt[0],-9999.)<=130'
lep1pt_bin2='Alt$(GenDressedLepton_pt[0],-9999.)>130'
lep1pt_out='Alt$(GenDressedLepton_pt[0],-9999.)<=30'
samples['WpWp_EWK_lep1pt_bin0'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep1pt_bin0+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_lep1pt_bin1'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep1pt_bin1+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_lep1pt_bin2'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep1pt_bin2+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_lep1pt_out'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep1pt_out+')',
    'FilesPerJob': 4
}

# gen pt lep2 bin
lep2pt_bin0='Alt$(GenDressedLepton_pt[1],-9999.)>30 && Alt$(GenDressedLepton_pt[1],-9999.)<=85'
lep2pt_bin1='Alt$(GenDressedLepton_pt[1],-9999.)>85 && Alt$(GenDressedLepton_pt[1],-9999.)<=130'
lep2pt_bin2='Alt$(GenDressedLepton_pt[1],-9999.)>130'
lep2pt_out='Alt$(GenDressedLepton_pt[1],-9999.)<=30'
samples['WpWp_EWK_lep2pt_bin0'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep2pt_bin0+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_lep2pt_bin1'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep2pt_bin1+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_lep2pt_bin2'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep2pt_bin2+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_lep2pt_out'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+lep2pt_out+')',
    'FilesPerJob': 4
}
# gen pt jet1 bin
jet1pt_bin0='Alt$(GenJet_pt[0],-9999.)>30 && Alt$(GenJet_pt[0],-9999.)<80'
jet1pt_bin1='Alt$(GenJet_pt[0],-9999.)>=80 && Alt$(GenJet_pt[0],-9999.)<150'
jet1pt_bin2='Alt$(GenJet_pt[0],-9999.)>=150'
jet1pt_out='Alt$(GenJet_pt[0],-9999.)<=30'
samples['WpWp_EWK_jet1pt_bin0'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet1pt_bin0+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_jet1pt_bin1'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet1pt_bin1+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_jet1pt_bin2'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet1pt_bin2+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_jet1pt_out'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet1pt_out+')',
    'FilesPerJob': 4
}
# gen pt jet2 bin
jet2pt_bin0='Alt$(GenJet_pt[1],-9999.)>30 && Alt$(GenJet_pt[1],-9999.)<80'
jet2pt_bin1='Alt$(GenJet_pt[1],-9999.)>=80 && Alt$(GenJet_pt[1],-9999.)<150'
jet2pt_bin2='Alt$(GenJet_pt[1],-9999.)>=150'
jet2pt_out='Alt$(GenJet_pt[1],-9999.)<=30'
samples['WpWp_EWK_jet2pt_bin0'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet2pt_bin0+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_jet2pt_bin1'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet2pt_bin1+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_jet2pt_bin2'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet2pt_bin2+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_jet2pt_out'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+jet2pt_out+')',
    'FilesPerJob': 4
}
# gen mll bin
mll_bin0='gendressedmll>20 && gendressedmll<=100'
mll_bin1='gendressedmll>100 && gendressedmll<=200'
mll_bin2='gendressedmll>200 && gendressedmll<=300'
mll_bin3='gendressedmll>300'
mll_out='gendressedmll<=20'

samples['WpWp_EWK_mll_bin0'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mll_bin0+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mll_bin1'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mll_bin1+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mll_bin2'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mll_bin2+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mll_bin3'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mll_bin3+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mll_out'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mll_out+')',
    'FilesPerJob': 4
}
# gen mjj bin
#500,800,1100,1500,2000
mjj_bin0='genmjj>500 && genmjj<=800'
mjj_bin1='genmjj>800 && genmjj<=1100'
mjj_bin2='genmjj>1100 && genmjj<=1500'
mjj_bin3='genmjj>1500'
mjj_out='genmjj<=500'
samples['WpWp_EWK_mjj_bin0'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mjj_bin0+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mjj_bin1'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mjj_bin1+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mjj_bin2'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mjj_bin2+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mjj_bin3'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mjj_bin3+')',
    'FilesPerJob': 4
}
samples['WpWp_EWK_mjj_out'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+mjj_out+')',
    'FilesPerJob': 4
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
    'FilesPerJob': 17
}

for _, sd in DataRun_2018:
    for pd in DataSets_2018:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv5_Full2018v5/DATAl1loose2018v5__l2loose__l2tightOR2018v5/', pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig_2018[pd]] * len(files))
