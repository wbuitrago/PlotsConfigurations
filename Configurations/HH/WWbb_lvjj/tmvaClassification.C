using namespace TMVA;


void tmvaClassification(  ) {

TMVA::Tools::Instance();

std::map<std::string,int> Use;

std::cout << std::endl;
std::cout << "==> Start TMVAClassification" << std::endl;

TString outfileName;
outfileName = "BDT_Bagging_nCuts20.root";
TFile* outputFile = TFile::Open( outfileName, "RECREATE" );

TMVA::Factory *factory = new TMVA::Factory( "TMVAClassification", outputFile,
                                            "!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" );

TMVA::DataLoader* dataloader = new TMVA::DataLoader("dataset") ;


//////////////////////////////////////
////////////VARIABLES/////////////////
//////////////////////////////////////
dataloader->AddVariable( "mjj_b", 'F' );
dataloader->AddVariable( "deltaR_lep_wjet", 'F' );
dataloader->AddVariable( "deltaR_b", 'F' );
dataloader->AddVariable( "deltaphi_lep_wjet_high", 'F' );
dataloader->AddVariable( "deltaR_lep_b", 'F' );
dataloader->AddVariable( "deltaphi_lep_b_high", 'F' );
dataloader->AddVariable( "b_pt_high", 'F' );
dataloader->AddVariable( "deltaeta_b", 'F' );
dataloader->AddVariable( "deltaphi_lep_wjet_low", 'F' );

TString fname;

//////////////////////////////////////
////////////SIGNAL////////////////////
//////////////////////////////////////

TString directory = "/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/";
fname = Form ("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/nanoLatino_GluGluToHHTo2B2WToLNu2J__part0.root");
TChain *signal1 = new TChain("Events");
signal1->Add(fname);
signal1->Add("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/nanoLatino_GluGluToHHTo2B2WToLNu2J__part1.root");
signal1->Add("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/nanoLatino_GluGluToHHTo2B2WToLNu2J__part2.root");

//////////////////////////////////////
////////////////BACKGROUNDS///////////
//////////////////////////////////////

fname = Form ("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/nanoLatino_TTToSemiLeptonic__part0.root");
TChain *background = new TChain("Events");
background->Add(fname);
background->Add("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/nanoLatino_TTToSemiLeptonic__part1*");
background->Add("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/nanoLatino_TTToSemiLeptonic__part2*");
//background->Add("/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__HHbblnuSkim2017v1/nanoLatino_TTToSemiLeptonic__part3*");

//////////////////////////////////////
////////////WEIGHTS///////////////////
//////////////////////////////////////
TString eleWP = "mvaFall17V1Iso_WP90";
TString muWP  = "cut_Tight_HWWW";

TString LepWPCut_1l    =  "(Lepton_isTightElectron_"+eleWP+"[0]>0.5 || Lepton_isTightMuon_"+muWP+"[0]>0.5)";
TString LepWPWeight_1l =  "Lepton_tightElectron_"+eleWP+"_IdIsoSF"+"[0]*\
                           Lepton_tightMuon_"+muWP+"_IdIsoSF"+"[0]";

TString LepWPCut    = LepWPCut_1l;
TString LepWPWeight = LepWPWeight_1l;

TString XSWeight   =   "XSWeight";
TString SFweight1l =   "puWeight*\
                        TriggerEffWeight_1l*\
                        Lepton_RecoSF[0]*\
                        EMTFbug_veto";

TString SFweight       = SFweight1l+"*"+LepWPWeight_1l+"*"+LepWPCut_1l+"*PrefireWeight";
TString METFilter_MC   = "METFilter_MC";

Double_t signalWeight     = 1.0;
Double_t backgroundWeight = 1.0;
dataloader->SetInputTrees(signal1, background, signalWeight, backgroundWeight );
dataloader->SetSignalWeightExpression("0.00115228*"+XSWeight+"*"+SFweight+"*"+METFilter_MC);
dataloader->SetBackgroundWeightExpression(XSWeight+'*'+SFweight+'*'+METFilter_MC);

//////////////////////////////////////
////////////CUTS//////////////////////
//////////////////////////////////////
TCut mycuts = "Lepton_pt[0]>=25 && CleanJet_pt[1]>25 && (H_jets[1]!=-1 && W_jets_nearest_massWZ[1]!=-1)";
TCut mycutb = mycuts;

dataloader->PrepareTrainingAndTestTree( mycuts, mycutb,  "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V" );

//////////////////////////////////////
/////////BDT OPTIMIZATION/////////////
//////////////////////////////////////
factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDT",
                      "!H:!V:NTrees=900:MinNodeSize=4%:MaxDepth=3:BoostType=Bagging:SeparationType=CrossEntropy:nCuts=20");

factory->TrainAllMethods();


factory->TestAllMethods();

factory->EvaluateAllMethods();

outputFile->Close();

std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
std::cout << "==> TMVAClassification is done!" << std::endl;

delete factory;
delete dataloader ;

// Launch the GUI for the root macros
if (!gROOT->IsBatch()) TMVAGui( outfileName );

}
