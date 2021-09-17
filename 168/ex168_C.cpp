#include<iostream>
#include<stdio.h>
#include<string>
#include<math.h>
using namespace std;


int main(){
  int A,B,H,M;
  cin>>A>>B>>H>>M;
  int w;
  w = H*30 - M*6 ;
  cout<<H*30 - M*6<<endl;
  double D = pow(A,2.0) + pow(B,2.0) - 2 *A *B *cos(w* M_PI/180);
  double answer = sqrt(D);

  cout<<answer<<endl;
  return 0;
}
