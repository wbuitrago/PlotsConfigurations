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

## 2 lepton categorization

# same sign
ssLep   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) > 0'       # SS generic leptons
ss_ee   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11'  # double electron
ss_emu  = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13'  # muon & electron
ss_mumu = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13'  # double muon

# # opposite sign
# osLep   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) < 0'        # SS generic leptons
# os_ee   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -11*11'  # double electron
# os_emu  = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -11*13'  # muon & electron
# os_mumu = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -13*13'  # double muon

#############################################
########## DY control phase space ###########
#############################################

# cuts['DY_cr']  = { 
#    'expr' : osLep,
#    # sub categorization
#    'categories' : {
#          'ee'    : os_ee,
#          'emu'   : os_emu,
#          'mumu'  : os_mumu,
#    }
# }

#############################################
########## top control phase space ##########
#############################################

# top =       '\
#             nCleanJet >= 2 \
#             && detajj > 1.\
#             && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
#             && Lepton_pt[0]>50 \
#             && Lepton_pt[1]>40 \
#             && CleanJet_pt[0] > 40 \
#             && CleanJet_pt[1] > 30 \
#             '

# cuts['topcr'] = {
#    'expr' : top,
#    # sub categorization
#    'categories' : {
#          'ee'    : os_ee,
#          'emu'   : os_emu,
#          'mumu'  : os_mumu,
#    }
# }
  
#############################################
########### VBS_SS signal region ############
#############################################

cuts['SS_signal_region']  = { 
   'expr' : ssLep + ' && zVeto && bVeto',
   # sub categorization
   'categories' : {
         'ee'    : ss_ee,
         'emu'   : ss_emu,
         'mumu'  : ss_mumu,
   }
}

