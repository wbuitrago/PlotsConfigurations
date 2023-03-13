import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # WWSS
configurations = os.path.dirname(configurations) # 2018
configurations = os.path.dirname(configurations) # VBS
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseWnAOD, addSampleWeight

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

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
MCDir = os.path.join(treeBaseDir,  mcProduction , mcSteps)



# MCDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'


################################################
################### WEIGHTS ####################
################################################

# ---------------------------------------- Basic MC weights
mcCommonWeightNoMatch = 'XSWeight*SFweight_mod*samesign_requirement'
mcCommonWeight = 'XSWeight*SFweight_mod*PromptGenLepMatch2l*samesign_requirement'

# ---------------------------------------- Number of leptons
Nlep='2'
#Nlep='3'
#Nlep='4'

# ---------------------------------------- Lepton WP
eleWP = 'mvaFall17V1Iso_WP90_SS_tthmva_70'
# eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP  = 'cut_Tight_HWWW_tthmva_80'
#muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

# ---------------------------------------- MET filters
METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

# ---------------------------------------- fake weights
#fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
#fakeW = 'fakeW_ele_mvaFall17V1Iso_WP90_SS_tthmva_70_mu_cut_Tight_HWWW_2l2j'
fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2j'
# ---------------------------------------- Basic MC weights
XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'

################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}


################################################
################ MC SAMPLES ####################
################################################


# ---------------------------------------- Wrong-sign
files = nanoGetSampleFiles(MCDir, 'WWTo2L2Nu') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToENEN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToENMN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToENTN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToMNEN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToMNMN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToMNTN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToTNEN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToTNMN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToTNTN')
samples['WW'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

# ---------------------------------------- Top
samples['Top'] = {
    'name': nanoGetSampleFiles(MCDir, 'TTTo2L2Nu') + \
            nanoGetSampleFiles(MCDir, 'ST_tW_top_ext1') + \
            nanoGetSampleFiles(MCDir, 'ST_tW_antitop_ext1'),
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 3,
}

# ---------------------------------------- DY
ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
samples['DY'] = {
    'name': nanoGetSampleFiles(MCDir, 'DYJetsToLL_M-50_ext2') + \
            nanoGetSampleFiles(MCDir, 'DYJetsToLL_M-10to50-LO_ext1'),
    'weight':  'mcCommonWeight_os*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 3,
}

# ---------------------------------------- Higgs
samples['Higgs'] = {
    'name': nanoGetSampleFiles(MCDir, 'GluGluHToWWTo2L2Nu_M125') + \
            nanoGetSampleFiles(MCDir, 'GluGluHToTauTau_M125') + \
            nanoGetSampleFiles(MCDir, 'VBFHToWWTo2L2Nu_M125') + \
            nanoGetSampleFiles(MCDir, 'VBFHToTauTau_M125') + \
            nanoGetSampleFiles(MCDir, 'ttHToNonbb_M125'),
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

