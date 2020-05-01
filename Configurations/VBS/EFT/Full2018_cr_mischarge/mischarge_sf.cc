// modified version to take into account differences 
// between the data and MC measurement of the chargeflip rate

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class misID_sf : public multidraw::TTreeFunction {
public:
  misID_sf();

  char const* getName() const override { return "misID_sf"; }
  TTreeFunction* clone() const override { return new misID_sf(); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader* nLepton;
  IntArrayReader* Lepton_pdgId;  
  FloatArrayReader* Lepton_pt;
  FloatArrayReader* Lepton_eta;

};

misID_sf::misID_sf() :
  TTreeFunction()
{
}

double
misID_sf::evaluate(unsigned)
{
    unsigned nL{*nLepton->Get()};
    if (nL < 2)
        return 0.;

    // more lepton selections
    std::vector<unsigned> iPromptL{};
    iPromptL.reserve(nL);

    for (unsigned iL{0}; iL != nL; ++iL) {
        unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId->At(iL)))};
        if (absId != 11 && absId != 13)
        continue;
        iPromptL.push_back(iL);
    }

    // 2 leptons or more required
    if (iPromptL.size() < 2)
        return 0.; // false
    if (iPromptL.size() > 2){
        if (Lepton_pt->At(iPromptL[2])>10){
            return 0;
        }
    } 


    // ch. flip probability measured from DATA (for different |eta| regions)
    double chargeflip_rate_data[3]={5.53316e-05,3.72575e-04,1.14568e-03};
    // ch. flip probability measured from MC
    double chargeflip_rate_mc[3]={4.65073e-05,2.44799e-04,9.31889e-04};
    // DATA/MC prob. ratios
    double sf[3]={1.18974,1.52196,1.22942}; // not used...


    // keep only ee or emu events
    if(Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1]) != 11*11 &&
       Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1]) != 11*13) 
    {
        return 0;
    }

    // selecting same sign e-e events
    if(Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1]) == 11*11)  {
 
        // assigns |eta| regions to the leptons
        int idx1=0;
        int idx2=0;
        if(abs(Lepton_eta->At(iPromptL[0]))>=0 && abs(Lepton_eta->At(iPromptL[0]))<1.0){
            idx1=0;
        }else if(abs(Lepton_eta->At(iPromptL[0]))>=1.0 && abs(Lepton_eta->At(iPromptL[0]))<1.5){
            idx1=1;
        }else if(abs(Lepton_eta->At(iPromptL[0]))>=1.5 && abs(Lepton_eta->At(iPromptL[0]))<2.5){
            idx1=2;
        }

        if(abs(Lepton_eta->At(iPromptL[1]))>=0 && abs(Lepton_eta->At(iPromptL[1]))<1.0){
            idx2=0;
        }else if(abs(Lepton_eta->At(iPromptL[1]))>=1.0 && abs(Lepton_eta->At(iPromptL[1]))<1.5){
            idx2=1;
        }else if(abs(Lepton_eta->At(iPromptL[1]))>=1.5 && abs(Lepton_eta->At(iPromptL[1]))<2.5){
            idx2=2;
        }

        // compute data mis id sf 
        double _rate1=chargeflip_rate_data[idx1];
        double _rate2=chargeflip_rate_data[idx2];
        double mis_id_sf_data= _rate1*(1-_rate2)+(1-_rate1)*_rate2;

        // compute mc mis id sf
        _rate1=chargeflip_rate_mc[idx1];
        _rate2=chargeflip_rate_mc[idx2];
        double mis_id_sf_mc= _rate1*(1-_rate2)+(1-_rate1)*_rate2;
            
        double corr_w = mis_id_sf_data/mis_id_sf_mc ;
        return corr_w;
    }

    // selecting same sign e-mu events
    if(Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1]) == 11*13)  {
        // select electron (muon chflip prob is neglectable)
        int e_index = 0 ;
        if(abs(Lepton_pdgId->At(iPromptL[0]))==13) e_index = 1 ;
        // assigns |eta| regions to the leptons
        int idx=0;
        if(abs(Lepton_eta->At(iPromptL[e_index]))>=0 && abs(Lepton_eta->At(iPromptL[e_index]))<1.0){
            idx=0;
        }else if(abs(Lepton_eta->At(iPromptL[e_index]))>=1.0 && abs(Lepton_eta->At(iPromptL[e_index]))<1.5){
            idx=1;
        }else if(abs(Lepton_eta->At(iPromptL[e_index]))>=1.5 && abs(Lepton_eta->At(iPromptL[e_index]))<2.5){
            idx=2;
        }
        
        // compute data mis id sf 
        double mis_id_sf_data = chargeflip_rate_data[idx1];
        // compute mc mis id sf
        double mis_id_sf_mc   = chargeflip_rate_mc[idx1];
        double corr_w = mis_id_sf_data/mis_id_sf_mc ;
        return corr_w;
    }


}

void
misID_sf::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
}