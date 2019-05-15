#include <iostream>
#include <cmath>


using namespace std;

Float_t  deltaR(double eta1, double eta2, 
                double phi1, double phi2)
{
        double deta = eta1 - eta2;
        double dphi = phi1 - phi2;
	double deltaR = sqrt(deta*deta + dphi*dphi  );

	return deltaR;



}
