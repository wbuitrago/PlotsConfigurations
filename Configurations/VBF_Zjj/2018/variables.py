# variables


import os
import copy
import inspect


folderpath = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
folderpath = os.path.dirname(folderpath)

with open(folderpath + "/config.py") as file:
    exec(file.read())

if extract:
    branches = {
        'Lepton_pt1': 'Lepton_pt[0]',
        'Lepton_pt2': 'Lepton_pt[1]',
        'Lepton_eta1': 'Lepton_eta[0]',
        'Lepton_eta2': 'Lepton_eta[1]',
        'deltaphill': 'abs(Lepton_phi[0]-Lepton_phi[1])',
        'deltaetall':'abs(Lepton_eta[0]-Lepton_eta[1])' ,
        'ptll': 'ptll',
        'mjj': 'mjj',
        'mll': 'mll',
        'ZeppenfeldDilepton': 'ZeppenfeldDilepton',
        'detajj':'detajj',
        'met': 'PuppiMET_pt',
        'ptj1': 'Alt$(CleanJet_pt[0],999999)',
        'ptj2': 'Alt$(CleanJet_pt[1],999999)',
        'npv': 'PV_npvs',
        #'ptj1': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
        #'ptj1': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[1], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
        'deltaphijj': 'abs(CleanJet_phi[0]-CleanJet_phi[1])',
        'R_j1l1': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Lepton_eta[0],2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Lepton_phi[0],2))',
        'R_j2l1': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[0],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[0],2))',
        'R_j1l2': 'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[0],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[0],-9999.)-Lepton_phi[1],2))',
        'R_j2l2':'TMath::Sqrt(TMath::Power(Alt$(CleanJet_eta[1],-9999.)-Lepton_eta[1],2)+TMath::Power(Alt$(CleanJet_phi[1],-9999.)-Lepton_phi[1],2))',
        'bVeto': 'bVeto'
    }


    variables['dnn_inputs'] = {
        'tree': branches,
        'cuts' : ['DY_13TeV_2j', 'Optimization_13TeV_2j', 'DYPU_13TeV_2j']
        #'cuts' : ['Total_13TeV_2j']
        #'cuts' : ['Total_13TeV_2j']

    }

else:




    #variables = {}
        
    # 'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

    """
    variables['detajjmjj'] = {   'name': 'mjj:detajj',            #   variable name    
                                'range' : ([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],[200., 1500., 2000., 3000., 5000.],),    #   variable range
                                'xaxis' : 'm_{jj} [GeV] : #Delta#eta_{jj}',  #   x axis name
                                'fold' :3 ,
                                # do weighted plot too
                                'doWeight' : 1,
                                'binX'     : 6,
                                'binY'     : 4
                            }
    """


    # to plot

    variables['events']   = {   'name': '1',
                                'range' : (1,0,2),
                                'xaxis' : 'events',
                                'fold' : 3
                            }
    """
    variables['mjjbins']      = {   'name': 'mjj',            #   variable name    
                                'range' : ([500., 750., 1000., 1500., 2000., 4000.],),    #   variable range
                                'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                                'fold' :3
                            }
    """



    variables['mjj']      = {   'name': 'mjj',            #   variable name    
                                'range' : ([200., 500., 750., 1000., 1250., 1500., 1750, 2000., 3000., 4000., 5000.],),    #   variable range
                                'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                                'fold' :3
                            }
    """
    variables['mjjLow']      = {   'name': 'mjj',            #   variable name    
                                'range' : (30, 200, 2000),    #   variable range
                                'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                                'fold' :3
                            }

    variables['mjjHigh']      = {   'name': 'mjj',            #   variable name    
                                'range' : (30, 2000, 7000),    #   variable range
                                'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                                'fold' :3
                            }
    """

    """variables['ptllptj1'] = {   'name': 'ptll:CleanJet_pt[0]',            #   variable name    
                                'range' : ([30.0, 40.434782608695656, 50.869565217391305, 61.30434782608695, 71.73913043478261, 82.17391304347827, 92.6086956521739, 103.04347826086956, 113.47826086956522, 123.91304347826087, 134.34782608695653, 144.7826086956522, 155.2173913043478, 165.65217391304347, 176.08695652173913, 186.52173913043478, 196.95652173913044, 207.3913043478261, 217.82608695652175, 228.2608695652174, 238.69565217391306, 249.1304347826087, 259.5652173913044, 270.0, 280.4347826086956, 290.8695652173913, 301.30434782608694, 311.7391304347826, 322.17391304347825, 332.60869565217394, 343.04347826086956, 353.47826086956525, 363.9130434782609, 374.3478260869565, 384.7826086956522, 395.2173913043478, 405.6521739130435, 416.0869565217391, 426.5217391304348, 436.95652173913044, 447.3913043478261, 457.82608695652175, 468.2608695652174, 478.69565217391306, 489.1304347826087, 499.5652173913044, 510.0, 520.4347826086957, 530.8695652173913, 541.304347826087, 551.7391304347826, 562.1739130434783, 572.6086956521739, 583.0434782608696, 593.4782608695652, 603.9130434782609, 614.3478260869565, 624.7826086956521, 635.2173913043479, 645.6521739130435, 656.0869565217391, 666.5217391304348, 676.9565217391305, 687.3913043478261, 697.8260869565217, 708.2608695652174, 718.695652173913, 729.1304347826087, 739.5652173913044, 750.0, 850, 950],[50.0, 55.69620253164557, 61.392405063291136, 67.08860759493672, 72.78481012658227, 78.48101265822785, 84.17721518987342, 89.87341772151899, 95.56962025316456, 101.26582278481013, 106.9620253164557, 112.65822784810126, 118.35443037974684, 124.05063291139241, 129.74683544303798, 135.44303797468353, 141.13924050632912, 146.8354430379747, 152.53164556962025, 158.2278481012658, 163.9240506329114, 169.62025316455697, 175.31645569620252, 181.0126582278481, 186.7088607594937, 192.40506329113924, 198.10126582278482, 203.79746835443038, 209.49367088607596, 215.18987341772151, 220.8860759493671, 226.58227848101265, 232.27848101265823, 237.97468354430382, 243.67088607594937, 249.36708860759495, 255.0632911392405, 260.75949367088606, 266.4556962025316, 272.1518987341772, 277.8481012658228, 283.5443037974684, 289.24050632911394, 294.9367088607595, 300.63291139240505, 306.32911392405066, 312.0253164556962, 317.72151898734177, 323.4177215189874, 329.11392405063293, 334.8101265822785, 340.50632911392404, 346.20253164556965, 351.8987341772152, 357.59493670886076, 363.2911392405063, 368.9873417721519, 374.6835443037975, 380.37974683544303, 386.07594936708864, 391.7721518987342, 397.46835443037975, 403.1645569620253, 408.8607594936709, 414.55696202531647, 420.253164556962, 425.94936708860763, 431.6455696202532, 437.34177215189874, 443.0379746835443, 448.7341772151899, 454.43037974683546, 460.126582278481, 465.8227848101266, 471.5189873417722, 477.2151898734177, 482.9113924050633, 488.6075949367089, 494.30379746835445, 500.0] ),    #   variable range
                                'xaxis' : 'p^{T}_{ll} [GeV] : p^{T}_{j1}',  #   x axis name
                                'fold' :3 ,
    #                            # do weighted plot too
    #                            'doWeight' : 1,
    #                            'binX'     : 6,
    #                            'binY'     : 4
                            }
    """

    variables['ptll']  = {   'name': 'ptll',
                            'range' : (70, 30,1000),
                            'xaxis' : 'p_{T}^{ll} [GeV]',
                            'fold' : 3
                            }
    variables['ptll_check']  = {   'name': 'ptll',
                            'range' : ([60.,100.,200.,300.,400.,600.,800.,1000.],),
                            'xaxis' : 'p_{T}^{ll} [GeV]',
                            'fold' : 3
                            }


    variables['mll']  = {   'name': 'mll',
                            'range' : (100, 66,107),
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
                            'range' : (100,0,500),
                            'xaxis' : 'p_{T} 1st jet',
                            'fold'  : 3
                            }

    variables['ptjet2']  = {   'name': 'ptj2',
                            'range' : (40,0,500),
                            'xaxis' : 'p_{T} 2nd jet',
                            'fold'  : 3
                            }
    variables['ptjet2_check']  = {   'name': 'ptj2',
                            'range' : ([125., 200., 300., 500.],),
                            'xaxis' : 'p_{T} 2nd jet',
                            'fold'  : 3
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
