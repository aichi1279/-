/*
あなたはAtCoder王国の入国審査官です。
入国者の書類はいくつかの整数が書かれており、あなたの仕事はこれらが
条件を満たすかを判定することです。
規約では、次の条件を満たす時、またその時に限り、入国を承認をすることになっています。
・書類に書かれている整数のうち、偶数であるものは全て、３または５で割り切れる。
上の規約に従う時、書類にN個の整数A1,A２...Anが書かれた入国者を承認するならば、
’APPROVED'を、しないならば’DENIED’を出力してください。
*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
int N,z;
cin>>N;
const int X = N;
int A[X];

for(int i=0;i<X;i++){
  cin>>z;
  A[i]=z;
}

int count1=0,count2=0;
for(int i=0;i<X;i++){
  if(A[i]%2==0){
    count1++;
    if(A[i]%3==0 || A[i]%5==0){
      count2++;
    }
  }
}

if(count1==count2){
  cout<<"APPROVE"<<endl;
}else{
  cout<<"DENIED"<<endl;
}

return 0;
}
