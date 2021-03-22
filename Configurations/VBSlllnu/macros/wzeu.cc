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

class WZeu : public multidraw::TTreeFunction {
public:
  WZeu();
  ~WZeu();

  char const* getName() const override { return "WZeu"; }
  TTreeFunction* clone() const override { return new WZeu(); }

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
  IntArrayReader* Lepton_electronIdx;
  IntArrayReader* Lepton_muonIdx;
  FloatArrayReader* Electron_mass;
  FloatArrayReader* Muon_mass;

//  void setValues(std::vector<unsigned> iPromptL);
  void setValues();
  std::array<double, 9> outputValues;
};

WZeu::WZeu() :
  TTreeFunction(){}

double
WZeu::evaluate(unsigned iJ)
{
//{ mee, mllZ, mlll, ptl1Z, ptl2Z, ptlW, etal1Z, etal2Z, etalW };
//  if (!filled) setValues(iPromptL);
  if (!filled) setValues();
  return outputValues[iJ];
}

void
//WZeu::setValues(std::vector<unsigned> iPromptL)
WZeu::setValues()
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
  ROOT::Math::PtEtaPhiMVector pl0l1{pl0 + pl1};
  ROOT::Math::PtEtaPhiMVector pl0l2{pl0 + pl2};
  ROOT::Math::PtEtaPhiMVector pl1l2{pl1 + pl2};

  ROOT::Math::PtEtaPhiMVector pl[]={pl0,pl1,pl2};
  int zlepton1_idx=0;
  int zlepton2_idx=1;
  int wlepton_idx=2;
  double zMass_min=-999999;
  for (int i=0; i<2; i++){
    for (int j=i+1; j<3; j++){
        if (Lepton_pdgId->At(iPromptL[i])+Lepton_pdgId->At(iPromptL[j])==0){
            if(abs((pl[i]+pl[j]).M()-91.1876)<abs(zMass_min-91.1876)){
                zMass_min=(pl[i]+pl[j]).M();
                zlepton1_idx=i;
                zlepton2_idx=j;
                wlepton_idx=3-i-j;
            }
        }
    }
  }

  if (std::abs(Lepton_pdgId->At(zlepton1_idx)) == 11 && std::abs(Lepton_pdgId->At(zlepton2_idx)) == 11) {
    ROOT::Math::PtEtaPhiMVector pe0 {
      Lepton_pt->At(iPromptL[zlepton1_idx]),
      Lepton_eta->At(iPromptL[zlepton1_idx]),
      Lepton_phi->At(iPromptL[zlepton1_idx]),
      Electron_mass->At(Lepton_electronIdx->At(iPromptL[zlepton1_idx]))
    };
    ROOT::Math::PtEtaPhiMVector pe1 {
      Lepton_pt->At(iPromptL[zlepton2_idx]),
      Lepton_eta->At(iPromptL[zlepton2_idx]),
      Lepton_phi->At(iPromptL[zlepton2_idx]),
      Electron_mass->At(Lepton_electronIdx->At(iPromptL[zlepton2_idx]))
    };
    ROOT::Math::PtEtaPhiMVector p_ee{pe0 + pe1};
    outputValues[0] = p_ee.M();
  }
  else {
    outputValues[0] = 0;
  }

//{ mee, mllZ, mlll, ptl1Z, ptl2Z, ptlW, etal1Z, etal2Z, etalW };
  outputValues[1] = zMass_min;
  outputValues[2] = plll.M();
  outputValues[3] = Lepton_pt->At(iPromptL[zlepton1_idx]);
  outputValues[4] = Lepton_pt->At(iPromptL[zlepton2_idx]);
  outputValues[5] = Lepton_pt->At(iPromptL[wlepton_idx]);
  outputValues[6] = Lepton_eta->At(iPromptL[zlepton1_idx]);
  outputValues[7] = Lepton_eta->At(iPromptL[zlepton2_idx]);
  outputValues[8] = Lepton_eta->At(iPromptL[wlepton_idx]);

  filled = true;

}

void
WZeu::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
  _library.bindBranch(Lepton_electronIdx, "Lepton_electronIdx");
  _library.bindBranch(Lepton_muonIdx, "Lepton_muonIdx");
  _library.bindBranch(Muon_mass, "Muon_mass");
  _library.bindBranch(Electron_mass, "Electron_mass");
}

WZeu::~WZeu()
{
  nLepton = nullptr;
  Lepton_pdgId = nullptr;
  Lepton_pt = nullptr;
  Lepton_eta = nullptr;
  Lepton_phi = nullptr;
  Lepton_electronIdx = nullptr;
  Lepton_muonIdx = nullptr;
  Muon_mass = nullptr;
  Electron_mass = nullptr;
}

