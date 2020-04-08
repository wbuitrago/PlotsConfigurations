# cuts


#cuts = {}
    
supercut = 'mll>50  \
            && ptll > 30 \
            && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && PuppiMET_pt>20 \
           '



cuts['top_me']  =              'mjj>500 \
                               && detajj > 3.5 \
                               && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                               && ((zeroJet && !bVeto) || bReq) \
'

cuts['DYtt']  =  'mjj>500 \
                  && detajj > 3.5 \
                  && mth<60 \
                  && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                  && mll>40 && mll<80 \
                  && bVeto\
'


