#ifndef FUNCTIONS_HH
#define FUNCTIONS_HH

#include "TMath.h"
#include "Math/Vector4D.h"
#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"

using namespace ROOT::VecOps;
using namespace std;
#include "TLorentzVector.h"

bool wz(int nLepton, RVec<float> & Lepton_pt, RVec<float> & Lepton_eta,RVec<float> & Lepton_phi,
                RVec<int> & Lepton_pdgId, RVec<int> & Lepton_electronIdx, RVec<int> & Lepton_muonIdx,RVec<float> & Muon_mass,RVec<float> & Electron_mass)
{
    if (nLepton<3) return false;
    if (nLepton>3){
        if (Lepton_pt.at(3)>10)
            return false;
    }
    unsigned nL=nLepton;
    std::vector<unsigned> iPromptL{};
    iPromptL.reserve(nLepton);

    for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId.at(iL)))};
    if (absId != 11 && absId != 13)
        continue;
        iPromptL.push_back(iL);
    }

    for(int i=0; i<3; i++){
      if (!((abs(Lepton_pdgId.at(iPromptL[i])) == 11 && abs(Lepton_eta.at(iPromptL[i])) < 2.4) || (abs(Lepton_pdgId.at(iPromptL[i])) == 13 && abs(Lepton_eta.at(iPromptL[i])) < 2.5))){
        return false;
      }
    }

  if ((Lepton_pdgId.at(iPromptL[0])+ Lepton_pdgId.at(iPromptL[1]) != 0)&&(Lepton_pdgId.at(iPromptL[0])+ Lepton_pdgId.at(iPromptL[2]) != 0)&&(Lepton_pdgId.at(iPromptL[1])+ Lepton_pdgId.at(iPromptL[2]) != 0))
    return 0.;

  double lepton_mass0;
  double lepton_mass1;
  double lepton_mass2;

  if (abs(Lepton_pdgId.at(iPromptL[0]))==13){
    lepton_mass0=Muon_mass.at(Lepton_muonIdx.at(iPromptL[0]));
  }else{
    lepton_mass0=Electron_mass.at(Lepton_electronIdx.at(iPromptL[0]));
  }

  if (abs(Lepton_pdgId.at(iPromptL[1]))==13){
    lepton_mass1=Muon_mass.at(Lepton_muonIdx.at(iPromptL[1]));
  }else{
    lepton_mass1=Electron_mass.at(Lepton_electronIdx.at(iPromptL[1]));
  }

  if (abs(Lepton_pdgId.at(iPromptL[2]))==13){
    lepton_mass2=Muon_mass.at(Lepton_muonIdx.at(iPromptL[2]));
  }else{
    lepton_mass2=Electron_mass.at(Lepton_electronIdx.at(iPromptL[2]));
  }

    TLorentzVector pl0,pl1,pl2;
    pl0.SetPtEtaPhiM(Lepton_pt.at(iPromptL[0]),
                    Lepton_eta.at(iPromptL[0]),
                    Lepton_phi.at(iPromptL[0]),
                    lepton_mass0);
    pl1.SetPtEtaPhiM(Lepton_pt.at(iPromptL[1]),
                    Lepton_eta.at(iPromptL[1]),
                    Lepton_phi.at(iPromptL[1]),
                    lepton_mass1);
    pl2.SetPtEtaPhiM(Lepton_pt.at(iPromptL[2]),
                    Lepton_eta.at(iPromptL[2]),
                    Lepton_phi.at(iPromptL[2]),
                    lepton_mass2);
    TLorentzVector plll,pl0l1,pl0l2,pl1l2;
    plll=pl0 + pl1 + pl2;
    pl0l1=pl0 + pl1;
    pl0l2=pl0 + pl2;
    pl1l2=pl1 + pl2;
    TLorentzVector pl[]={pl0,pl1,pl2};
    int zlepton1_idx=0;
    int zlepton2_idx=1;
    int wlepton_idx=2;
    double zMass_min=-999999;
    for (int i=0; i<2;i++){
    for (int j=i+1; j<3;j++){
        if (Lepton_pdgId.at(iPromptL[i])+Lepton_pdgId.at(iPromptL[j])==0){
            if(abs((pl[i]+pl[j]).M()-91.1876)<abs(zMass_min-91.1876)){
                zMass_min=(pl[i]+pl[j]).M();
                zlepton1_idx=i;
                zlepton2_idx=j;
                wlepton_idx=3-i-j;
            }
        }
    }
    }
    if (!(Lepton_pt.at(iPromptL[zlepton1_idx])>25 && Lepton_pt.at(iPromptL[zlepton2_idx])>10 && Lepton_pt.at(iPromptL[wlepton_idx])>20)){
    return false;
    }
    if (abs(zMass_min-91.1876)>15){
    return false;
    }

    if (!((Lepton_pdgId.at(iPromptL[0])*Lepton_pdgId.at(iPromptL[1])>0||pl0l1.M()>4) && (Lepton_pdgId.at(iPromptL[0])*Lepton_pdgId.at(iPromptL[2])>0||pl0l2.M()>4) && (Lepton_pdgId.at(iPromptL[1])*Lepton_pdgId.at(iPromptL[2])>0||pl1l2.M()>4)))
    return false;

    if (plll.M() <= 100.)
    return false;

    return true;
}

float drjll(int nLepton, RVec<float> & Lepton_pt, RVec<float> & Lepton_eta,RVec<float> & Lepton_phi, RVec<int> & Lepton_pdgId,
            int nCleanJet, RVec<float> & CleanJet_pt, RVec<float> & CleanJet_eta,RVec<float> & CleanJet_phi, RVec<int> & CleanJet_jetIdx,RVec<float> & Jet_mass,int idx){
            if (nLepton<2) return -9999.;
            if (nCleanJet<0) return -9999.;

            double lepton_mass0;
            double lepton_mass1;
            if (abs(Lepton_pdgId.at(0))==13){
            lepton_mass0=0.1057128;
            }else{
            lepton_mass0=0.000511;
            }
            if (abs(Lepton_pdgId.at(1))==13){
            lepton_mass1=0.1057128;
            }else{
            lepton_mass1=0.000511;
            }

            TLorentzVector pl0,pl1,jet;
            pl0.SetPtEtaPhiM(Lepton_pt.at(0),
                            Lepton_eta.at(0),
                            Lepton_phi.at(0),
                            lepton_mass0);
            pl1.SetPtEtaPhiM(Lepton_pt.at(1),
                            Lepton_eta.at(1),
                            Lepton_phi.at(1),
                            lepton_mass1);
            jet.SetPtEtaPhiM(CleanJet_pt[idx],
                            CleanJet_eta[idx],
                            CleanJet_phi[idx],
                            Jet_mass[CleanJet_jetIdx[idx]]);
            TLorentzVector pll;
            pll=pl0+pl1;
            return jet.DeltaR(pll);
            }

float drjll(int nLepton, RVec<float> & Lepton_pt, RVec<float> & Lepton_eta,RVec<float> & Lepton_phi, RVec<int> & Lepton_pdgId,
            int nCleanJet, RVec<float> & CleanJet_pt, RVec<float> & CleanJet_eta,RVec<float> & CleanJet_phi, RVec<int> & CleanJet_jetIdx,RVec<float> & Jet_mass,int idx){
            if (nLepton<2) return -9999.;
            if (nCleanJet<0) return -9999.;

            double lepton_mass0;
            double lepton_mass1;
            if (abs(Lepton_pdgId.at(0))==13){
            lepton_mass0=0.1057128;
            }else{
            lepton_mass0=0.000511;
            }
            if (abs(Lepton_pdgId.at(1))==13){
            lepton_mass1=0.1057128;
            }else{
            lepton_mass1=0.000511;
            }

            TLorentzVector pl0,pl1,jet;
            pl0.SetPtEtaPhiM(Lepton_pt.at(0),
                            Lepton_eta.at(0),
                            Lepton_phi.at(0),
                            lepton_mass0);
            pl1.SetPtEtaPhiM(Lepton_pt.at(1),
                            Lepton_eta.at(1),
                            Lepton_phi.at(1),
                            lepton_mass1);
            jet.SetPtEtaPhiM(CleanJet_pt[idx],
                            CleanJet_eta[idx],
                            CleanJet_phi[idx],
                            Jet_mass[CleanJet_jetIdx[idx]]);
            TLorentzVector pll;
            pll=pl0+pl1;
            return jet.DeltaR(pll);
            }
float jet1_pt(int nCleanJet, RVec<float> & CleanJet_pt, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<1) return -9999.;
    float jet1_pt=-9999.;
    // year: 2016:0; 2017:1; 2018:2
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))<btagWP[year]){
            jet1_pt=CleanJet_pt.at(i);
            break;
        }
    }
    return jet1_pt;
}
float jet1_eta(int nCleanJet, RVec<float> & CleanJet_eta, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<1) return -9999.;
    float jet1_eta=-9999.;
    // year: 2016:0; 2017:1; 2018:2
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))<btagWP[year]){
            jet1_eta=CleanJet_eta.at(i);
            break;
        }
    }
    return jet1_eta;
}
float jet2_pt(int nCleanJet, RVec<float> & CleanJet_pt, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<2) return -9999.;
    float jet2_pt=-9999.;
    int jet_count=0;
    // year: 2016:0; 2017:1; 2018:2
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))<btagWP[year]){
            jet_count++;
            jet2_pt=CleanJet_pt.at(i);
            if(jet_count>1){
                break;
            }
        }
    }
    return jet2_pt;
}
float jet2_eta(int nCleanJet, RVec<float> & CleanJet_eta, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<2) return -9999.;
    float jet2_eta=-9999.;
    int jet_count=0;
    // year: 2016:0; 2017:1; 2018:2
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))<btagWP[year]){
            jet_count++;
            jet2_eta=CleanJet_eta.at(i);
            if(jet_count>1){
                break;
            }
        }
    }
    return jet2_eta;
}
float mj1j2(int nCleanJet, RVec<float> & CleanJet_pt, RVec<float> & CleanJet_eta, RVec<float> & CleanJet_phi,RVec<float> & CleanJet_mass, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<2) return -9999.;
    float mj1j2=-9999.;
    int jet_count=0;
    // year: 2016:0; 2017:1; 2018:2
    RVec<ROOT::Math::PtEtaPhiMVector> parts;
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))<btagWP[year]){
            jet_count++;
            ROOT::Math::PtEtaPhiMVector p(CleanJet_pt[i], CleanJet_eta[i], CleanJet_phi[i], CleanJet_mass[i]);
            parts.push_back(p);
            if(jet_count>1){
                break;
            }
        }
    }
    if(jet_count>1){
        mj1j2=(parts[0]+parts[1]).M();
    }
    return mj1j2;
}
float detaj1j2(int nCleanJet, RVec<float> & CleanJet_eta, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<2) return -9999.;
    float detaj1j2=-9999.;
    int jet_count=0;
    // year: 2016:0; 2017:1; 2018:2
    RVec<float> jet_eta;
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))<btagWP[year]){
            jet_count++;
            jet_eta.push_back(CleanJet_eta.at(i));
            if(jet_count>1){
                break;
            }
        }
    }
    if(jet_count>1){
        detaj1j2=(jet_eta[0]-jet_eta[1]);
    }
    return detaj1j2;
}
float dphij1j2(int nCleanJet, RVec<float> & CleanJet_phi, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<2) return -9999.;
    float dphij1j2=-9999.;
    int jet_count=0;
    // year: 2016:0; 2017:1; 2018:2
    RVec<float> jet_phi;
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))<btagWP[year]){
            jet_count++;
            jet_phi.push_back(CleanJet_phi.at(i));
            if(jet_count>1){
                break;
            }
        }
    }
    if(jet_count>1){
        dphij1j2=(jet_phi[0]-jet_phi[1]);
         if ( dphij1j2 > TMath::Pi() ) {
            dphij1j2 -= 2.0*TMath::Pi();
         } else if ( dphij1j2 <= -TMath::Pi() ) {
            dphij1j2 += 2.0*TMath::Pi();
         }
    }
    return dphij1j2;
}
float bjet_pt(int nCleanJet, RVec<float> & CleanJet_pt, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<1) return -9999.;
    float bjet_pt=-9999.;
    // year: 2016:0; 2017:1; 2018:2
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))>btagWP[year]){
            bjet_pt=CleanJet_pt.at(i);
            break;
        }
    }
    return bjet_pt;
}
float bjet_eta(int nCleanJet, RVec<float> & CleanJet_eta, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year){
    if (nCleanJet<1) return -9999.;
    float bjet_eta=-9999.;
    // year: 2016:0; 2017:1; 2018:2
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))>btagWP[year]){
            bjet_eta=CleanJet_eta.at(i);
            break;
        }
    }
    return bjet_eta;
}
float mlb(int nCleanJet, RVec<float> & CleanJet_pt, RVec<float> & CleanJet_eta, RVec<float> & CleanJet_phi,RVec<float> & CleanJet_mass, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year,
RVec<float> & Lepton_pt, RVec<float> & Lepton_eta, RVec<float> & Lepton_phi, RVec<int> & Lepton_pdgId){
    if (nCleanJet<2) return -9999.;
    float mlb=-9999.;
    int jet_count=0;
    // year: 2016:0; 2017:1; 2018:2
    RVec<ROOT::Math::PtEtaPhiMVector> parts;
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))>btagWP[year]){
            jet_count++;
            ROOT::Math::PtEtaPhiMVector p(CleanJet_pt[i], CleanJet_eta[i], CleanJet_phi[i], CleanJet_mass[i]);
            parts.push_back(p);
            break;
        }
    }
    if (abs(Lepton_pdgId.at(0))==13){
        ROOT::Math::PtEtaPhiMVector p(Lepton_pt[0], Lepton_eta[0], Lepton_phi[0], 0.1057128);
        parts.push_back(p);
    }else{
        ROOT::Math::PtEtaPhiMVector p(Lepton_pt[0], Lepton_eta[0], Lepton_phi[0], 0.000511);
        parts.push_back(p);
    }
    if(jet_count>0){
        mlb=(parts[0]+parts[1]).M();
    }
    return mlb;
}
float ptlb(int nCleanJet, RVec<float> & CleanJet_pt, RVec<float> & CleanJet_eta, RVec<float> & CleanJet_phi,RVec<float> & CleanJet_mass, RVec<int> & CleanJet_jetIdx, RVec<float> & Jet_btagDeepB, int year,
RVec<float> & Lepton_pt, RVec<float> & Lepton_eta, RVec<float> & Lepton_phi, RVec<int> & Lepton_pdgId){
    if (nCleanJet<2) return -9999.;
    float ptlb=-9999.;
    int jet_count=0;
    // year: 2016:0; 2017:1; 2018:2
    RVec<ROOT::Math::PtEtaPhiMVector> parts;
    float btagWP[]={0.6321,0.4941,0.4184};
    for (int i=0; i<nCleanJet; i++){
        if(Jet_btagDeepB.at(CleanJet_jetIdx.at(i))>btagWP[year]){
            jet_count++;
            ROOT::Math::PtEtaPhiMVector p(CleanJet_pt[i], CleanJet_eta[i], CleanJet_phi[i], CleanJet_mass[i]);
            parts.push_back(p);
            break;
        }
    }
    if (abs(Lepton_pdgId.at(0))==13){
        ROOT::Math::PtEtaPhiMVector p(Lepton_pt[0], Lepton_eta[0], Lepton_phi[0], 0.1057128);
        parts.push_back(p);
    }else{
        ROOT::Math::PtEtaPhiMVector p(Lepton_pt[0], Lepton_eta[0], Lepton_phi[0], 0.000511);
        parts.push_back(p);
    }
    if(jet_count>0){
        ptlb=(parts[0]+parts[1]).Pt();
    }
    return ptlb;
}
,zlep1,Zlep2
#endif
