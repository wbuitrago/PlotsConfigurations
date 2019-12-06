# cuts


##############################################################
##################### SIGNAL REGION ##########################
##############################################################


# Lepton Selection Cut for Signal region
# leptonSel =   '\
#                nLepton >= 2 \
#                && Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) > 0 \
#                && mll > 20 \
#                && Alt$(Lepton_pt[2],0.)<10 \
#                && tauVeto_ww \
#                && zveto_ww \
#                && lep0eta \
#                && lep1eta '

# ## JET selections

# # inclusive region
# inclusive = 'nCleanJet >= 0'

# # njets >= 2 selection
# jetSel   = 'nCleanJet >= 2'

# ## Signal Region

# cuts['ssww_incl']  = { 
#    'expr' : leptonSel + '&&' + inclusive,
#    # Define the sub-categorization of ssww
#    'categories' : {
#          'ee'    : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11', # double electron
#          'emu'   : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13', # muon & electron
#          'mumu'  : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13', # double muon
#    }
# }

# cuts['ssww_jetSel']  = { 
#    'expr' : leptonSel + '&&' + jetSel,
#    # Define the sub-categorization of ssww
#    'categories' : {
#          'ee'    : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11', # double electron
#          'emu'   : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13', # muon & electron
#          'mumu'  : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13', # double muon
#    }
# }



### this is working! ###
# # these are my test cuts for leptons
# # removing jet cuts from ssww_region (see aliases or cut above)
# cuts['ssww_leptons']={
#     'expr': 'nLepton>1 \
#             && Alt$(Lepton_pdgId[0],0) * Alt$(Lepton_pdgId[1],0) > 0 \
#             && Alt$(Lepton_pt[2],0.)<10 \
#             && MET_pt>30 \
#             && mll > 20 \
#             && tauVeto_ww \
#             && zveto_ww \
#             && lep0eta \
#             && lep1eta \
#             \
#             && bVeto \
#             && leppt30 \
#             && softmuon_veto',
# }

## Lepton Selection
lepSel =    'nLepton>1 \
            && Alt$(Lepton_pdgId[0],0) * Alt$(Lepton_pdgId[1],0) > 0 \
            && Alt$(Lepton_pt[2],0.)<10 \
            && MET_pt>30 \
            && mll > 20 \
            && tauVeto_ww \
            && zveto_ww \
            && lep0eta \
            && lep1eta \
            \
            && bVeto \
            && leppt30 \
            && softmuon_veto'

# inclusive region
inclusive = 'nCleanJet >= 0'

## JET Selections
jetSel   = 'nCleanJet >= 2'

#############################
##### Signal Region Cut #####
#############################

# inclusive cut without jet selections
cuts['ssww_incl']  = { 
   'expr' : lepSel + '&&' + inclusive,
   # Define the sub-categorization for
   'categories' : {
         'ee'    : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11', # double electron
         'emu'   : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13', # muon & electron
         'mumu'  : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13', # double muon
   }
}

# with jet selections
cuts['ssww_jetSel']  = { 
   'expr' : lepSel + '&&' + jetSel,
   # Define the sub-categorization (ee, emu, mumu)
   'categories' : {
         'ee'    : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11', # double electron
         'emu'   : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13', # muon & electron
         'mumu'  : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13', # double muon
   }
}


