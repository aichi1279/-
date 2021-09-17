#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;

int main(){
  int N;
  cin>>N;

  string s;
  int c_AC=0,c_WA=0,c_TLE=0,c_RE=0;
  for(int i=0;i<N;i++){
    cin>>s;
    if(s=="AC\n"){
      c_AC++;
    }else if(s=="WA\n"){
      c_WA++;
    }else if(s=="TLE\n"){
      c_TLE++;
    }else if(s=="RE\n"){
      c_RE++;
    }
  }


  for(int i=0;i<4;i++){
    int fir = std::max(c_AC, c_WA);
    int thr = std::max(fir, c_TLE);
    int sec = std::max(thr, c_RE);
    if(sec ==c_AC){cout<<"AC x "<<sec<<endl; c_AC=-1;}
    else if(sec ==c_WA){cout<<"WA x "<<sec<<endl; c_WA=-1;}
    else if(sec ==c_TLE){cout<<"TLE x "<<sec<<endl; c_TLE=-1;}
    else if(sec ==c_RE){cout<<"RE x "<<sec<<endl; c_RE=-1;}
  }
return 0;
}
