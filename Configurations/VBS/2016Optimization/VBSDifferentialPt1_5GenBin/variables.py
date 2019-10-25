# variables tested

variables = {}
#    
##'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#
##20 Fixed Bin
#variables['pt1_20_25_200']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (20,25,200),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#                       
#variables['pt1_20_25_250']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (20,25,250),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_20_25_300']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (20,25,300),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }        
#
##10 Fixed Bin
#variables['pt1_10_25_200']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (10,25,250),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }  
#variables['pt1_10_25_250']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (10,25,250),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_10_25_300']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (10,25,300),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }                          
#
##30 Fixed Bin 
#variables['pt1_30_25_200']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (30,25,250),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }  
#variables['pt1_30_25_250']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (30,25,250),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_30_25_300']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (30,25,300),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       } 
##40 Fixed Bin 
#variables['pt1_40_25_200']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (40,25,250),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }  
#variables['pt1_40_25_250']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (40,25,250),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_40_25_300']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (40,25,300),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       } 
#
## Variable RecoBin width 
##1st Gen Bin 75  RecoBin: [25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 300]		
#
#variables['pt1_1st_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,27,29,31,33,35,38,41,44,47,50,55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_1st_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,31,32,33,34,35,36,37,38,39,40,44,48,52,56,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#                       
#
#
## Variable RecoBin width
##2ndt Gen Bin 75->95  RecoBin: [25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 300]
#
#variables['pt1_2nd_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,95,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_2nd_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,84, 88, 92, 96, 100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#
## Variable RecoBin width
##3rd Gen Bin 95->125  RecoBin: [25,30,35,40 ,45, 50,55,60,65,70,77.5,85,92.5,100,107.5,115,122.5,#################]
#
#variables['pt1_3rd_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,95,98,102,106,110,115,120,125,130 , 140, 150 ,160, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_3rd_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,95,105,115,125,130 , 140, 150 ,160, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
# # Variable RecoBin width
##4th Gen Bin 125->165  RecoBin: [25,30,35,40 ,45, 50,55,60,65,70,77.5,85,92.5,100,107.5,115,122.5,#################]
#
#variables['pt1_4th_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,125,130,135,140,145,150,165, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_4th_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130,138,146,154,165, 180, 220, 300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }                      
#
# # Variable RecoBin width
##5th Gen Bin 125->165  RecoBin: [25,30,35,40 ,45, 50,55,60,65,70,77.5,85,92.5,100,107.5,115,122.5,#################]
#
#variables['pt1_5th_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,165,175,185,200,220,240,260,300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#
#variables['pt1_5th_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,140,155,170,200,230,260,300],),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       } 


x=175/40
variables['pt1_5th_Gen_Test']  = {   'name': 'std_vector_lepton_pt[0]',
                       'range' : ([25, 25+1*x, 25+2*x, 25+3*x, 25+4*x, 25+5*x, 25+6*x, 25+7*x, 25+8*x, 25+9*x, 25+10*x, 25+11*x, 25+12*x,80,85,90,95,98,102,106,110,115,120, 125, 125+1*x, 125+2*x, 125+3*x, 125+4*x, 125+5*x, 125+6*x, 125+7*x, 125+8*x, 125+9*x, 125+10*x, 125+11*x, 125+12*x, 125+13*x, 125+14*x, 125+15*x, 125+16*x, 125+17*x, 125+18*x, 125+19*x, 125+20*x, 125+21*x, 125+22*x, 125+23*x, 125+24*x, 125+25*x, 125+26*x, 125+27*x, 125+28*x, 125+29*x],),
                       'xaxis' : 'p_{T} 1st lep',
                       'fold'  : 3
                       }

variables['pt1_5th_Gen_Test_App']  = {   'name': 'std_vector_lepton_pt[0]',
                       'range' : ([25,29.5, 34.0, 38.5, 43.0, 47.5, 52.0, 56.5, 61.0, 65.5, 70.0, 74.5, 79.0, 83.5,85,90,95,98,102,106,110,115,120, 125, 129.5, 134.0, 138.5, 143.0, 147.5, 152.0, 156.5, 161.0, 165.5, 170.0, 174.5, 179.0, 183.5, 188.0, 192.5, 197.0, 201.5, 206.0, 210.5, 215.0, 219.5, 224.0, 228.5, 233.0, 237.5, 242.0, 246.5, 251.0],),
                       'xaxis' : 'p_{T} 1st lep',
                       'fold'  : 3
                       } 

variables['pt1_5th_Gen_Final']  = {   'name': 'std_vector_lepton_pt[0]',
                       'range' : (15, 25 , 200),
                       'xaxis' : 'p_{T} 1st lep',
                       'fold'  : 3                                                                                                             }
