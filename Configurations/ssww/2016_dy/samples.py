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

mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5/'
private_mcDirectory='/eos/user/j/jixiao/HWWnano3/Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5/'
#mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_nAOD_v1_Full2017v2LP19/MCl1loose2017__MCCorr2017LP19__l2loose__l2tightOR2017/'
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
mcCommonWeight = 'SFweight*PromptGenLepMatch2l'
#mcCommonWeight = 'XSWeight*SFweight*41.53'
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
'''
DataRun_2017 = [
    ['B','Run2017B-Nano14Dec2018-v1'] ,
    ['C','Run2017C-Nano14Dec2018-v1'] ,
    ['D','Run2017D-Nano14Dec2018-v1'] ,
    ['E','Run2017E-Nano14Dec2018-v1'] ,
    ['F','Run2017F-Nano14Dec2018-v1'] ,
]
'''
DataRun_2017 = [
    ['B','Run2017B-31Mar2018-v1'] ,
    #['B','Run2017B-Nano14Dec2018-v1'] ,
    #['C','Run2017C-Nano14Dec2018-v1'] ,
    #['D','Run2017D-Nano14Dec2018-v1'] ,
    #['E','Run2017E-Nano14Dec2018-v1'] ,
    #['F','Run2017F-Nano14Dec2018-v1'] ,
]

#DataSets_2017 = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']
DataSets_2017 = ['MuonEG']

DataTrig_2017 = {
    'MuonEG'         : '1',#Trigger_ElMu' ,
    #'DoubleMuon'     : '!Trigger_ElMu &&  Trigger_dblMu' ,
    #'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu &&  Trigger_sngMu' ,
    #'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu &&  Trigger_dblEl' ,
    #'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl &&  Trigger_sngEl' ,
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

ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'

files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2')
samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',ptllDYW_NLO)


files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

samples['DYtt'] = {
    'name': files,
    'weight': mcCommonWeight + '*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt > 20.) == 0)',
    'FilesPerJob': 4,
}
addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    #'weight': mcCommonWeight + '*nllW', # temporary - nllW module not run on PS and UE variation samples
    'weight': mcCommonWeight + '*nllWOTF', # temporary
    'FilesPerJob': 1
}

samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*(lhe_mW1[0] > 60. && lhe_mW1[0] < 100. && lhe_mW2[0] > 60. && lhe_mW2[0] < 100.)', #filter tops and Higgs, limit w mass
    'FilesPerJob': 4
}

samples['ggWW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluWWTo2L2Nu_MCFM'),
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}

'''
samples['DY']=	{  	'name'	:getSampleFiles(chargeFlipDir,'DYJetsToLL_M-10to50',False,'nanoLatino_')
                                       +getSampleFiles(chargeFlipDir,'DYJetsToLL_M-10to50_ext1',False,'nanoLatino_')
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
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM')
samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight,# + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['VG'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch,# + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 4
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
######### VV #########
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q_AMCNLOFXFX') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L_AMCNLOFXFX')
samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['WZTo2L2Q'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 7
}
files = nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
        nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-4To50_QCD_1Jet') + \
        nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
        nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet') + \
        nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
        nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
        nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-50_QCD_2Jet') + \
        nanoGetSampleFiles(private_mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet')

samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.2',
    'FilesPerJob': 7
}
files = nanoGetSampleFiles(private_mcDirectory, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 7
}
#addSampleWeight(samples,'WZ_EWK','WLLJJ_WToLNu_EWK', '(Gen_ZGstar_mass>=0.1)')
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

files = nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToQQ') + \
        nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10_ext3') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll_4f')
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
files = nanoGetSampleFiles(private_mcDirectory, 'll')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?
samples['LL'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(private_mcDirectory, 'tl') + \
        nanoGetSampleFiles(private_mcDirectory, 'tt')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['TL_TT'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
'''
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['WW_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
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
    'FilesPerJob': 47
}

for _, sd in DataRun_2016:
    for pd in DataSets_2016:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv4_Full2016v5/DATAl1loose2016v5__l2loose__fakeW/', pd + '_' + sd)
        samples['Fake_lep']['name'].extend(files)
        samples['Fake_lep']['weights'].extend([DataTrig_2016[pd]] * len(files))
###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun_2016:
    for pd in DataSets_2016:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv4_Full2016v5/DATAl1loose2016v5__l2loose__l2tightOR2016v5/', pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig_2016[pd]] * len(files))
