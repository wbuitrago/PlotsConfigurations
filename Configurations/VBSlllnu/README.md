# VBS WZ Configuration

This folder includes the VBS WZ configuration for dimension-6 EFT studies. Further information about the fit procedure and the extraction of Wilson coefficient ranges can be found here

https://github.com/elenavernazza/Recofit

# Instructions

Three main folders are predent in the WZ configuration: WZ, WZeu, macros.

The "WZ" folder contains the ultimate configuration for the VBS WZ analysis; the "WZeu" folder is related to preliminary studies that consider only the WZ decay to eemu; the "macros" folder contains some scripts that are used for the extraction of variables, for the individuation of leptons coming from Z and W bosons, and for the definition of some selections.

This guide describes the WZ folder content.

1. conf_WZ_SM

The "conf_WZ_SM" folder contains the configuration for the comparison between WZ SM official samples and WZ SM samples obtained with a private production. The reference for the private sample production can be found here

https://github.com/UniMiBAnalyses/CMSSWGeneration

The comparison is made both for the EWK and QCD component, just plotting the two and looking for deviations.

`mkPlot.py --pycfg=configuration.py --showIntegralLegend=1 --linearOnly --inputFile=rootFile_WZ_SM_l3_2018/plots_VBS_WZ_SM_l3_2018.root --plotFile=plot_EWK.py --outputDirPlots=plotVBS_WZ_SM_l3_2018_EWK --onlyPlot=cratio`

`mkPlot.py --pycfg=configuration.py --showIntegralLegend=1 --linearOnly --inputFile=rootFile_WZ_SM_l3_2018/plots_VBS_WZ_SM_l3_2018.root --plotFile=plot_QCD.py --outputDirPlots=plotVBS_WZ_SM_l3_2018_QCD --onlyPlot=cratio`

2. conf_WZ_BSM

The "conf_WZ_BSM" folder contains the configuration for the dimension-6 EFT analysis. 

In "configuration.py" all the name of the process and the output folders are defined.

In "samples.py" all the samples for the analysis are included:
- WZ SM
- EFT Lin components for each EFT operator under study
- EFT Quad components for each EFT operator under study
- EFT Mixed components for each EFT operators couple
- Backgrounds: WZ QCD, ZZ, Vgamma, ...

In "structure.py" the samples are divided in signal and background.

In "aliases.py" some expressions are defined for the definition of the selections, the variables and the systematic uncertainties.

In "cuts.py" a control region "CR" and different signal regions according to the leptons in the final state are defined: "SR_3e" for eee, "SR_2e_mu" for eemu, "SR_2mu_e" for mumue, "SR_3mu" for mumumu and "SR_3l" for the inclusive final state with all lepton flavours.

In "variables.py" all the variables under study and the ranges are defined.

In "total_nuisances.py" all the systematic uncertainties are included.

Four different "plot.py" files are used.

- plot_CR.py for the control region (also data are shown)

`mkPlot.py --pycfg=configuration.py --showIntegralLegend=1 --linearOnly --inputFile=rootFile_WZ_BSM_l3_2018/plots_VBS_WZ_BSM_l3_2018_1D.root --plotFile=plot_CR.py --outputDirPlots=plotVBS_WZ_l3_2018_CR --onlyPlot=c,cratio --onlyCut=CR`

- plot_SR.py for the blinded signal region

`mkPlot.py --pycfg=configuration.py --showIntegralLegend=1 --linearOnly --inputFile=rootFile_WZ_BSM_l3_2018/plots_VBS_WZ_BSM_l3_2018_1D.root --plotFile=plot_SR.py --outputDirPlots=plotVBS_WZ_l3_2018_SR --onlyPlot=c,cratio`

- plot_BSM_1D.py to plot the BSM distribution of one operator (op) for three different values of the Wilson coefficients (k1,k2,k3)

`mkPlot.py --pycfg=configuration.py --showIntegralLegend=1 --linearOnly --inputFile=rootFile_WZ_BSM_l3_2018/plots_VBS_WZ_BSM_l3_2018_1D.root --plotFile=plot_BSM_1D.py --outputDirPlots=plotVBS_WZ_l3_2018_BSM_1D/cll1 --onlyPlot=cratio --fileFormats=png,pdf`

- plot_BSM_2D.py to plot the BSM distribution of a couple of operators (op) for different values of the Wilson coefficients (k1,k2)

`mkPlot.py --pycfg=configuration.py --linearOnly --inputFile=rootFile_WZ_BSM_l3_2018/plots_VBS_WZ_BSM_l3_2018_2D.root --plotFile=plot_BSM_2D.py --outputDirPlots=plotVBS_WZ_l3_2018_BSM_2D/cHl3_cqq1 --onlyPlot=cratio --onlyVariable=ptj1`

3. conf_WZ_BSM_QCD

The "conf_WZ_BSM_QCD" folder contains the configuration for the dimension-6 EFT analysis, the difference with "conf_WZ_BSM" is that the WZ QCD background is now considered as part of the signal and the EFT contributions in the WZ QCD are considered as well.
The instructions for this folder are similar to the ones presented above. 