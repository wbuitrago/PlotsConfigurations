
##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }


######## lepton 1 ##########

variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (25,0,175),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }

variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (24,-2.4,2.4),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3                         
                        }
                        
variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold'  : 3
                        }

variables['puppimet_phi']  = {  'name': 'PuppiMET_phi',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi MET',
                        'fold'  : 3
                        }

variables['mtw1']  = {   'name': 'mtw1',
                        'range' : (20,0,200),
                         'xaxis' : 'm_{T}^{l1+MET} [GeV]',
                        'fold' : 3
                       }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (30,0,300),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }

#variables['nlep_30']  = {
#                         'name': 'Sum$(Lepton_pt>30)',     
#                         'range' : (8,0,8),   
#                         'xaxis' : 'Number of leptons w/ pt>30 GeV',
#                         'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }   

#variables['nlep_10']  = {
#                         'name': 'Sum$(Lepton_pt>10)',     
#                         'range' : (20,0,20),   
#                         'xaxis' : 'Number of leptons w/ pt>10 GeV',
#                         'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }               

#variables['nlep']  = {
#                         'name': 'nLepton',     
#                         'range' : (20,0,20),   
#                         'xaxis' : 'Number of leptons',
#                         'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }      

variables['Dphilep1met']  = {   'name': 'Dphilep1met',     
                        'range' : (30,0,3.14),   
                        'xaxis' : '#Delta#phi_{L1, MET}',
                        'fold' : 3
                        }

variables['ptW']  = {   'name': 'ptW',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3
                        }

############# getti ###################
variables['njet_30']  = {
                         'name': 'Sum$(CleanJet_pt>30)',     
                         'range' : (8,0,8),   
                         'xaxis' : 'Number of jets w/ pt>30 GeV',
                         'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                         }

variables['njet_40']  = {
                         'name': 'Sum$(CleanJet_pt>40)',     
                         'range' : (8,0,8),   
                         'xaxis' : 'Number of jets w/ pt>40 GeV',
                         'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                         }

variables['njet_80']  = {
                         'name': 'Sum$(CleanJet_pt>80)',     
                         'range' : (8,0,8),   
                         'xaxis' : 'Number of jets w/ pt>80 GeV',
                         'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                         }

variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (100,0,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt2']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (100,0,300),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jeteta1']  = {
                        'name': 'CleanJet_eta[0]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 1st jet',
                         'fold'  : 3
                        }

variables['jeteta2']  = {
                        'name': 'CleanJet_eta[1]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 2nd jet',
                         'fold'  : 3
                        }

variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : (25,0,2500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :3
                        }

variables['detajj'] = {   'name': 'detajj',            #   variable name    
                            'range' : (80,-1,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                            'fold' : 3
                            # do weighted plot too
                            #'doWeight' : 1,
                            #'binX'     : 6,
                            #'binY'     : 4
                        }

variables['Dphijet1met']  = {   'name': 'Dphijet1met',     
                        'range' : (30,0,3.14),   
                        'xaxis' : '#Delta#phi{J1, MET}',
                        'fold' : 3
                        }

variables['Dphijet2met']  = {   'name': 'Dphijet2met',     
                        'range' : (30,0,3.14),   
                        'xaxis' : '#Delta#phi{J2, MET}',
                        'fold' : 3
                        }

variables['Dphijet1jet2']  = {   'name': 'Dphijet1jet2',     
                        'range' : (30,0,3.14),   
                        'xaxis' : '#Delta#phi{J1, J2}',
                        'fold' : 3
                        }

variables['Dphilep1jet1']  = {   'name': 'Dphilep1jet1',     
                        'range' : (30,0,3.14),   
                        'xaxis' : '#Delta#phi{L1, J1}',
                        'fold' : 3
                        }

variables['Dphilep1jet2']  = {   'name': 'Dphilep1jet2',     
                        'range' : (30,0,3.14),   
                        'xaxis' : '#Delta#phi{L1, J2}',
                        'fold' : 3
                        }

variables['R'] = {   'name': 'R_AN',     
                        'range' : (50,0,1),   
                        'xaxis' : 'R_AN',
                        'fold' : 3
}

#PU
#variables['PV_npvs']      = {   'name': 'PV_npvs',            #   variable name    
#                            'range' : (60,0,60),    #   variable range
#                            'xaxis' : 'nPV',  #   x axis name
#                            'fold' :3
#                        }

#variables['PV_npvsGood']      = {   'name': 'PV_npvsGood',            #   variable name    
#                            'range' : (60,0,60),    #   variable range
#                            'xaxis' : 'PV_npvsGood',  #   x axis name
#                            'fold' :3
#                        }


##control
#variables['ele_trig_eff[0]']      = {   'name': 'ele_trig_eff[0]',            #   variable name    
#                            'range' : (100,0,10),    #   variable range
#                            'xaxis' : 'ele_trig_eff[0]',  #   x axis name
#                            'fold' :3
#                        }

#variables['events']  = {   'name': '1',      
#                        'range' : (1,0,2),  
#                        'xaxis' : 'events', 
#                        'fold' : 3,
#                        'weight': 'btagSF'
#                        }

#variables['Lepton_pt[0]']  = {   'name': 'Lepton_pt[0]',      
#                        'range' : (100,30,3030),  
#                        'xaxis' : 'pt', 
#                        'fold' : 3,
#                        #'weight': 'btagSF'
#                        }

########################3



#variables['nJetsBtag'] = {   'name': 'nJetsBtag',      
#                        'range' : (8, 2, 10),  
#                        'xaxis' : 'N jets btaggable', 
#                        'fold' : 3,
#                        }


#variables['nJetsBtag_btagSF'] = {   'name': 'nJetsBtag',      
#                        'range' : (8, 2, 10),  
#                        'xaxis' : 'N jets btaggable', 
#                        'fold' : 3,
#                        'weight': 'btagSF'
#                        }


#jets 
#variables['nJets'] = {   'name': 'nJets30',      
#                        'range' : (8,2,10),  
#                        'xaxis' : 'nJets cleaned from Ak8 >= 30 GeV', 
#                        'fold' : 3
#                        }

#variables['nJets_btagSF'] = {   'name': 'nJets30',      
#                        'range' : (8,2,10),  
#                        'xaxis' : 'nJets cleaned from Ak8 >= 30 GeV', 
#                        'fold' : 3,
#                         'weight': 'btagSF'
#                        }

# variables['mTi']  = {   'name': 'mTi',
#                         'range' : (40, 20,300),
#                         'xaxis' : 'm_{ll+MET} [GeV]',
#                         'fold' : 0
#                         }

#variables['ptll']  = {   'name': 'ptll',     
#                        'range' : (30, 30,300),   
#                        'xaxis' : 'p_{T}^{ll} [GeV]',
#                        'fold' : 3
#                        }


#variables['pt2']  = {   'name': 'Lepton_pt[1]',     
#                        'range' : (30,10,150),   
#                        'xaxis' : 'p_{T} 2nd lep',
#                        'fold'  : 3 
#                        }



# variables['phi2']  = {  'name': 'Lepton_phi[1]',
#                         'range' : (40,-3.2,3.2),
#                         'xaxis' : '#phi 2nd lep',
#                         'fold'  : 3
#                         }


# variables['PfMetDivSumMet']  = {
#                         'name': 'PfMetDivSumMet',
#                         'range' : (30,0,10),
#                         'xaxis' : 'METsig',
#                         'fold'  : 3
#                         }


# variables['pfmet']  = {
#                         'name': 'MET_pt',
#                         'range' : (40,0,200),
#                         'xaxis' : 'pfmet [GeV]',
#                         'fold'  : 3
#                         }


# variables['Fixedpfmet']  = {
#                         'name': 'METFixEE2017_pt',
#                         'range' : (40,0,300),
#                         'xaxis' : 'Fixedpfmet [GeV]',
#                         'fold'  : 3
#                         }

#variables['mpmet']  = {
#                        'name': 'mpmet',
#                        'range' : (30,20,200),
#                        'xaxis' : 'mpmet [GeV]',
#                        'fold'  : 3
#                        }



# variables['trkMet']  = {   'name': 'TkMET_pt',
#                         'range' : (40,0,200),
#                         'xaxis' : 'trk met [GeV]',
#                          'fold' : 3
#                         }

#variables['dphill']  = {   'name': 'abs(dphill)',     
#                        'range' : (30,0,3.14),   
#                        'xaxis' : '#Delta#phi_{ll}',
#                        'fold' : 3
#                        }

