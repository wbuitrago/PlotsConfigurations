// g++ fit.cpp -o fit `root-config --cflags --glibs`
#include <cstdlib>
#include <ctime>
#include <TApplication.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <TStyle.h>
#include <TColor.h>
#include <TFile.h>
#include <stdio.h>
#include <TLegend.h>


 
#include <TH1D.h>
#include <TF1.h>
#include <TAttFill.h>
#include <TCanvas.h>
#include <TFitResultPtr.h>
#include <TGraphErrors.h>
#include <TObject.h>
#include <TKey.h>
#include <TCollection.h>

using namespace std;


//double fitFunz(const double * x, const double * par){
 //  return par[0] - par[1]*erf((x[0]-par[2])/par[3]) + par[4]*erf((x[0]-par[5])/par[6]);
//}

double fitFunz(const double * x, const double * par){
    return par[0] - par[1]*erf((x[0]-par[2])/par[3]);
}

int main(int argc,char**argv){ 
//hardjet region
    TFile f("rootFile_H/plots_RWH_vbf_w_2018.root");
  //  TFile f("rootFile/plots_RW_vbf_w_2018.root");

    TDirectory* dir = (TDirectory*)f.Get("hardWJ-mtw/pt1");

    TH1D* pt1_hardJets = (TH1D*)dir->Get("histo_Wjets_HT_hardJets");
    TH1D* pt1_DATA_H = (TH1D*)dir->Get("histo_DATA");

    TIter keyList(dir->GetListOfKeys());
    TKey *key;
    while ((key = (TKey*)keyList())) {
        TClass *cl = gROOT->GetClass(key->GetClassName());
        if (!cl->InheritsFrom("TH1")) continue;
        TObject *obj = (TObject*)key->ReadObj();
        const char *name = obj->GetName();
        string obj_name = name;
        string h_DATA = "histo_DATA";
        string h_WJ_hard = "histo_Wjets_HT_hardJets";
        if(obj_name != h_DATA && obj_name != h_WJ_hard) {
            TH1 *h = (TH1*)key->ReadObj();
            pt1_DATA_H->Add(h,-1);
        }
    }

    bool division1 = false;
    division1 = pt1_DATA_H->Divide(pt1_hardJets);
    if (division1 == false) {
        cout << "error in division 1" << endl;
    }

//PU region

    TFile f1("rootFile_PU/plots_RWPU_vbf_w_2018.root");
    dir = (TDirectory*)f1.Get("WJetsPUCRmtw1/pt1");

    TH1D* pt1_DATA_PU = (TH1D*)dir->Get("histo_DATA");
    TH1D* pt1_PU = (TH1D*)dir->Get("histo_Wjets_HT_PUJets");

    keyList = dir->GetListOfKeys();
    while ((key = (TKey*)keyList())) {
        TClass *cl = gROOT->GetClass(key->GetClassName());
        if (!cl->InheritsFrom("TH1")) continue;
        TObject *obj = (TObject*)key->ReadObj();
        const char *name = obj->GetName();
        string obj_name = name;
        string h_DATA = "histo_DATA";
        string h_WJ_PU = "histo_Wjets_HT_PUJets";
        if(obj_name != h_DATA && obj_name != h_WJ_PU) {
            TH1 *h = (TH1*)key->ReadObj();
            pt1_DATA_PU->Add(h,-1);
        }
    }
    cout << "pt1 :" << pt1_DATA_PU->GetEntries() << endl;
    bool division2 = false;
    division2 = pt1_DATA_PU->Divide(pt1_PU);
    if (division2 == false) {
        cout << "error in division 2" << endl;
        return 1;
    }

    TF1* fitH = new TF1("fitH",fitFunz,0,400,4);
    fitH->SetLineColor(kBlue);

    fitH->SetParameter(0,1);
    fitH->SetParameter(1,0.1);
    fitH->SetParameter(2,10);
    fitH->SetParameter(3,10);
   // fitH->SetParameter(4,1);
   // fitH->SetParameter(5,1);
   // fitH->SetParameter(6,1);

    pt1_DATA_H->Fit("fitH");

    TF1* fitPU = new TF1("fitPU",fitFunz,0,200,4);
    fitPU->SetLineColor(kBlue);

    fitPU->SetParameter(0,1);
    fitPU->SetParameter(1,0.1);
    fitPU->SetParameter(2,14);
    fitPU->SetParameter(3,8);
    //fitPU->SetParameter(4,0.07);
    //fitPU->SetParameter(5,50);
    //fitPU->SetParameter(6,40);

    pt1_DATA_PU->Fit("fitPU");
    gStyle->SetOptFit(1112);

//object rename
    TH1D *RWH = (TH1D*)pt1_DATA_H->Clone("Reweighting_H");
    TH1D *RWPU = (TH1D*)pt1_DATA_PU->Clone("Reweighting_PU");
    string outFile = "result_pt.root";

	TFile* file1 = new TFile(outFile.c_str(), "RECREATE"); 
    file1->WriteTObject(RWH);
    file1->WriteTObject(RWPU);
    file1->Close();


    return 0;
}