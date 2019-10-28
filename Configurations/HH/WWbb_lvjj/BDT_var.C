#include <TMVA/Reader.h>

using namespace std;

TMVA::Reader* reader_BDTweights = new TMVA::Reader();

float mbb_var, dR_lep_w_var, dR_b_var, dphi_lep_w1_var, dR_lep_b_var, dphi_lep_b1_var, b_pt1_var, deta_b_var, dphi_lep_w2_var;



void initReader()
{

    reader_BDTweights->AddVariable("mjj_b",			   &mbb_var);
    reader_BDTweights->AddVariable("deltaR_lep_wjet",              &dR_lep_w_var);
    reader_BDTweights->AddVariable("deltaR_b",                     &dR_b_var);
    reader_BDTweights->AddVariable("deltaphi_lep_wjet_high",       &dphi_lep_w1_var);
    reader_BDTweights->AddVariable("deltaR_lep_b",                 &dR_lep_b_var);
    reader_BDTweights->AddVariable("deltaphi_lep_b_high",          &dphi_lep_b1_var);
    reader_BDTweights->AddVariable("b_pt_high",          &b_pt1_var);
    reader_BDTweights->AddVariable("deltaeta_b",       &deta_b_var);
    reader_BDTweights->AddVariable("deltaphi_lep_wjet_low",       	   &dphi_lep_w2_var);



    TString direction = "";
    direction = "/afs/cern.ch/user/g/govoni/work/Arianna/CMSSW_10_0_2/src/PlotsConfigurations/Configurations/HH/WWbb_lvjj/dataset_true/weights/TMVAClassification_BDT.weights.xml";
    reader_BDTweights->BookMVA("BDT",direction);

}

Float_t BDT_var(float mjj_b,
	            float deltaR_lep_wjet,
	            float deltaR_b,
                float deltaphi_lep_wjet_high,
                float deltaR_lep_b,
                float deltaphi_lep_b_high,
                float b_pt_high,
                float deltaeta_b,
                float deltaphi_lep_b_low)
{
    
    mbb_var = mjj_b;
    dR_lep_w_var = deltaR_lep_wjet;
    dR_b_var = deltaR_b;
    dphi_lep_w1_var = deltaphi_lep_wjet_high;
    dR_lep_b_var = deltaR_lep_b;
    dphi_lep_b1_var = deltaphi_lep_b_high;
    b_pt1_var = b_pt_high;
    deta_b_var = deltaeta_b;
    dphi_lep_w2_var = deltaphi_lep_b_low;


    return reader_BDTweights->EvaluateMVA("BDT");



}
