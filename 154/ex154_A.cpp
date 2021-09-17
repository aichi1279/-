/*
文字列Sの書かれたボールがA個、文字列Tの書かれたボールがB個あります。
高橋君は、文字列Uの書かれたボールを１個選んで捨てました。
文字列S,Tの書かれたボールがそれぞれ何個残っているか求めなさい。*/

#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

int main(){
  string S,T,N;
  int A,B;

  cin>>S>>T;
  cin>>A>>B;
  cin>>N;

  if(S == N){
    A--;
  }else if(T == N){
    B--;
  }

  cout<<A<<" "<<B<<endl;

  return 0;

}
