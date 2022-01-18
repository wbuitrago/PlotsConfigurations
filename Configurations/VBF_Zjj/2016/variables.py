# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

#gROOT.ProcessLineSync('.L m4l.C+')
#gROOT.ProcessLineSync('.L mucca.C+')
#gROOT.ProcessLineSync('initMyReader()')

variables['events']   = {   'name': '1',
                            'range' : (1,0,2),
                            'xaxis' : 'events',
                            'fold' : 3
                        }

variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : ([500., 750., 1000., 1500., 2000., 4000.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :3
                        }



variables['ptll']  = {   'name': 'ptll',
                        'range' : (30, 0,200),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 3
                        }


variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }

variables['detajj']  = {  'name': 'detajj',
                        'range' : (32,0,8.0),
                        'xaxis' : '#Delta_{#eta} jets',
                        'fold'  : 3
                        }



