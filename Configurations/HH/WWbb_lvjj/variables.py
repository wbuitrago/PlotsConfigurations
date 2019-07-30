variables['BDT_classifier'] = {
                                 'name': 'BDT_var(mjj_b, deltaR_lep_wjet, deltaR_b, deltaphi_lep_wjet_high, deltaR_lep_b, deltaeta_lep_wjet_high, deltaphi_lep_b_high, deltaphi_met_wjet_high, deltaphi_lep_b_low)',
                                 'range' : (100, 0.3,0.8),
                                 'xaxis' : 'MVA discriminant',
                                 'fold' : 3,
                                 'linesToAdd' : ['.L /gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/BDT_var.C', 'initReader()']
                              }

variables['mjj_b']  = {
                          'name': 'mjj_b',#'mjj(std_vector_jet_eta[H_jets[0]],std_vector_jet_eta[H_jets[1]], std_vector_jet_pt[H_jets[0]], std_vector_jet_pt[H_jets[1]], std_vector_jet_phi[H_jets[0]], std_vector_jet_phi[H_jets[1]])',            #   variable name    
                           'range' : (30,20,500),    #   variable range
                           'xaxis' : 'm_{bb}',  #   x axis name
                           'fold' : 3#,
                        #'linesToAdd' : ['.L /gwpool/users/achiapparini/CMSSW_8_0_26_patch1/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/mjj.C+']
                        }
variables['b_pt_high'] = { 'name': 'b_pt_high',
                      'range': (40,30,400),
                      'xaxis': 'p_{T} (b high)',
                      'fold': 3
                    }

variables['b_pt_low'] = { 'name': 'b_pt_low',
                      'range': (0,30,140),
                      'xaxis': 'p_{T} (b low)',
                      'fold': 3
                    }
variables['deltaR_lep_w']  = {
                           'name': 'deltaR_lep_wjet',
                           'range' : (30,0.4,4),
                           'xaxis' : '#Delta R (lep - wjets)',
                           'fold' : 3,
                           #'SignalOnRight': 1
                        }

