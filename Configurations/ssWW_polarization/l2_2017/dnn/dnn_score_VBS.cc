#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"

#include <cmath>
#include <string>
#include <iostream>
#include "TLorentzVector.h"

using namespace std;
using namespace NNEvaluation;

#ifndef DNNSCOREVBS_H
#define DNNSCOREVBS_H

class DNNScoreVBS : public multidraw::TTreeFunction {
public:

  DNNScoreVBS(const char* model_path, bool verbose);

  char const* getName() const override { return "DNNScoreVBS"; }
  TTreeFunction* clone() const override { return new DNNScoreVBS(model_path_.c_str(), verbose); }

  bool initialized_ = false;
  std::string model_path_;
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:

  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  DNNEvaluator* dnn_tensorflow;
  UIntValueReader* nLepton{};
  IntArrayReader* Lepton_pdgId{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  FloatValueReader* detall{};
  FloatArrayReader* Lepton_phi{};
  FloatValueReader* dphill{};
  FloatValueReader* mll{};
  FloatValueReader* ptll{};
  FloatValueReader* mTi{};
  UIntValueReader* nCleanJet{};
  FloatArrayReader* CleanJet_pt{};
  FloatArrayReader* CleanJet_eta{};
  FloatValueReader* dphijj{};
  FloatArrayReader* CleanJet_phi{};
  IntArrayReader* CleanJet_jetIdx{};
  FloatArrayReader* Jet_mass{};
  FloatValueReader* detajj{};
  FloatValueReader* METFixEE2017_pt{};
};


DNNScoreVBS::DNNScoreVBS(const char* model_path, bool verbose):
    model_path_(model_path),
    verbose(verbose)
{
    dnn_tensorflow = new DNNEvaluator(model_path_, verbose);
    initialized_ = true;
}

double
DNNScoreVBS::evaluate(unsigned)
{
  unsigned nL{*nLepton->Get()};
  unsigned nJ{*nCleanJet->Get()};
  if(nL<2 || nJ<2){
    return -999.;
  }

  std::vector<float> input{};
  input.push_back( *(dphijj->Get()) );
  input.push_back( CleanJet_pt->At(0) );
  input.push_back( CleanJet_pt->At(1) );
  input.push_back( Lepton_pt->At(0) );
  input.push_back( Lepton_pt->At(1) );
  input.push_back( *(dphill->Get()) );
  input.push_back( *(mll->Get()) );
  input.push_back( *(METFixEE2017_pt->Get()) );
  input.push_back( *(ptll->Get()) );
  input.push_back( *(mTi->Get()) );
  float _detajj=*(detajj->Get());
  float zlep1=std::abs((Lepton_eta->At(0)-(CleanJet_eta->At(0)+CleanJet_eta->At(1))/2)/_detajj);
  float zlep2=std::abs((Lepton_eta->At(1)-(CleanJet_eta->At(0)+CleanJet_eta->At(1))/2)/_detajj);
  input.push_back(zlep1);
  input.push_back(zlep2);

  //drjll
  double lepton_mass0;
  double lepton_mass1;
  if (abs(Lepton_pdgId->At(0))==13){
    lepton_mass0=0.1057128;
  }else{
    lepton_mass0=0.000511;
  }

  if (abs(Lepton_pdgId->At(1))==13){
    lepton_mass1=0.1057128;
  }else{
    lepton_mass1=0.000511;
  }
    TLorentzVector pl0,pl1,j0,j1;
    pl0.SetPtEtaPhiM(Lepton_pt->At(0),
                    Lepton_eta->At(0),
                    Lepton_phi->At(0),
                    lepton_mass0);
    pl1.SetPtEtaPhiM(Lepton_pt->At(1),
                    Lepton_eta->At(1),
                    Lepton_phi->At(1),
                    lepton_mass1);
    j0.SetPtEtaPhiM(CleanJet_pt->At(0),
                    CleanJet_eta->At(0),
                    CleanJet_phi->At(0),
                    Jet_mass->At(CleanJet_jetIdx->At(0)));
    j1.SetPtEtaPhiM(CleanJet_pt->At(1),
                    CleanJet_eta->At(1),
                    CleanJet_phi->At(1),
                    Jet_mass->At(CleanJet_jetIdx->At(1)));
    TLorentzVector pll;
    pll=pl0+pl1;
    float drj0ll=j0.DeltaR(pll);
    float drj1ll=j1.DeltaR(pll);

  input.push_back(drj0ll);
  input.push_back(drj1ll);
  float pt_ratio=(Lepton_pt->At(0)+Lepton_pt->At(1))/(CleanJet_pt->At(0)+CleanJet_pt->At(1));
  input.push_back(pt_ratio);

  //aliases['zlep1'] = {'expr' : '(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj'}
  return dnn_tensorflow->analyze(input);

}

void
DNNScoreVBS::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(detall, "detall");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
  _library.bindBranch(dphill, "dphill");
  _library.bindBranch(mll, "mll");
  _library.bindBranch(ptll, "ptll");
  _library.bindBranch(mTi, "mTi");
  _library.bindBranch(nCleanJet, "nCleanJet");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(dphijj, "dphijj");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");
  _library.bindBranch(Jet_mass, "Jet_mass");
  _library.bindBranch(dphijj, "dphijj");
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(METFixEE2017_pt, "METFixEE2017_pt");
}

#endif