#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TFile.h"
#include "TF1.h"
#include "TString.h"
#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/VectorUtil.h"

#include <iostream>
using namespace ROOT::Math;
typedef TTreeReaderValue<Double_t> DoubleValueReader;


class ReweightJet1pT: public multidraw::TTreeFunction {
public:
  ReweightJet1pT(const char * weights_file, bool debug);
  ~ReweightJet1pT();

  char const* getName() const override { return "ReweightJet1pT"; }
  TTreeFunction* clone() const override { return new ReweightJet1pT(_weights_file.Data(),_debug); }

  unsigned getNdata() override { return 1; } 
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;
  

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  void setValues();
  TString _weights_file;
  TFile* _file;

  TF1* mu_hard_weight;
  TF1* mu_PU_weight;
  TF1* ele_hard_weight;
  TF1* ele_PU_weight;

  bool _debug;
  
  DoubleArrayReader* category_WJets;
  IntArrayReader * Lepton_pdgId;
  FloatArrayReader* CleanJet_pt;

};

ReweightJet1pT::ReweightJet1pT(const char * weights_file ,bool debug) :
  TTreeFunction(), _weights_file(weights_file),_debug(debug)
{
  _file = new TFile(weights_file,"READ");

  ele_hard_weight = (TF1*)_file->Get("ele_MultiplyHWJ");
  ele_PU_weight = (TF1*)_file->Get("ele_MultiplyPUWJ");

  mu_hard_weight = (TF1*)_file->Get("mu_MultiplyHWJ");
  mu_PU_weight = (TF1*)_file->Get("mu_MultiplyPUWJ");

  // ele_hard_weight->SetDirectory(0);
  // ele_PU_weight->SetDirectory(0);
  // mu_hard_weight->SetDirectory(0);
  // mu_PU_weight->SetDirectory(0);

}

ReweightJet1pT::~ReweightJet1pT(){
  _file->Close();
  delete ele_hard_weight;
  delete ele_PU_weight;
  delete mu_hard_weight;
  delete mu_PU_weight;
  delete _file;
  category_WJets = nullptr;
}


double
ReweightJet1pT::evaluate(unsigned iJ){
  int lepId = abs(Lepton_pdgId->At(0));
  int cat = (int) (category_WJets->At(0));
  float jet1pt = CleanJet_pt->At(0);
  double weight = 1.;

  if(cat==0 and lepId == 11){
      weight = ele_hard_weight->Eval(jet1pt);
  }

  if(cat==0 and lepId == 13){
      weight = mu_hard_weight->Eval(jet1pt);
  } 

  if(cat==1 and lepId == 11){
      weight = ele_PU_weight->Eval(jet1pt);
  }
  
  if(cat==1 and lepId == 13){
      weight = mu_PU_weight->Eval(jet1pt);
  }


  return weight;
}

void
ReweightJet1pT::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(category_WJets, "category_WJets");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
}
