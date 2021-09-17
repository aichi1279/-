/*
ある町に、N人のすぬけ君（すぬけ君１、すぬけ君２,...,N）が住んでいます。

この町には、K種類のお菓子（お菓子1、お菓子2,...,K）

 */

#include<iostream>
#include<stdio.h>
using namespace std;
int main（）｛

int N,K,*d,*A;

cin>>N>>K;

for(int i=1;i<=N;i++){
  *(d+i)=i;
 }

for(int j=1;j<
