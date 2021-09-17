/*高橋君はAtCoderのコンテストに参加しています。
このコンテストでは、N問の問題が出題されます。
高橋君はコンテスト中にM回の提出を行いました。
i回目の提出は、pi番目の問題への提出であり、結果はSi('AC'or'WA')でした。
高橋君の正答数は、’AC’を１回以上以上出した各問題において、初めて’AC’を出すまでに出した’WA’の数の総和です。
高橋君の正答数とペナルテ数を答えてください。
*/


#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int N,M,n;
  int pi[10500];
  string s;
  string Si[10500];
  
  cin>>N>>M;

  for(int i=0;i<M;i++){
    pi[i]=0;
    Si[i]="";
  }
  int i=0;
  
  while(i <M){
    cin>>n>>s;
    pi[i]=n;
    Si[i]=s;
    i++;
  }

  
  int pena=0,num=0,count=0;
    
  for(int j=0;j<M;j++){
    if(Si[j]=="AC"){
      num+=1;
      for(int k=j+1;k<M;k++){
	if(pi[j]==pi[k]){
	  j++;
      	}
      }
    }
  }

  for(int j=0;j<M;j++){
     if(Si[j]=="WA"){
       count++;
       for(int k=j+1;k<M;k++){
	 if(pi[j]==pi[k] && Si[k]=="WA"){
	   count++;
	 }
	 if(pi[j]==pi[k] && Si[k]=="AC"){
	   pena += count;
	   count=0;
	 }
       }
     }
  }
  cout<<num<<" "<<pena<<endl;
}
