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
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }      
variables['mTi']  = {   'name': 'mTi',            #   variable name    
                        'range' : ([100,150,200,250,300,350,400,450,500,600,700,1000],),    #   variable range
                        'xaxis' : 'm_{T,i} [GeV]',  #   x axis name
                        'fold' : 3
                        }


variables['mjj']  = {   'name': 'mjj',            #   variable name    
                        'range' : (10,500,3000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['detajj']  = {   'name': 'detajj',            #   variable name    
                           'range' : (10,3.5,8.5),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :0
                           }

variables['mth']  = {   'name': 'mth',            #   variable name    
                        'range' : (20,0,400),    #   variable range
                        'xaxis' : 'm_{TH} [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['mth-DY']  = {   'name': 'mth',            #   variable name    
                        'range' : (10,0,60),    #   variable range
                        'xaxis' : 'm_{TH} [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['ptll']  = {   'name': 'ptll',            #   variable name    
                        'range' : (20,30,400),    #   variable range
                        'xaxis' : 'pT_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (20,50,400),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }
variables['mll-DY']  = {   'name': 'mll',            #   variable name    
                        'range' : (10,40,80),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['Zepp1']  = {   'name': 'Lepton_eta[0]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])',            #   variable name    
                           'range' : (10,-5,5),    #   variable range
                           'xaxis' : 'Zeppenfeld_1',  #   x axis name
                           'fold' :0
                           }

variables['Zepp2']  = {   'name': 'Lepton_eta[1]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])',            #   variable name    
                           'range' : (10,-5,5),    #   variable range
                           'xaxis' : 'Zeppenfeld_2',  #   x axis name
                           'fold' :0
                           }

variables['Zeppll']  = {   'name': 'Zll[0]',            #   variable name    
                           'range' : (10,0,5),    #   variable range
                           'xaxis' : 'Zeppenfeld_ll',  #   x axis name
                           'fold' :0
                           }            

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3
                        }
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3
                        }



variables['eta1']  = {   'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range' : (10,-3.14,3.14),
                        'xaxis' : '#eta 1st lep',
                        'fold' :3
                        }



variables['eta2']  = {   'name': 'Alt$(Lepton_eta[1],-9999.)',
                        'range' : (10,-3.14,3.14),
                        'xaxis' : '#eta 2nd lep',
                        'fold' : 3
                        }


variables['jeteta1'] = {  'name': 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': '#eta 1st jet',
                        'fold' : 3
                        }
variables['jeteta2'] = {  'name': 'Alt$(CleanJet_eta[1],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': '#eta 2nd jet',
                        'fold' : 3
                        }

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',            #   variable name    
                        'range' : (20,0,300),    #   variable range
                        'xaxis' : 'p_{T} 1st jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',            #   variable name    
                        'range' : (20,0,300),    #   variable range
                        'xaxis' : 'p_{T} 2nd jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['jetpt3']  = {   'name': 'Alt$(CleanJet_pt[2],-9999.)',            #   variable name    
                        'range' : (20,0,300),    #   variable range
                        'xaxis' : 'p_{T} 3rd jet [GeV]',  #   x axis name
                        'fold' : 3
                        }


variables['puppiMET_pt']  = {   'name': 'PuppiMET_pt',  
                        'range' : (25,0,250),    #   variable range
                        'xaxis' : 'MET p_{T} [GeV]',  #   x axis name
                        'fold' : 3          
                        }
variables['puppiMET_phi']  = {   'name': 'PuppiMET_phi',  
                        'range' : (20,-3.14,3.14),    #   variable range
                        'xaxis' : 'MET #phi',  #   x axis name
                        'fold' : 3          
                        }


variables['njet']  = {   'name': 'Sum$(CleanJet_pt > 30)',            #   variable name    
                        'range' : (10,0,10),    #   variable range
                        'xaxis' : 'njet',  #   x axis name
                        'fold' : 3
                        }





#--- 2D variables --


variables['MjjVSmTi'] = {   'name': 'mjj:mTi',               
                             'range' : ([100,250,400,600],[500,700,1000,1500,2000],),            #   variable range
                             'xaxis' : 'm_{jj} : m_{Ti}',      #   x axis name
                             'fold' : 3  
                             }

variables['MjjVSmTi_ext']  = {   'name': 'mjj:mTi',            #   variable name    
                        'range' : ([100,250,400,600,1000],[500,700,1000,1300,1600,2000],),    #   variable range
                        'xaxis' : 'mjj:mTi',  #   x axis name
                        'fold' : 3
                        }


