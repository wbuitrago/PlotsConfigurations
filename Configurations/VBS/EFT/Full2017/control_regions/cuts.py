# cuts

# TEMPLATE CUT (leave commented)

'''
cuts['ssww_incl']  = { 
   'expr' : lepSel + '&&' + inclusive,
   # Define the sub-categorization for
   'categories' : {
         'ee'    : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11', # double electron
         'emu'   : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13', # muon & electron
         'mumu'  : 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13', # double muon
   }
}
'''

## 2 lepton categorization

# same sign
ssLep   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) > 0'       # SS generic leptons
ss_ee   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11'  # double electron
ss_emu  = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13'  # muon & electron
ss_mumu = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13'  # double muon

# opposite sign
osLep   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) < 0'       # SS generic leptons
os_ee   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -11*11'  # double electron
os_emu  = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -11*13'  # muon & electron
os_mumu = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -13*13'  # double muon


#############################################
########## DY control phase space ###########
#############################################

cuts['DY_cr']  = { 
   'expr' : osLep
}

#############################################
########## top control phase space ##########
#############################################

## Top control regions
# 2 or more jets
# OS e+- & mu-+ (different flavour)

# ricomincia da qui
top =       '\
            nCleanJet >= 2 \
            && detajj > 1.\
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 \
            && Lepton_pt[0]>50 \
            && Lepton_pt[1]>40 \
            && CleanJet_pt[0] > 40 \
            && CleanJet_pt[1] > 30 \
            '

cuts['topcr'] = top  

#############################################
########## DPS control phase space ##########
#############################################

cuts['DPS_cr']  = { 
   'expr' : ssLep
}



