# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#

## Reducible Bkg

# MisCharge # --------------------
structure['mischarge']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
# --------------------------------

structure['Vg']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['VgS_L'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['VgS_H'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

# structure['WZTo2L2Q']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

structure['WZ_QCD']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
                
structure['WLLJJ_EWK']  = {
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

structure['DPS']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }                               

structure['WW_QCD']  = {
                      'isSignal' : 0,
                      'isData'   : 0
                      }


# signal with EFT samples
structure['sm']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }

structure['linear']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }

structure['quadratic']  = {
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

# ##Signal (official SM sample)
# structure['WpWp_EWK']  = {
#                       'isSignal' : 1,
#                       'isData'   : 0
#                       }









