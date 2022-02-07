# variables

#variables = {}
    
# 'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow


variables['detajjmjj'] = {   'name': 'mjj:detajj',            #   variable name    
                            'range' : ([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],[200., 1500., 2000., 3000., 5000.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV] : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            # do weighted plot too
                            'doWeight' : 1,
                            'binX'     : 6,
                            'binY'     : 4
                        }


# to plot

variables['events']   = {   'name': '1',
                            'range' : (1,0,2),
                            'xaxis' : 'events',
                            'fold' : 3
                        }

variables['mjjbins']      = {   'name': 'mjj',            #   variable name    
                            'range' : ([500., 750., 1000., 1500., 2000., 4000.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :3
                        }



variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : ([200., 500., 750., 1000., 1250., 1500., 1750, 2000., 3000., 4000., 5000.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :3
                        }



variables['ptll']  = {   'name': 'ptll',
                        'range' : (30, 0,200),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 3
                        }


variables['mll']  = {   'name': 'mll',
                        'range' : (100, 0,200),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 3
                        }



variables['ptl1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (60,30,300),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }

variables['ptl2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (30,20,150),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }


variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }

variables['detajj']  = {  'name': 'detajj',
                        'range' : (40, 0.0, 10.0),
                        'xaxis' : '#Delta#eta_{jj}',
                        'fold'  : 3
                        }




variables['ptjet1']  = {   'name': 'CleanJet_pt[0]',
                        'range' : (100,50,500),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold'  : 3
                        }

variables['ptjet2']  = {   'name': 'CleanJet_pt[1]',
                        'range' : (100,30,300),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold'  : 3
                        }


"""

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }


# variables['mjjLow']  = {   'name': 'mjj',
#                         'range' : (30, 200,300),
#                         'xaxis' : 'm_{jj} [GeV]',
#                         'fold' : 3
#                         }
# variables['mjjHigh']  = {   'name': 'mjj',
#                         'range' : (30, 300,3000),
#                         'xaxis' : 'm_{jj} [GeV]',
#                         'fold' : 3
#                         }
variables['mjjHigh']  = {   'name': 'mjj',
                        'range' : (30, 200,3000),
                        'xaxis' : 'm_{jj} [GeV]',
                        'fold' : 3,
                        'blind': {
                            'Zjj_13TeV_superinclusive': [1000, 3000]
                            }
}
variables['ZeppenfeldZ']  = {   'name': 'ZeppenfeldDilepton',
                        'range' : (30, -2,2),
                        'xaxis' : 'z_{Z}',
                        'fold' : 3,
}
variables['Zeppenfeldl1']  = {   'name': 'ZeppenfeldLeadingLepton',
                        'range' : (30, -2,2),
                        'xaxis' : 'z_{l1}',
                        'fold' : 3,
}
# variables['ZeppenfeldLow']  = {   'name': 'ZeppenfeldDilepton',
#                         'range' : (30, 0,0.5),
#                         'xaxis' : 'z^*_{Z}',
#                         'fold' : 3,
#                         # 'blind': {
#                         #     'Zjj_13TeV_superinclusive': [1000, 3000]
#                         #     }
# }

# variables['ZeppenfeldHigh']  = {   'name': 'ZeppenfeldDilepton',
#                         'range' : (30, 0.5,2),
#                         'xaxis' : 'z^*_{Z}',
#                         'fold' : 3,
#                         # 'blind': {
#                         #     'Zjj_13TeV_superinclusive': [1000, 3000]
#                         #     }
# }
# variables['mjj_High']  = {   'name': 'mjj',
#                         'range' : (30, 200,7000),
#                         'xaxis' : 'm_{jj} [GeV]',
#                         'fold' : 3
#                         }
# variables['nvtx']  = {   'name': 'PV_npvsGood',
#                         'range' : (20,0,100),
#                         'xaxis' : 'nvtx',
#                          'fold' : 3
#                       }

# variables['mll']  = {   'name': 'mll',
#                         'range' : (30, 50,500),
#                         'xaxis' : 'm_{ll} [GeV]',
#                         'fold' : 3
#                         }


# variables['mll-near-Z']  = {   'name': 'mll',
#                         'range' : (30, 76,106),
#                         'xaxis' : 'm_{ll} [GeV]',
#                         'fold' : 3
#                         }

# variables['mth']  = {   'name': 'mth',
#                         'range' : (20, 60,200),
#                         'xaxis' : 'm_{T}^{H} [GeV]',
#                         'fold' : 0
#                         }

# variables['mth-DY']  = {   'name': 'mth',
#                         'range' : (10, 0, 60),
#                         'xaxis' : 'm_{T}^{H} [GeV]',
#                         'fold' : 0
#                         }

variables['ptll']  = {   'name': 'ptll',
                        'range' : (30, 0,200),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 3
                        }

# variables['ptl1']  = {   'name': 'Lepton_pt[0]',
#                         'range' : (30,30,150),
#                         'xaxis' : 'p_{T} 1st lep',
#                         'fold'  : 0
#                         }

# variables['ptl2']  = {   'name': 'Lepton_pt[1]',
#                         'range' : (30,20,150),
#                         'xaxis' : 'p_{T} 2nd lep',
#                         'fold'  : 0
#                         }
# variables['etaj1']  = {   'name': 'CleanJet_eta[0]',
#                         'range' : (30,-4.7,4.7),
#                         'xaxis' : '#eta_{j} 1st jet',
#                         'fold'  : 3
#                         }
# variables['etaj2']  = {   'name': 'CleanJet_eta[1]',
#                         'range' : (30,-4.7,4.7),
#                         'xaxis' : '#eta_{j} 2nd jet',
#                         'fold'  : 3
#                         }

#
# Reduced variables to be faster
# 
#
# variables['eta1']  = {  'name': 'Lepton_eta[0]',
#                         'range' : (20,-2.5,2.5),
#                         'xaxis' : '#eta 1st lep',
#                         'fold'  : 3
#                         }

# variables['eta2']  = {  'name': 'Lepton_eta[1]',
#                         'range' : (20,-2.5,2.5),
#                         'xaxis' : '#eta 2nd lep',
#                         'fold'  : 3
#                         }
# # 
# # 
# variables['phi1']  = {  'name': 'Lepton_phi[0]',
#                         'range' : (20,-3.2,3.2),
#                         'xaxis' : '#phi 1st lep',
#                         'fold'  : 3
#                         }

# variables['phi2']  = {  'name': 'Lepton_phi[1]',
#                         'range' : (20,-3.2,3.2),
#                         'xaxis' : '#phi 2nd lep',
#                         'fold'  : 3
#                         }
# 
variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }
# 
# variables['njet']  = {
#                         'name': 'Sum$(CleanJet_pt>30)',
#                         'range' : (5,0,5),
#                         'xaxis' : 'Number of jets',
#                         'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }
# 
# variables['jetpt1']  = {
#                         'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
#                         'range' : (20,50,200),
#                         'xaxis' : 'p_{T} 1st jet',
#                         'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }

# variables['jetpt2']  = {
#                         'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[1], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
#                         'range' : (20,30,200),
#                         'xaxis' : 'p_{T} 2nd jet',
#                         'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }
# 
# variables['jeteta1']  = {  'name': '(Sum$(CleanJet_pt>50)>0)*(Alt$(CleanJet_eta[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
#                         'range' : (20,-5.0,5.0),
#                         'xaxis' : '#eta 1st jet',
#                         'fold'  : 0
#                         }
# # 
# variables['jeteta2']  = {  'name': '(Sum$(CleanJet_pt>30)>1)*(Alt$(CleanJet_eta[1], 0)) - (Sum$(CleanJet_pt>30)<=1)*99',
#                         'range' : (20,-5.0,5.0),
#                         'xaxis' : '#eta 2nd jet',
#                         'fold'  : 0
#                         }
variables['detajTot']  = {  'name': 'detajj',
                        'range' : (16,0,8.0),
                        'xaxis' : '#Delta_{#eta} jets',
                        'fold'  : 3
                        }
# variables['detajLow']  = {  'name': 'detajj',
#                     'range' : (16,0,2.5),
#                     'xaxis' : '#Delta_{#eta} jets',
#                     'fold'  : 3
#                     }
# variables['detajHigh']  = {  'name': 'detajj',
#                     'range' : (16,2.5,8),
#                     'xaxis' : '#Delta_{#eta} jets',
#                     'fold'  : 3
#                     }

# 
# 
# 
# variables['mllVSmth_pt2ge20'] = {   'name': 'mll:mth',            #   variable name    
#                              'range' : ([60,80,90,100,110,120,130,150,200],[12,25,35,40,45,50,55,70,90,210],),            #   variable range
#                              'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
#                              'fold' : 3 ,
#                              # do weighted plot too
#                              'doWeight' : 1,
#                              'binX'     : 8,
#                              'binY'     : 9
#                              #
#                              }
# 
# variables['mllVSmth_pt2lt20'] = {   'name': 'mll:mth',            #   variable name    
#                              'range' : ([60,80,90,110,130,150,200],[12,25,40,50,70,90,210],),            #   variable range
#                              'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
#                              'fold' : 3 ,
#                              # do weighted plot too
#                              'doWeight' : 1,
#                              'binX'     : 6,
#                              'binY'     : 6
#                              #
#                              }
#""" 
