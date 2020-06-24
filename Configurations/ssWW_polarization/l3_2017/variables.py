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
variables['eta_lep1'] = {'name' : 'Alt$(Lepton_eta[0],-9999.)',
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
                     'range':(10,0.0,3.5),
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
                     'range':([500, 1000, 1500,2000, 3000],),
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
                     'range':(5,2.5,7.5),
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

variables['met']={'name':'METFixEE2017_pt',  # variable name
                  'range':(10,30,250),  # variable range
                  'xaxis':'met [GeV]',  # x axis name
                  'fold':3
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

variables['Zlep1']  = {  'name': 'zlep1',
                         'range': (10,-0.75,0.75),
                         'xaxis': 'Z^{lep}_{1}',
                         'fold': 3
                         }
variables['Zlep2']  = {  'name': 'zlep2',
                         'range': (10,-0.75,0.75),
                         'xaxis': 'Z^{lep}_{2}',
                         'fold': 3
                         }
variables['mllVSmjj']={'name':'mll:mjj',
                       'range':([20,120,220,320],[500,1000,1800,2500],),
                       'xaxis' : 'm_{ll} : m_{jj}',
                       'fold': 3,
                       'doWeight': 1,
                       'binX': 3,
                       'binY': 3
                       }

variables['mllVSmjj_v2']={'name':'mll:mjj',
                          'range':([20, 80, 140, 240 ,500],[500, 650, 800, 1000, 1200, 1500, 1800, 2300,3000],),
                          'xaxis' : 'm_{ll} : m_{jj}',
                          'fold': 3,
                          'doWeight': 1,
                          'binX': 4,
                          'binY': 8
                          }
variables['DNNScore_WW'] = {
    'name': 'DNNScore_WW',
    'range': (20,0.,1),
    'xaxis': 'DNN output',
    'fold': 3 ,
}
variables['DNNScore_WW_v1'] = {
    'name': 'DNNScore_WW',
    'range': ([0,0.45,0.62,0.74,0.8,1.0],),
    'xaxis': 'DNN output',
    'fold': 3 ,
}
variables['DNNScore_WW_v2'] = {
    'name': 'DNNScore_WW',
    'range': ([0,0.50,0.68,0.79,1.0],),
    'xaxis': 'DNN output',
    'fold': 3 ,
}
variables['mjjVSDNNScore_WW'] = {
    'name': 'mjj:DNNScore_WW',            #   variable name
    'range' : ([0,0.45,0.62,0.74,0.8,1.0],[500,800,1200,1800,3000],),            #   variable range
    'xaxis' : 'm_{jj}:DNN',      #   x axis name
    'fold' : 3 ,
}
variables['mjjVSDNNScore_WW_v2'] = {
    'name': 'mjj:DNNScore_WW',            #   variable name
    'range' : ([0,0.50,0.68,0.79,1.0],[500,800,1200,1800,3000],),            #   variable range
    'xaxis' : 'm_{jj}:DNN',      #   x axis name
    'fold' : 3 ,
}

#variables['DNNScore_PP'] = {
#    'name': 'DNNScore_PP',
#    'range': (20,0.,1),
#    'xaxis': 'DNN output',
#    'fold': 3 ,
#}
#variables['DNNScore_PP_v1'] = {
#    'name': 'DNNScore_PP',
#    'range': ([0,0.45,0.62,0.74,0.8,1.0],),
#    'xaxis': 'DNN output',
#    'fold': 3 ,
#}
#variables['DNNScore_PP_v2'] = {
#    'name': 'DNNScore_PP',
#    'range': ([0,0.50,0.68,0.79,1.0],),
#    'xaxis': 'DNN output',
#    'fold': 3 ,
#}
#variables['mjjVSDNNScore_PP'] = {
#    'name': 'mjj:DNNScore_PP',            #   variable name
#    'range' : ([0,0.45,0.62,0.74,0.8,1.0],[500,800,1200,1800,3000],),            #   variable range
#    'xaxis' : 'm_{jj}:DNN',      #   x axis name
#    'fold' : 3 ,
#}
#variables['mjjVSDNNScore_PP_v2'] = {
#    'name': 'mjj:DNNScore_PP',            #   variable name
#    'range' : ([0,0.50,0.68,0.79,1.0],[500,800,1200,1800,3000],),            #   variable range
#    'xaxis' : 'm_{jj}:DNN',      #   x axis name
#    'fold' : 3 ,
#}

variables['mjjVSdetajj']={'name':'mjj:detajj',
                          'range':([2.5, 4.0, 5.0, 7.0],[500, 1000, 1500,2000, 3000],),
                          'xaxis' : 'm_{jj} : |#Delta#eta_{jj}|',
                          'fold': 3,
                          }
variables['DNNScore_VBS1'] = {
    'name': 'DNNScore_VBS',            #   variable name
    'range' : ([0,0.454,0.588,0.669,0.740,1],),            #   variable range
    'xaxis' : 'DNNScore_VBS',      #   x axis name
    'fold' : 3 ,
}
variables['DNNScore_VBS2'] = {
    'name': 'DNNScore_VBS',            #   variable name
    'range' : ([0,0.495,0.632,0.721,1],),            #   variable range
    'xaxis' : 'DNNScore_VBS',      #   x axis name
    'fold' : 3 ,
}
variables['mjjVSDNNScore_VBS1'] = {
    'name': 'mjj:DNNScore_VBS',            #   variable name
    'range' : ([0,0.454,0.588,0.669,0.740,1],[500,800,1200,1800,3000],),            #   variable range
    'xaxis' : 'm_{jj}:DNN',      #   x axis name
    'fold' : 3 ,
}
variables['mjjVSDNNScore_VBS2'] = {
    'name': 'mjj:DNNScore_VBS',            #   variable name
    'range' : ([0,0.495,0.632,0.721,1],[500,800,1200,1800,3000],),            #   variable range
    'xaxis' : 'm_{jj}:DNN',      #   x axis name
    'fold' : 3 ,
}
variables['DNNVSDNN1'] = {
    'name': 'DNNScore_nonVBS:DNNScore_VBS',            #   variable name
    'range' : ([0,0.495,0.632,0.721,1],[0,0.476,0.695,0.864,1],),            #   variable range
    'xaxis' : 'DNN^{nonVBS}:DNN^{WW}',      #   x axis name
    'fold' : 3 ,
}
variables['DNNVSDNN2'] = {
    'name': 'DNNScore_nonVBS:DNNScore_VBS',            #   variable name
    'range' : ([0,0.454,0.588,0.669,0.740,1],[0,0.476,0.695,0.864,1],),            #   variable range
    'xaxis' : 'DNN^{nonVBS}:DNN^{WW}',      #   x axis name
    'fold' : 3 ,
}
variables['DNNVSDNN3'] = {
    'name': 'DNNScore_nonVBS:DNNScore_VBS',            #   variable name
    'range' : ([0,0.454,0.588,0.669,0.740,1],[0,0.417,0.618,0.767,0.890,1],),            #   variable range
    'xaxis' : 'DNN^{nonVBS}:DNN^{WW}',      #   x axis name
    'fold' : 3 ,
}