#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluatorSavedModel.hh"

#include "TFile.h"
#include "TMath.h"
#include "TGraph.h"

#include <cmath>
#include <string>
#include <iostream>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAREADERDNN
#define MVAREADERDNN

typedef TTreeReaderValue<Double_t> DoubleValueReader;

class MVAReaderDNN : public multidraw::TTreeFunction {
public:
  
  MVAReaderDNN(const char* model_path,  const char* transform_path, bool verbose, int category);

  char const* getName() const override { return "MVAReaderDNN"; }
  TTreeFunction* clone() const override { return new MVAReaderDNN(model_path_.c_str(), 
                                           transform_path_.c_str(), verbose, category_); }

  std::string model_path_;
  std::string transform_path_;
  int category_;
  TGraph * dnn_transformation; 
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  ~MVAReaderDNN();
  
  DNNEvaluatorSavedModel* dnn_tensorflow;

  FloatValueReader* detajj{};
  FloatArrayReader* CleanJet_pt{};
  FloatValueReader* mjj{};
  // DoubleValueReader* R_AN{};
  FloatArrayReader* Jet_qgl{};

  // DoubleValueReader* x_ptl1{};
//  DoubleValueReader* ptW{};

  FloatArrayReader* Lepton_eta{};
  FloatArrayReader* Lepton_pt{};
  // DoubleValueReader* Zl1{};
  

/*
- detajj
- jetpt1
- mjj
- ptW
- R
- pt1
- Zl1
- eta1
- QGL1
- QGL2
*/
};


MVAReaderDNN::MVAReaderDNN(const char* model_path, const char* transform_path, bool verbose, int category):
    model_path_(model_path), 
    transform_path_(transform_path),
    verbose(verbose),
    category_(category)
{
    std::cout << "PATH_model: " << model_path_.c_str();
    dnn_tensorflow = new DNNEvaluatorSavedModel(model_path_, verbose);

    // Load the TGRaph used to transform the DNN score
    // The TGraph is the cumulative distribution of the DNN on the signal
    TFile * tf_file = new TFile(transform_path_.c_str(), "READ");
    std::cout << "PATH: " << transform_path_.c_str();
    dnn_transformation = (TGraph*) tf_file->Get("Graph");
    tf_file->Close();
}



double
MVAReaderDNN::evaluate(unsigned)
{

  std::vector<float> input{};

  input.push_back( *(detajj->Get()) );
  input.push_back( CleanJet_pt->At(0) );
  input.push_back( *(mjj->Get()) );
  // std::cout << "sto per fare R_AN" << endl;
  input.push_back( 1. );
  // std::cout << "Fatta R_AN" << endl;
  input.push_back( Jet_qgl->At(0) );
  input.push_back( Jet_qgl->At(1) );

  input.push_back( 1. );
  input.push_back( Lepton_eta->At(0) );
  input.push_back( Lepton_pt->At(0) );
  input.push_back( 1. );
  
  vector<float> dnn_scores = dnn_tensorflow->analyze(input);
  return dnn_transformation->Eval(dnn_scores.at(0));
}

void
MVAReaderDNN::bindTree_(multidraw::FunctionLibrary& _library)
{  
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(mjj, "mjj");
  // _library.bindBranch(x_ptl1, "x_ptl1");
  // std::cout << "sto per bindare R_AN" << endl;
  // _library.bindBranch(R_AN, "R_AN");
  // std::cout << "bindata R_AN" << endl;
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  // _library.bindBranch(Zl1, "Zl1");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Jet_qgl, "Jet_qgl");

}


MVAReaderDNN::~MVAReaderDNN(){  
  delete dnn_transformation;
  delete dnn_tensorflow;

  detajj = nullptr;
  CleanJet_pt = nullptr;
  mjj = nullptr;
  // x_ptl1 = nullptr;
  // R_AN = nullptr;
  Lepton_pt = nullptr;
  // Zl1 = nullptr;
  Lepton_eta = nullptr;
  Jet_qgl = nullptr;
}

#endif 
