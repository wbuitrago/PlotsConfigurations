# cuts


##############################################################
##################### SIGNAL REGION ##########################
##############################################################


# Lepton Selection Cut for Signal region
# for the moment i didn't add tauVeto_ww zveto_ww requests
lepton_sel =   '\
               nLepton >= 2 \
               && Lepton_pdgId[0]*Lepton_pdgId[1] > 0 \
               && mll > 20 \
               && Alt$(Lepton_pt[2],0.)<10 \
               && lep0eta \
               && lep1eta \
               '

# jet inclusive region
jet_inclusive = ' nCleanJet >= 0 '

# jet selections
jet_selection = ' nCleanJet >= 2 '

## Signal Region
cuts['ssww']  = { 
   'expr' : lepton_sel,
    # Define the sub-categorization of topcr
   'categories' : {
      'incl' : jet_inclusive,
      '2j'   : jet_selection,
   }
}