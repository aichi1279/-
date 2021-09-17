/*Repsept
高橋君はKの倍数と７が好きです。
7,77,777,...という数列の中に初めてKの倍数が登場するのは何項目ですか？
存在しない場合は代わりに'-1'を出力してください。
*/

#include<iostream>
#include<stdlib.h>
using namespace std;

int main(){
  int a[1000001];
  int K;
  cin>>K;
  a[1]=7%K;

  for(int i=2;i<=K;i++){
    a[i] = (a[i-1]*10+7) %K;
  }

  //for(int i=1;i<=K;i++){
    //cout<<a[i]<<" ";
  //}

  for(int i=1;i<=K;i++){
    if(a[i]==0){
      cout<<i<<endl;
      return 0;
    }
  }

  cout<<-1<<endl;
}
