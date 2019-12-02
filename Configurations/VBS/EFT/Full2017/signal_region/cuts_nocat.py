# cuts

##############################################################
##################### SIGNAL REGION ##########################
##############################################################

# Lepton Selection Cut for Signal region
# for the moment i didn't add tauVeto_ww zveto_ww requests
lepton_sel =   '\
               nLepton > 1 \
               && Lepton_pdgId[0]*Lepton_pdgId[1] > 0 \
               && mll > 20 \
               && Alt$(Lepton_pt[2],0.)<10 \
               && lep0eta \
               && lep1eta \
               '

## JET selections

# njets >= 2 selection
jet2sel = 'nCleanJet > 1'

# trying a different way to get the same result
jet_selection = '  Alt$(CleanJet_pt[0],-1) > 0 \
                && Alt$(CleanJet_pt[1],-1) > 0 \
                '



## Signal Region

cuts['ssww_incl']  = { 
   'expr' : lepton_sel 
}

cuts['ssww_2j']  = { 
   'expr' : lepton_sel + '&&' + jet2sel
}

cuts['ssww_jet_sel']  = { 
   'expr' : lepton_sel + '&&' + jet_selection
}


