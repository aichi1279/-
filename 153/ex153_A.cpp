/*
サーバルはモンスターと戦っています。
モンスターの体力はHです。
サーバルが攻撃を1回行うとモンスターの体力はA減らすことができます。
攻撃以外の方法でモンスターの体力を減らすことはできません。
モンスターの体力を０以下にすれば、サーバルの勝ちです。
サーバルがモンスターに勝つ為に必要な攻撃回数を求めよ。

*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){

  int H,A;

  cin>>H>>A;

  if(H%A ==0){
    cout<<H/A<<endl;
  }else{
    cout<<(H/A)+1<<endl;
  }

}
