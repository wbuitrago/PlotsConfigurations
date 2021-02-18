# variables

# variables = {}

###########################
##### LEPTON VARS #########
###########################

variables['nJet']={'name':'Sum$(CleanJet_pt>30)',
                   'range':(4,0,4),
                   'xaxis':'njets',
                   'fold':3
                   }

variables['mll']={'name':'mll',  # variable name
                  'range':(12,20.,500),  # variable range
                  'xaxis':'mll [GeV]',  # x axis name
                  'fold':3
                  }

variables['ptl1']={'name':'Alt$(Lepton_pt[0],-9999.)',
                  'range':(10,30.,300.),
                  'xaxis':'p_{T} 1st lep [GeV]',
                  'fold':3
                  }

variables['ptl2']={'name':'Alt$(Lepton_pt[1],-9999.)',
                  'range':(16,30.,210.),
                  'xaxis':'p_{T} 2nd lep [GeV]',
                  'fold':3
                  }

variables['etal1'] = {'name' : 'Alt$(Lepton_eta[0],-9999.)',
                         'range': (10,-2.5,2.5),
                         'xaxis': 'eta lep1',
                         'fold' : 3
                         }

variables['etal2'] = {   'name' : 'Alt$(Lepton_eta[1],-9999.)',
                            'range': (10,-2.5,2.5),
                            'xaxis': 'eta lep2',
                            'fold' : 3
                            }

###########################
##### JETS   VARS #########
###########################

variables['mjj']={'name':'mjj',
                  'range':([500,800,1200,1800,3000],),
                  'xaxis':'mjj [GeV]',
                  'fold':3
                  }

variables['ptj1']={'name':'Alt$(CleanJet_pt[0],-9999.)',
                     'range':(10,30,300),
                     'xaxis':'p_{T} 1st jet [GeV]',
                     'fold':3
                     }

variables['ptj2']={'name':'Alt$(CleanJet_pt[1],-9999.)',
                     'range':(10,30,250),
                     'xaxis':'p_{T} 2nd jet [GeV]',
                     'fold':3
                     }

variables['etaj1'] = {  'name' : 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'eta j1',
                        'fold' : 3
                        }

variables['etaj2'] = {  'name' : 'Alt$(CleanJet_eta[1],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'eta j2',
                        'fold' : 3
                     }

variables['detajj'] = { 'name'  : 'detajj',
                        'range' : (5,2.5,7.5),
                        'xaxis' : 'deta jj',
                        'fold'  : 3
                      }

variables['phi_j1'] = { 'name' : 'Alt$(CleanJet_phi[0],-9999.)',
                        'range': (10,-3.141592,3.141592),
                        'xaxis': 'phi_j1',
                        'fold' : 3
                        }

variables['phi_j2'] = { 'name' : 'Alt$(CleanJet_phi[1],-9999.)',
                        'range': (10,-3.141592,3.141592),
                        'xaxis': 'phi_j2',
                        'fold' : 3
                        }

variables['dphijj']={'name':'dphijj',
                     'range':(10,0.0,3.141592),
                     'xaxis':'dphi jj',
                     'fold':3
                     }

###########################
##### MET    VARS #########
###########################

variables['met']={'name':'MET_pt',  # variable name
                  'range':(10,30,250),  # variable range
                  'xaxis':'met [GeV]',  # x axis name
                  'fold':3
                  }
