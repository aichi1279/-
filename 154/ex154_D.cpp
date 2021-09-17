/*
N個のサイコロが左から右に一列に並べてあります。
左からi番目のサイコロは１からpi種類の目がそれぞれ等確率ででます。
隣接するK個のサイコロを選んでそれぞれ独立に振った時、
出る目の合計の期待値の最大値を求めなさい。
*/
#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int N,K,P;
  cin>>N>>K;
  const int SIZE=N;
  double p[SIZE];

  if (N<K || N>200000) {
    cout<<" can't calculate it! "<<endl;
    return 0;
  }

  for(int i=0;i<N;i++){//入力
    cin>>P;
    p[i]=P;
  }


  double sum=0;
  for(int i=0;i<N;i++){//期待値計算
    for(int j=1;j <= p[i];j++){
      sum += j / p[i];
    }
    p[i]=sum;
    sum=0;
  }

  double max=0;
  for(int i=0;i<N-K+1;i++){//期待値最大値計算
    sum=0;
    for(int j=i;j<K+i;j++){
      sum += p[j];
    }
    if(max<sum){
      max=sum;
    }
  }

  cout<<max<<endl;
  return 0;

}
