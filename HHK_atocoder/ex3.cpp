#include<iostream>
#include<list>
using namespace std;

int main(){
  int N;
  cin>>N;


  int ans=0;
  int line[N],p[200001];
  for(int i=0;i<N;i++){
    line[i]=1;
  }///////////定義＆入力

  for(int i=0;i<N;i++){
    cin>>p[i];
    line[p[i]]=0;

    while(line[ans]==0 && ans<N){
      ans++;
  }

    /*if(table[i]==ans){
      ans++;
      for(int j=0;j<i;j++){
        if(table[j]==ans){
          ans++;
          j=-1;
        }
      }
    }*/

    cout<<ans<<endl;
  }
  return 0;
}
