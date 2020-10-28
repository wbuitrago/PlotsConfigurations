#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/work/f/fcetorel/private/work2/combine/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
date=140820
var=mjj
flav=ee  #could be sf, df, all
workDir=/afs/cern.ch/work/f/fcetorel/private/work2/VBS_OS/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBS_OS/Full2016_v6/FitDir/
workspaceDir=${workDir}/workspace

cd $workDir
output=${flav}_${var}
datacardDir=${workDir}/datacards

#DF categories only

#combineCards.py   vbs_lowZ=${datacardDir}/VBS_2j_em_me_lowZ/mjj/datacard.txt \
#                  vbs_highZ=${datacardDir}/VBS_2j_em_me_highZ/mjj/datacard.txt \
#                  top=${datacardDir}/top_2j_em_me/events/datacard.txt \
#                  dy=${datacardDir}//DY_2j_em_me/events/datacard.txt \
#> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Vg top CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_hf" >> ${workspaceDir}/${output}.txt

## ee categories only

combineCards.py   vbs_ee_lowZ=${datacardDir}//VBS_2j_ee_lowZ/mjj_merged/datacard.txt \
                  vbs_ee_highZ=${datacardDir}//VBS_2j_ee_highZ/mjj_merged/datacard.txt \
                  top_ee=${datacardDir}//top_2j_ee/events/datacard.txt \
                  dy_ee=${datacardDir}//DY_2j_ee/events/datacard.txt \
> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hfstats1_2016" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hfstats2_2016" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lfstats1_2016" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lfstats2_2016" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_eff_e_2016" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_eff_hwwtrigger_2016" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_eff_m_2016" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee QCDscale_VV" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_eff_prefiring_2016 Up" >> ${workspaceDir}/${output}.txt

# mumu categories only

#combineCards.py   vbs_mm_lowZ=${datacardDir}//VBS_2j_mm_lowZ/mjj_merged/datacard.txt \
#                  vbs_mm_highZ=${datacardDir}//VBS_2j_mm_highZ/mjj_merged/datacard.txt \
#                  top_mm=${datacardDir}//top_2j_mm/events/datacard.txt \
#                  dy_mm=${datacardDir}//DY_2j_mm/events/datacard.txt \
#> ${workspaceDir}/${output}.txt



#combineCards.py   vbs_lowZ=${datacardDir}//VBS_2j_em_me_lowZ/mjj/datacard.txt \
#                  vbs_highZ=${datacardDir}//VBS_2j_em_me_highZ/mjj/datacard.txt \
#                  top=${datacardDir}//top_2j_em_me/events/datacard.txt \
#                  dy=${datacardDir}//DY_2j_em_me/events/datacard.txt \
#                  vbs_ee_lowZ=${datacardDir}//VBS_2j_ee_lowZ/mjj_merged/datacard.txt \
#                  vbs_ee_highZ=${datacardDir}//VBS_2j_ee_highZ/mjj_merged/datacard.txt \
#                  vbs_mm_lowZ=${datacardDir}//VBS_2j_mm_lowZ/mjj_merged/datacard.txt \
#                  vbs_mm_highZ=${datacardDir}//VBS_2j_mm_highZ/mjj_merged/datacard.txt \
#                  top_ee=${datacardDir}//top_2j_ee/events/datacard.txt \
#                  top_mm=${datacardDir}//top_2j_mm/events/datacard.txt \
#                  dy_ee=${datacardDir}//DY_2j_ee/events/datacard.txt \
#                  dy_mm=${datacardDir}//DY_2j_mm/events/datacard.txt \
#> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Vg top CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Vg top_ee CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_hfstats1_2016" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_hfstats2_2016" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_lfstats1_2016" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_lfstats2_2016" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_eff_e_2016" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_eff_hwwtrigger_2016" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_eff_m_2016" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee QCDscale_VV" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_eff_prefiring_2016 Up" >> ${workspaceDir}/${output}.txt



text2workspace.py ${workspaceDir}/${output}.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/WWewk:r_vbs[1,-10,10]' -o ${workspaceDir}/${output}.root 

echo ${var}":" "" > ${workspaceDir}/fitdiagnostic_${output}.txt
combine -M FitDiagnostics ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/fitdiagnostic_${output}.txt
mv higgsCombineTest.FitDiagnostics.mH120.root ${workspaceDir}/fitdiagnostic_${output}.root

echo ${var}":" "" > ${workspaceDir}/significance_${output}.txt
combine -M Significance ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >>  ${workspaceDir}/significance_${output}.txt


mv higgsCombineTest.Significance.mH120.root ${workspaceDir}/significance_${output}.root

