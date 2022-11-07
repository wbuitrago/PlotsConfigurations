#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TFile.h"
#include "TH1D.h"
#include "TString.h"
#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/VectorUtil.h"

#include <iostream>
using namespace ROOT::Math;
typedef TTreeReaderValue<Double_t> DoubleValueReader;


class ReweightEFTDipoleRecoil : public multidraw::TTreeFunction {
public:
  ReweightEFTDipoleRecoil(const char * weights_file,bool debug);
  ~ReweightEFTDipoleRecoil();

  char const* getName() const override { return "ReweightEFT"; }
  TTreeFunction* clone() const override { return new ReweightEFTDipoleRecoil(_weights_file.Data(),_debug); }

  unsigned getNdata() override { return 1; } 
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;
  

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  void setValues();
  TString _weights_file;
  TFile* _file;
  // TH1D* boost_topcr_mu_weight;
  // TH1D* boost_wjetcr_mu_weight;
  // TH1D* res_wjetcr_ele_weight;
  // TH1D* res_sig_mu_weight;
  // TH1D* res_topcr_ele_weight;
  // TH1D* boost_wjetcr_ele_weight;
  // TH1D* boost_topcr_ele_weight;
  // TH1D* res_wjetcr_mu_weight;
  // TH1D* boost_sig_ele_weight;
  // TH1D* boost_sig_mu_weight;
  // TH1D* res_topcr_mu_weight;
  // TH1D* res_sig_ele_weight;
  TH1D* res_ele_weight;
  TH1D* res_mu_weight;
  TH1D* boost_ele_weight;
  TH1D* boost_mu_weight;
  bool _debug;
  
  IntValueReader * VBS_category;
  IntArrayReader * Lepton_pdgId;
  DoubleValueReader * nJets30;

};

ReweightEFTDipoleRecoil::ReweightEFTDipoleRecoil(const char * weights_file ,bool debug) :
  TTreeFunction(), _weights_file(weights_file),_debug(debug)
{
  _file = new TFile(weights_file,"READ");
  // boost_topcr_mu_weight = (TH1D*)_file->Get('boost_topcr_mu');
  // boost_wjetcr_mu_weight = (TH1D*)_file->Get('boost_wjetcr_mu');
  // res_wjetcr_ele_weight = (TH1D*)_file->Get('res_wjetcr_ele');
  // res_sig_mu_weight = (TH1D*)_file->Get('res_sig_mu');
  // res_topcr_ele_weight = (TH1D*)_file->Get('res_topcr_ele');
  // boost_wjetcr_ele_weight = (TH1D*)_file->Get('boost_wjetcr_ele');
  // boost_topcr_ele_weight = (TH1D*)_file->Get('boost_topcr_ele');
  // res_wjetcr_mu_weight = (TH1D*)_file->Get('res_wjetcr_mu');
  // boost_sig_ele_weight = (TH1D*)_file->Get('boost_sig_ele');
  // boost_sig_mu_weight = (TH1D*)_file->Get('boost_sig_mu');
  // res_topcr_mu_weight = (TH1D*)_file->Get('res_topcr_mu');
  // res_sig_ele_weight = (TH1D*)_file->Get('res_sig_ele');
  // boost_topcr_mu_weight->SetDirectory(0);
  // boost_wjetcr_mu_weight->SetDirectory(0);
  // res_wjetcr_ele_weight->SetDirectory(0);
  // res_sig_mu_weight->SetDirectory(0);
  // res_topcr_ele_weight->SetDirectory(0);
  // boost_wjetcr_ele_weight->SetDirectory(0);
  // boost_topcr_ele_weight->SetDirectory(0);
  // res_wjetcr_mu_weight->SetDirectory(0);
  // boost_sig_ele_weight->SetDirectory(0);
  // boost_sig_mu_weight->SetDirectory(0);
  // res_topcr_mu_weight->SetDirectory(0);
  // res_sig_ele_weight->SetDirectory(0);

  res_ele_weight = (TH1D*)_file->Get("res_sig_ele");
  res_mu_weight = (TH1D*)_file->Get("res_sig_mu");
  boost_ele_weight = (TH1D*)_file->Get("boost_sig_ele");
  boost_mu_weight =(TH1D*) _file->Get("boost_sig_mu");

  res_ele_weight->SetDirectory(0);
  res_mu_weight->SetDirectory(0);
  boost_ele_weight->SetDirectory(0);
  boost_mu_weight->SetDirectory(0);
}

ReweightEFTDipoleRecoil::~ReweightEFTDipoleRecoil(){
  _file->Close();
  // delete boost_topcr_mu_weight;
  // delete boost_wjetcr_mu_weight;
  // delete res_wjetcr_ele_weight;
  // delete res_sig_mu_weight;
  // delete res_topcr_ele_weight;
  // delete boost_wjetcr_ele_weight;
  // delete boost_topcr_ele_weight;
  // delete res_wjetcr_mu_weight;
  // delete boost_sig_ele_weight;
  // delete boost_sig_mu_weight;
  // delete res_topcr_mu_weight;
  // delete res_sig_ele_weight;
  delete res_ele_weight;
  delete res_mu_weight;
  delete boost_ele_weight;
  delete boost_mu_weight;
  delete _file;
}


double
ReweightEFTDipoleRecoil::evaluate(unsigned iJ){
  int vbs_category = *(VBS_category->Get());
  int lepId = abs(Lepton_pdgId->At(0));

  double weight = 1.0;
  double njet;
  if (vbs_category == 0 and lepId == 11){
    njet = *(nJets30->Get());
    weight=   boost_ele_weight->GetBinContent(boost_ele_weight->FindBin(njet));
  }
  if (vbs_category == 0 and lepId == 13){
    njet = *(nJets30->Get());
    weight=  boost_mu_weight->GetBinContent(boost_mu_weight->FindBin(njet));
  }
  if (vbs_category == 1 and lepId == 11){
    njet = *(nJets30->Get());
    weight=  res_ele_weight->GetBinContent(res_ele_weight->FindBin(njet));
  }
  if (vbs_category == 1 and lepId == 13){
    njet = *(nJets30->Get());
    weight=  res_mu_weight->GetBinContent(res_mu_weight->FindBin(njet));
  }
  if (_debug) std::cout << "VBScat: "<<vbs_category << " lepId: "<<lepId << " nJets: "<< njet << " --> weight = "<< weight << std::endl;
  std::cout << "VBScat: "<<vbs_category << " lepId: "<<lepId << " nJets: "<< njet << " --> weight = "<< weight << std::endl;
  return weight;
}

void
ReweightEFTDipoleRecoil::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(VBS_category, "VBS_category");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(nJets30, "nJets30");
}

