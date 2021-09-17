#include<iostream>
#include<math.h>
#include <iomanip>
#include <stdlib.h>
using namespace std;


int main(){
  int n;
  cin>> n;
  int x;
  long long  square = 0,sum=0, maxi=0;


  for(int idx=0; idx<n ;idx++){
      cin>>x;
      if(x<0) x *= -1;

      sum += x;
      square += pow(x,2);

      if(maxi<x) maxi = x;
  }

  cout<<sum<<endl;
  cout <<fixed << setprecision(15)<<pow(square, 0.5)<<endl;
  cout<<maxi<<endl;


  return 0;
}
