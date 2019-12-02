# cuts


##############################################################
##################### SIGNAL REGION ##########################
##############################################################


# Lepton Selection Cut for Signal region
# for the moment i didn't add tauVeto_ww zveto_ww requests
leptonSel =   '\
               nLepton >= 2 \
               && Lepton_pdgId[0]*Lepton_pdgId[1] > 0 \
               && mll > 20 \
               && Alt$(Lepton_pt[2],0.)<10 \
               && lep0eta \
               && lep1eta \
               '

## JET selections

# inclusive region
inclusive = 'nCleanJet >= 0'

# njets >= 2 selection
jetSel   = 'nCleanJet >= 2'



## Signal Region

cuts['ssww_incl']  = { 
   'expr' : leptonSel + '&&' + inclusive
}

cuts['ssww_jetSel']  = { 
   'expr' : leptonSel + '&&' + jetSel
}



# # trying a different way to get the same result
# jet_selection = '  Alt$(CleanJet_pt[0],-1) > 0 \
#                 && Alt$(CleanJet_pt[1],-1) > 0 \
#                 '


# cannot use categories.. they are mutually exclusives
# ## Signal Region
# cuts['ssww']  = { 
#    'expr' : lepton_sel,
#     # Define the sub-categorization of ssww
#    'categories' : {
#          'incl'    : inclusive,
#          '2j'      : jet2sel,
#          'jetSel'  : jet_selection,
#          }
# }

