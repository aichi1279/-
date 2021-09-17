#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
using namespace std;

int main(){

  int N=0;
  cin>>N;
  vector<string> dataSeq;
  string s;

  cin>>s;

  int count=0,tmp=0;
  for(int start=0; start<s.size()-1 ;start++){
    for(int end=N-1; end>start ;end--){
      dataSeq.push_back(s.substr(start,end-start+1)) ;
    }
  }

  for(int m=0 ;m< dataSeq.size() ;m++){
    int a=0,t=0,c=0,g=0;
    for(int i=0; i< dataSeq[m].size() ;i++){
      if(dataSeq[m][i]=='A'){
        a++;
      }else if(dataSeq[m][i]=='T'){
        t++;
      }else if(dataSeq[m][i]=='C'){
        c++;
      }else if(dataSeq[m][i]=='G'){
        g++;
      }
    }
    if(a==t && c==g){
      count++;
    }
  }
  cout<<count<<endl;

  return 0;
}
