#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;


int main(){
  int K;
  string S;

  cin>>K>>S;
  string tmp="";

  int i=0;
  while(i<K){
    tmp += S[i];
    i++;
  }


  if(S.size() > K){

    cout<<tmp<<"..."<<endl;
  }else{
    cout<<S<<endl;
  }
  return 0;
}
