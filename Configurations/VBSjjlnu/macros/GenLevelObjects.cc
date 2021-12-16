#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TFile.h"
#include "TH2D.h"
#include "TString.h"
#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/GenVector/VectorUtil.h"

#include <iostream>
using namespace ROOT::Math;

std::pair<int,int> maxMjjPair(vector<PtEtaPhiMVector> vectors){
    std::pair<int,int> current_max;
    // if (debug_) std::cout << "  - VBS jets" << std::endl;
    double maxMjj = -1.;
    for (long unsigned int i=0; i< vectors.size()-1; ++i){
        for (long unsigned int k=i+1; k<vectors.size() ; ++k){
            double mass = (vectors.at(i) + vectors.at(k)).M();
            // if (debug_) std::cout << "  - "<< i << "," << k<< " mass: "<< mass << std::endl;
            if (mass > maxMjj){
                maxMjj = mass;
                current_max = {i, k};
            }
        }
    }
    return current_max;
}

std::pair<int,int> closest85(vector<PtEtaPhiMVector> vectors, std::pair<int,int> exclude){
    std::pair<int,int> current_max;
    double closest = 1e99;
    for (long unsigned int i=0; i< vectors.size()-1; ++i){
      if (i != exclude.first) {
        for (long unsigned int k=i+1; k<vectors.size() ; ++k){
          if (k != exclude.second){
            double mass_diff = abs((vectors.at(i) + vectors.at(k)).M() - 85);
            if (mass_diff < closest){
                closest = mass_diff;
                current_max = {i, k};
            }
          }
        }
      }
    }
    return current_max;
}

class GenLevelObjects : public multidraw::TTreeFunction {
public:
  GenLevelObjects();
  ~GenLevelObjects(){};

  char const* getName() const override { return "GenLevelObjects"; }
  TTreeFunction* clone() const override { return new GenLevelObjects(); }

  void setValues();
  void beginEvent(long long) override;
  unsigned getNdata() override { return outputValues.size(); } 
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;
  

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  
  std::array<double,32> outputValues;
  
  IntValueReader * VBS_category;
  UIntValueReader* nGenPart{};
  IntArrayReader* GenPart_status{};
  IntArrayReader* GenPart_statusFlags{};
  IntArrayReader* GenPart_pdgId{};
  FloatArrayReader* GenPart_pt{};
  FloatArrayReader* GenPart_eta{};
  FloatArrayReader* GenPart_phi{};
  FloatArrayReader* GenPart_mass{};
  UIntValueReader* nGenJet{};
  FloatArrayReader* GenJet_pt{};
  FloatArrayReader* GenJet_eta{};
  FloatArrayReader* GenJet_phi{};
  FloatArrayReader* GenJet_mass{};
  FloatValueReader* GenMET_phi{};
  FloatValueReader* GenMET_pt{};
};

GenLevelObjects::GenLevelObjects() :
  TTreeFunction(){}

void
GenLevelObjects::beginEvent(long long _iEntry)
{
  setValues();
}


double
GenLevelObjects::evaluate(unsigned iJ)
{
  // 0) VBS category
  // 1) Gen Lepton E
  // 2) Gen lepton Px
  // 3) Gen lepton Py
  // 4) Gen lepton Pz
  // 5) Gen lepton PDGID
  // 6) Gen VBS Jet 1 E
  // 7) Gen VBS Jet 1 Px
  // 8) Gen VBS Jet 1 Py
  // 9) Gen VBS Jet 1 Pz
  // 10) Gen VBS Jet 2 E
  // 11) Gen VBS Jet 2 Px
  // 12) Gen VBS Jet 2 Py
  // 13) Gen VBS Jet 2 Pz
  // 14) Gen VBS Jets Mjj
  // 15) Gen VBS Jets Pt
  // 16) Gen V Jet 1 E
  // 17) Gen V Jet 1 Px
  // 18) Gen V Jet 1 Py
  // 19) Gen V Jet 1 Pz
  // 20) Gen V Jet 2 E
  // 21) Gen V Jet 2 Px
  // 22) Gen V Jet 2 Py
  // 23) Gen V Jet 2 Pz
  // 24) Gen V Jets Mjj
  // 25) Gen V Jets Pt
  // 26) Gen MET phi
  // 27) Gen MET Pt
  // 28) njets
  // 29) nlep
  // 30) n_elec
  // 31) n_mu
  return outputValues[iJ];
}

void
GenLevelObjects::setValues()
{

  int vbs_cat = *(VBS_category->Get());
  
  outputValues[0] = vbs_cat;

  for (int idx = 1; idx < 23; ++idx){
    outputValues[idx] = -999;
  }

  // if (_debug) std:cout << "=========================" << std::endl;
  PtEtaPhiMVector lep;
  int n_good_lep =0;
  int n_el =0;
  int n_mu =0;
  int pdgid = -999;
  for (long unsigned int i= 0; i<*(nGenPart->Get()); i++){
    pdgid =  GenPart_pdgId->At(i);
    if( GenPart_status->At(i)==1 && (GenPart_statusFlags->At(i) & 1)==1 && ( abs(pdgid)==11 || abs(pdgid) == 13) && GenPart_pt->At(i)>10){


      lep = {GenPart_pt->At(i),GenPart_eta->At(i),GenPart_phi->At(i),GenPart_mass->At(i)};
      n_good_lep+=1;


      outputValues[1] = lep.E();
      outputValues[2] = lep.Px();
      outputValues[3] = lep.Py();
      outputValues[4] = lep.Pz();
      outputValues[5] = pdgid;

      if (abs(pdgid)==11) n_el+=1;
      if (abs(pdgid)==13) n_mu+=1;
      // if (_debug) std::cout << "Good lep|  pt: "<< lep.Pt() << " eta: "<< lep.Eta() << " phi:"<< lep.Phi() << std::endl;
    }

  }

  vector<PtEtaPhiMVector> good_jets;
  unsigned nJ{*nGenJet->Get()};
  for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    if (GenJet_pt->At(iJ) < 30.)  continue;

    PtEtaPhiMVector jet {GenJet_pt->At(iJ), GenJet_eta->At(iJ), GenJet_phi->At(iJ), GenJet_mass->At(iJ)};
    if (VectorUtil::DeltaR(jet.Vect(), lep.Vect()) > 0.4){
      good_jets.push_back(jet);
    }
  }

  int njets = good_jets.size();

  if(good_jets.size() > 2){
    // Now we have a list of cleaned GenJets with at least 30 GeV of Pt and we need to take the max mjj pair
    std::pair<int,int> vbs_jets = maxMjjPair(good_jets);
  
    outputValues[6] = good_jets[vbs_jets.first].E();
    outputValues[7] = good_jets[vbs_jets.first].Px();
    outputValues[8] = good_jets[vbs_jets.first].Py();
    outputValues[9] = good_jets[vbs_jets.first].Pz();

    outputValues[10] = good_jets[vbs_jets.second].E();
    outputValues[11] = good_jets[vbs_jets.second].Px();
    outputValues[12] = good_jets[vbs_jets.second].Py();
    outputValues[13] = good_jets[vbs_jets.second].Pz();

    auto vbs_jets_quadri = good_jets[vbs_jets.first] + good_jets[vbs_jets.second];
    outputValues[14] = vbs_jets_quadri.M();
    outputValues[15] = vbs_jets_quadri.Pt();

    if (good_jets.size() > 4){
      std::pair<int,int> v_jets = closest85(good_jets, vbs_jets);
    
      outputValues[16] = good_jets[v_jets.first].E();
      outputValues[17] = good_jets[v_jets.first].Px();
      outputValues[18] = good_jets[v_jets.first].Py();
      outputValues[19] = good_jets[v_jets.first].Pz();

      outputValues[20] = good_jets[v_jets.second].E();
      outputValues[21] = good_jets[v_jets.second].Px();
      outputValues[22] = good_jets[v_jets.second].Py();
      outputValues[23] = good_jets[v_jets.second].Pz();

      auto v_jets_quadri = good_jets[v_jets.first] + good_jets[v_jets.second];
      outputValues[24] = v_jets_quadri.M();
      outputValues[25] = v_jets_quadri.Pt();
    }

  }

  outputValues[26] = *(GenMET_phi->Get());
  outputValues[27] = *(GenMET_pt->Get());

  outputValues[28] = njets;
  outputValues[29] = n_good_lep;
  outputValues[30] = n_el;
  outputValues[31] = n_mu;

  return;
}

void
GenLevelObjects::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nGenPart, "nGenPart");
  _library.bindBranch(GenPart_status, "GenPart_status"),
  _library.bindBranch(GenPart_statusFlags, "GenPart_statusFlags");
  _library.bindBranch(GenPart_pdgId, "GenPart_pdgId");
  _library.bindBranch(GenPart_pt, "GenPart_pt");
  _library.bindBranch(GenPart_eta, "GenPart_eta");
  _library.bindBranch(GenPart_phi, "GenPart_phi");
  _library.bindBranch(GenPart_mass, "GenPart_mass");
  _library.bindBranch(nGenJet, "nGenJet");
  _library.bindBranch(GenJet_pt, "GenJet_pt");
  _library.bindBranch(GenJet_eta, "GenJet_eta");
  _library.bindBranch(GenJet_phi, "GenJet_phi");
  _library.bindBranch(GenJet_mass, "GenJet_mass");
  _library.bindBranch(GenMET_phi, "GenMET_phi");
  _library.bindBranch(GenMET_pt, "GenMET_pt");
  _library.bindBranch(VBS_category, "VBS_category");
}

