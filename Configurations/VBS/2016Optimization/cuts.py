# cuts
cuts = {}
#Different supercut used

supercut='\
std_vector_jet_pt[0]>30 && std_vector_jet_pt[1]>30 \
&& veto_EMTFBug \
&& abs(std_vector_jet_eta[1])<5 && abs(std_vector_jet_eta[0])<5 '


#supercut='1'#for test on raw samples


tauVeto = '\
( std_vector_tau_pt[0] < 18 || std_vector_tau_looseIso_dbeta[0] < 1. || (sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[1] < 18 || std_vector_tau_looseIso_dbeta[1] < 1. || (sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[2] < 18 || std_vector_tau_looseIso_dbeta[2] < 1. || (sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[3] < 18 || std_vector_tau_looseIso_dbeta[3] < 1. || (sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[4] < 18 || std_vector_tau_looseIso_dbeta[4] < 1. || (sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[5] < 18 || std_vector_tau_looseIso_dbeta[5] < 1. || (sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) '
            

BVeto = '\
( std_vector_jet_pt[0] < 20 || (std_vector_jet_csvv2ivf[0] < 0.8484 )  ) \
&& ( std_vector_jet_pt[1] < 20 || (std_vector_jet_csvv2ivf[1] < 0.8484 )  ) \
&& ( std_vector_jet_pt[2] < 20 || (std_vector_jet_csvv2ivf[2] < 0.8484 )  ) \
&& ( std_vector_jet_pt[3] < 20 || (std_vector_jet_csvv2ivf[3] < 0.8484 )  ) \
&& ( std_vector_jet_pt[4] < 20 || (std_vector_jet_csvv2ivf[4] < 0.8484 )  ) \
&& ( std_vector_jet_pt[5] < 20 || (std_vector_jet_csvv2ivf[5] < 0.8484 )  ) '

#csvv2ivf combined secondary vertex alghortim. Higher values means a better probability of tagging a b-jet

softMuVeto='\
( std_vector_softMuPt[0] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) )< 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[1] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[2] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[3] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[4] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[5] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) '


bJetVeto = BVeto +'&&'+ softMuVeto
bJetTag  = '(!(' + bJetVeto + '))>=1'  

zveto ='(abs(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) != 11*11 ||(mll>20 && abs(mll - 91) > 15))'


##############################################################################################
## Comparison with table page 90 of Jasper thesis ###########################################


met = 'metPfType1 > 30'
zlep='\
(abs((std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&&(abs((std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) '

#cuts['NoCut']='1' # supercut only
cuts['Met_Z_bJet_MuV_TauV_Zv_mee_All']=met + '&&' +zlep+'&&' +BVeto+'&&'+softMuVeto+'&&'+tauVeto+'&&'+zveto


# 11 = e
# 13 = mu
# 15 = tau
