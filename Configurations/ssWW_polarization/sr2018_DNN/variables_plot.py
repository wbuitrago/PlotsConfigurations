# variables

# variables = {}

# 'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

###########################
##### LEPTON VARS #########
###########################

# variables['nLepton'] =  {   'name': 'nLepton',
#                             'range': (7,0,7),
#                             'xaxis': '# leptons',
#                             'fold': 3
# }
variables['nJet']={'name':'Sum$(CleanJet_pt>30)',
                   'range':(4,0,4),
                   'xaxis':'njets',
                   'fold':3
                   }

variables['nLepton']={
    'name':'1*(Alt$(Lepton_pt[0],0.)>10) + 1*(Alt$(Lepton_pt[1],0.)>10) + 1*(Alt$(Lepton_pt[2],0.)>10)+ 1*(Alt$(Lepton_pt[3],0.)>10) + 1*(Alt$(Lepton_pt[4],0.)>10)',
    'range':(5,0,5),
    'xaxis':'# leptons',
    'fold':3
}
variables['mll']={'name':'mll',  # variable name
                  'range':(12,20.,500),  # variable range
                  'xaxis':'mll [GeV]',  # x axis name
                  'fold':3
                  }
# variables['mll_v1']  = {    'name'  : 'mll',            #   variable name
#                            'range' : ([20,80,140,240,500],),    #   variable range
#                            'xaxis' : 'mll v1 [GeV]',      #   x axis name
#                            'fold'  : 3
#                            }
variables['mll_v2']={'name':'mll',  # variable name
                     'range':([20,60,80,110,140,240,380,500],),  # variable range
                     'xaxis':'mll v1 [GeV]',  # x axis name
                     'fold':3
                     }
variables['pt1']={'name':'Alt$(Lepton_pt[0],-9999.)',
                  'range':(10,30.,300.),
                  'xaxis':'p_{T} 1st lep [GeV]',
                  'fold':3
                  }
variables['pt1_v1']={'name':'Alt$(Lepton_pt[0],-9999.)',
                     'range':(15,30.,510.),
                     'xaxis':'p_{T} 1st lep [GeV]',
                     'fold':3
                     }

variables['pt2']={'name':'Alt$(Lepton_pt[1],-9999.)',
                  'range':(6,30.,210.),
                  'xaxis':'p_{T} 2nd lep [GeV]',
                  'fold':3
                  }
variables['pt2_v2']={'name':'Alt$(Lepton_pt[1],-9999.)',
                  'range':(10,30.,300.),
                  'xaxis':'p_{T} 2nd lep [GeV]',
                  'fold':3
                  }
## eta leptons
variables['eta_lep1'] = {   'name' : 'Alt$(Lepton_eta[0],-9999.)',
                            'range': (10,-2.5,2.5),
                            'xaxis': 'eta lep1',
                            'fold' : 3
                            }

variables['eta_lep2'] = {   'name' : 'Alt$(Lepton_eta[1],-9999.)',
                            'range': (10,-2.5,2.5),
                            'xaxis': 'eta lep2',
                            'fold' : 3
                            }

variables['detall']={'name':'detall',
                     'range':(10,0.0,5.0),
                     'xaxis':'deta ll',
                     'fold':3
                     }

## phi leptons

variables['phi_lep1'] = {   'name' : 'Alt$(Lepton_phi[0],-9999.)',
                            'range': (10,-3.141592,3.141592),
                            'xaxis': 'phi lep1',
                            'fold' : 3
}

variables['phi_lep2'] = {   'name' : 'Alt$(Lepton_phi[1],-9999.)',
                            'range': (10,-3.141592,3.141592),
                            'xaxis': 'phi lep2',
                            'fold' : 3
                            }

variables['dphill']={'name':'dphill',
                     'range':(10,0,3.141592),
                     'xaxis':'dphi ll',
                     'fold':3
                     }

###########################
##### JETS   VARS #########
###########################

# variables['nJet']  = {      'name'  : 'nCleanJet',
#                             'range' : (7,0,7),
#                             'xaxis' : '# Clean Jets',
#                             'fold'  : 3
#                             }

variables['mjj']={'name':'mjj',
                  'range':([500,800,1200,1800,3000],),
                  'xaxis':'mjj [GeV]',
                  'fold':3
                  }

variables['mjj_v1']={'name':'mjj',
                     'range':([500,800,1100,1500,2000,3000],),
                     'xaxis':'mjj v1[GeV]',
                     'fold':3
                     }
variables['mjj_v2']={'name':'mjj',
                     'range':(10,500,3000),
                     'xaxis':'mjj v1[GeV]',
                     'fold':3
                     }
# for low mjj control region
# variables['low_mjj']  = {   'name' : 'mjj',
#                             'range': (10,150,500.),
#                             'xaxis': 'mjj [GeV]',
#                             'fold' : 3
#                         }

variables['jetpt1']={'name':'Alt$(CleanJet_pt[0],-9999.)',
                     'range':(10,30,300),
                     'xaxis':'p_{T} 1st jet [GeV]',
                     'fold':3
                     }

variables['jetpt1_v1']={'name':'Alt$(CleanJet_pt[0],-9999.)',
                        'range':(12,30,510),
                        'xaxis':'p_{T} 1st jet v1[GeV]',
                        'fold':3
                        }

variables['jetpt2']={'name':'Alt$(CleanJet_pt[1],-9999.)',
                     'range':(10,30,250),
                     'xaxis':'p_{T} 2nd jet [GeV]',
                     'fold':3
                     }
# eta
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

variables['detajj']={'name':'detajj',
                     'range':(10,2.5,9.0),
                     'xaxis':'deta jj',
                     'fold':3
                     }

variables['detajj_v1']={'name':'detajj',
                        'range':([2.5,3.5,5.0,6.5,9.0],),
                        'xaxis':'deta jj v1',
                        'fold':3
                        }

# phi jets

variables['phi_j1'] = {     'name' : 'Alt$(CleanJet_phi[0],-9999.)',
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
variables['MET_significance']  = {  'name'  : 'MET_significance',
                                    'range' : (10,0.,1.),
                                    'xaxis' : 'MET_significance',
                                    'fold'  : 3
                    }

###########################
##### bTag Variables ######
###########################

# variables['Jet_btagDeepB_0']  = {   'name'  : 'Jet_btagDeepB[CleanJet_jetIdx[0]]',
#                                     'range' : (10,0,1),
#                                     'xaxis' : 'Jet_btagDeepB_0',
#                                     'fold'  : 3
#                                 }

# variables['Jet_btagDeepB_1']  = {   'name'  : 'Jet_btagDeepB[CleanJet_jetIdx[1]]',
#                                     'range' : (10,0,1),
#                                     'xaxis' : 'Jet_btagDeepB_1',
#                                     'fold'  : 3
#                                 }

# # one only for the first two jets. It gives the btag variable for the most central of the first two CleanJets
# variables['my_btag_var']  = {   'name'  : '(fabs(CleanJet_eta[0]) <= fabs(CleanJet_eta[1])) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(CleanJet_eta[0]) > fabs(CleanJet_eta[1])) * Jet_btagDeepB[CleanJet_jetIdx[1]]',
#                                 'range' : (10,0,1),
#                                 'xaxis' : 'central_jet_btag_var',
#                                 'fold'  : 3
#                             }


#############################
#### Zeppenfeld Variable ####
#############################
variables['DNNScore'] = {
    'name': 'DNNScore',
    'range': ([0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
}
variables['Zlep1']  = {  'name': 'zlep1',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{1}',
                         'fold': 3
                         }
variables['Zlep2']  = {  'name': 'zlep2',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{2}',
                         'fold': 3
                         }
variables['mllVSmjj']={'name':'mll:mjj',
                       'range':([20,120,220,320],[500,1000,1800,2500]),
                       'xaxis' : 'm_{ll} : m_{jj}',
                       'fold': 3,
                       'doWeight': 1,
                       'binX': 3,
                       'binY': 3
                       }

variables['mllVSmjj_v2']={'name':'mll:mjj',
                          'range':([20, 80, 140, 240 ,500],[500, 650, 800, 1000, 1200, 1500, 1800, 2300,3000]),
                          'xaxis' : 'm_{ll} : m_{jj}',
                          'fold': 3,
                          'doWeight': 1,
                          'binX': 4,
                          'binY': 8
                          }
variables['mjjVSdetajj']={'name':'mjj:detajj',
                          'range':([500, 1000, 1500, 2000,3000],[2,5, 4.0, 5.0, 6.0]),
                          'xaxis' : 'm_{ll} : m_{jj}',
                          'fold': 3,
                          'doWeight': 1,
                          'binX': 4,
                          'binY': 3
                          }
