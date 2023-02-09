import os

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
MCDir = os.path.join(treeBaseDir,  mcProduction , mcSteps)
print (MCDir)

# samples = ['WpWpJJ_EWK']
samples = ['WpWpJJ_EWK',
           'WLLJJ_WToLNu_EWK',
           # WW QCD
           'WpWpJJ_QCD',
           # WZ_QCD
           'WZTo3LNu',
           # ZZ
           'ZZTo2L2Nu_ext1',
           'ZZTo2L2Nu_ext2',
           'ZZTo2L2Q',
           'ZZTo4L_ext1',
           'ZZTo4L_ext2',
           'ggZZ4m',
           'ggZZ4m_ext1',
           'ggZZ4t',
           'ggZZ2e2t',
           'ggZZ2m2t',
           'ggZZ2e2m',
           # TTV
           'TTZToLLNuNu_M-10',
           'TTWJetsToLNu',
           # tZq
           'tZq_ll',
           # Vg
           'ZGToLLG',
           'WGJJ',
           # VgS1
           'ZGToLLG',
           'WGJJ',
           'WZTo3LNu_mllmin01',
           # WW
           'WWTo2L2Nu',
           'GluGluToWWToENEN',
           'GluGluToWWToENMN',
           'GluGluToWWToENTN',
           'GluGluToWWToMNEN',
           'GluGluToWWToMNMN',
           'GluGluToWWToMNTN',
           'GluGluToWWToTNEN',
           'GluGluToWWToTNMN',
           'GluGluToWWToTNTN',
           # Top
           'TTTo2L2Nu',
           'ST_tW_top_ext1',
           'ST_tW_antitop_ext1',
           # DY
           'DYJetsToLL_M-50_ext2',
           'DYJetsToLL_M-10to50-LO_ext1',
           # Higgs
           'GluGluHToWWTo2L2Nu_M125',
           'GluGluHToTauTau_M125',
           'VBFHToWWTo2L2Nu_M125',
           'VBFHToTauTau_M125',
           'ttHToNonbb_M125',
           # DPS
           'WWTo2L2Nu_DoubleScattering',
           # VVV
           'ZZZ',
           'WZZ',
           'WWZ',
           'WWW',
           'WWG'
]

import glob


def findmissingfiles(nuisance, samples, MCDir):
    print ("####  "+nuisance+"  ####")
    errors = []
    nominalsmiss = []
    upmiss = []
    domiss = []
    for sam in samples:
        a = glob.glob(MCDir+'/nanoLatino_'+sam+'__part*.root')
        if a == []:
            print("lista vuota")
            errors.append(sam)
        else:
            # print ("len = ", len(a))
            # print ("\nMissing nominals:")
            for part in range(len(a)):
                #print ("part = ", part)
                if os.path.exists(MCDir+'/nanoLatino_'+sam+'__part'+str(part)+'.root') == False:
                    print('NOMINAL --> /nanoLatino_'+sam+'__part'+str(part)+'.root')
                    #nominalsmiss.append('missing part '+str(part)+' in '+sam)
            #print ("\nMissing nuisances:")
            for part in range(len(a)):
                if os.path.exists(MCDir+'__'+nuisance+'up_suffix/nanoLatino_'+sam+'__part'+str(part)+'.root') == False:
                            #upmiss.append('missing part '+str(part)+' in '+sam)
                    print('up_suffix/nanoLatino_'+sam+'__part'+str(part)+'.root')
                if os.path.exists(MCDir+'__'+nuisance+'do_suffix/nanoLatino_'+sam+'__part'+str(part)+'.root') == False:
                            #domiss.append('missing part '+str(part)+' in '+sam)
                    print('do_suffix/nanoLatino_'+sam+'__part'+str(part)+'.root')

### missing JER ?
findmissingfiles("JER", samples, MCDir)

### missing JES ?
jes_systs = ['JESAbsolute','JESBBEC1','JESEC2','JESFlavorQCD','JESHF','JESRelative', 'JESFlavorQCD']
for j in jes_systs:
    findmissingfiles(j, samples, MCDir)


