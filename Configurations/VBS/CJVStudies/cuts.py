#cuts
#cuts = {}

supercut= 'abs(std_vector_jet_eta[1])<5 && abs(std_vector_jet_eta[0])<5 \
&& metPfType1 > 30 \
&& std_vector_jet_pt[0]>30 && std_vector_jet_pt[1]>30 \
&& (abs((std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&& (abs((std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&& (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) > 0 \
&& veto_EMTFBug'

JetVeto = '(std_vector_jet_pt[2]<30)'

CentralJetVeto = '\
(std_vector_jet_pt[2]<=30 \
|| (std_vector_jet_pt[2]>30 \
&& std_vector_jet_eta[2] <  \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) \
|| std_vector_jet_eta[2] > \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0]) )) \
'

DynamicJetVeto35mjj = '(std_vector_jet_pt[2] < 0.035 * mjj)'

DynamicCentralJetVeto35mjj = '\
(std_vector_jet_pt[2]<=0.035 * mjj \
|| (std_vector_jet_pt[2]>0.035 * mjj \
&& std_vector_jet_eta[2] <  \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) \
|| std_vector_jet_eta[2] > \
((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0]) )) \
'

cuts['VBS_13TeV_BaseCut']='1'
cuts['JV'] = JetVeto
cuts['CJV'] = CentralJetVeto
cuts['DJV_35mjj'] = DynamicJetVeto35mjj
cuts['DCJV_35mjj'] = DynamicCentralJetVeto35mjj

# 11 = e
# 13 = mu
# 15 = tau


