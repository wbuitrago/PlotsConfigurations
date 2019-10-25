# variables

variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

#20 Fixed Bin
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
#variables['pt1_20_25_350']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (20,25,350),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
##10 Fixed Bin
#variables['pt1_10_25_200']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (10,25,200),
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
#variables['pt1_10_25_350']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (10,25,350),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
##30 Fixed Bin 
#variables['pt1_30_25_200']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (30,25,200),
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
#variables['pt1_30_25_350']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (30,25,350),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       } 
##40 Fixed Bin 
#variables['pt1_40_25_200']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (40,25,200),
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
#variables['pt1_40_25_350']  = {   'name': 'std_vector_lepton_pt[0]',
#                       'range' : (40,25,350),
#                       'xaxis' : 'p_{T} 1st lep',
#                       'fold'  : 3
#                       }
#                       
## Variable RecoBin width GenBin: [60 , 90, 150]
## RecoBin: [25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 350]
##1st Gen Bin 35  RecoBin: [#######,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 350]		
#
#variables['pt1_1st_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,62,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 260, 300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#variables['pt1_1st_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,26,27,28,29,30,32,34,36,38,40,44,48,52,56,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 260, 300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#variables['pt1_1st_Gen_v3']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,28,31,34,37,40,44,48,52,56,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 260, 300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#                      
## Variable RecoBin width
##2ndt Gen Bin 35->50  RecoBin: [25,30,35,40 ,45 , 50, 55,##############,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 350]
#
#variables['pt1_2nd_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,30,35,40 ,45 , 50, 55,57,59,61,63,65,67,69,71,73,75,80,85,90,95,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 260, 300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#variables['pt1_2nd_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,30,35,40 ,45 , 50, 55,58,61,64,67,70,73,76,79,82,85,88,91,96,100,106,112,118,124,130 , 140, 150 ,160, 180, 220,260, 300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }             
## Variable RecoBin width
##3rd Gen Bin 90->150  RecoBin: [25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,############# ,160, 180, 220, 350]
#
#variables['pt1_3rd_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,95,100,105,110,115,120,130,140,150,160, 180, 220, 260, 300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#variables['pt1_3rd_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,110,135,150,165, 180, 220,260, 300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
## Variable RecoBin width
##4th Gen Bin 150  RecoBin: [25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,160, 180, 220, 350]
#
#variables['pt1_4th_Gen_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150 ,155,160,165,170,175,180,185,190,195,200,210,220,230,240,250,260,280,300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#variables['pt1_4th_Gen_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,30,35,40 ,45 , 50, 55,60,65,70,75,80,85,90,100,106,112,118,124,130 , 140, 150,165,180,195,210,225,240,260,280,300],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#x=175/40
#y=225/40
#
#variables['pt1_4Gen_Test_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,61,62,63,65,67,69,71,73,75,80,80+1*x,80+2*x,90+1*x, 90+2*x, 90+3*x, 90+4*x, 90+5*x, 90+6*x, 90+7*x, 90+8*x, 90+9*x, 90+10*x, 90+11*x, 90+12*x, 90+13*x, 90+14*x,150+1*y, 150+2*y, 150+3*y, 150+4*y, 150+5*y, 150+6*y, 150+7*y, 150+8*y, 150+9*y, 150+10*y, 150+11*y, 150+12*y, 150+13*y, 150+14*y, 150+15*y, 150+16*y, 150+17*y, 150+18*y],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#
#variables['pt1_4Gen_Test_v3']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,61,62,63,65,67,69,71,73,75,80,80+1*x, 80+2*x, 80+3*x, 80+4*x, 80+5*x, 80+6*x, 80+7*x, 80+8*x, 80+9*x, 80+10*x, 80+11*x, 80+12*x, 80+13*x, 80+14*x,140+1*y, 140+2*y, 140+3*y, 140+4*y, 140+5*y, 140+6*y, 140+7*y, 140+8*y, 140+9*y, 140+10*y, 140+11*y, 140+12*y, 140+13*y, 140+14*y, 140+15*y, 140+16*y, 140+17*y, 140+18*y, 140+19*y, 140+20*y],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      } 
#
#variables['pt1_4Gen_App_v1']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,61,62,63,65,67,69,71,73,75,80, 84.5, 88.8, 93.0, 97.5, 102.0, 106.3, 110.5, 115.0, 119.5, 123.8, 128.0, 132.5, 137.0, 141.3,145.5, 151.3, 157.0, 162.5, 168.0, 173.8, 179.5, 185.0, 190.5, 196.3, 202.0, 207.5, 213.0, 218.8, 224.5, 230.0, 235.5, 241.3, 247.0, 252.5],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#variables['pt1_4Gen_App_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,61, 64.5, 69.0, 73.5, 78.0,81,84.5, 89.0, 93.5, 98.0, 102.5, 107.0, 111.5, 116.0, 120.5, 125.0, 129.5, 134.0, 138.5, 143.0,145.5, 151.0, 156.5, 162.0, 167.5, 173.0, 178.5, 184.0, 189.5, 195.0, 200.5, 206.0, 211.5, 217.0, 222.5, 228.0, 233.5, 239.0, 244.5, 250.0],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#variables['pt1_4Gen_Final']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,61,69.8, 78.5, 87.3, 96.0, 104.8, 113.5, 122.3, 131.0, 139.8, 148.5, 157.3, 166.0, 174.8, 183.5, 192.3, 200],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#variables['pt1_4Gen_Final_v2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,30,35,40,45,50,55,60,70,80,90,100, 110,120,130,140,150,160,170,180,190,200],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                     }
#variables['pt1_4Gen_Test_new']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,61,64.5, 69.0, 73.5, 78.0, 82.5, 87.0, 91.5, 96.0, 100.5, 105.0, 109.5, 114.0, 118.5, 123.0, 127.5, 132.0, 136.5, 141.0, 146.5, 152.0, 157.5, 163.0, 168.5, 174.0, 179.5, 185.0, 190.5, 196.0, 201.5, 207.0, 212.5, 218.0, 223.5, 229.0, 234.5, 240.0, 245.5, 251.0],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }
#
#
#variables['pt1_4Gen_Test_2']  = {   'name': 'std_vector_lepton_pt[0]',
#                      'range' : ([25,27,29,31,33,35,37,39,41,44,47,50,54,58,61,62,63,65,67,69,71,73,75,80,85,90,90+1*x, 90+2*x, 90+3*x, 90+4*x, 90+5*x, 90+6*x, 90+7*x, 90+8*x, 90+9*x, 90+10*x, 90+11*x, 90+12*x,
#90+13*x, 90+14*x,150+1*y, 150+2*y, 150+3*y, 150+4*y, 150+5*y, 150+6*y, 150+7*y, 150+8*y, 150+9*y],),
#                      'xaxis' : 'p_{T} 1st lep',
#                      'fold'  : 3
#                      }


variables['pt1_4Gen_Final_v2']  = {   'name': 'std_vector_lepton_pt[0]',
                      'range' : ([25,33,41,49,57,65,73,81,90,100,108,116,124,132,140,148,156,164,172,180,188,196,204],),
                      'xaxis' : 'p_{T} 1st lep',
                      'fold'  : 3
			}

variables['pt1_4Gen_Final_v3']  = {   'name': 'std_vector_lepton_pt[0]',
                      'range' : ([25,35,45,55,65,75,85,100,120,140,160,180,200],),
                      'xaxis' : 'p_{T} 1st lep',
                      'fold'  : 3
                        }

variables['pt1_4Gen_Final_v4']  = {   'name': 'std_vector_lepton_pt[0]',
                      'range' : (15,25,200),
                      'xaxis' : 'p_{T} 1st lep',
                      'fold'  : 3
                        }
