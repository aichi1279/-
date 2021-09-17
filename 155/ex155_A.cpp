/*
３つの組の数について、ある２つが等しく、残りの１つがそれらと異なる時、
その３つ組を「かわいそう」である。と言います。
３つの整数をA,B,Cが与えられるので、この３つ組がかわいそうであれば’Yes’を、
そうでなければ、’No'を出力してください。
*/
#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int A,B,C;
  cin>>A>>B>>C;

  if((A==B&&A!=C) || (A==C&&A!=B) || (B==C&&A!=B)){
    cout<<"Yes"<<endl;
  }else{
    cout<<"No"<<endl;
  }

  return 0;
}
