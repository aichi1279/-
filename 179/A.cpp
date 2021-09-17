#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

int main(){
  string s;
  cin>>s;
  if(s[s.length()-1]=='s'){
    cout<<s<<"es"<<endl;
  }else{
    cout<<s<<'s'<<endl;
  }
  return 0;

}
