/*
高橋君はN科目のテストを受けます。各テストはK点満点であり、点数はそれぞれ0以上の整数です。
高橋君はNー１科目のテストをすでに受けており、i番目の科目のテストの点数でAi点でした。
高橋君の目標は、N科目のテストの平均点をM点以上にすることです。
高橋君が目標を達成するには、最後のテストで最低何点取る必要があるか出力しなさい。

達成不可能な場合は、かわりにー１を出力してください。
*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int N,M,K,A[100];

  cin>>N>>K>>M;
  
  int i=1,sum=0;
  
  while(i<N && cin>>A[i]){
    sum += A[i];
    i++;
  }
  int score = M*N-sum;
  
  if(score>K){
    cout<<-1<<endl;
  }else if(score<0){
    cout<<0<<endl;
  }else{
    cout<<score<<endl;
  }

}
