/*英大文字のみからなる長さNの文字列Sがあります。
S の連続する部分列（入出力例を御覧下さい）として’ABC’がいくつふくまれるかを求めてください

*/


#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int N,count=0;
  string S;
  
  cin>>N>>S;
  
  if(N<3){
    cout<<"0"<<endl;
  }
  
  for(int i=0;i<N-3;i++){
    if(S[i]=='A'&&S[i+1]=='B'&&S[i+2]=='C'){
      count++;
    }
  }
  cout<<count<<endl;
}
