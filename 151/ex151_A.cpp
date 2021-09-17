/*
'z'でない英小文字Cが与えられます。アルファベット順でCの次の文字を出力してください。
*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  char C,next_C;

  cin>>C;

  next_C = C+1;
  
  cout<<next_C<<endl;

}
