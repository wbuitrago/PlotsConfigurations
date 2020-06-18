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

variables['mjj']  = {   'name': 'mjj',            #   variable name    
                        'range' : (10,500,3000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        } 

variables['ptll']  = {   'name': 'ptll',            #   variable name    
                        'range' : (10,30,450),    #   variable range
                        'xaxis' : 'pT_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }
variables['ptll_var']  = {   'name': 'ptll',            #   variable name    
                        'range' : ([30,70,110,150,250,350,450],),    #   variable range
                        'xaxis' : 'pT_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (10,50,350),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }
variables['mllSF']  = {   'name': 'mll',            #   variable name    
                        'range' : (10,120,350),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (10,30.,200),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3
                        }
variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (10,30.,200),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3
                        }
variables['detall']  = {  'name' : 'fabs(Alt$(Lepton_eta[0],-9999.)-Alt$(Lepton_eta[1],9999.))',
                          'range': (4,0.0,4.0),
                          'xaxis': 'deta ll',
                          'fold' : 3
                          } 
#--- 2D variables --




variables['mjjVSmTi']  = {   'name': 'mjj:mTi',            #   variable name    
                        'range' : ([100,250,400,600,1000],[500,700,1000,1300,1600,2000],),    #   variable range
                        'xaxis' : 'mjj:mTi',  #   x axis name
                        'fold' :3
                        }
variables['mjjVSmll']  = {   'name': 'mjj:mll',            #   variable name    
                        'range' : ([50,150,250,350],[500,700,1000,1300,1600,2000],),    #   variable range
                        'xaxis' : 'mjj:mTi',  #   x axis name
                        'fold' :3
                        }


