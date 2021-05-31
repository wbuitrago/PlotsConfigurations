#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>
#include <array>
#include <map>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/PxPyPzM4D.h"
#include "Math/GenVector/Boost.h"
#include "Math/GenVector/VectorUtil.h"

// using namespace ROOT::Math;

class WZvar : public multidraw::TTreeFunction {
public:
  WZvar();
  ~WZvar();

  char const* getName() const override { return "WZvar"; }
  TTreeFunction* clone() const override { return new WZvar(); }

  void beginEvent(long long iEv) override {filled=false;};
  unsigned getNdata() override { return outputValues.size(); }
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;
  bool filled;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader* nLepton;
  IntArrayReader* Lepton_pdgId;
  FloatArrayReader* Lepton_pt;
  FloatArrayReader* Lepton_eta;
  FloatArrayReader* Lepton_phi;
  FloatArrayReader* PuppiMET_pt;
  FloatArrayReader* PuppiMET_phi;
  IntArrayReader* Lepton_electronIdx;
  IntArrayReader* Lepton_muonIdx;
  FloatArrayReader* Electron_mass;
  FloatArrayReader* Muon_mass;

//  void setValues(std::vector<unsigned> iPromptL);
  void setValues();
  std::array<double, 17> outputValues;
};

WZvar::WZvar() :
  TTreeFunction(){}

double
WZvar::evaluate(unsigned iJ)
{
// {mlll, ptlll, ptl1Z, ptl2Z, ptlW, etal1Z, etal2Z, etalW, mZ, mWZ, deltaetaWZ, deltaphiWZ, 
// Philanes, ThetaWZ, ThetalW, ThetalZ};
//  if (!filled) setValues(iPromptL);
  if (!filled) setValues();
  return outputValues[iJ];
}

void
//WZvar::setValues(std::vector<unsigned> iPromptL)
WZvar::setValues()
{
  outputValues.fill(-1.);

  unsigned nL{*nLepton->Get()};
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId->At(iL)))};
    if (absId != 11 && absId != 13) continue;
    iPromptL.push_back(iL);
  }

  double lepton_mass0;
  double lepton_mass1;
  double lepton_mass2;

  if (abs(Lepton_pdgId->At(iPromptL[0]))==13){
    lepton_mass0=Muon_mass->At(Lepton_muonIdx->At(iPromptL[0]));
  } else {
    lepton_mass0=Electron_mass->At(Lepton_electronIdx->At(iPromptL[0]));
  }

  if (abs(Lepton_pdgId->At(iPromptL[1]))==13){
    lepton_mass1=Muon_mass->At(Lepton_muonIdx->At(iPromptL[1]));
  } else {
    lepton_mass1=Electron_mass->At(Lepton_electronIdx->At(iPromptL[1]));
  }

  if (abs(Lepton_pdgId->At(iPromptL[2]))==13){
    lepton_mass2=Muon_mass->At(Lepton_muonIdx->At(iPromptL[2]));
  } else {
    lepton_mass2=Electron_mass->At(Lepton_electronIdx->At(iPromptL[2]));
  }

  ROOT::Math::PtEtaPhiMVector pl0 {
    Lepton_pt->At(iPromptL[0]),
    Lepton_eta->At(iPromptL[0]),
    Lepton_phi->At(iPromptL[0]),
    lepton_mass0
  };

  ROOT::Math::PtEtaPhiMVector pl1 {
    Lepton_pt->At(iPromptL[1]),
    Lepton_eta->At(iPromptL[1]),
    Lepton_phi->At(iPromptL[1]),
    lepton_mass1
  };

  ROOT::Math::PtEtaPhiMVector pl2 {
    Lepton_pt->At(iPromptL[2]),
    Lepton_eta->At(iPromptL[2]),
    Lepton_phi->At(iPromptL[2]),
    lepton_mass2
  };

  ROOT::Math::PtEtaPhiMVector plll{pl0 + pl1 + pl2};

  ROOT::Math::PtEtaPhiMVector pl[]={pl0,pl1,pl2};
  int zlepton1_idx=0;
  int zlepton2_idx=1;
  int wlepton_idx=2;
  int zlepton1_pdgId=0;
  int zlepton2_pdgId=0;
  int wlepton_pdgId=0;
  double zlepton1_m=0;
  double zlepton2_m=0;
  double wlepton_m=0;  
  double zMass_min=-999999;
  for (int i=0; i<2; i++){
    for (int j=i+1; j<3; j++){
        if (Lepton_pdgId->At(iPromptL[i])+Lepton_pdgId->At(iPromptL[j])==0){
            if(abs((pl[i]+pl[j]).M()-91.1876)<abs(zMass_min-91.1876)){
                zMass_min=(pl[i]+pl[j]).M();
                zlepton1_idx=i;
                zlepton2_idx=j;
                wlepton_idx=3-i-j;
                zlepton1_pdgId = Lepton_pdgId->At(iPromptL[i]);
                zlepton2_pdgId = Lepton_pdgId->At(iPromptL[j]);
                wlepton_pdgId = Lepton_pdgId->At(iPromptL[3-i-j]);
            }
        }
    }
  }

  if (zlepton1_pdgId==13){
    zlepton1_m=Muon_mass->At(Lepton_muonIdx->At(iPromptL[zlepton1_idx]));
  } else {
    zlepton1_m=Electron_mass->At(Lepton_electronIdx->At(iPromptL[zlepton1_idx]));
  }

  if (zlepton2_pdgId==13){
    zlepton2_m=Muon_mass->At(Lepton_muonIdx->At(iPromptL[zlepton2_idx]));
  } else {
    zlepton2_m=Electron_mass->At(Lepton_electronIdx->At(iPromptL[zlepton2_idx]));
  }

  if (wlepton_pdgId==13){
    wlepton_m=Muon_mass->At(Lepton_muonIdx->At(iPromptL[wlepton_idx]));
  } else {
    wlepton_m=Electron_mass->At(Lepton_electronIdx->At(iPromptL[wlepton_idx]));
  }

  ROOT::Math::PtEtaPhiMVector lZ1 {
    Lepton_pt->At(iPromptL[zlepton1_idx]),
    Lepton_eta->At(iPromptL[zlepton1_idx]),
    Lepton_phi->At(iPromptL[zlepton1_idx]),
    zlepton1_m
  };

  ROOT::Math::PtEtaPhiMVector lZ2 {
    Lepton_pt->At(iPromptL[zlepton2_idx]),
    Lepton_eta->At(iPromptL[zlepton2_idx]),
    Lepton_phi->At(iPromptL[zlepton2_idx]),
    zlepton2_m
  };  
    
  ROOT::Math::PtEtaPhiMVector lW {
    Lepton_pt->At(iPromptL[wlepton_idx]),
    Lepton_eta->At(iPromptL[wlepton_idx]),
    Lepton_phi->At(iPromptL[wlepton_idx]),
    wlepton_m
  };    

  ROOT::Math::PtEtaPhiMVector n {
    PuppiMET_pt->At(0),
    0,
    PuppiMET_phi->At(0),
    0
  };

// Compute P_z neutrino

  double Pz_nu = 0;
  double mW = 80.385 ;
  double Pl = sqrt(pow(lW.Px(),2) + pow(lW.Py(),2) + pow(lW.Pz(),2)) ;
  double a = sqrt(pow(n.Px(),2) + pow(n.Py(),2)) ;
  double b = lW.Pz() / Pl ;
  double c = (pow(mW,2) + 2.*(n.Px()*lW.Px() + n.Py()*lW.Py())) / (2.*Pl) ;
  double Delta = pow(c,2) + pow(a,2) * (pow(b,2) - 1.) ;
  if (Delta <= 0)
    {
      Pz_nu = -1. * b * c / (pow(b,2) - 1.) ;
    }
  else if (Delta > 0)
    {
      double Pz_nu_1 = (-1.*b*c + sqrt(Delta)) / (pow(b,2) - 1.) ;
      double Pz_nu_2 = (-1.*b*c - sqrt(Delta)) / (pow(b,2) - 1.) ;
      if (abs(Pz_nu_1 - lW.Pz()) < abs(Pz_nu_2 - lW.Pz()))
        {
          Pz_nu = Pz_nu_1 ;
        }
      else
        {
          Pz_nu = Pz_nu_2 ;
        }
    }

  ROOT::Math::PxPyPzMVector nu_reco {
    n.Px(),
    n.Py(),
    Pz_nu,
    0
  };

// Compute invariant mass of WZ system

  ROOT::Math::PtEtaPhiMVector nu {
    nu_reco.Pt(),
    nu_reco.Eta(),
    nu_reco.Phi(),
    0
  };

  ROOT::Math::PtEtaPhiMVector Z = lZ1 + lZ2 ;
  ROOT::Math::PtEtaPhiMVector W = lW + nu ;
  ROOT::Math::PtEtaPhiMVector WZ = W + Z ;

// Compute angulare variables for WZ system

  float deltaphiWZ = abs(W.Phi() - Z.Phi()) ;
  if (deltaphiWZ > M_PI)
    {
      deltaphiWZ = 2. * M_PI - deltaphiWZ ;
    } 

  ROOT::Math::Boost WZboost {WZ.BoostToCM()} ;
  ROOT::Math::Boost Wboost  {W.BoostToCM()} ;
  ROOT::Math::Boost Zboost  {Z.BoostToCM()} ;

  ROOT::Math::PtEtaPhiMVector W_WZcm = WZboost(W) ;
  ROOT::Math::PtEtaPhiMVector Z_WZcm = WZboost(Z) ;
  ROOT::Math::PtEtaPhiMVector L_W_Wcm = Wboost(lW) ;
  ROOT::Math::PtEtaPhiMVector L_Z_Zcm = Zboost(lZ1) ;
  auto W_plane = L_W_Wcm.Vect().Cross(W) ;
  auto Z_plane = L_Z_Zcm.Vect().Cross(Z) ;

// {mlll, ptlll, ptl1Z, ptl2Z, ptlW, etal1Z, etal2Z, etalW, mZ, mWZ, deltaetaWZ, deltaphiWZ, 
// Philanes, ThetaWZ, ThetalW, ThetalZ};
  outputValues[0] = plll.M();
  outputValues[1] = plll.Pt();
  outputValues[2] = Lepton_pt->At(iPromptL[zlepton1_idx]);
  outputValues[3] = Lepton_pt->At(iPromptL[zlepton2_idx]);
  outputValues[4] = Lepton_pt->At(iPromptL[wlepton_idx]);
  outputValues[5] = Lepton_eta->At(iPromptL[zlepton1_idx]);
  outputValues[6] = Lepton_eta->At(iPromptL[zlepton2_idx]);
  outputValues[7] = Lepton_eta->At(iPromptL[wlepton_idx]);
  outputValues[8] = Z.M(); //zMass_min;
  outputValues[9] = Z.Pt();
  outputValues[10] = WZ.M();
  outputValues[11] = fabs(W.Eta() - Z.Eta());
  outputValues[12] = deltaphiWZ ;
  outputValues[13] = abs(ROOT::Math::VectorUtil::DeltaPhi(W_plane, Z_plane)) ;
  outputValues[14] = W_WZcm.Theta() ;
  outputValues[15] = L_W_Wcm.Theta() ;
  outputValues[16] = L_Z_Zcm.Theta() ;

  filled = true;

}

void
WZvar::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
  _library.bindBranch(PuppiMET_pt, "PuppiMET_pt");
  _library.bindBranch(PuppiMET_phi, "PuppiMET_phi");
  _library.bindBranch(Lepton_electronIdx, "Lepton_electronIdx");
  _library.bindBranch(Lepton_muonIdx, "Lepton_muonIdx");
  _library.bindBranch(Muon_mass, "Muon_mass");
  _library.bindBranch(Electron_mass, "Electron_mass");
}

WZvar::~WZvar()
{
  nLepton = nullptr;
  Lepton_pdgId = nullptr;
  Lepton_pt = nullptr;
  Lepton_eta = nullptr;
  Lepton_phi = nullptr;
  PuppiMET_pt = nullptr;
  PuppiMET_phi = nullptr;
  Lepton_electronIdx = nullptr;
  Lepton_muonIdx = nullptr;
  Muon_mass = nullptr;
  Electron_mass = nullptr;
}

