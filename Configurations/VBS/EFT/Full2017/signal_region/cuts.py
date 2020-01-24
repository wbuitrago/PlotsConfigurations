# cuts

#############################################
################# SUPERCUT ##################
#############################################

and_separator = ' && '

# 2 jets and 2 leptons with p_t > 30 GeV and eta comprised in detector acceptance

supercut_vector = [     'nLepton>1',
                        'Lepton_pt[0] > 30',
                        'Lepton_pt[1] > 30',    
                        '((fabs(Lepton_eta[0]) < 2.5 && abs(Lepton_pdgId[0])==11) || (fabs(Lepton_eta[0]) < 2.4 && abs(Lepton_pdgId[0])==13))',
                        '((fabs(Lepton_eta[1]) < 2.5 && abs(Lepton_pdgId[1])==11) || (fabs(Lepton_eta[1]) < 2.4 && abs(Lepton_pdgId[1])==13))',                        'Alt$(CleanJet_pt[0],-9999.) > 30', 
                        'nCleanJet > 1',
                        'CleanJet_pt[0] > 30', 
                        'CleanJet_pt[1] > 30', 
                        'fabs(CleanJet_eta[0]) < 5',
                        'fabs(CleanJet_eta[1]) < 5',
                        'mll > 10',
                  ]

# supercut definition
supercut = and_separator.join(supercut_vector)     

#############################################
########### VBS_SS signal region ############
#############################################

cuts['SS_sr']  = { 
   'expr' : 'ssLep && zVeto ',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# same with bVeto

cuts['SS_sr_bveto']  = { 
   'expr' : 'ssLep && zVeto && bVeto',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}