# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

#gROOT.ProcessLineSync('.L m4l.C+')
#gROOT.ProcessLineSync('.L mucca.C+')
#gROOT.ProcessLineSync('initMyReader()')



# to fit



#variables['detajjmjj'] = {   'name': 'mjj:detajj',            #   variable name    
                            #'range' : ([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],[200., 500., 750., 1000., 1500., 2000., 3000., 5000.],),    #   variable range
                            #'xaxis' : 'm_{jj} [GeV] : #Delta#eta_{jj}',  #   x axis name
                            #'fold' :3 ,
                            ## do weighted plot too
                            #'doWeight' : 1,
                            #'binX'     : 6,
                            #'binY'     : 7
                        #}


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






