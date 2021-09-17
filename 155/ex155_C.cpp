/*
N枚の投票用紙があり、i(1<= i <=N)枚目には文字列Siが書かれています。
書かれた回数が最も多い文字列を全て、辞書順で小さい順に出力してください。
*/

#include<iostream>
#include<stdio.h>
#include<set>
#include<map>
#include<algorithm>
using namespace std;

int main(){
  int N;
  cin >> N;
  const int X=N;
  string s,S[X];

  for(int i=0;i<X;i++){
    cin>>s;
    S[i]=s;
  }
  for(int i=0;i<X;i++){
    for(int j=0;j<X;j++){
      if(S[0][i] > S[0][j+1]){
        swap(S[i],S[j]);
      }
    }
  }
  //-------------------------------------------

  map<string,int> word_count;//count
  int max = 0;
  for(int i=0;i<X;i++){
    word_count[S[i]] += 1;
    if(max < word_count[S[i]]){
      max = word_count[S[i]];
    }
  }

  cout<<"-------------------"<<endl;
  map<string,int> flag;//output
  for(int i=0;i < X;i++){
    if(max == word_count[S[i]] && flag[S[i]]!=1){
      cout<<S[i]<<endl;
      flag[S[i]]=1;
    }
  }

  return 0;
}
