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
  //~MVAReaderDNN();
  
  DNNEvaluatorSavedModel* dnn_tensorflow;

  FloatValueReader* detajj{};
  // DoubleValueReader* jetpt1{};
  // FloatValueReader* mjj{};
  // DoubleValueReader* R{};
  // DoubleValueReader* QGL1{};
  // DoubleValueReader* QGL2{};

  // DoubleValueReader* ptW{};
  
  // DoubleValueReader* pt1{};
  // DoubleValueReader* Zl1{};
  // DoubleValueReader* eta1{};

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
    dnn_tensorflow = new DNNEvaluatorSavedModel(model_path_, verbose);

    // Load the TGRaph used to transform the DNN score
    // The TGraph is the cumulative distribution of the DNN on the signal
    TFile * tf_file = new TFile(transform_path_.c_str(), "READ");
    dnn_transformation = (TGraph*) tf_file->Get("Graph");
    tf_file->Close();
}



double
MVAReaderDNN::evaluate(unsigned)
{

  std::vector<float> input{};

  input.push_back( *(detajj->Get()) );
  // input.push_back( *(jetpt1->Get()) );
  // input.push_back( *(mjj->Get()) );
  // input.push_back( *(ptW->Get()) );
  // input.push_back( *(R->Get()) );
  // input.push_back( *(pt1->Get()) );
  // input.push_back( *(Zl1->Get()) );
  // input.push_back( *(eta1->Get()) );
  // input.push_back( *(QGL1->Get()) );
  // input.push_back( *(QGL2->Get()) );
  
  vector<float> dnn_scores = dnn_tensorflow->analyze(input);
  return dnn_transformation->Eval(dnn_scores.at(0));
}

void
MVAReaderDNN::bindTree_(multidraw::FunctionLibrary& _library)
{  
  _library.bindBranch(detajj, "detajj");
  // _library.bindBranch(jetpt1, "jetpt1");
  // _library.bindBranch(mjj, "mjj");
  // _library.bindBranch(ptW, "ptW");
  // _library.bindBranch(R, "R");
  // _library.bindBranch(pt1, "pt1");
  // _library.bindBranch(Zl1, "Zl1");
  // _library.bindBranch(eta1, "eta1");
  // _library.bindBranch(QGL1, "QGL1");
  // _library.bindBranch(QGL2, "QGL2");


}


// MVAReaderDNN::~MVAReaderDNN(){  
//   delete dnn_transformation;
//   delete dnn_tensorflow;

//   detajj = nullptr;
//   jetpt1 = nullptr;
//   mjj = nullptr;
//   ptW = nullptr;
//   R = nullptr;
//   pt1 = nullptr;
//   Zl1 = nullptr;
//   eta1 = nullptr;
//   QGL1 = nullptr;
//   QGL2 = nullptr;
// }

#endif 
