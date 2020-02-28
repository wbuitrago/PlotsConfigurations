#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class Zz : public multidraw::TTreeFunction {
public:
  Zz();

  char const* getName() const override { return "Zz"; }
  TTreeFunction* clone() const override { return new Zz(); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

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

  FloatValueReader* METFixEE2017_pt;
};

Zz::Zz() :
  TTreeFunction()
{
}

double
Zz::evaluate(unsigned)
{
  unsigned nL{*nLepton->Get()};
  if (nL < 3)
    return 0.;

  // more gen lepton selections
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId->At(iL)))};
    if (absId != 11 && absId != 13)
      continue;

    iPromptL.push_back(iL);
  }

  if (iPromptL.size() < 4)
    return 0.; // false

  if (iPromptL.size() >= 5 && Lepton_pt->At(iPromptL[4]) >= 10.)
    return 0.;

  if (Lepton_pdgId->At(iPromptL[0])+ Lepton_pdgId->At(iPromptL[1]) + Lepton_pdgId->At(iPromptL[2])+ Lepton_pdgId->At(iPromptL[3]) != 0)
    return 0.;

  double lepton_mass0;
  double lepton_mass1;
  double lepton_mass2;
  double lepton_mass3;

  if (abs(Lepton_pdgId->At(iPromptL[0]))==13){
    lepton_mass0=Muon_mass->At(Lepton_muonIdx->At(iPromptL[0]));
  }else{
    lepton_mass0=Electron_mass->At(Lepton_electronIdx->At(iPromptL[0]));
  }

  if (abs(Lepton_pdgId->At(iPromptL[1]))==13){
    lepton_mass1=Muon_mass->At(Lepton_muonIdx->At(iPromptL[1]));
  }else{
    lepton_mass1=Electron_mass->At(Lepton_electronIdx->At(iPromptL[1]));
  }

  if (abs(Lepton_pdgId->At(iPromptL[2]))==13){
    lepton_mass2=Muon_mass->At(Lepton_muonIdx->At(iPromptL[2]));
  }else{
    lepton_mass2=Electron_mass->At(Lepton_electronIdx->At(iPromptL[2]));
  }

  if (abs(Lepton_pdgId->At(iPromptL[3]))==13){
    lepton_mass3=Muon_mass->At(Lepton_muonIdx->At(iPromptL[3]));
  }else{
    lepton_mass3=Electron_mass->At(Lepton_electronIdx->At(iPromptL[3]));
  }

  ROOT::Math::PtEtaPhiMVector pl0(
    Lepton_pt->At(iPromptL[0]),
    Lepton_eta->At(iPromptL[0]),
    Lepton_phi->At(iPromptL[0]),
    lepton_mass0
  );
  ROOT::Math::PtEtaPhiMVector pl1(
    Lepton_pt->At(iPromptL[1]),
    Lepton_eta->At(iPromptL[1]),
    Lepton_phi->At(iPromptL[1]),
    lepton_mass1
  );
  ROOT::Math::PtEtaPhiMVector pl2(
    Lepton_pt->At(iPromptL[2]),
    Lepton_eta->At(iPromptL[2]),
    Lepton_phi->At(iPromptL[2]),
    lepton_mass2
  );
  ROOT::Math::PtEtaPhiMVector pl3(
    Lepton_pt->At(iPromptL[3]),
    Lepton_eta->At(iPromptL[3]),
    Lepton_phi->At(iPromptL[3]),
    lepton_mass3
  );

  ROOT::Math::PtEtaPhiMVector pl[]={pl0,pl1,pl2,pl3};

  int z0lepton1_idx=0;
  int z0lepton2_idx=1;
  int z1lepton1_idx=2;
  int z1lepton2_idx=3;
  bool z0flag=false;
  bool z1flag=false;
  double z0Mass_min=-999999;
  double z1Mass_min=-999999;

  vector<int> veci;
  veci.push_back(1);
  veci.push_back(2);
  veci.push_back(3);

  vector<int>::iterator it;

  for(int i=1; i<4; i++){
    if(Lepton_pdgId->At(iPromptL[0])+Lepton_pdgId->At(iPromptL[i])==0){
        if(abs((pl[0]+pl[i]).M()-91.1876)<abs(z0Mass_min-91.1876)){
            z0Mass_min=(pl[0]+pl[i]).M();
            z0lepton2_idx=i;
            z0flag=true;
        }
    }
  }
  for(it = veci.begin(); it!=veci.end();){
    if(*it==z0lepton2_idx){
        it=veci.erase(it);
        z1lepton1_idx=veci.at(0);
        z1lepton2_idx=veci.at(1);
        break;
    }else{
        ++it;
    }
  }
  if(Lepton_pdgId->At(iPromptL[z1lepton1_idx])+Lepton_pdgId->At(iPromptL[z1lepton2_idx])==0){
    z1flag=true;
    z1Mass_min=(pl[z1lepton1_idx]+pl[z1lepton2_idx]).M();
  }

  if(!(Lepton_pt->At(iPromptL[0])>25 && Lepton_pt->At(iPromptL[z0lepton2_idx])>10 && Lepton_pt->At(iPromptL[z1lepton1_idx])>25 && Lepton_pt->At(iPromptL[z1lepton2_idx])>10)){
    return 0.;
  }
  if(!(abs(z0Mass_min-91.1876)<15 && abs(z1Mass_min-91.1876)<15)){
    return 0.;
  }

  double Met{*METFixEE2017_pt->Get()};
  if (Met<=30)
    return 0.;

  return 1.;
}

void
Zz::bindTree_(multidraw::FunctionLibrary& _library)
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

  _library.bindBranch(METFixEE2017_pt, "METFixEE2017_pt");
}
