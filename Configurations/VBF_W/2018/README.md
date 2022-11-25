
# How to run the analysis --> CMSSW_11_1_4 IS NEEDED FOR DNN OUTPUT VARIABLE!!
To run it on CMSSW_10_6_4 pls comment the dnn variable everywhere
Furtheremore (refer to Giorgio for this) it is needed a customization of https://github.com/UniMiBAnalyses/NNEvaluation/blob/master/DNNTensorflow/src/DNNEvaluatorSavedModel.cpp#L74:

{
void NNEvaluation::DNNEvaluatorSavedModel::open_session(){
    if (session_ready_) return;

    // metaGraph_ = tensorflow::loadMetaGraph(graphPath_); // TODO check what happens if file not present
    // // create a new session and add the graphDef
    // session_ = tensorflow::createSession(metaGraph_, graphPath_);
    tensorflow::GraphDef* graphDef = tensorflow::loadGraphDef(graphPath_);
    session_ = tensorflow::createSession(graphDef);
    session_ready_ = true;
    std::cout << "Tensorflow session ready" <<std::endl;
}  
}
    
# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=tomorrow

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_vbf_w_2018.root rootFile/plots_vbf_w_2018_ALL_*.root
    hadd rootFile/plots_vbf_w_2018.root rootFile/plots_vbf_w_2018_do.root rootFile/prov/plots_vbf_w_2018.root 


# Make plots:
# For this section, at the time being (nov. 2022), it is needed CMSSW10_6_4 (for example) recreating the same path ~/CMSSW 10../src/Plotconfig/config/VBF_W/2018/ and here it is needed utils folder
# this is due to root, i think, because when running mkplot segmentation violation happens!


    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2018.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1 --plotNormalizedDistributions

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2018.root --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2018.root --showIntegralLegend=1  --plotNormalizedDistributionsTHstack
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2018.root --showIntegralLegend=1  --plotNormalizedDistributions

# Make DataCards
    mkDatacards.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2018.root


# Make nuis plot
    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurations/Configurations/VBF_W/2018/datacards/topcr/eta1/shapes/histos_topcr.root  \
     --outputDirPlots ../../../../PlotsConfigurations/Configurations/VBF_W/2018/topcr_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurations/Configurations/VBF_W/2018/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurations/Configurations/VBF_W/2018/samples.py \
     --cutName topcr
