#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"

#include <cmath>
#include <string>
#include <iostream>

using namespace std;
using namespace NNEvaluation;

#ifndef DNNSCORE_H
#define DNNSCORE_H

class DNNScore : public multidraw::TTreeFunction {
public:

  DNNScore(const char* model_path, bool verbose);

  char const* getName() const override { return "DNNScore"; }
  TTreeFunction* clone() const override { return new DNNScore(model_path_.c_str(), verbose); }

  bool initialized_ = false;
  std::string model_path_;
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:

  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;

  DNNEvaluator* dnn_tensorflow;
  FloatValueReader* mll{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  FloatValueReader* detall{};
  FloatArrayReader* Lepton_phi{};
  FloatValueReader* dphill{};
  FloatValueReader* mjj{};
  FloatArrayReader* CleanJet_pt{};
  FloatArrayReader* CleanJet_eta{};
  FloatValueReader* detajj{};
  FloatArrayReader* CleanJet_phi{};
  FloatValueReader* dphijj{};
  FloatValueReader* MET_pt{};
};


DNNScore::DNNScore(const char* model_path, bool verbose):
    model_path_(model_path),
    verbose(verbose)
{
    dnn_tensorflow = new DNNEvaluator(model_path_, verbose);
    initialized_ = true;
}


double
DNNScore::evaluate(unsigned)
{

  std::vector<float> input{};
  input.push_back( *(mll->Get()) );
  input.push_back( Lepton_pt->At(0) );
  input.push_back( Lepton_pt->At(1) );
  input.push_back( Lepton_eta->At(0) );
  input.push_back( Lepton_eta->At(1) );
  input.push_back( *(detall->Get()) );
  input.push_back( Lepton_phi->At(0) );
  input.push_back( Lepton_phi->At(1) );
  input.push_back( *(dphill->Get()) );
  input.push_back( *(mjj->Get()) );
  input.push_back( CleanJet_pt->At(0) );
  input.push_back( CleanJet_pt->At(1) );
  input.push_back( CleanJet_eta->At(0) );
  input.push_back( CleanJet_eta->At(1) );
  input.push_back( *(detajj->Get()) );
  input.push_back( CleanJet_phi->At(0) );
  input.push_back( CleanJet_phi->At(1) );
  input.push_back( *(MET_pt->Get()) );


  return dnn_tensorflow->analyze(input);

}

void
DNNScore::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(mll, "mll");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(detall, "detall");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
  _library.bindBranch(dphill, "dphill");
  _library.bindBranch(mjj, "mjj");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(dphijj, "dphijj");
  _library.bindBranch(MET_pt, "MET_pt");
}


#endif