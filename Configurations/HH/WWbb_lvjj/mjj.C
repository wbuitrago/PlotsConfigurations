#include <iostream>
#include <cmath>


using namespace std;

Float_t  mjj(double eta1, double eta2, 
                 double pt1, double pt2, 
                 double phi1, double phi2)
{

        double m_12 = sqrt(2*pt1*pt2*(cosh(eta1-eta2) - cos(phi1-phi2)));
 
	return m_12;
}

