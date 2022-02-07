#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluatorSavedModel.hh"

#include "TMath.h"
#include "TFile.h"
#include "TGraph.h"

#include <cmath>
#include <string>
#include <iostream>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAReader_notTop_H
#define MVAReader_notTop_H

typedef  TTreeReaderValue<Double_t> DoubleValueReader;

class MVAReader_notTop : public multidraw::TTreeFunction {
public:
  
  MVAReader_notTop(const char* model_path, const char* transform_path, bool verbose, int cut);

  char const* getName() const override { return "MVAReader_notTop"; }
  TTreeFunction* clone() const override { return new MVAReader_notTop(model_path_.c_str(), transform_path_.c_str(), verbose, cut_); }

  std::string model_path_;
  std::string transform_path_;
  int cut_;
  TGraph * dnn_transformation; 
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  ~MVAReader_notTop(); 

  DNNEvaluatorSavedModel* dnn_tensorflow;
  // GP variables
  FloatValueReader* mjj{};
  FloatValueReader* detajj{};

  DoubleValueReader* ptj1{};
  TTreeReaderArray<Double_t>* R_j1l1{};
  TTreeReaderArray<Double_t>* R_j1l2{};
  TTreeReaderArray<Double_t>* R_j2l1{};
  TTreeReaderArray<Double_t>* R_j2l2{};
  DoubleValueReader* deltaphijj{};

  TTreeReaderArray<Double_t>* ZeppenfeldDilepton{};
  DoubleValueReader* Lepton_eta1{};
  DoubleValueReader* Lepton_eta2{};
  DoubleValueReader* deltaetall{};
  DoubleValueReader* deltaphill{};

  /*
  TTreeReaderValue<Double_t>* ptj1{};
  TTreeReaderValue<Double_t>* R_j1l1{};
  TTreeReaderValue<Double_t>* R_j1l2{};
  TTreeReaderValue<Double_t>* R_j2l1{};
  TTreeReaderValue<Double_t>* R_j2l2{};
  TTreeReaderValue<Double_t>* deltaphijj{};

  TTreeReaderValue<Double_t>* ZeppenfeldDilepton{};
  TTreeReaderValue<Double_t>* Lepton_eta1{};
  TTreeReaderValue<Double_t>* Lepton_eta2{};
  TTreeReaderValue<Double_t>* deltaetall{};
  TTreeReaderValue<Double_t>* deltaphill{};
  */

 // TTreeReaderArray <Double_t>* cut_index{};
  //  
  //    FloatValueReader* mjj{};
  //    TTreeReaderValue<Double_t>* jetpt1{};
  //    TTreeReaderValue<Double_t>* jetpt2{};
  //    FloatValueReader* detajj{};
  //    FloatValueReader* ptll{};
  //    // TTreeReaderValue<Double_t>* detall{};
  //    // FloatValueReader* met{};
  //    // TTreeReaderValue<Double_t>* dphijj{};
  //    // FloatValueReader* Mll{};
  //    // TTreeReaderValue<Double_t>* dR_jl1{};
  //    // TTreeReaderValue<Double_t>* dR_jl2{};
  //    TTreeReaderValue<Double_t>* Zepp1{};
  //    TTreeReaderValue<Double_t>* Zepp2{};
  //    FloatValueReader* dphill{};
  //    //TTreeReaderValue<Double_t>* qgl_forward{};
  //    //TTreeReaderValue<Double_t>* qgl_central{};
  //    //FloatValueReader* mtw1{};
  //    // FloatValueReader* mtw2{};
  
};

MVAReader_notTop::MVAReader_notTop(const char* model_path,const char* transform_path,  bool verbose, int cut):
    model_path_(model_path), 
    transform_path_(transform_path),
    verbose(verbose),
    cut_(cut)
{
    dnn_tensorflow = new DNNEvaluatorSavedModel(model_path_, verbose);
    
    // Load the TGRaph used to transform the DNN score
    //
    // The TGraph is the cumulative distribution of the DNN on the signal
    TFile * tf_file = new TFile(transform_path_.c_str(), "READ");
    dnn_transformation = (TGraph*) tf_file->Get("cumulative_signal");
    tf_file->Close();
}


double 
MVAReader_notTop::evaluate(unsigned)
{
  // Run only if 
/*
  if ((int)((cut_index->At(0))) != cut_) {
    return -999.;
  }
*/
  //    // std::cout << "cut_index = " << (int)(*(cut_index->Get())) << "; cut =  " << cut_ << std::endl;

  std::vector<float> input{};
 
  // GP variables

  input.push_back((float)* (Lepton_eta1->Get()) );
  input.push_back((float)* (Lepton_eta2->Get()) );
  input.push_back((float) (R_j1l1->At(0)) );
  input.push_back((float) (R_j1l2->At(0)) );
  input.push_back((float) (R_j2l1->At(0)) );
  input.push_back((float) (R_j2l2->At(0)) );
  input.push_back((float) (ZeppenfeldDilepton->At(0)) );
  input.push_back((float)* (deltaetall->Get()) );
  input.push_back((float)* (deltaphijj->Get()) );
  input.push_back((float)* (deltaphill->Get()) );
  input.push_back((float)* (detajj->Get()) );

  input.push_back((float)* (mjj->Get()) );

  input.push_back((float)* (ptj1->Get()) );

 

  // old variables 
 
  //    input.push_back( *(mjj->Get()) );
  //    input.push_back( *(jetpt1->Get()) );
  //    input.push_back( *(jetpt2->Get()) );
  //    input.push_back( TMath::Abs(*(detajj->Get())));
  //    input.push_back( *(ptll->Get()) );
  //    //input.push_back( *(qgl_forward->Get()) );
  //    //input.push_back( *(qgl_central->Get()) );
  //    // input.push_back( *(detall->Get()) );
  //    // input.push_back( *(met->Get()) );
  //    // input.push_back( *(Mll->Get()) );
  //    // input.push_back( *(dR_jl1->Get()) );
  //    // input.push_back( *(dR_jl2->Get()) );
  //    input.push_back( *(Zepp1->Get()) );
  //    input.push_back( *(Zepp2->Get()) );
  //    //input.push_back( *(dphijj->Get()) );
  //    input.push_back( TMath::Abs(*(dphill->Get())));
  //    input.push_back( *(mtw1->Get()) );
  //    // input.push_back( *(mtw2->Get()) );
  std::cout << "Siamo arrivati fin qui"  << std::endl;

  // return dnn_tensorflow->analyze(input).at(0);
  vector<float> dnn_scores = dnn_tensorflow->analyze(input);
  return dnn_transformation->Eval(dnn_scores.at(0));

}

void
MVAReader_notTop::bindTree_(multidraw::FunctionLibrary& _library)
{  
  // GP variables
  _library.bindBranch(mjj, "mjj");
  _library.bindBranch(detajj, "detajj");

  _library.bindBranch(ptj1, "ptj1");
  _library.bindBranch(R_j1l1, "R_j1l1");
  _library.bindBranch(R_j1l2, "R_j1l2");
  _library.bindBranch(R_j2l1, "R_j2l1");
  _library.bindBranch(R_j2l2, "R_j2l2");
  _library.bindBranch(deltaphijj, "deltaphijj");

  _library.bindBranch(ZeppenfeldDilepton, "ZeppenfeldDilepton");
  _library.bindBranch(Lepton_eta1, "Lepton_eta1");
  _library.bindBranch(Lepton_eta2, "Lepton_eta2");
  _library.bindBranch(deltaetall, "deltaetall");
  _library.bindBranch(deltaphill, "deltaphill");

  // old variables
  //    _library.bindBranch(cut_index, "cut_index");
  //    _library.bindBranch(mjj, "mjj");
  //    _library.bindBranch(jetpt1, "jetpt1_al");
  //    _library.bindBranch(jetpt2, "jetpt2_al");
  //    _library.bindBranch(detajj, "detajj");
  //    _library.bindBranch(ptll, "ptll");
  //    _library.bindBranch(Zepp1, "Zepp1_al");
  //    _library.bindBranch(Zepp2, "Zepp2_al");
  //    // _library.bindBranch(detall, "detall_al");
  //    // _library.bindBranch(met, "MET_pt");
  //    _library.bindBranch(dphill, "dphill");
  //    // _library.bindBranch(dphijj, "dphijj_al");
  //    // _library.bindBranch(Mll, "mll");
  //    // _library.bindBranch(dR_jl1, "dR_jl1_al");
  //    // _library.bindBranch(dR_jl2, "dR_jl2_al");
  //    // _library.bindBranch(qgl_forward, "qgl_forward");
  //    // _library.bindBranch(qgl_central, "qgl_central");
  //    _library.bindBranch(mtw1, "mtw1");
  //    // _library.bindBranch(mtw2, "mtw2");
}
MVAReader_notTop::~MVAReader_notTop(){
  delete dnn_transformation;
  delete dnn_tensorflow;

}

#endif
