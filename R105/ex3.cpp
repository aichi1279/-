#include<iostream>
#include<cmath>
#include<list>
#include<memory>
using namespace std;

int main(){
  int N,M;
  int W[N],L[M],V[M];
  cin>>N>>M;

  for(int i=0;i<N;i++){
    cin>>W[i];
  }
  for(int i=0;i<M;i++){
    cin>>L[i]>>V[i];
  }
  for(int i=0;i<N;i++){
    for(int j=0;j<M;i++){
      if(W[i]>V[j]){
        cout<<"-1"<<endl;
      }
    }
  }

}
