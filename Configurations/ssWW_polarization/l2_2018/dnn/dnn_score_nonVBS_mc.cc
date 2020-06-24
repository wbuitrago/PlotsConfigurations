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

#ifndef DNNSCORENONVBS_H
#define DNNSCORENONVBS_H

class DNNScorenonVBS : public multidraw::TTreeFunction {
public:

  DNNScorenonVBS(const char* model_path, bool verbose);

  char const* getName() const override { return "DNNScorenonVBS"; }
  TTreeFunction* clone() const override { return new DNNScorenonVBS(model_path_.c_str(), verbose); }

  bool initialized_ = false;
  std::string model_path_;
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:

  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  DNNEvaluator* dnn_tensorflow;
  FloatValueReader* mjj{};
  FloatValueReader* detajj{};
  FloatValueReader* dphijj{};
  UIntValueReader* nLepton{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  UIntValueReader* nCleanJet{};
  FloatArrayReader* CleanJet_pt{};
  FloatArrayReader* CleanJet_eta{};
  FloatValueReader* MET_pt{};
  FloatValueReader* ptll{};
};


DNNScorenonVBS::DNNScorenonVBS(const char* model_path, bool verbose):
    model_path_(model_path),
    verbose(verbose)
{
    dnn_tensorflow = new DNNEvaluator(model_path_, verbose);
    initialized_ = true;
}

double
DNNScorenonVBS::evaluate(unsigned)
{
  unsigned nL{*nLepton->Get()};
  unsigned nJ{*nCleanJet->Get()};
  if(nL<2 || nJ<2){
    return -999.;
  }
  std::vector<float> input{};
  input.push_back( *(mjj->Get()) );
  input.push_back( *(detajj->Get()) );
  input.push_back( *(dphijj->Get()) );
  input.push_back( CleanJet_pt->At(0) );
  input.push_back( CleanJet_pt->At(1) );
  input.push_back( Lepton_pt->At(0) );
  input.push_back( Lepton_pt->At(1) );
  input.push_back( *(MET_pt->Get()) );
  input.push_back( *(ptll->Get()) );
  float _detajj=*(detajj->Get());
  float zlep1=std::abs((Lepton_eta->At(0)-(CleanJet_eta->At(0)+CleanJet_eta->At(1))/2)/_detajj);
  float zlep2=std::abs((Lepton_eta->At(1)-(CleanJet_eta->At(0)+CleanJet_eta->At(1))/2)/_detajj);
  input.push_back(zlep1);
  input.push_back(zlep2);

  //aliases['zlep1'] = {'expr' : '(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj'}
  return dnn_tensorflow->analyze(input);

}
void
DNNScorenonVBS::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(mjj, "mjj");
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(dphijj, "dphijj");
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(nCleanJet, "nCleanJet");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(MET_pt, "MET_pt");
  _library.bindBranch(ptll, "ptll");
}

#endif