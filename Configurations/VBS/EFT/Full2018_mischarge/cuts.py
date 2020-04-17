# cuts

#############################################
################# SUPERCUT ##################
#############################################

and_separator = ' && '

# 2 jets and 2 leptons with p_t > thresholds for triggers and eta comprised in detector acceptance

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

# lookout! I removed zveto from inclusive region!

cuts['SS_incl']  = { 
   'expr' : '1', # dummy cut.. true selection in categories
   # sub categorization
   'categories' : {
         'ee'    : 'ee',
         #'emu'   : 'emu',
         #'mumu'  : 'mumu',
   }
}

# corresponding to the eta interval of the mischarge measurements
cuts['SS_incl_ee']  = { 
   'expr' : '1', # dummy cut.. true selection in categories
   # sub categorization
   'categories' : {
         'eta_00_10' : 'fabs(Lepton_eta[0]<1.0) && fabs(Lepton_eta[1]<1.0)',
         'eta_10_15' : 'fabs(Lepton_eta[0]>1.0) && fabs(Lepton_eta[1]>1.0) && fabs(Lepton_eta[0]<1.5) && fabs(Lepton_eta[1]<1.5) ',
         'eta_15_25' : 'fabs(Lepton_eta[0]>1.5) && fabs(Lepton_eta[1]>1.5) && fabs(Lepton_eta[0]<2.5) && fabs(Lepton_eta[1]<2.5) ',
   }
}

# cuts['SS_incl_all']  = { 
#    'expr' : '1',
# }

# #############################################
# ########### VBS_SS signal region ############
# #############################################

cuts['SS_sr']  = { 
   'expr': 'Lepton_pt[0] > 30 &&\
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
         'ee'    : 'ee',
      #    'emu'   : 'emu',
      #    'mumu'  : 'mumu',
   }
}

# # signal region w/o categories

# cuts['SS_sr_all']  = { 
#    'expr': 'Lepton_pt[0] > 30 &&\
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

# #############################################
# ########### low_mjj control region ##########
# #############################################

# cuts['SS_lowmjj_all']  = { 
#    'expr': 'Lepton_pt[0] > 30 &&\
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

# cuts['SS_lowmjj']  = { 
#    'expr': 'Lepton_pt[0] > 30 &&\
#             Lepton_pt[1] > 30 &&\
#             3rd_lep_veto && \
#             zVeto && \
#             bVeto && \
#             (150 < mjj && mjj < 500) &&\
#             mll > 20 &&\
#             MET_pt>30 &&\
#             softmuon_veto &&\
#             tauVeto_ww',
#    # sub categorization
#    'categories' : {
#          'ee'    : 'ee',
#          'emu'   : 'emu',
#          'mumu'  : 'mumu',
#    }
# }
