# variables

#variables = {}
'''
variables['VARIABLE']  = {  
          'name': 'expression',        # variable expression as one would use in TTree::Draw. Also 2D expression works e.g. var1:var2    
          'range' : range:             # anything that a TH1 can digest van be put here: 
                                       # a 3-valued tuple is interpreted as (nbins, xmin, xmax).
                                       # a 6-valued tuple is interpreted as (nbinsx, xmin, xmax, nbinsy, ymin, ymax)
                                       # a ([list]) is interpreted as a vector of bin edges
                                       # a ([list],[list],) is interpreted as a 2D vector of bin edges (mind the comma before the closing ")")
          'xaxis' : 'DR_{ll}',         # x axis name, human readable name, what goes into h->GetXaxis()->SetTitle()
          'fold' : NUMBER,             # 0 -> no underflow/overflow folding. 1 -> fold underflow in the first bin. 2-> fold overflow in the last bin. 3 -> fold both underflow and overflow.
          'divideByBinWidth': VALUE,   #OPTIONAL, whether to divide (1) or not (0) the bin content by the bin width (for variable bin size histograms). Default is 0
} 
'''
#                    
variables['Mll']  = {       'name': 'mll',             
                            'range' : (10,50,200),  
                            'xaxis' : 'm_{ll} [GeV]', 
                        }


variables['ptll']    = {    'name': 'ptll',               
                            'range' : (20,0,200),   
                            'xaxis' : 'pt_{ll} [GeV]', 
                        }
variables['Mjj']  = {       'name': 'mjj',            
                            'range' : ([500,700,900,1100,1300,1500,2000],),  
                            'xaxis' : 'm_{jj} [GeV]',  
                        }


variables['mth']  = {   'name': 'mth',              
                        'range' : (20,0,400),    
                        'xaxis' : 'm_{T}^{H} [GeV]', 
                        }
variables['mTi']  = {   'name': 'mTi',                
                        'range' : ([100,150,200,250,300,350,400,500,700],),   
                        'xaxis' : 'm_{Ti} [GeV]',  
                        }
variables['detajj']  = {   'name': 'abs(detajj)',
                            'range' : (6,3.5,6.5),
                        '    xaxis' : '#Delta#eta_{jj}',

                        }
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep'
                        }


variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 2nd lep'
                        }
variables['eta1']  = {   'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 1st lep'
                        }


variables['eta2']  = {   'name': 'Alt$(Lepton_eta[1],-9999.)',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 2nd lep'
                        }


variables['jeteta1'] = {  'name': 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'eta_{j1}',
                        }

variables['jeteta2'] = {         'name': 'Alt$(CleanJet_eta[1],-9999.)',
                               'range': (20,-5,5),
                               'xaxis': 'eta_{j2}',

                               }


variables['Zlep1']  = {  'name': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.,1.),
                         'xaxis': 'Z^{lep}_{1}',
                         }

variables['Zlep2']  = {  'name': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.,1.),
                         'xaxis': 'Z^{lep}_{2}',
                         }
variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                            'range' : ([30,50,70,90,110,130,150,190,230,300],),  
                           'xaxis' : 'p_{T} 1st jet'
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                            'range' : ([30,50,70,90,110,130,150,190,230,300],),  
                           'xaxis' : 'p_{T} 2nd jet'
                           }

variables['met']  = {   'name': 'MET_pt',            
                        'range' : (50,0,250),    
                        'xaxis' : 'MET [GeV]', 
                        }
variables['nJet']  = {   'name': 'Sum$(CleanJet_pt>30)',
                         'range' : (4,0,4),
                         'xaxis' : 'njets'
                         }
variables['my_btag_var']  = {   'name'  : '(fabs(CleanJet_eta[0]) <= fabs(CleanJet_eta[1])) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(CleanJet_eta[0]) > fabs(CleanJet_eta[1])) * Jet_btagDeepB[CleanJet_jetIdx[1]]',
                                'range' : (10,0,1),        
                                'xaxis' : 'central_jet_btag_var'
                            }

#--- 2D variables --


variables['MjjVSmTi'] = {   'name': 'mjj:mTi',               
                             'range' : ([100,250,400,600],[500,700,1000,1500,2000],),            #   variable range
                             'xaxis' : 'm_{jj} : m_{Ti}',      #   x axis name
                             'binX'     : 3,
                             'binY'     : 4
                          
                             }
variables['MjjVSdeatjj'] = {   'name': 'mjj:detajj',            #   variable name    
                             'range' : ([3.5,4.5,5.5,6.5],[500,700,1000,1500,2000],),            #   variable range
                             'xaxis' : 'm_{jj}:#Delta#eta_{jj}',      #   x axis name
                             'binX'     : 3,
                             'binY'     : 4
                            
                             }
variables['MjjVSjetpt1'] = {   'name': 'mjj:Alt$(CleanJet_pt[0],-9999.)',            #   variable name    
                             'range' : ([30,70,110,150,200,300],[500,700,1000,1500,2000],),            #   variable range
                             'xaxis' : 'm_{jj}:p_{T_{jet1}}',      #   x axis name
                             'binX'     : 5,
                             'binY'     : 4
                            
                             }
variables['MjjVSZlep1'] = {   'name': 'mjj:(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj',        
                             'range' : ([-1,-0.5,0,0.5,1],[500,700,1000,1500,2000]),            #   variable range
                             'xaxis' : 'm_{jj}:Zepp_{lep1}',      #   x axis name
                             'binX'     : 4,
                             'binY'     : 4
                            
                             }

