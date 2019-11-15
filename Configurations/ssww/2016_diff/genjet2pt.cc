#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class Genjet2pt : public multidraw::TTreeFunction {
public:
  Genjet2pt();

  char const* getName() const override { return "Genjet2pt"; }
  TTreeFunction* clone() const override { return new Genjet2pt(); }

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

  UIntValueReader* nGenJet;
  FloatArrayReader* GenJet_pt;
  FloatArrayReader* GenJet_eta;
  FloatArrayReader* GenJet_phi;
  FloatArrayReader* GenJet_mass;

  //FloatValueReader* GenMET_pt;
  //FloatValueReader* GenMET_phi;
};

Genjet2pt::Genjet2pt() :
  TTreeFunction()
{
}

double
Genjet2pt::evaluate(unsigned)
{
  unsigned nJ{*nGenJet->Get()};
  if (nJ<2)
    return -9999.;
  unsigned nL{*nGenDressedLepton->Get()};

  // more gen lepton selections
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(GenDressedLepton_pdgId->At(iL)))};
    if (absId != 11 && absId != 13)
      continue;

    iPromptL.push_back(iL);
  }

  if (iPromptL.size() == 0) {
    unsigned n{0};
    for (unsigned iJ{0}; iJ != nJ; ++iJ) {
      if (GenJet_pt->At(iJ) > 30.)
        ++n;
    }
    if (n<2)
        return -9999.;
    return GenJet_pt->At(1);

  }

  // more gen jet selections
  std::vector<unsigned> iCleanJ{};
  iCleanJ.reserve(nJ);

  std::vector<ROOT::Math::PtEtaPhiMVector> dressedLeptons{};
  for (unsigned iL : iPromptL) {
    dressedLeptons.emplace_back(
      GenDressedLepton_pt->At(iL),
      GenDressedLepton_eta->At(iL),
      GenDressedLepton_phi->At(iL),
      GenDressedLepton_mass->At(iL));
  }
  unsigned n{0};
  for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    if (GenJet_pt->At(iJ) <= 30.)
      continue;

    bool overlap{false};
    for (auto& p4 : dressedLeptons) {
      if (p4.pt() < 10.)
        continue;

      double dEta{p4.eta() - GenJet_eta->At(iJ)};
      double dPhi{TVector2::Phi_mpi_pi(p4.phi() - GenJet_phi->At(iJ))};
      if (dEta * dEta + dPhi * dPhi < 0.016) {
        overlap = true;
        break;
      }
    }
    if (!overlap)
      ++n;
      iCleanJ.push_back(iJ);
  }
  if (n<2)
    return -9999.;
  return GenJet_pt->At(iCleanJ[1]);
}

void
Genjet2pt::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nGenDressedLepton, "nGenDressedLepton");
  _library.bindBranch(GenDressedLepton_pdgId, "GenDressedLepton_pdgId");
  _library.bindBranch(GenDressedLepton_pt, "GenDressedLepton_pt");
  _library.bindBranch(GenDressedLepton_eta, "GenDressedLepton_eta");
  _library.bindBranch(GenDressedLepton_phi, "GenDressedLepton_phi");
  _library.bindBranch(GenDressedLepton_mass, "GenDressedLepton_mass");

  _library.bindBranch(nGenJet, "nGenJet");
  _library.bindBranch(GenJet_pt, "GenJet_pt");
  _library.bindBranch(GenJet_eta, "GenJet_eta");
  _library.bindBranch(GenJet_phi, "GenJet_phi");
  _library.bindBranch(GenJet_mass, "GenJet_mass");

  //_library.bindBranch(GenMET_pt, "GenMET_pt");
  //_library.bindBranch(GenMET_phi, "GenMET_phi");
}
