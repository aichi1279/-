/*大きさNの順序（（1、２、....N）を並び換えてできる配列）P、Qがあります。
大きさNの順序はN！通り考えられます。このうち、Pが辞書順でa番目に小さく、Qが辞書順でb番目に
小さいとして、｜a-b｜を求めて下さい
*/

#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<functional>
using namespace std;

int main(){
  int N;
  int P,Q;
  int list[8][8]={0},p[8],q[8],ex[8];
  
  cin>>N;
  int i=0;
  while(i<N){
    cin>>P;
    p[i]=P;
    i++;
  }
  i=0;
  while(i<N){
    cin>>Q;
    q[i]=Q;
    i++;
  }
  
  for(int i=0;i<N;i++){
    ex[i]=i+1;
  }
  i=0
    foreach_permutation(N,[](int *indexes){
	for(int j=0;j<N;j++){
	  cout<< indexes[j];
	}
	i++;
      });
	
  
 
  for(i=0;i<N;i++){
    for(int j=0;j<N;j++){
      cout<<list[i][j]<<' ';
    }
    cout<<endl;
  }
 
}
    
	
void foreach_permutation(int n ,function<void(int *)>f){
  int indexes[n];
  for(int i= 0;i<n;i++) indexes[i]=i;
  do{
    f(indexes);
  }while
      (next_permutation(indexes,indexes+n));
}
    
