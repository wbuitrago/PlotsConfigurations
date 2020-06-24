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
structure['LL']  = {'isSignal' : 1, 'isData' : 0}
structure['TL']  = {'isSignal' : 0, 'isData' : 0}
structure['TT']  = {'isSignal' : 0, 'isData' : 0}
#structure['SSWW']  = {'isSignal' : 1, 'isData' : 0}
#structure['cHbox_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHDD_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHl1_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHq3_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHWB_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHW_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cll1_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq11_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq1_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq31_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq3_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cW_int']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHbox_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHDD_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHe_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHl1_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHl3_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHq1_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHq3_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHWB_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cHW_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cll1_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq11_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq1_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq31_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cqq3_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['cW_bsm']  = {'isSignal' : 0, 'isData' : 0}
#structure['WZ_EWK']  = {'isSignal' : 0, 'isData' : 0}
structure['WZ_LL_EWK']  = {'isSignal' : 1, 'isData' : 0}
structure['WZ_LT_EWK']  = {'isSignal' : 0, 'isData' : 0}
structure['WZ_TL_EWK']  = {'isSignal' : 0, 'isData' : 0}
structure['WZ_TT_EWK']  = {'isSignal' : 0, 'isData' : 0}
structure['WpWp_QCD']  = {'isSignal' : 0, 'isData' : 0}
structure['WZ_QCD']  = {'isSignal' : 0, 'isData' : 0}
#structure['WZ_QCD_powheg']  = {'isSignal' : 0, 'isData' : 0}
#structure['WZ_QCD_AMCNLO']  = {'isSignal' : 0, 'isData' : 0}
#structure['WZ_QCD_mllmin01']  = {'isSignal' : 0, 'isData' : 0}
structure['ZZ4L']  = {'isSignal' : 0, 'isData' : 0}
structure['ggZZ']  = {'isSignal' : 0, 'isData' : 0}
structure['TTV']  = {'isSignal' : 0, 'isData' : 0}
structure['tZq']  = {'isSignal' : 0, 'isData' : 0}
structure['Vg']  = {'isSignal' : 0, 'isData' : 0}
structure['VgS1_L']  = {'isSignal' : 0, 'isData' : 0}
structure['VgS1_H']  = {'isSignal' : 0, 'isData' : 0}
structure['WW']  = {'isSignal' : 0, 'isData' : 0}
structure['Top']  = {'isSignal' : 0, 'isData' : 0}
structure['DY']  = {'isSignal' : 0, 'isData' : 0}
structure['Higgs']  = {'isSignal' : 0, 'isData' : 0}
structure['DPS']  = {'isSignal' : 0, 'isData' : 0}
structure['VVV']  = {'isSignal' : 0, 'isData' : 0}
structure['Fake']  = {'isSignal' : 0, 'isData' : 0}
structure['DATA']  = {'isSignal' : 0, 'isData' : 1}