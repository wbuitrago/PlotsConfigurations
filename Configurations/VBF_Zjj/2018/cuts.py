# cuts
supercut = '   Lepton_pt[0]>30 \
            && Lepton_pt[1]>20 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
            && multiJet \
            && abs(CleanJet_eta[0])<4.7 && abs(CleanJet_eta[1])<4.7 \
            && mjj>120 \
            && mll>50 \
           '

cuts['Top_13TeV_2j'] = {
   'expr': 'topcr',
    # Define the sub-categorization of sr
   'categories' : {
      'eemm': '1'
   }
}

cuts['VV_13TeV_2j'] = {
   'expr': 'vvcr',
   'categories' : {
      'eemm': '1'
   }
}

cuts['DY_13TeV_2j'] = {
   'expr': 'dycr',
   'categories' : {
      'eemm' : '1',
   }
}

cuts['DYPU_13TeV_2j'] = {
   'expr': 'dypucr',
   'categories' : {
      'eemm' : '1',
   }
}

#cuts['Check_13TeV_2j'] = {
#   'expr': 'checkRegion',
#   'categories' : {
#      'eemm' : '1'
#    }
#}

### Signal regions

cuts['Zjj_13TeV_2j'] = {
   'expr': 'sr',
   'categories' : {
      'eemm' : '1',
   }
}

cuts['Optimization_13TeV_2j'] = {
   'expr': 'srInclusive',
   'categories' : {
      'eemm' : '1'
    }
}        
