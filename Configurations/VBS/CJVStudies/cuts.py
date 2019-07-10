#cuts
#cuts = {}

#supercut = '1'

supercut= 'abs(std_vector_jet_eta[1])<5 && abs(std_vector_jet_eta[0])<5 \
&& metPfType1 > 30 \
&& std_vector_jet_pt[0]>30 && std_vector_jet_pt[1]>30 \
&& (abs((std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&& (abs((std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&& (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) > 0 \
&& veto_EMTFBug'

JetVeto = '(std_vector_jet_pt[2]<27.6)'

CentralJetVeto = '\
(std_vector_jet_pt[2]<27 \
|| (std_vector_jet_pt[2]>=27 \
&& std_vector_jet_eta[2] <  \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) \
|| std_vector_jet_eta[2] > \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0]) )) \
'

DynamicJetVeto = '(std_vector_jet_pt[2] < 0.0342 * mjj)'

DynamicCentralJetVeto = '\
(std_vector_jet_pt[2]<0.038 * mjj \
|| (std_vector_jet_pt[2]>=0.038 * mjj \
&& std_vector_jet_eta[2] <  \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) \
|| std_vector_jet_eta[2] > \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0]) )) \
'

cuts['VBS_13TeV_BaseCut']='1'
cuts['JV'] = JetVeto
cuts['CJV'] = CentralJetVeto
cuts['DJV'] = DynamicJetVeto
cuts['DCJV'] = DynamicCentralJetVeto

# 11 = e
# 13 = mu
# 15 = tau


