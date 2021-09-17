/*
1以上　N以下の整数であって、１０進法で表した時に、０でない数字が
ちょうどK個あるようなものの個数を求めなさい。
*/
#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int N,K;
  cin>>N>>K;
  const int X = N;
  int H[X];
  //--------------------------

  for(int i=0;i<X;i++){
    H[i]=i+1;
  }
  int answer = 0;
  for(int i=0;i<X;i++){
    int count =0;
    int tmp=H[i];
    while(tmp!=0){
      if(tmp%10!=0){
        count++;
      }
      tmp = tmp/10;
    }
    if(count == K){
      answer++;
    }
  }
  //----------------------------
  cout<<answer<<endl;
  return 0;
}
