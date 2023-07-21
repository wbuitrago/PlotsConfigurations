#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TSystem.h"

#include <iostream>
#include <vector>

#include "TLorentzVector.h"
#include "TMath.h"

class MLL : public multidraw::TTreeFunction {
public:
  MLL(const char* variable_);

  char const* getName() const override { return "MLL"; }
  TTreeFunction* clone() const override { return new MLL(variable.c_str()); }
  //TTreeFunction* clone() const override;

  unsigned getNdata() override { return 1; }
  float deltaPhi(float, float);
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  std::string variable;

  UIntValueReader* nLepton;
  FloatArrayReader* Lepton_pt;
  FloatArrayReader* Lepton_eta;
  FloatArrayReader* Lepton_phi;
};

MLL::MLL(const char* variable_) :
  TTreeFunction(),
  variable{variable_}
{}

// --- Helper
float
MLL::deltaPhi(float phi1, float phi2)
{
  float PHI = std::abs(phi1-phi2);
if (PHI<=3.14159265)
  return PHI;
else
  return 2*3.14159265-PHI;
}
// Helper ---

double
MLL::evaluate(unsigned)
{
  TLorentzVector l1(0.,0.,0.,0.);
  TLorentzVector l2(0.,0.,0.,0.);
  TLorentzVector l3(0.,0.,0.,0.);
  TLorentzVector l4(0.,0.,0.,0.);
  unsigned nlep{*nLepton->Get()};

  if (nlep < 3)
    return -9999.;
    

  l1.SetPtEtaPhiM( Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0. );
  l2.SetPtEtaPhiM( Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0. );
  l3.SetPtEtaPhiM( Lepton_pt->At(2), Lepton_eta->At(2), Lepton_phi->At(2), 0. );
  l4.SetPtEtaPhiM( Lepton_pt->At(3), Lepton_eta->At(3), Lepton_phi->At(3), 0. );
  
  if (variable == "m01" || variable == "m10") return((l1+l2).M());
  if (variable == "m02" || variable == "m20") return((l1+l3).M());
  if (variable == "m03" || variable == "m30") return((l1+l4).M());
  if (variable == "m23" || variable == "m32") return((l3+l4).M());
  if (variable == "m13" || variable == "m31") return((l2+l4).M());
  if (variable == "m12" || variable == "m21") return((l2+l3).M());
  if (variable == "m4l") return((l1+l2+l3+l4).M());

  std::cout << "Invalid variable! Supported variables are m10, m01, m20,m02,m30,m03,m32,m23,m31,m13,m21,m12,m4l" << std::endl;
  return -9999.0;

}

void
MLL::bindTree_(multidraw::FunctionLibrary& _library)
{
  std::cout << "Loading MLL" << std::endl;
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
}