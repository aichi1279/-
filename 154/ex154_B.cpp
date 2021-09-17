/*
文字列Sが与えられます。Sの全ての文字を’x’で置き換えて出力してください。
*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  string S;
  cin>>S;

  if(S.size()>100){
  cout<<"The length of S is over. "<<endl;
  }

  for(int i=0;i<S.size();i++){
    S[i]='x';
  }

   cout<<S<<endl;
   return 0;
}
