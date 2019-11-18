# cuts

## Top control regions
# 2 or more jets
# OS e+- & mu-+ (different flavour)
cuts['top']  = { 
      'expr' : 'nJet >= 2 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13'
}



# kept as example of categories

# ## Top control regions
# cuts['hww2l2v_13TeV_top']  = { 
#    'expr' : 'topcr',
#     # Define the sub-categorization of topcr
#    'categories' : {
#       '0j' : 'zeroJet',
#       '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
#       '2j' : 'mjj<400 && multiJet',
#    }
# }

