#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class Genlep1pt : public multidraw::TTreeFunction {
public:
  Genlep1pt();

  char const* getName() const override { return "Genlep1pt"; }
  TTreeFunction* clone() const override { return new Genlep1pt(); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader* nGenDressedLepton;
  IntArrayReader* GenDressedLepton_pdgId;
  FloatArrayReader* GenDressedLepton_pt;
  FloatArrayReader* GenDressedLepton_eta;
  FloatArrayReader* GenDressedLepton_phi;
  FloatArrayReader* GenDressedLepton_mass;

  //UIntValueReader* nGenJet;
  //FloatArrayReader* GenJet_pt;
  //FloatArrayReader* GenJet_eta;
  //FloatArrayReader* GenJet_phi;
  //FloatArrayReader* GenJet_mass;

  //FloatValueReader* GenMET_pt;
  //FloatValueReader* GenMET_phi;
};

Genlep1pt::Genlep1pt() :
  TTreeFunction()
{
}

double
Genlep1pt::evaluate(unsigned)
{
  unsigned nL{*nGenDressedLepton->Get()};
  if (nL < 1)
    return -9999.;

  // more gen lepton selections
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(GenDressedLepton_pdgId->At(iL)))};
    if (absId != 11 && absId != 13)
      continue;

    iPromptL.push_back(iL);
  }

  if (iPromptL.size() < 1)
    return -9999.; // false

  return GenDressedLepton_pt->At(iPromptL[0]);
}

void
Genlep1pt::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nGenDressedLepton, "nGenDressedLepton");
  _library.bindBranch(GenDressedLepton_pdgId, "GenDressedLepton_pdgId");
  _library.bindBranch(GenDressedLepton_pt, "GenDressedLepton_pt");
  _library.bindBranch(GenDressedLepton_eta, "GenDressedLepton_eta");
  _library.bindBranch(GenDressedLepton_phi, "GenDressedLepton_phi");
  _library.bindBranch(GenDressedLepton_mass, "GenDressedLepton_mass");

  //_library.bindBranch(nGenJet, "nGenJet");
  //_library.bindBranch(GenJet_pt, "GenJet_pt");
  //_library.bindBranch(GenJet_eta, "GenJet_eta");
  //_library.bindBranch(GenJet_phi, "GenJet_phi");
  //_library.bindBranch(GenJet_mass, "GenJet_mass");

  //_library.bindBranch(GenMET_pt, "GenMET_pt");
  //_library.bindBranch(GenMET_phi, "GenMET_phi");
}
