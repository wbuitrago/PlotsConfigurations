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

def makeMCDirectory(var=''):
    if var:
        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
        return '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6__{var}'.format(var=var)
    else:
        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR'

# samples
try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6/'
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
DataRun = [
    ['B','Run2016B-Nano1June2019_ver2-v1'] ,
    ['C','Run2016C-Nano1June2019-v1'] ,
    ['D','Run2016D-Nano1June2019-v1'] ,
    ['E','Run2016E-Nano1June2019-v1'] ,
    ['F','Run2016F-Nano1June2019-v1'] ,
    ['G','Run2016G-Nano1June2019-v1'] ,
    ['H','Run2016H-Nano1June2019-v1'] ,
]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
}
###########################################
############  Reducible Bkg  ##############
###########################################

######## Vgamma ########
files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(!(Gen_ZGstar_mass > 0))',
    'FilesPerJob': 4
}
addSampleWeight(samples, 'Vg', 'Zg', '(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')

######## VgS ########
files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
        nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['VgS1'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS1', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS1', 'Zg', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['VgS2'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS2', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS2', 'Zg', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
######### VV #########
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_EWK') + \
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
files = nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-4To50_QCD_3Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_0Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_1Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_2Jet') + \
        nanoGetSampleFiles(mcDirectory, 'WLLJJToLNu_M-50_QCD_3Jet')

samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight+'*1.2',
    'FilesPerJob': 7
}

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_ext1')
samples['WZ_QCD_powheg'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 7
}
files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_AMCNLO')
samples['WZ_QCD_AMCNLO'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 7
}

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
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

files = nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToQQ') + \
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

samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
###########################################
#############   SIGNALS  ##################
###########################################
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK')
out_fid='!(fiducial)'

samples['WpWp_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
samples['WpWp_EWK_fid'] = {
    'name': files,
    'weight': mcCommonWeight+'*(fiducial)',
    'FilesPerJob': 4
}

samples['WpWp_EWK_out'] = {
    'name': files,
    'weight': mcCommonWeight+'*('+out_fid+')',
    'FilesPerJob': 4
}
lep1pt_bin0='fiducial && genlep1pt>30 && genlep1pt<=70'
lep1pt_bin1='fiducial && genlep1pt>70 && genlep1pt<=120'
lep1pt_bin2='fiducial && genlep1pt>120'

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

# gen pt lep2 bin
lep2pt_bin0='fiducial && genlep2pt>30 && genlep2pt<=45'
lep2pt_bin1='fiducial && genlep2pt>45 && genlep2pt<=70'
lep2pt_bin2='fiducial && genlep2pt>70'
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

# gen pt jet1 bin
jet1pt_bin0='fiducial && genjet1pt>30 && genjet1pt<=145'
jet1pt_bin1='fiducial && genjet1pt>145 && genjet1pt<=245'
jet1pt_bin2='fiducial && genjet1pt>245'
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

# gen pt jet2 bin
jet2pt_bin0='fiducial && genjet2pt>30 && genjet2pt<=70'
jet2pt_bin1='fiducial && genjet2pt>70 && genjet2pt<=120'
jet2pt_bin2='fiducial && genjet2pt>120'
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

# gen mll bin
mll_bin0='fiducial && genmll>20 && genmll<=120'
mll_bin1='fiducial && genmll>120 && genmll<=220'
mll_bin2='fiducial && genmll>220'

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

# gen mjj bin
#500,800,1100,1500,2000
mjj_bin0='fiducial && genmjj>500 && genmjj<=1000'
mjj_bin1='fiducial && genmjj>1000 && genmjj<=1800'
mjj_bin2='fiducial && genmjj>1800'
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

for _, sd in DataRun:
    for pd in DataSets:
        if not (pd=='MuonEG' and _=='E'):
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__fakeW/', pd + '_' + sd)
        else:
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__fakeW/', pd + '_Run2016E-Nano1June2019-v3')
        samples['Fake_lep']['name'].extend(files)
        samples['Fake_lep']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        if not (pd=='MuonEG' and _=='E'):
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__l2tightOR2016v6/', pd + '_' + sd)
        else:
            files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__l2tightOR2016v6/', pd + '_Run2016E-Nano1June2019-v3')
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
