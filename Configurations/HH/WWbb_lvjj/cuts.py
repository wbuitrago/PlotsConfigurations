cuts = {}
  
supercut = 'Lepton_pt[0] >= 25 && CleanJet_pt[1] >= 25 && (H_jets[1]!=-1 && W_jets_nearest_massWZ[1]!=-1)'
cuts["no_cut"] = '1.'

######################################
### CUT ON BDT CLASSIFIER: >= -0.4 ###
######################################
cuts["BDT_m0.4"] = 'BDT_var(mjj_b, deltaR_lep_wjet, deltaR_b, deltaphi_lep_wjet_high, deltaR_lep_b, deltaphi_lep_b_high,b_pt_high, deltaeta_b, deltaphi_lep_b_low)>=-0.4'

