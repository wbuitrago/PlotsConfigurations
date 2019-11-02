# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

# variables['events']  = {   'name': '1',
# 'range' : (1,0,2),
# 'xaxis' : 'events',
# 'fold' : 3
# }

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : ([30, 55, 90, 130, 180, 250],),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }
