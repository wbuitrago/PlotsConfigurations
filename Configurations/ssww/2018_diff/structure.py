# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#

## Reducible Bkg

structure['Vg']  = {
    'isSignal' : 0,
    'isData'   : 0
}

#structure['ChMisId']  = {
#    'isSignal' : 0,
#    'isData'   : 0
#}

#structure['ttbar'] = {
#    'isSignal' : 0,
#    'isData'   : 0
#}

structure['ZZ']  = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['WZ_QCD']  = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['WZ_EWK']  = {
    'isSignal' : 0,
    'isData'   : 0
}
structure['VgS']  = {
    'isSignal' : 0,
    'isData'   : 0
}
structure['DPS']  = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['VVV']  = {
    'isSignal' : 0,
    'isData'   : 0,
}
structure['TTV']  = {
    'isSignal' : 0,
    'isData'   : 0,
}
##Irreducible Bkg

structure['WpWp_QCD']  = {
    'isSignal' : 0,
    'isData'   : 0
}

##Signal
'''
structure['WpWp_EWK_fid']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
'''
structure['WpWp_EWK_out']  = {
                      'isSignal' : 0,
                      'isData'   : 0
                      }

'''
# lep1 pt
structure['WpWp_EWK_lep1pt_bin0']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_lep1pt_bin1']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_lep1pt_bin2']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
# lep2 pt
structure['WpWp_EWK_lep2pt_bin0']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_lep2pt_bin1']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_lep2pt_bin2']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
# jet1 pt
structure['WpWp_EWK_jet1pt_bin0']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_jet1pt_bin1']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_jet1pt_bin2']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
# jet2 pt
structure['WpWp_EWK_jet2pt_bin0']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_jet2pt_bin1']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_jet2pt_bin2']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
# mll
structure['WpWp_EWK_mll_bin0']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_mll_bin1']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
structure['WpWp_EWK_mll_bin2']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
                      
'''
# mjj
structure['WpWp_EWK_mjj_bin0']  = {
    'isSignal' : 1,
    'isData'   : 0
}
structure['WpWp_EWK_mjj_bin1']  = {
    'isSignal' : 1,
    'isData'   : 0
}
structure['WpWp_EWK_mjj_bin2']  = {
    'isSignal' : 1,
    'isData'   : 0
}

#Fake
structure['Fake_lep']  = {
    'isSignal' : 0,
    'isData'   : 0,
}

# data


structure['DATA']  = {
    'isSignal' : 0,
    'isData'   : 1
}