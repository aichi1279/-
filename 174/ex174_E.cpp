/* E - Logs

丸太がN本あり、それぞれの長さは、A1,A2,A3,...,ANです。
これらの丸太を合計K回まで切ることができます。長さLの丸太を片端から(0<t<L)
の位置で切ると、長さt,L-tの丸太に分かれます。

丸太を合計K回まで切った後最も長い丸太の長さが最小で幾つになるかを求め、
小数点以下を切り上げた値を出力してください。

*/

#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<cmath>
#include<random>
using namespace std;

int main(){
  int N,K;
  cin >> N >>K;

  double A[N];
  int cut[N];
  for(int i=0; i<N ;i++){
    cin >> A[i];
    cut[i]=1;
  }

  double maximum[200]={};
  int cut2[N];
  for(int phase=0;phase<pow(N,K);phase++){
    memcpy(cut2,cut,N);
    double temp[N];
    for(int i=0;i<K;i++){ //探索
      int j=random()%N;
      cut2[j]++;
    }
    for(int i=0;i<N;i++){
      temp[i]=A[i]/cut2[i];
      if(temp[i]>maximum[phase]){
        maximum[phase]=temp[i];
      }
    }

  }
  int i=1;
  double mini=maximum[0];
  while(true){
    if(i==pow(N,K)){
      break;
    }
    if(mini>maximum[i]){
      mini=maximum[i];
    }

  }

  cout<<ceil(mini)<<endl;
  return 0;
}
