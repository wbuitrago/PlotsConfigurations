// run command:
// root -l -e ".x plot.cxx(0,500,25)" -q

void plot(int var_number,int m, int detajj) {

    TString filename = "../rootFile_VBS_SS_interf_test_mar13/plots_VBS_SS_interf_test_mar13.root";

    TCanvas *c1 = new TCanvas("test","test",800,800);
    
    auto * spad1 = new TPad("spad1","The first subpad",0.0,0.54,1.0,1.0);
    spad1->Draw();
    spad1->cd();
    

    TString var ;
    TString plot_var ;

    if(var_number == 0) 
    {
        // mjj case
        var = "mjj_v2";
        plot_var = "m jj [GeV]";
    }
    if (var_number == 1)
    {
        // detajj case
        var = "detajj";
        plot_var = "deta jj ";
    }
    if (var_number == 2)
    {
        // second jet pt case
        var = "jetpt2";
        plot_var = "2nd jet pt [GeV]";
    }
    if (var_number == 3)
    {
        // dilepton invariant mass
        var = "mll";
        plot_var = "m ll [GeV]";
    }
    
    // setting up titles and cut names etc...
    TString title_name , cut;
    cut.Form("SS_sr_m%dd%d_emu",m,detajj);
    title_name.Form("SS sr emu | m_{jj}>%d GeV | d#eta_{jj}> %1.1f  ",m,(float)detajj/10.);
    
    cout << title_name << endl << cut << endl ;

    TFile *f = new TFile(filename);

    // needed to make correct error propagation in histogram operations
    TH1::SetDefaultSumw2(1);

    // EWK histogram    
    TH1D *histo_ewk ;
    gDirectory->GetObject(cut + "/" + var + "/histo_WpWp_EWK_mg",histo_ewk) ;
    histo_ewk->SetFillColor(kAzure);
    histo_ewk->SetLineColor(kAzure);

    // QCD histogram
    TH1D *histo_qcd ;
    gDirectory->GetObject(cut + "/" + var + "/histo_WW_QCD",histo_qcd) ;
    histo_qcd->SetFillColor(kGreen);
    histo_qcd->SetLineColor(kGreen);

    // stack EWK and QCD
    THStack * my_stack = new THStack("bkg","bkg");
    my_stack->SetTitle(title_name);
    my_stack->Add(histo_qcd);
    my_stack->Add(histo_ewk);

    
    // EWK+QCD+INTERFERENCE histogram
    TH1D *histo_ewk_qcd ;
    gDirectory->GetObject(cut + "/" + var + "/histo_WW_EWK_QCD",histo_ewk_qcd) ;
    //histo_ewk_qcd->SetFillColor(kRed);
    histo_ewk_qcd->SetLineColor(kRed);
    histo_ewk_qcd->SetLineWidth(2);

    THStack * my_stack_signal = new THStack("signal","signal");
    my_stack_signal->Add(histo_ewk_qcd);

    // draws
    

    my_stack->Draw("HIST");
    my_stack->GetXaxis()->SetTitle(plot_var);
    my_stack->GetXaxis()->SetTitleOffset(0.8);
    my_stack->GetXaxis()->SetTitleSize(0.05);
    my_stack->GetYaxis()->SetTitle("Events");
    my_stack->GetYaxis()->SetTitleOffset(0.5);
    my_stack->GetYaxis()->SetTitleSize(0.05);
    
    
    my_stack_signal->Draw("HIST same");
 
    if (my_stack_signal->GetMaximum() > my_stack->GetMaximum() ) {
        cout << "hey! wrong maximum! Let's fix it..." << endl;
        my_stack->SetMaximum(my_stack_signal->GetMaximum());
    }

    // computing integrals...
    float ewk_qcd_int = histo_ewk_qcd->Integral();
    float ewk_int = histo_ewk->Integral();
    float qcd_int = histo_qcd->Integral();

    ofstream outfile;
    outfile.open("make_plot_log.txt",std::ios_base::app);

    outfile << title_name 
        // << "WpWpJJ_EWK_QCD\t" << ewk_qcd_int << endl
        // << "WpWpJJ_QCD\t" << qcd_int << endl
        // << "WpWpJJ_EWK\t" << ewk_int << endl 
        << "interference: " << (ewk_qcd_int - (ewk_int + qcd_int) ) / (ewk_int + qcd_int) << endl << endl;
    
    // ewk
    TString legend_ewk ;
    legend_ewk.Form("WpWpJJ_EWK [%3.1f]",ewk_int);
    // qcd
    TString legend_qcd ;
    legend_qcd.Form("WpWpJJ_QCD [%3.1f]",qcd_int);
    // qcd ewk
    TString legend_ewk_qcd ;
    legend_ewk_qcd.Form("WpWpJJ_EWK_QCD [%3.1f]",ewk_qcd_int);

    auto legend = new TLegend(0.6,0.7,0.88,0.88);
    //legend->SetHeader("Legend","C"); // option "C" allows to center the header
    legend->AddEntry(histo_ewk_qcd,legend_ewk_qcd,"f");
    legend->AddEntry(histo_ewk,legend_ewk,"f");
    legend->AddEntry(histo_qcd,legend_qcd,"f");
    legend->Draw();
    gPad->SetGrid();
    
    /*****************************************/
    /********* ratio of histograms ***********/
    /*****************************************/
    
    // pad settings...
    c1->cd();
    auto * spad2 = new TPad("spad2","The second subpad",0.0,0.27,1.0,0.54);
    spad2->Draw();
    spad2->cd();

    TH1D * h_sum   = (TH1D*) histo_ewk->Clone();
    h_sum->Add(histo_qcd);  // ewk + qcd sum
    TH1D * h_ratio = (TH1D*) histo_ewk_qcd->Clone();
    h_ratio->Divide(h_sum);
    h_ratio->SetLineColor(kBlack);

    h_ratio->SetTitle("");
    // gStyle->SetOptTitle(0);
    h_ratio->GetYaxis()->SetRangeUser(0.7,1.3);
    h_ratio->GetYaxis()->SetLabelSize(0.05);
    h_ratio->GetXaxis()->SetLabelSize(0.05);

    h_ratio->GetYaxis()->SetTitle("Ratio");
    h_ratio->GetYaxis()->SetTitleOffset(0.3);
    h_ratio->GetYaxis()->SetTitleSize(0.08);

    h_ratio->GetXaxis()->SetTitleOffset(1);
    h_ratio->GetXaxis()->SetTitleSize(0.08);
    // h_ratio->GetXaxis()->SetTitle(plot_var);

    h_ratio->SetMarkerStyle(8);
    h_ratio->Draw();
    gPad->SetGrid();
    gStyle->SetOptStat("");

    TLine *l1 = new TLine(spad2->GetUxmin(),1.0,spad2->GetUxmax(),1.0);
    l1->SetLineWidth(2);
    l1->SetLineStyle(2);
    l1->SetLineColor(kGray+3);
    l1->Draw();

    /*****************************************/
    /********* diff. of histograms ***********/
    /*****************************************/

    // pad settings...
    c1->cd();
    auto * spad3 = new TPad("spad3","The third subpad",0.0,0.0,1.0,0.27);
    spad3->Draw();
    spad3->cd();

    TH1D * h_diff = (TH1D*) histo_ewk_qcd->Clone();
    h_diff->Add(h_sum,-1);
    // h_diff->Divide(h_sum); //...normalization? if you want you can..

    h_diff->SetLineColor(kBlack);
    
    h_diff->SetTitle("");
    //gStyle->SetOptTitle(0);
    //h_diff->GetYaxis()->SetRangeUser(-1,1);
    
    double range, aux = 0;
    range = fabs(h_diff->GetMaximum()) + 0.5 ; 
    aux   = fabs(h_diff->GetMinimum()) + 0.5 ;
    if (range < aux) range = aux ;

    h_diff->GetYaxis()->SetRangeUser(-range,+range);    
    
    h_diff->GetYaxis()->SetLabelSize(0.05);
    h_diff->GetXaxis()->SetLabelSize(0.05);
    h_diff->GetYaxis()->SetTitleSize(0.08);
    h_diff->GetXaxis()->SetTitleSize(0.05);
    h_diff->GetYaxis()->SetTitle("Difference");
    h_diff->GetYaxis()->SetTitleOffset(0.3);
    h_diff->GetXaxis()->SetTitleOffset(1);
    //h_diff->GetXaxis()->SetTitle(plot_var);

    h_diff->SetMarkerStyle(8);
    h_diff->Draw();
    gPad->SetGrid();
    gStyle->SetOptStat("");

    TLine *l2 = new TLine(spad3->GetUxmin(),0.0,spad3->GetUxmax(),0.0);
    l2->SetLineWidth(2);
    l2->SetLineStyle(2);
    l2->SetLineColor(kGray+3);
    l2->Draw();

    
    //final prints
    c1->Print(cut + "_" + var + ".png","png");
    //log plots
    spad1->SetLogy();
    c1->Print("log_" + cut + "_" + var + ".png","png");
    return ;
}