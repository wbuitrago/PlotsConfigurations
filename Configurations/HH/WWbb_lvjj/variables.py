# variables

#variables = {}
    
   
variables['events']  = {   'name': '1',      
                        'range' : (1000,0,1000),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

################################
########## KINEMATICS ##########
################################

variables['mjj_b']  = {
                          'name': 'mjj_b',#'mjj(std_vector_jet_eta[H_jets[0]],std_vector_jet_eta[H_jets[1]], std_vector_jet_pt[H_jets[0]], std_vector_jet_pt[H_jets[1]], std_vector_jet_phi[H_jets[0]], std_vector_jet_phi[H_jets[1]])',            #   variable name    
                           'range' : (30,0,600),    #   variable range
                           'xaxis' : 'm_{bb}',  #   x axis name
                           'fold' : 3#,
                        #'linesToAdd' : ['.L /gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/mjj.C+']
                        }

variables['mjj_w']  = {
                          'name': 'mjj_wjet',#'mjj(std_vector_jet_eta[W_jets[0]],std_vector_jet_eta[W_jets[1]], std_vector_jet_pt[W_jets[0]], std_vector_jet_pt[W_jets[1]], std_vector_jet_phi[W_jets[0]], std_vector_jet_phi[W_jets[1]])',            #   variable name    
                           'range' : (30,0,600),    #   variable range
                           'xaxis' : 'm_{w}',  #   x axis name
                           'fold' : 3#,
                        #'linesToAdd' : ['.L /gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/mjj.C+']
                        }

variables['b_pt_high'] = { 'name': 'b_pt_high',
                      'range': (40,0,1000),
                      'xaxis': 'p_{T} (b high)',
                      'fold': 3
                    }

variables['b_pt_low'] = { 'name': 'b_pt_low',
                      'range': (40,0,1000),
                      'xaxis': 'p_{T} (b low)',
                      'fold': 3
                    }
variables['w_pt_high'] = { 'name': 'wjet_pt_high',
                      'range': (40,0,1000),
                      'xaxis': 'p_{T} (wjet high)',
                      'fold': 3
                    }

variables['w_pt_low'] = { 'name': 'wjet_pt_low',
                      'range': (40,0,1000),
                      'xaxis': 'p_{T} (wjet low)',
                      'fold': 3
                    }

variables['b_eta_high'] = { 'name': 'b_eta_high',
                      'range': (10,-5.0,5.0),
                      'xaxis': '#eta(b high)',
                      'fold': 3
                    }

variables['b_eta_low'] = { 'name': 'b_eta_low',
                      'range': (10,-5.0,5.0),
                      'xaxis': '#eta (b low)',
                      'fold': 3
                    }
variables['w_eta_high'] = { 'name': 'wjet_eta_high',
                      'range': (10,-5.0,5.0),
                      'xaxis': '#eta (wjet high)',
                      'fold': 3
                    }

variables['w_eta_low'] = { 'name': 'wjet_eta_low',
                      'range': (10,-5.0,5.0),
                      'xaxis': '#eta (wjet low)',
                      'fold': 3
                    }


variables['deltaeta_b'] = { 'name': 'deltaeta_b',#' abs( std_vector_jet_eta[H_jets[0]] - std_vector_jet_eta[H_jets[1]] )',
                      'range': (14,0,7),
                      'xaxis': '#Delta #eta_{bb}',
                      'fold': 3
                    }
   
variables['deltaphi_b'] = { 'name': 'deltaphi_b',#' abs( std_vector_jet_phi[H_jets[0]] - std_vector_jet_phi[H_jets[1]] )',
                      'range': (10,0,7),
                      'xaxis': '#Delta #phi_{bb}',
                      'fold': 3
                    }

variables['deltaeta_w'] = { 'name': 'deltaeta_wjet',#' abs( std_vector_jet_eta[W_jets[0]] - std_vector_jet_eta[W_jets[1]] )',
                      'range': (10,0,7),
                      'xaxis': '#Delta #eta_{w}',
                      'fold': 3
                    }
variables['deltaphi_w'] = { 'name': 'deltaphi_wjet',#' abs( std_vector_jet_phi[W_jets[0]] - std_vector_jet_phi[W_jets[1]] )',
                      'range': (10,0,7),
                      'xaxis': '#Delta #phi_{w}',
                      'fold': 3
                    }


variables['deltaphi_lep_b1'] = { 'name': 'deltaphi_lep_b_high',
                      'range': (10,0,7),
                      'xaxis': '#Delta #phi (lep-b high)',
                      'fold': 3
                    }

variables['deltaphi_lep_b2'] = { 'name': 'deltaphi_lep_b_loe',
                      'range': (10,0,7),
                      'xaxis': '#Delta #phi (lep-b low)',
                      'fold': 3
                    }
variables['deltaeta_lep_b1'] = { 'name': 'deltaphi_eta_b_high',
                      'range': (10,0,7),
                      'xaxis': '#Delta #eta (lep-b high)',
                      'fold': 3
                    }

variables['deltaeta_lep_b2'] = { 'name': 'deltaeta_lep_b_low',
                      'range': (10,0,7),
                      'xaxis': '#Delta #eta (lep-b low)',
                      'fold': 3
                    }
variables['deltaR_lep_b']  = {
                          'name': 'deltaR_lep_b',    
                           'range' : (30,0,10),  
                           'xaxis' : '#Delta R (lep - b)', 
                           'fold' : 3
                        }
variables['deltaR_lep_w']  = {
                          'name': 'deltaR_lep_wjet',                    
                           'range' : (30,0,10),  
                           'xaxis' : '#Delta R (lep - wjets)',
                           'fold' : 3
                        }


variables['deltaR_bb']  = {
                          'name': 'deltaR_b',#'deltaR(std_vector_jet_eta[H_jets[0]],std_vector_jet_eta[H_jets[1]], std_vector_jet_phi[H_jets[0]], std_vector_jet_phi[H_jets[1]])',    
                           'range' : (30,0,10),  
                           'xaxis' : '#Delta R_{bb}', 
                           'fold' : 3,
                        #'linesToAdd' : ['.L /gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/deltaR.C+']
                        }

variables['deltaR_w']  = {
                          'name': 'deltaR_wjet',#'deltaR(std_vector_jet_eta[W_jets[0]],std_vector_jet_eta[W_jets[1]], std_vector_jet_phi[W_jets[0]], std_vector_jet_phi[W_jets[1]])',            #   variable name    
                           'range' : (30,0,10),    #   variable range
                           'xaxis' : '#Delta R_{w}',  #   x axis name
                           'fold' : 3,
                        #'linesToAdd' : ['.L /gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/deltaR.C+']
                        }


#variables['nvtx']  = {  'name': 'nvtx',      
#                        'range' : (30,0,40),  
#                        'xaxis' : 'nvtx', 
#                       'fold' : 3
#                      }
#


################################
############ LEPTON ############
################################
#
#variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]',     
#                        'range' : (40,0,500),   
#                        'xaxis' : 'p_{T} 1st lep',
#                        'fold'  : 3                         
#                        }
#
#variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]',     
#                        'range' : (40,0,200),   
#                        'xaxis' : 'p_{T} 2nd lep',
#                        'fold'  : 3                         
#                        }
#
#variables['pt3']  = {   'name': 'std_vector_lepton_pt[2]',
#                        'range' : (40,0,200),
#                        'xaxis' : 'p_{T} 3rd lep',
#                        'fold'  : 3
#                        }
#
#
#variables['nlep'] =  {
#                'name': '1*(std_vector_lepton_pt[0]>20) + 1*(std_vector_lepton_pt[1]>20) + 1*(std_vector_lepton_pt[2]>20)+ 1*(std_vector_lepton_pt[3]>20) + 1*(std_vector_lepton_pt[4]>20)',
#                'range': (5,0,5),
#                'xaxis': '# leptons',
#                'fold': 3
#        }

#variables['eta1']  = {  'name': 'std_vector_lepton_eta[0]',     
#                        'range' : (20,-3,3),   
#                        'xaxis' : '#eta 1st lep',
#                        'fold'  : 0                         
#                        }
#
#variables['eta2']  = {  'name': 'std_vector_lepton_eta[1]',     
#                        'range' : (10,-3,3),   
#                        'xaxis' : '#eta 2nd lep',
#                        'fold'  : 0                         
#                       }
#

##############################
############ JETS ############
##############################

#variables['njets'] =  {
#               'name': 'njet',
#               'range': (10,0,10),
#               'xaxis': '# jets',
#               'fold': 3
#       }


#variables['cmva_nbjet_loose']  = {
#                        'name': '(1*(std_vector_jet_cmvav2[0]>-0.5884)*std_vector_jet_pt[0]>20 + \
#                        1*(std_vector_jet_cmvav2[1]>-0.5884)*std_vector_jet_pt[1]>20 + \
#                        1*(std_vector_jet_cmvav2[2]>-0.5884)*std_vector_jet_pt[2]>20 + \
#                        1*(std_vector_jet_cmvav2[3]>-0.5884)*std_vector_jet_pt[3]>20 + \
#                        1*(std_vector_jet_cmvav2[4]>-0.5884)*std_vector_jet_pt[4]>20 + \
#                        1*(std_vector_jet_cmvav2[5]>-0.5884)*std_vector_jet_pt[5]>20 + \
#                        1*(std_vector_jet_cmvav2[6]>-0.5884)*std_vector_jet_pt[6]>20 + \
#                        1*(std_vector_jet_cmvav2[7]>-0.5884)*std_vector_jet_pt[7]>20 + \
#                        1*(std_vector_jet_cmvav2[8]>-0.5884)*std_vector_jet_pt[8]>20 + \
#                        1*(std_vector_jet_cmvav2[9]>-0.5884)*std_vector_jet_pt[9]>20)',
#                        'range' : (10,0,10),
#                        'xaxis' : '(cmva) nbjet_loose',
#                        'fold'  : 3
#                        }
#
#variables['cmva_nbjet_medium'] = {
#                                 'name' : '1*(std_vector_jet_cmvav2[0]>0.4432)*(std_vector_jet_pt[0]>20) + \
#                                           1*(std_vector_jet_cmvav2[1]>0.4432)*(std_vector_jet_pt[1]>20) + \
#                                           1*(std_vector_jet_cmvav2[2]>0.4432)*(std_vector_jet_pt[2]>20) + \
#                                           1*(std_vector_jet_cmvav2[3]>0.4432)*(std_vector_jet_pt[3]>20) + \
#                                           1*(std_vector_jet_cmvav2[4]>0.4432)*(std_vector_jet_pt[4]>20) + \
#                                           1*(std_vector_jet_cmvav2[5]>0.4432)*(std_vector_jet_pt[5]>20) + \
#                                           1*(std_vector_jet_cmvav2[6]>0.4432)*(std_vector_jet_pt[6]>20) + \
#                                           1*(std_vector_jet_cmvav2[7]>0.4432)*(std_vector_jet_pt[7]>20) + \
#                                           1*(std_vector_jet_cmvav2[8]>0.4432)*(std_vector_jet_pt[8]>20) + \
#                                           1*(std_vector_jet_cmvav2[9]>0.4432)*(std_vector_jet_pt[9]>20)',
#                                 'range' :  (10,0,10),
#                                 'xaxis' : '(cmva) nbjet_medium',
#                                 'fold'  : 3
#                                 }
#
#
#
#variables['cmva_nbjet_tight']  = {
#                        'name': '1*(std_vector_jet_cmvav2[0]>0.9432)*std_vector_jet_pt[0]>20 + \
#                        1*(std_vector_jet_cmvav2[1]>0.9432)*std_vector_jet_pt[1]>20 + \
#                        1*(std_vector_jet_cmvav2[2]>0.9432)*std_vector_jet_pt[2]>20 + \
#                        1*(std_vector_jet_cmvav2[3]>0.9432)*std_vector_jet_pt[3]>20 + \
#                        1*(std_vector_jet_cmvav2[4]>0.9432)*std_vector_jet_pt[4]>20 + \
#                        1*(std_vector_jet_cmvav2[5]>0.9432)*std_vector_jet_pt[5]>20 + \
#                        1*(std_vector_jet_cmvav2[6]>0.9432)*std_vector_jet_pt[6]>20 + \
#                        1*(std_vector_jet_cmvav2[7]>0.9432)*std_vector_jet_pt[7]>20 + \
#                        1*(std_vector_jet_cmvav2[8]>0.9432)*std_vector_jet_pt[8]>20 + \
#                        1*(std_vector_jet_cmvav2[9]>0.9432)*std_vector_jet_pt[9]>20',
#                        'range' : (10,0,10),
#                        'xaxis' : '(cmva) nbjet_tight',
#                        'fold'  : 3
#                        }
#
#variables['deepCSV_nbjet_loose']  = {
#                                      'name': '1*(std_vector_jet_DeepCSVB[0] > 0.2219)*std_vector_jet_pt[0]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[1] > 0.2219)*std_vector_jet_pt[1]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[2] > 0.2219)*std_vector_jet_pt[2]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[3] > 0.2219)*std_vector_jet_pt[3]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[4] > 0.2219)*std_vector_jet_pt[4]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[5] > 0.2219)*std_vector_jet_pt[5]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[6] > 0.2219)*std_vector_jet_pt[6]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[7] > 0.2219)*std_vector_jet_pt[7]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[8] > 0.2219)*std_vector_jet_pt[8]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[9] > 0.2219)*std_vector_jet_pt[9]>20',
#                                      'range': (10,0,10),
#                                      'xaxis' : '(deepCSV) nbjet_loose',
#                                      'fold'  : 3
#                                    }
#
#variables['deepCSV_nbjet_medium']  = {
#                                      'name': '1*(std_vector_jet_DeepCSVB[0] > 0.6324)*(std_vector_jet_pt[0]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[1] > 0.6324)*(std_vector_jet_pt[1]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[2] > 0.6324)*(std_vector_jet_pt[2]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[3] > 0.6324)*(std_vector_jet_pt[3]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[4] > 0.6324)*(std_vector_jet_pt[4]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[5] > 0.6324)*(std_vector_jet_pt[5]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[6] > 0.6324)*(std_vector_jet_pt[6]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[7] > 0.6324)*(std_vector_jet_pt[7]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[8] > 0.6324)*(std_vector_jet_pt[8]>20) +\
#                                               1*(std_vector_jet_DeepCSVB[9] > 0.6324)*(std_vector_jet_pt[9]>20)',
#                                      'range': (10,0,10),
#                                      'xaxis' : '(deepCSV) nbjet_medium',
#                                      'fold'  : 3
#                                    }
#variables['deepCSV_nbjet_tight']  = {
#                                      'name': '1*(std_vector_jet_DeepCSVB[0] > 0.8958)*std_vector_jet_pt[0]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[1] > 0.8958)*std_vector_jet_pt[1]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[2] > 0.8958)*std_vector_jet_pt[2]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[3] > 0.8958)*std_vector_jet_pt[3]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[4] > 0.8958)*std_vector_jet_pt[4]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[5] > 0.8958)*std_vector_jet_pt[5]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[6] > 0.8958)*std_vector_jet_pt[6]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[7] > 0.8958)*std_vector_jet_pt[7]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[8] > 0.8958)*std_vector_jet_pt[8]>20 +\
#                                      1*(std_vector_jet_DeepCSVB[9] > 0.8958)*std_vector_jet_pt[9]>20',
#                                      'range': (10,0,10),
#                                      'xaxis' : '(deepCSV) nbjet_tight',
#                                      'fold'  : 3
#                                    }
#
#
#
#variables['jetpt1']  = {
#                        'name': 'std_vector_jet_pt[0]',     
#                        'range' : (40,0,1000),   
#                        'xaxis' : 'p_{T} 1st jet',
#                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                        }
#
#variables['jetpt2']  = {
#                        'name': 'std_vector_jet_pt[1]',     
#                        'range' : (40,0,1000),   
#                        'xaxis' : 'p_{T} 2nd jet',
#                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                        }
#
#
#variables['jetpt3']  = { 
#                        'name': 'std_vector_jet_pt[2]',     
#                        'range' : (40,0,500),   
#                        'xaxis' : 'p_{T} 3rd jet',
#                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                        }
#
#variables['jetpt4']  = {
#                        'name': 'std_vector_jet_pt[3]',     
#                        'range' : (35,0,250),   
#                        'xaxis' : 'p_{T} 4th jet',
#                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                        }
#variables['mjj']  = {
#                        'name': 'mjj',            #   variable name    
#                        'range' : (30, 0,1600),    #   variable range
#                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
#                         'fold' : 3
#                        }
#
#variables['max_mjj']  = {   
#                          'name': 'max_mjj(std_vector_jet_eta[0],std_vector_jet_eta[1],std_vector_jet_eta[2], std_vector_jet_pt[0], std_vector_jet_pt[1], std_vector_jet_pt[2], std_vector_jet_phi[0], std_vector_jet_phi[1], std_vector_jet_phi[2])',            #   variable name    
#                           'range' : (30,0,1200),    #   variable range
#                           'xaxis' : 'max m_{jj}',  #   x axis name
#                           'fold' : 3,
#                        'linesToAdd' : ['.L /gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/max_mjj.C+']
#			 }
#
#                        
#variables['pfmet']  = { 
#                        'name': 'metPfType1',     
#                        'range' : (20,0,1000),   
#                        'xaxis' : 'pfmet [GeV]',
#                        'fold'  : 3                         
#                        }




#variables['jeteta1']  = {  'name': 'std_vector_jet_eta[0]',
#                        'range' : (10,-5.0,5.0),
#                        'xaxis' : '#eta 1st jet',
#                        'fold'  : 0
#                        }

#variables['jeteta2']  = {  'name': 'std_vector_jet_eta[1]',
#                        'range' : (10,-5.0,5.0),
#                        'xaxis' : '#eta 2nd jet',
#                        'fold'  : 0
#                        }















#############################################
#################### NOT USED ###############
#############################################

#variables['mtw1']  = {  'name': 'mtw1',
                        #'range' : (40,0,200),
                        #'xaxis' : 'm_{T}^{W_{1}} [GeV]',
                         #'fold' : 3
                        #}

#variables['mtw2']  = {  'name': 'mtw2',
                        #'range' : (40,0,200),
                        #'xaxis' : 'm_{T}^{W_{2}} [GeV]',
                         #'fold' : 3
                        #}

#variables['trkMet']  = {   'name': 'metTtrk',
                        #'range' : (40,0,200),
                        #'xaxis' : 'trk met [GeV]',
                         #'fold' : 3
                        #}

#variables['mpmet']  = { 'name': 'mpmet',
                        #'range' : (40,0,200),
                        #'xaxis' : 'min proj met [GeV]',
                        #'fold' : 3
                        #}

#variables['dymvaggh']  = { 'name': 'dymvaggh',
                        #'range' : (40,-1,1),
                        #'xaxis' : 'DY MVA',
                        #'fold' : 3
                        #}

#variables['dymvavbf']  = { 'name': 'dymvavbf',
                        #'range' : (40,-1,1),
                        #'xaxis' : 'DY MVA',
                        #'fold' : 3
                        #}
#variables['mll']  = {   'name': 'mll',            #   variable name    
#                        'range' : (40, 0,200),    #   variable range
#                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
#                         'fold' : 0
#                        }

#variables['mllpeak'] = {   'name': 'mll',            #   variable name
                           #'range' : (100,80,100),    #   variable range
                           #'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           #'fold' : 0
                        #}

#variables['mth']  = {   'name': 'mth',            #   variable name    
                        #'range' : (40,0,200),    #   variable range
                        #'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                         #'fold' : 0
                        #}

#variables['dphill']  = {   'name': 'abs(dphill)',     
                        #'range' : (20,0,3.14),   
                        #'xaxis' : '#Delta#phi_{ll}',
                        #'fold' : 3
                        #}

#variables['ptll']  = {   'name': 'ptll',     
                        #'range' : (40, 0,200),   
                        #'xaxis' : 'p_{T}^{ll} [GeV]',
                        #'fold' : 3
                        #}


#variables['eta1large']  = {  'name': 'std_vector_lepton_eta[0]',
                       #'range' : ([-2.4, -2.1, -1.6, -1.2, -0.8, -0.3, -0.2, 0.2, 0.3, 0.8, 1.2, 1.6, 2.1, 2.4,],),
                       #'xaxis' : '#eta 1st lep',
                       #'fold'  : 3
                       #}

#variables['eta2large']  = {  'name': 'std_vector_lepton_eta[1]',
                       #'range' : ([-2.4, -2.1, -1.6, -1.2, -0.8, -0.3, -0.2, 0.2, 0.3, 0.8, 1.2, 1.6, 2.1, 2.4,],),
                       #'xaxis' : '#eta 2nd lep',
                       #'fold'  : 3
                       #}

#variables['taupt1']  = {'name': 'std_vector_tau_pt[0]',     
                        #'range' : (100,0,200),   
                        #'xaxis' : 'p_{T} 1st tau',
                        #'fold'  : 3                         
                        #}
