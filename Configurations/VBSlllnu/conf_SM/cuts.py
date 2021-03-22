# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

## Signal regions

supercut='nLepton>2 && \
          (abs(Alt$(Lepton_pdgId[0],9999))==11 && abs(Alt$(Lepton_pdgId[1],9999))==11 && abs(Alt$(Lepton_pdgId[2],9999))==13)  || \
          (abs(Alt$(Lepton_pdgId[0],9999))==13 && abs(Alt$(Lepton_pdgId[1],9999))==11 && abs(Alt$(Lepton_pdgId[2],9999))==11) || \
          (abs(Alt$(Lepton_pdgId[0],9999))==11 && abs(Alt$(Lepton_pdgId[1],9999))==13 && abs(Alt$(Lepton_pdgId[2],9999))==11)'

cuts['WZ_ee_mu'] = 'mll>60'


