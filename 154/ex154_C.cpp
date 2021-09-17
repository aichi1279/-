/*
整数A1，A2...Anが与えられます。この整数列のどの２つの要素もお互いに異なるならば、
’Yes’を、そうでないなら’No’を出力してください。
*/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){

  int N,*A,a;
  bool flag = true;
  cin>>N;
  for(int i=0; i<N ;i++){
    cin>>a;
    *(A+i)=a;
  }

  for(int i=0; i<N ;i++){
    for(int j=0; j<N ;j++){
      if(i==j){
        continue;
      }else if(*(A+i) == *(A+j)){
        flag=false;
      }
    }
  }

  if(flag){
    cout<<"Yes"<<endl;
  }else{
    cout<<"No"<<endl;
  }
  return 0;

}
