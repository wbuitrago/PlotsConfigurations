#!/bin/bash
## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/work/f/fcetorel/private/work2/combine/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
date=140820
var=mjj
flav=all #could be sf, df, all
workDir=/afs/cern.ch/work/f/fcetorel/private/work2/VBS_OS/CMSSW_10_2_15_patch2/src/PlotsConfigurations/Configurations/VBS_OS/Full2018_v6/FitDir/
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
#
#
#
#echo "nuisance edit drop Vg top CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top QCDscale_VV" >> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Vg dy CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg dy QCDscale_VV" >> ${workspaceDir}/${output}.txt

#only ee categories
#combineCards.py   vbs_ee_lowZ=${datacardDir}//VBS_2j_ee_lowZ/mjj_merged/datacard.txt \
#                  vbs_ee_highZ=${datacardDir}//VBS_2j_ee_highZ/mjj_merged/datacard.txt \
#                  top_ee=${datacardDir}//top_2j_ee/events/datacard.txt \
#                  dy_ee=${datacardDir}//DY_2j_ee/events/datacard.txt \
#> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Vg top_ee CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_ee QCDscale_VV" >> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_ee QCDscale_VV" >> ${workspaceDir}/${output}.txt


#only mm categories
#combineCards.py   vbs_mm_lowZ=${datacardDir}//VBS_2j_mm_lowZ/mjj_merged/datacard.txt \
#                  vbs_mm_highZ=${datacardDir}//VBS_2j_mm_highZ/mjj_merged/datacard.txt \
#                  top_mm=${datacardDir}//top_2j_mm/events/datacard.txt \
#                  dy_mm=${datacardDir}//DY_2j_mm/events/datacard.txt \
#> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Vg top_mm CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Vg top_mm QCDscale_VV" >> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop VgS_L top_mm CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L top_mm QCDscale_VV" >> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Vg vbs_mm_lowZ QCDscale_VV" >> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_hf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_jes" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_lf" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop VgS_L dy_mm QCDscale_VV" >> ${workspaceDir}/${output}.txt
#
#echo "nuisance edit drop Fake_m dy_mm CMS_fake_e_2018 Up" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Fake_m dy_mm CMS_fake_m_2018 Up" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Fake_m dy_mm CMS_fake_stat_e_2018 Up" >> ${workspaceDir}/${output}.txt
#echo "nuisance edit drop Fake_m dy_mm CMS_fake_stat_m_2018 Up" >> ${workspaceDir}/${output}.txt




#All categories togheter
combineCards.py   vbs_lowZ=${datacardDir}//VBS_2j_em_me_lowZ/mjj/datacard.txt \
                  vbs_highZ=${datacardDir}//VBS_2j_em_me_highZ/mjj/datacard.txt \
                  top=${datacardDir}//top_2j_em_me/events/datacard.txt \
                  dy=${datacardDir}//DY_2j_em_me/events/datacard.txt \
                  vbs_ee_lowZ=${datacardDir}//VBS_2j_ee_lowZ/mjj_merged/datacard.txt \
                  vbs_ee_highZ=${datacardDir}//VBS_2j_ee_highZ/mjj_merged/datacard.txt \
                  vbs_mm_lowZ=${datacardDir}//VBS_2j_mm_lowZ/mjj_merged/datacard.txt \
                  vbs_mm_highZ=${datacardDir}//VBS_2j_mm_highZ/mjj_merged/datacard.txt \
                  top_ee=${datacardDir}//top_2j_ee/events/datacard.txt \
                  top_mm=${datacardDir}//top_2j_mm/events/datacard.txt \
                  dy_ee=${datacardDir}//DY_2j_ee/events/datacard.txt \
                  dy_mm=${datacardDir}//DY_2j_mm/events/datacard.txt \
> ${workspaceDir}/${output}.txt

echo "nuisance edit drop Vg top CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop Vg dy CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg dy QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop Vg top_ee CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_ee QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_ee QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop Vg top_mm CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Vg top_mm QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop VgS_L top_mm CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L top_mm QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop Vg vbs_mm_lowZ QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop VgS_L dy_mm CMS_btag_cferr1" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_cferr2" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_hf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_hfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_hfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_jes" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_lf" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_lfstats1_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_btag_lfstats2_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_eff_e_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_eff_hwwtrigger_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm CMS_eff_m_2018" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop VgS_L dy_mm QCDscale_VV" >> ${workspaceDir}/${output}.txt

echo "nuisance edit drop Fake_m dy_mm CMS_fake_e_2018 Up" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Fake_m dy_mm CMS_fake_m_2018 Up" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Fake_m dy_mm CMS_fake_stat_e_2018 Up" >> ${workspaceDir}/${output}.txt
echo "nuisance edit drop Fake_m dy_mm CMS_fake_stat_m_2018 Up" >> ${workspaceDir}/${output}.txt



text2workspace.py ${workspaceDir}/${output}.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/WWewk:r_vbs[1,-10,10]' -o ${workspaceDir}/${output}.root 

echo ${var}":" "" > ${workspaceDir}/fitdiagnostic_${output}.txt
combine -M FitDiagnostics ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --saveNormalizations --saveWithUncertainties >> ${workspaceDir}/fitdiagnostic_${output}.txt
mv higgsCombineTest.FitDiagnostics.mH120.root ${workspaceDir}/fitdiagnostic_${output}.root

echo ${var}":" "" > ${workspaceDir}/significance_${output}.txt
combine -M Significance ${workspaceDir}/${output}.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >>  ${workspaceDir}/significance_${output}.txt


mv higgsCombineTest.Significance.mH120.root ${workspaceDir}/significance_${output}.root

