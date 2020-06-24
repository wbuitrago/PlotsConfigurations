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

#mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'
mcDirectory = '/eos/user/j/jixiao/HWWnano3/link/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'
mcDir_private='/eos/user/j/jixiao/HWWnano3/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'

treeBaseDir = '/eos/user/j/jixiao/HWWnano3/link'#/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction = 'Autumn18_102X_nAODv6_Full2018v6'
mcSteps = 'MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6{var}'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

################################################
############ BASIC MC WEIGHTS ##################
################################################
eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP = 'cut_Tight_HWWW'
SFWeight='SFweight2l*LepSF2l__ele_'+ eleWP + '__mu_' + muWP+'*LepCut2l__ele_'+eleWP+'__mu_'+muWP+'*XSWeight*METFilter_MC*btagSF*59.74'
mcCommonWeightNoMatch = SFWeight+'*(Lepton_pdgId[0] * Lepton_pdgId[1] > 0)'
mcCommonWeight = SFWeight+'*(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1])*(Lepton_pdgId[0] * Lepton_pdgId[1] > 0)'
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['A','Run2018A-Nano25Oct2019-v1'] ,
    ['B','Run2018B-Nano25Oct2019-v1'] ,
    ['C','Run2018C-Nano25Oct2019-v1'] ,
    ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,
]
DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}
###########################################
############  Reducible Bkg  ##############
############################################
### Signal
#files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK_madgraph')
#samples['SSWW'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
files = nanoGetSampleFiles(mcDirectory, 'llWWrf')
samples['LL'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(mcDirectory, 'tlWWrf')
samples['TL'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
files = nanoGetSampleFiles(mcDirectory, 'ttWWrf')
samples['TT'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
#### eft
#files = nanoGetSampleFiles(mcDirectory, 'cHbox_int')
#samples['cHbox_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cHDD_int')
#samples['cHDD_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
##files = nanoGetSampleFiles(mcDirectory, 'cHe_int')
##samples['cHe_int'] = {
##    'name': files,
##    'weight': mcCommonWeight,
##    'FilesPerJob': 1
##}
##
#files = nanoGetSampleFiles(mcDirectory, 'cHl1_int')
#samples['cHl1_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
##files = nanoGetSampleFiles(mcDirectory, 'cHl3_int')
##samples['cHl3_int'] = {
##    'name': files,
##    'weight': mcCommonWeight,
##    'FilesPerJob': 1
##}
##
##files = nanoGetSampleFiles(mcDirectory, 'cHq1_int')
##samples['cHq1_int'] = {
##    'name': files,
##    'weight': mcCommonWeight,
##    'FilesPerJob': 1
##}
##
#files = nanoGetSampleFiles(mcDirectory, 'cHq3_int')
#samples['cHq3_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cHWB_int')
#samples['cHWB_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cHW_int')
#samples['cHW_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cll1_int')
#samples['cll1_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq11_int')
#samples['cqq11_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq1_int')
#samples['cqq1_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq31_int')
#samples['cqq31_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq3_int')
#samples['cqq3_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cW_int')
#samples['cW_int'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cHbox_bsm')
#samples['cHbox_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cHDD_bsm')
#samples['cHDD_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
##files = nanoGetSampleFiles(mcDirectory, 'cHe_bsm')
##samples['cHe_bsm'] = {
##    'name': files,
##    'weight': mcCommonWeight,
##    'FilesPerJob': 1
##}
##
##files = nanoGetSampleFiles(mcDirectory, 'cHl1_bsm')
##samples['cHl1_bsm'] = {
##    'name': files,
##    'weight': mcCommonWeight,
##    'FilesPerJob': 1
##}
##
##files = nanoGetSampleFiles(mcDirectory, 'cHl3_bsm')
##samples['cHl3_bsm'] = {
##    'name': files,
##    'weight': mcCommonWeight,
##    'FilesPerJob': 1
##}
##
##files = nanoGetSampleFiles(mcDirectory, 'cHq1_bsm')
##samples['cHq1_bsm'] = {
##    'name': files,
##    'weight': mcCommonWeight,
##    'FilesPerJob': 1
##}
##
#files = nanoGetSampleFiles(mcDirectory, 'cHq3_bsm')
#samples['cHq3_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cHWB_bsm')
#samples['cHWB_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cHW_bsm')
#samples['cHW_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cll1_bsm')
#samples['cll1_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq11_bsm')
#samples['cqq11_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq1_bsm')
#samples['cqq1_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq31_bsm')
#samples['cqq31_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cqq3_bsm')
#samples['cqq3_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'cW_bsm')
#samples['cW_bsm'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 1
#}

files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### Interference
# need:
# WpWpJJ_Interference_TuneCUETP8M1_13TeV-madgraph-pythia8
# WLLJJ_WToLNu_Interference_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8
#files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_Interference')
#samples['WpWpJJ_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_Interference')
#samples['WLLJJ_WToLNu_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

### WW QCD
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### WZ QCD
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

#files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_powheg')
#samples['WZ_QCD_powheg'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_ext1')
#samples['WZ_QCD_AMCNLO'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
#samples['WZ_QCD_mllmin01'] = {
#    'name': files,
#    'weight': mcCommonWeight+'*(Gen_ZGstar_mass > 4)',
#    'FilesPerJob': 4
#}
#
### ZZ
# need:
# ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8
# ZZJJTo4L_QCD_TuneCP5_13TeV-madgraph-pythia8
# GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8
#files = nanoGetSampleFiles(mcDirectory, 'ZZJJTo4L_EWK') + \
#        nanoGetSampleFiles(mcDirectory, 'ZZJJTo4L_QCD')
files = nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')
samples['ZZ4L'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ggZZ2m2t_CP5') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2t') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2m') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4t_CP5') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4m_ext1')
        #nanoGetSampleFiles(mcDirectory, 'ggZZ4e')
samples['ggZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
#addSampleWeight(samples, 'ggZZ', 'ggZZ4e', '0.001')

### TVX
# need:
# TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8
# TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8
# TTWJetsToQQ_TuneTuneCP5_13TeV-amcatnloFXFX-madspin-pythia8

files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
        nanoGetSampleFiles(mcDirectory, 'tZq_ll')
samples['TVX'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

### Vg
# need: 
# LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# old: WGJJ Zg
files = nanoGetSampleFiles(mcDirectory, 'Zg') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

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
addSampleWeight(samples, 'VgS1', 'Zg', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

### Wrong-sign
#files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')
#samples['WW'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os',
#    'FilesPerJob': 17,
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
#        nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1') + \
#        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1')
#samples['Top'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os',
#    'FilesPerJob': 17,
#}
#
## MIT: 
## DY0JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY1JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY2JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY3JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY0JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY1JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY2JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY3JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
#ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
#ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
#files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')
#samples['DY'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os*( !(Sum(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && AbsVec(PhotonGen_eta)<2.6) > 0 &&\
#        Sum(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
#    'FilesPerJob': 17,
#}
## need:
## GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV714_pythia8
## # not found: VBFHToZZTo4L_M125_13TeV_powheg2_JHUGenV714_pythia8
## VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8
#files = nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125')
#samples['Higgs'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os',
#    'FilesPerJob': 17,
#}
### Others
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')
samples['DPS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW') + \
        nanoGetSampleFiles(mcDirectory, 'WWG') 
samples['VVV'] = {
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
    'weight': 'METFilter_DATA*fakeW*(Lepton_pdgId[0]*Lepton_pdgId[1]>0)',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}
for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__fakeW/', pd + '_' + sd)
        samples['Fake_lep']['name'].extend(files)
        samples['Fake_lep']['weights'].extend([DataTrig[pd]] * len(files))
###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut*(Lepton_pdgId[0]*Lepton_pdgId[1]>0)',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6/', pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
