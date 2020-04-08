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


cuts['sr_em_nocentralveto']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && mth>60 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          &&  centralVeto \
                 '
cuts['sr_em']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && mth>60 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          &&  centralVeto \
                 ' 
cuts['sr_em_highZ']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && mth>60 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          &&  centralVeto \
                          && Zll[0] >= 1 \
                 ' 

cuts['sr_em_lowZ']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && mth>60 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          &&  centralVeto \
                          && Zll[0] < 1 \
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


