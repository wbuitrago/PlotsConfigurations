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
                        # 'nCleanJet >= 2',
                        # 'CleanJet_pt[0] > 30', 
                        # 'CleanJet_pt[1] > 30', 
                        # 'fabs(CleanJet_eta[0]) < 5',
                        # 'fabs(CleanJet_eta[1]) < 5',
                  ]

# supercut definition
supercut = and_separator.join(supercut_vector)     

# Z -> ee region

cuts['SS_Z_ee_incl']  = { 
   'expr': 'ss_ee && \
            abs(mll - 91.1876) < 15',
}

cuts['SS_Z_ee']  = { 
   'expr': 'ss_ee && \
            abs(mll - 91.1876) < 15',
   'categories' : {
      '0j' : 'zeroJet',
      '1j' : 'oneJet',
      '2j' : 'twoJetOrMore',
   }           
}

# top ss cr
# emu, 2 jet + btag 
cuts['SS_top']  = { 
   'expr' : 'twoJet && \
            ( CleanJet_eta[0]<2.5 && Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.7527 ) && \
            ( CleanJet_eta[1]<2.5 && Jet_btagDeepB[CleanJet_jetIdx[1]] > 0.7527 )' 
   'categories' : {
      'ee'    : 'ss_ee',
      'emu'   : 'ss_emu',
   }
}

# following: same cuts, OPPOSITE SIGN region

# Z -> ee region

cuts['OS_Z_ee_incl']  = { 
   'expr': 'os_ee && \
            abs(mll - 91.1876) < 15',
}

cuts['OS_Z_ee']  = { 
   'expr': 'os_ee && \
            abs(mll - 91.1876) < 15',
   'categories' : {
      '0j' : 'zeroJet',
      '1j' : 'oneJet',
      '2j' : 'twoJetOrMore',
   }           
}

# top os cr
# emu or ee, 2 jet + btag (tight WP) 

cuts['OS_top']  = { 
   'expr' : 'twoJet && \
            ( CleanJet_eta[0]<2.5 && Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.7527 ) && \
            ( CleanJet_eta[1]<2.5 && Jet_btagDeepB[CleanJet_jetIdx[1]] > 0.7527 )' 
   'categories' : {
      'ee'    : 'os_ee',
      'emu'   : 'os_emu',
   }
}
