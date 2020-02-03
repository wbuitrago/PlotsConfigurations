# cuts

#############################################
################# SUPERCUT ##################
#############################################

and_separator = ' && '

# 2 jets and 2 leptons with p_t > 30 GeV and eta comprised in detector acceptance

supercut_vector = [     'nLepton > 1',
                        'Lepton_pt[0] > 18',
                        'Lepton_pt[1] > 8',    
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

# inclusive region

cuts['SS_incl']  = { 
   'expr' : 'ssLep && zVeto ',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}

# signal region

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

cuts['SS_sr_all']  = { 
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
}


# low mjj control region

cuts['SS_lowmjj_all']  = { 
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
            tauVeto_ww &&',
}

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
            tauVeto_ww &&',
   # sub categorization
   'categories' : {
         'ee'    : 'ss_ee',
         'emu'   : 'ss_emu',
         'mumu'  : 'ss_mumu',
   }
}