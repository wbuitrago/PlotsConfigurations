# cuts

supercut = '((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)) \
            && multiJet \
            && abs(mll-91.1876)<15 \
            && mjj>200\
           '
      #      && abs(mll-90)<40 \
# supercut: && ptll>30 \
#&& Alt$(Lepton_pt[2],0)<10) 



# ## Signal regions
# cuts['Zjj_13TeV'] = {
#    'expr': 'sr',
#     # Define the sub-categorization of sr
#    'categories' : {
#       #
#       #'em' : ' zeroJet  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && mth<60 && mll>40 && mll<80',
#       #
#       'superinclusive':'mjj>200',

#       'all' : 'abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 \
#          && Lepton_pt[0]>50 && Lepton_pt[1]>30 \
#          && CleanJet_pt[0]>50 \
#          ',
#       'ee' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
#          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 \
#          && Lepton_pt[0]>50 && Lepton_pt[1]>30 \
#          && CleanJet_pt[0]>50 \
#          ',
#       #&& abs(mll-91.1876) < 30 \
#       'mm' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
#          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 \
#          && Lepton_pt[0]>50 && Lepton_pt[1]>30 \
#          && CleanJet_pt[0]>50 \
#          ',
#       # 'sc' : ' abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 \
#       #       && Lepton_pt[0]>30 && Lepton_pt[1]>20 \
#       #       && abs(mll-91.1876)<15 \
#       #       && mjj>300 \
#       #       && detajj>3.5 \
#       #       ',
#       #&& abs(mll-90)<15 \
#       # && mjj>200 && Jet_eta[0]<4.7 \
#       # && Jet_pt[0]>50 && Jet_pt[1]>30 
#    }
# }

# cuts['Top']  = { 
#    'expr' : 'topcr',
#    'categories' : {
#       'alltop':'mjj>200',
#    }
# }


# cuts['WW']  = { 
#    'expr' : 'wwcr',
#    'categories' : {
#       'allww':'mjj>200',
#    }
# }

# ## DY control regions
# cuts['DY']  = { 
#    'expr' : 'dycr',
#    # 'categories' : { 
#    #    'lowDetajj'   : 'abs(mll-91.2)<15 && detajj < 2.5',
#    #    'highDetajj'  : ' abs(mll-91.2)<15 && detajj >= 2.5',
#    #    'lowMjj'   : 'abs(mll-91.2)<15 && mjj < 300 && mjj >=150',
#    #    'highMjj'  : 'abs(mll-91.2)<15 && mjj >= 300',
#    #    }
#    'categories' : {
#       'allDY':'mjj>200',
#    }
# }

# cuts['DYPU']  = { 
#    'expr' : 'dypucr',
#    'categories' : {
#       'allDYPU':'mjj>200',
#    }
# }

#cuts['total'] = {
#   'expr': 'mjj>200',
#   'categories' : {
#      'allTotal': 'mjj>200',
#      'highZeppenfeldZ': '(mjj>200) && (ZeppenfeldDilepton >= 0.5)',
#      'lowZeppenfeldZ': '(mjj>200) && (ZeppenfeldDilepton < 0.5)',
#   }
#}
#cuts['total'] = 'mjj>200'

cuts['notTop'] = {
    'expr': 'bVeto',
    'categories': {
        'total': '1'
    }
}
"""
    'categories': {
        'lowDeta': 'detajj<3',
        'highDeta': 'detajj>=3'
    }
"""
"""
cuts['highDeta'] = {
    'expr': 'detajj>=3 && bVeto',
    'categories': {
        'total': 'mjj>200'
    }
}
"""
