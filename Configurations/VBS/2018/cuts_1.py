#Definition of CRs

# Cut for number of leptons, pt leptons, pt jets, mjj and deta jj.
zz = 'nLepton>3 && Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)>10 && Alt$(Lepton_pt[3],0.)>10 && Alt$(Lepton_pt[4],0.)<10 && Alt$(CleanJet_pt[0],-9999.) >50 && Alt$(CleanJet_pt[1],-9999.) >50 && mjj > 500 && abs(detajj) > 2.5' 

# Cut for maz(zl*)
zlep_zz='\
(abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt$(Lepton_eta[2],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
&&(abs((Alt$(Lepton_eta[3],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75)'

# Cut for same flavor in each pair.
#z_flav = '( (abs(Alt$(Lepton_pdgId[0],-9999))==abs(Alt$(Lepton_pdgId[1],-9999)) && abs(Alt$(Lepton_pdgId[2],-9999))==abs(Alt$(Lepton_pdgId[3],-9999)))\
#          || (abs(Alt$(Lepton_pdgId[0],-9999))==abs(Alt$(Lepton_pdgId[2],-9999)) && abs(Alt$(Lepton_pdgId[1],-9999))==abs(Alt$(Lepton_pdgId[3],-9999)))\
#          || (abs(Alt$(Lepton_pdgId[0],-9999))==abs(Alt$(Lepton_pdgId[3],-9999)) && abs(Alt$(Lepton_pdgId[1],-9999))==abs(Alt$(Lepton_pdgId[2],-9999))) )'

#Cut for oposite signe of each pair test without verification of condition (mll-mz).
ztag_zz = '((((Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) <0) &&  (Alt$(Lepton_pdgId[2],-9999) * Alt$(Lepton_pdgId[3],-9999) <0)) \
          || ((Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[2],-9999) <0) &&  (Alt$(Lepton_pdgId[1],-9999) * Alt$(Lepton_pdgId[3],-9999) <0))\
          || ((Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[3],-9999) <0)  && (Alt$(Lepton_pdgId[1],-9999) * Alt$(Lepton_pdgId[2],-9999) <0)))'

#Cut for oposite signe of each pair and selection for |mll-mz|<15
#ztag_zz = '((abs(Alt$(Lepton_pdgId[0],-9999)) + abs(Alt$(Lepton_pdgId[1],-9999)) + abs(Alt$(Lepton_pdgId[2],-9999)) + abs(Alt$(Lepton_pdgId[3],-9999))) == 0 \
#          && ( (abs(m01 - 91) < 15 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) <0) && (abs(m23 - 91) < 15) && (Alt$(Lepton_pdgId[2],-9999) * Alt$(Lepton_pdgId[3],-9999) <0))  \
#          || (abs(m02 - 91) < 15 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[2],-9999) <0) && (abs(m13 - 91) < 15) && (Alt$(Lepton_pdgId[1],-9999) * Alt$(Lepton_pdgId[3],-9999) <0))\
#          || (abs(m03 - 91) < 15 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[3],-9999) <0) && (abs(m12 - 91) < 15) && (Alt$(Lepton_pdgId[1],-9999) * Alt$(Lepton_pdgId[2],-9999) <0)) )'


#Definition of ZZ LOOSE Region

#Cuts for number of leptons, and pt leptons.
loose_zz = 'nLepton>3 && Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)>10 && Alt$(Lepton_pt[3],0.)>10 && Alt$(Lepton_pt[4],0.)<10'

# We need to apply the same cut for same flavor z_flav.

#Cut for oposite signe of each pair and selection for |mll-mz|<30
#ztag_zz_loose = '((abs(Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999) + Alt$(Lepton_pdgId[2],-9999) + Alt$(Lepton_pdgId[3],-9999)) == 0 \
#          && ((abs(m01 - 91) < 30 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) <0) && (abs(m23 - 91) < 30) && (Alt$(Lepton_pdgId[2],-9999) * Alt$(Lepton_pdgId[3],-9999) <0))  \
#          || ((abs(m02 - 91) < 30 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[2],-9999) <0) && (abs(m13 - 91) < 30) && (Alt$(Lepton_pdgId[1],-9999) * Alt$(Lepton_pdgId[3],-9999) <0))\
#          || ((abs(m03 - 91) < 30 && (Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[3],-9999) <0) && (abs(m12 - 91) < 30) && (Alt$(Lepton_pdgId[1],-9999) * Alt$(Lepton_pdgId[2],-9999) <0))))'

#cut for zerojet, we will apply it in the Loose Region.

Zeroj = 'Alt$(CleanJet_pt[0], 0) > 30.'

# Cuts for ZZCR

#cuts['ZZCR']= zz+'&&'+zlep_zz+'&&'+z_flav+'&&'+ztag_zz
cuts['ZZCR']= zz+'&&'+zlep_zz+'&&'+ztag_zz#+'&&'+z_flav
#Cuts for ZZLOOSE

cuts['LOOSEZZ']=loose_zz+'&&'+ztag_zz#+'&&'+z_flav
cuts['LOOSEZZ_Not_0jet']=Zeroj+'&&'+loose_zz+'&&'+ztag_zz#+'&&'+z_flav
