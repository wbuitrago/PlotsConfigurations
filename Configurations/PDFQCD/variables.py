# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow


for ipdf in range(0,10):
  variables['weight_' + str(ipdf)]  = {   'name': 'std_vector_LHE_weight[' + str(ipdf) +'] / std_vector_LHE_weight[0]',    
                                           'range' : (100,0,2),  
                                           'xaxis' : 'weight ' + str(ipdf),
                                           'fold'  : 3                        
                                           }
    
   