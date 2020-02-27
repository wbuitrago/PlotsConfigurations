# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#

## Reducible Bkg


structure['ChMisId']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ttbar'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['Vg']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['WZ']  = {
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
                  #'removeFromCuts' : ['hww2l2v_13TeV_dytt_of2j_vbf'],
                  }
##Irreducible Bkg

structure['WW_strong']  = {
                      'isSignal' : 0,
                      'isData'   : 0
                      }

##Signal

structure['WpWp_EWK']  = {
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