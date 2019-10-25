# variables

#variables = {}
    

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

variables['BDT_classifier'] = {
                                 'name': 'BDT_var(mjj_b, deltaR_lep_wjet, deltaR_b, deltaphi_lep_wjet_high, deltaR_lep_b, deltaphi_lep_b_high, b_pt_high, deltaeta_b, deltaphi_lep_b_low)',
                                 'range' : (30, -1.,1.),
                                 'xaxis' : 'BDT discriminant',
                                 'fold' : 3,
                                 'linesToAdd' : ['.L /afs/cern.ch/user/g/govoni/work/Arianna/CMSSW_10_0_2/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/BDT_var.C', 'initReader()'],
                                 'SignalOnRight': 1
                              }

################
#### LEPTON ####
################

variables['lepton_pt']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (50,0,200),   
                        'xaxis' : 'lepton pt (GeV)',
                        'fold'  : 3                         
                        }

variables['lepton_eta'] = {   'name': 'abs(Lepton_eta[0])',      
                        'range' : (50,0,2.5),  
                        'xaxis' : 'Lepton #eta', 
                        'fold' : 3
                        }

###########
### JET ###
###########

variables['nJets'] = {   'name': 'Sum$(CleanJet_pt>= 30)',      
                        'range' : (9,-0.5,8.5),  
                        'xaxis' : 'nJets', 
                        'fold' : 3
                        }

variables['Jet1_pt'] = {   'name': 'abs(CleanJet_pt[0])',      
                        'range' : (40,0,300),  
                        'xaxis' : 'Jet 1st pt', 
                        'fold' : 3
                        }

variables['Jet2_pt'] = {   'name': 'abs(CleanJet_pt[1])',      
                        'range' : (40,0,200),  
                        'xaxis' : 'Jet 2nd pt', 
                        'fold' : 3
                        }

variables['Jet3_pt'] = {   'name': 'abs(CleanJet_pt[2])',      
                        'range' : (40,0,160),  
                        'xaxis' : 'Jet 3rd pt', 
                        'fold' : 3
                        }

variables['Jet4_pt'] = {   'name': 'abs(CleanJet_pt[3])',      
                        'range' : (30,0,120),  
                        'xaxis' : 'Jet 4th pt', 
                        'fold' : 3
                        }

variables['btagging_loose']  = {   'name': 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.1522)*(CleanJet_pt[0]>20))',
                        'range' : (5,-0.5,4.5),   
                        'xaxis' : 'N_{bjet} loose (GeV)',
                       'fold'  : 3                         
                        }
variables['btagging_medium']  = {   'name': 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.4941)*(CleanJet_pt[0]>20))',
                        'range' : (5,-0.5,4.5),   
                        'xaxis' : 'N_{bjet} medium (GeV)',
                        'fold'  : 3                         
                        }
variables['btagging_tight']  = {   'name': 'Sum$(1*(Jet_btagDeepB[CleanJet_jetIdx[0]] > 0.8001)*(CleanJet_pt[0]>20))',
                        'range' : (5,-0.5,4.5),   
                        'xaxis' : 'N_{bjet} tight (GeV)',
                        'fold'  : 3                         
                        }

###########
### MET ###
###########


variables['PuppiMET'] = {   'name': 'PuppiMET_pt',      
                        'range' : (30,0,250),  
                        'xaxis' : 'PuppiMET_pt', 
                        'fold' : 3
                        }
variables['MET_pt'] = {   'name': 'MET_pt',      
                        'range' : (30,0,250),  
                        'xaxis' : 'MET_pt', 
                        'fold' : 3
                        }

################
## JETPAIRING ##
################
variables['mjj_b']  = {
                          'name': 'mjj_b',    
                           'range' : (30,20,500), 
                           'xaxis' : 'm_{bb}',  
                           'fold' : 3
                        }

variables['mjj_w']  = {
                          'name': 'mjj_wjet',    
                           'range' : (30,0,300),   
                           'xaxis' : 'm_{w}', 
                           'fold' : 3
                      }

variables['b_pt_high'] = { 'name': 'b_pt_high',
                      'range': (35,30,350),
                      'xaxis': 'p_{T} (b1)',
                      'fold': 3
                    }

variables['b_pt_low'] = { 'name': 'b_pt_low',
                      'range': (25,20,100),
                      'xaxis': 'p_{T} (b2)',
                      'fold': 3
                    }

variables['b_pt_ratio'] = { 'name': 'b_pt_high/b_pt_low',
                      'range': (20,1,10),
                      'xaxis': 'pT_{b1}/pT_{b2}',
                      'fold': 3
                    }

variables['w_pt_high'] = { 'name': 'wjet_pt_high',
                      'range': (30,20,400),
                      'xaxis': 'p_{T} (w-jet 1)',
                      'fold': 3
                    }
variables['w_pt_low'] = { 'name': 'wjet_pt_low',
                      'range': (30,20,120),
                      'xaxis': 'p_{T} (w-jet 2)',
                      'fold': 3
                    }
variables['b_eta_high'] = { 'name': 'b_eta_high',
                      'range': (6, 0,3),
                      'xaxis': '#eta(b1)',
                      'fold': 3
                    }

variables['b_eta_low'] = { 'name': 'b_eta_low',
                      'range': (6, 0, 3),
                      'xaxis': '#eta (b2)',
                      'fold': 3
                    }
variables['w_eta_high'] = { 'name': 'wjet_eta_high',
                      'range': (25,0,4.5),
                      'xaxis': '#eta (w-jet 1)',
                      'fold': 3
                    }

variables['w_eta_low'] = { 'name': 'wjet_eta_low',
                      'range': (25,0,4.5),
                      'xaxis': '#eta (w-jet 2)',
                      'fold': 3
                    }

variables['deltaeta_b'] = { 'name': 'deltaeta_b',
                      'range': (25,0,5),
                      'xaxis': '#Delta #eta_{bb}',
                      'fold': 3
                    }

variables['deltaphi_b'] = { 'name': 'deltaphi_b',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi_{bb}',
                      'fold': 3
                    }

variables['deltaeta_w'] = { 'name': 'deltaeta_wjet',
                      'range': (25,0,4.5),
                      'xaxis': '#Delta #eta_{w1w2}',
                      'fold': 3
                    }
variables['deltaphi_w'] = { 'name': 'deltaphi_wjet',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi_{w1w2}',
                      'fold': 3
                    }


variables['deltaphi_lep_b1'] = { 'name': 'deltaphi_lep_b_high',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi (lep-b1)',
                      'fold': 3
                    }

variables['deltaphi_lep_b2'] = { 'name': 'deltaphi_lep_b_low',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi (lep-b2)',
                      'fold': 3
                    }
variables['deltaphi_lep_w1'] = { 'name': 'deltaphi_lep_wjet_high',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi (lep-wjet1)',
                      'fold': 3
                    }

variables['deltaphi_lep_w2'] = { 'name': 'deltaphi_lep_wjet_low',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi (lep-wjet2)',
                      'fold': 3
                    }

variables['deltaeta_lep_b1'] = { 'name': 'deltaeta_lep_b_high',
                      'range': (25,0,4),
                      'xaxis': '#Delta #eta (lep-b1)',
                      'fold': 3
                    }
variables['deltaeta_lep_b2'] = { 'name': 'deltaeta_lep_b_low',
                      'range': (25,0,4.2),
                      'xaxis': '#Delta #eta (lep-b2)',
                      'fold': 3
                    }
variables['deltaeta_lep_w1'] = { 'name': 'deltaeta_lep_wjet_high',
                      'range': (30,0,5),
                      'xaxis': '#Delta #eta (lep-wjet1)',
                      'fold': 3
                    }
variables['deltaeta_lep_w2'] = { 'name': 'deltaeta_lep_wjet_low',
                      'range': (30,0,5),
                      'xaxis': '#Delta #eta (lep-wjet2)',
                      'fold': 3
                    }

variables['deltaR_lep_b']  = {
                          'name': 'deltaR_lep_b',
                           'range' : (30,0.4,4),
                           'xaxis' : '#Delta R (lep - b)',
                           'fold' : 3
                        }

variables['deltaR_lep_w']  = {
                           'name': 'deltaR_lep_wjet',
                           'range' : (30,0.4,4),
                           'xaxis' : '#Delta R (lep - wjets)',
                           'fold' : 3,
                           #'SignalOnRight': 1
                        }

variables['deltaR_bb']  = {
                          'name': 'deltaR_b',    
                           'range' : (30,0.4,4),
                           'xaxis' : '#Delta R_{bb}',
                           'fold' : 3
                           }

variables['deltaR_w']  = {
                          'name': 'deltaR_wjet',    
                           'range' : (25,0,7),  
                           'xaxis' : '#Delta R_{w1w2}',  
                           'fold' : 3
                         }


variables['HT']  = {
                          'name': 'Ht',    
                           'range' : (80,50,1000),    
                           'xaxis' : 'Ht',  
                           'fold' : 3,
                    }

variables['deltaeta_met_b1'] = { 'name': 'deltaeta_met_b_high',
                      'range': (25,0,2.7),
                      'xaxis': '#Delta #eta (MET-b1)',
                      'fold': 3
                    }

variables['deltaeta_met_b2'] = { 'name': 'deltaeta_met_b_low',
                      'range': (25,0,2.7),
                      'xaxis': '#Delta #eta (MET-b2)',
                      'fold': 3
                    }

variables['deltaphi_met_b1'] = { 'name': 'deltaphi_met_b_high',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi (MET-b1)',
                      'fold': 3
                    }

variables['deltaphi_met_b2'] = { 'name': 'deltaeta_met_b_low',
                      'range': (25,0,2.5),
                      'xaxis': '#Delta #phi (met-b2)',
                      'fold': 3
}
variables['deltaeta_met_w1'] = { 'name': 'deltaeta_met_wjet_high',
                      'range': (30,0,4.5),
                      'xaxis': '#Delta #eta (MET-w1)',
                      'fold': 3
                    }

variables['deltaeta_met_w2'] = { 'name': 'deltaeta_met_wjet_low',
                      'range': (30,0,4.6),
                      'xaxis': '#Delta #eta (MET-w2)',
                      'fold': 3
                    }
variables['deltaphi_met_w1'] = { 'name': 'deltaphi_met_wjet_high',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi (MET-w1)',
                      'fold': 3
                    }
variables['deltaphi_met_w2'] = { 'name': 'deltaphi_met_wjet_low',
                      'range': (25,0,3.15),
                      'xaxis': '#Delta #phi (MET-w2)',
                      'fold': 3
                    }


################
# 2D VARIABLES #
################
'''
variables['b_pt1xdeltaR_b']  = {   'name': 'b_pt_high:deltaR_b',    
                       'range' : (4, 30 ,480, 4 , 0.4, 4),   
                       'xaxis' : 'pT_{b1}:#Delta R_{bb} ',  
                       'fold' : 3
                        }
variables['b_pt1xlep_pt1']  = {   'name': 'b_pt_high:Lepton_pt[0]',             
                       'range' : (4, 30 ,480, 4 , 0, 500),     
                       'xaxis' : 'pT_{b1}:pT_{lep} [GeV]',   
                         
                       'fold' : 3
                        }
variables['deltaR_bxHT']  = {   'name': 'deltaR_b:Ht',            #   variable name
                       'range' : (4, 0.4 ,4, 4 ,0, 1000),    #   variable range
                       'xaxis' : '#Delta R_{bb}:HT',  #   x axis name
                        #'yaxis': '',
                       'fold' : 3
                        }
variables['b_pt1xmjj_b']  = {   'name': 'b_pt_high:mjj_b',             
                       'range' : (4, 30 ,400, 4 , 20, 500),     
                       'xaxis' : 'pT_{b1}:m_{bb} ',   
                         
                       'fold' : 3
                        }
variables['deltaR_bxmjj_b']  = {   'name': 'deltaR_b:mjj_b',             
                       'range' : (4, 0.4 ,4, 4,20,500),     
                       'xaxis' : '#Delta R_{bb}:m_{bb}',   
                         
                       'fold' : 3
                        }
variables['mjj_bxHT']  = {   'name': 'mjj_b:Ht',             
                       'range' : (4,20,500, 5 ,0, 1000),     
                       'xaxis' : 'm_{bb}:HT',   
                         
                       'fold' : 3
                        }

variables['b_pt1xdeltaR_lep_w']  = {   'name': 'b_pt_high:deltaR_lep_wjet',             
                       'range' : (4, 30 ,480, 4 ,0.4, 4),     
                       'xaxis' : 'pT_{b1}:#delta R(lep-W) ',   
                         
                       'fold' : 3
                        }
variables['deltaR_bxdeltaR_lep_w']  = {   'name': 'deltaR_b:deltaR_lep_wjet',             
                       'range' : (4, 0.4 ,4, 4 ,0.4, 4),     
                       'xaxis' : '#Delta R_{bb}:#delta R(lep-W) ',   
                         
                       'fold' : 3
                        }
variables['mjj_bxdeltaR_lep_w']  = {   'name': 'mjj_b:deltaR_lep_wjet',             
                       'range' : (4, 20 ,500, 4 ,0.4, 4),     
                       'xaxis' : 'mjj_{bb}:#Delta R(lep-W) ',   
                         
                       'fold' : 3
                        }

variables['HTxdeltaR_lep_w']  = {   'name': 'Ht:deltaR_lep_wjet',             
                       'range' : (5, 0 ,1000, 4 ,0.4, 4),     
                       'xaxis' : 'Ht:#Delta R(lep-W) ',   
                         
                       'fold' : 3
}
'''
