# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#

## Reducible Bkg

'''
structure['ChMisId']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }
structure['ttbar'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
'''
structure['SM']  = {'isSignal' : 1, 'isData' : 0}
structure['cqq1_LI']  = {'isSignal' : 1, 'isData' : 0}
structure['cqq1_QU']  = {'isSignal' : 0, 'isData' : 0}
