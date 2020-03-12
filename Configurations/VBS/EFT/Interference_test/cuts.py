# cuts

#############################################
################# SUPERCUT ##################
#############################################

and_separator = ' && '

# 2 jets and 2 leptons with p_t > 30 GeV and eta comprised in detector acceptance

supercut_vector = [     'nLepton >= 2',
                        '3rd_lep_veto',
                        'mll > 12',
                        'Lepton_pt[0] > 20',
                        'Lepton_pt[1] > 10',   
                        '(abs(Lepton_pdgId[0])==13 || Lepton_pt[0]>25)', 
                        '(abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13)',
                        '((fabs(Lepton_eta[0]) < 2.5 && abs(Lepton_pdgId[0])==11) || (fabs(Lepton_eta[0]) < 2.4 && abs(Lepton_pdgId[0])==13))',
                        '((fabs(Lepton_eta[1]) < 2.5 && abs(Lepton_pdgId[1])==11) || (fabs(Lepton_eta[1]) < 2.4 && abs(Lepton_pdgId[1])==13))',                        
                        'nCleanJet >= 2',
                        'CleanJet_pt[0] > 30', 
                        'CleanJet_pt[1] > 30', 
                        'fabs(CleanJet_eta[0]) < 5',
                        'fabs(CleanJet_eta[1]) < 5',
                  ]

# supercut definition
supercut = and_separator.join(supercut_vector)     

#############################################
########### SS inclusive region ############
#############################################

cuts['SS_incl']  = { 
   'expr' : 'ssLep && zVeto ',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# cuts['SS_incl_all']  = { 
#    'expr' : 'ssLep && zVeto ',
# }

#############################################
########### VBS_SS signal region ############
#############################################

cuts['SS_sr']  = { 
   'expr': 'ssLep && \
            Lepton_pt[0] > 30 &&\
            Lepton_pt[1] > 30 &&\
            3rd_lep_veto && \
            zVeto && \
            bVeto && \
            detajj > 2.5 &&\
            mjj > 500 &&\
            mll > 20 &&\
            MET_pt>30 &&\
            softmuon_veto &&\
            tauVeto_ww &&\
            z_lep_sel',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# signal region w/o categories

# cuts['SS_sr_all']  = { 
#    'expr': 'ssLep && \
#             Lepton_pt[0] > 30 &&\
#             Lepton_pt[1] > 30 &&\
#             3rd_lep_veto && \
#             zVeto && \
#             bVeto && \
#             detajj > 2.5 &&\
#             mjj > 500 &&\
#             mll > 20 &&\
#             MET_pt>30 &&\
#             softmuon_veto &&\
#             tauVeto_ww &&\
#             z_lep_sel',
# }

#############################################
########### low_mjj control region ##########
#############################################

# cuts['SS_lowmjj_all']  = { 
#    'expr': 'ssLep && \
#             Lepton_pt[0] > 30 &&\
#             Lepton_pt[1] > 30 &&\
#             3rd_lep_veto && \
#             zVeto && \
#             bVeto && \
#             (150 < mjj && mjj < 500) &&\
#             mll > 20 &&\
#             MET_pt>30 &&\
#             softmuon_veto &&\
#             tauVeto_ww',
# }

cuts['SS_lowmjj']  = { 
   'expr': 'ssLep && \
            Lepton_pt[0] > 30 &&\
            Lepton_pt[1] > 30 &&\
            3rd_lep_veto && \
            zVeto && \
            bVeto && \
            (150 < mjj && mjj < 500) &&\
            mll > 20 &&\
            MET_pt>30 &&\
            softmuon_veto &&\
            tauVeto_ww',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}


######################################################
############### new signal cuts for testing ##########
######################################################

# mjj 100
cuts['SS_sr_m100d10']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>100 && detajj>1.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m100d15']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>100 && detajj>1.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m100d20']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>100 && detajj>2.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m100d25']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>100 && detajj>2.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# mjj 200
cuts['SS_sr_m200d10']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>200 && detajj>1.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m200d15']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>200 && detajj>1.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m200d20']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>200 && detajj>2.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m200d25']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>200 && detajj>2.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# mjj 300
cuts['SS_sr_m300d10']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>300 && detajj>1.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m300d15']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>300 && detajj>1.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m300d20']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>300 && detajj>2.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m300d25']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>300 && detajj>2.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# mjj 400
cuts['SS_sr_m400d10']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>400 && detajj>1.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m400d15']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>400 && detajj>1.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m400d20']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>400 && detajj>2.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m400d25']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>400 && detajj>2.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# mjj 500
cuts['SS_sr_m500d10']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>500 && detajj>1.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m500d15']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>500 && detajj>1.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m500d20']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>500 && detajj>2.0',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

cuts['SS_sr_m500d25']  = { 
   'expr': 'VBS_SS_cuts_pt30 && mjj>500 && detajj>2.5',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}