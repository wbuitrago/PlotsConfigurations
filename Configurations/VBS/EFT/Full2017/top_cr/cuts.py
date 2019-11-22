# cuts

## Top control regions
# 2 or more jets
# OS e+- & mu-+ (different flavour)
cuts['top']  = { 
      'expr' : '  nJet >= 2 \
                  && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 \
                  && Lepton_pt[0]>20 \
                  && Lepton_pt[1]>10 \
                  && (abs(Lepton_pdgId[0])==13 || Lepton_pt[0]>25) \
                  && (abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13) \
                  && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
                  && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
                  '
}


# cut to check wwsel
cuts['wwsel']  = { 
      'expr' : '( mll>12 && ptll>30 \
                  && (MET_pt > 20 || PuppiMET_pt>20)\
                  && Alt$(Lepton_pt[0],0.)>20\
                  && Alt$(Lepton_pt[1],0.)>10 \
                  && Alt$(Lepton_pt[2],0.)<10\
                  && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13)'
}

                  



# kept as example of categories but not needed anymore.. future removal?

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

