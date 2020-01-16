# cuts

# TEMPLATE CUT (TO BE LEFT COMMENTED)

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
   'expr' : osLep,
   # sub categorization
   'categories' : {
         'ee'    : os_ee,
         'emu'   : os_emu,
         'mumu'  : os_mumu,
   }
}

#############################################
########## top control phase space ##########
#############################################

top =       '\
            nCleanJet >= 2 \
            && detajj > 1.\
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && Lepton_pt[0]>50 \
            && Lepton_pt[1]>40 \
            && CleanJet_pt[0] > 40 \
            && CleanJet_pt[1] > 30 \
            '

cuts['topcr'] = {
   'expr' : top,
   # sub categorization
   'categories' : {
         'ee'    : os_ee,
         'emu'   : os_emu,
         'mumu'  : os_mumu,
   }
}
  

#############################################
########## DPS control phase space ##########
#############################################

cuts['DPS_cr']  = { 
   'expr' : 'nLepton > 1',
   # sub categorization
   'categories' : {
         'ee'    : ss_ee,
         'emu'   : ss_emu,
         'mumu'  : ss_mumu,
   }
}



