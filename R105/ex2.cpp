#include<iostream>
#include<cmath>
#include<list>
using namespace std;


int main(){
  int N;
  cin>>N;
  int line[N];
  int x, mini = pow(10,9);

  for(int i=0;i<N;i++){
    cin>>x;
    line[i] = x;
    if(mini>x){
      mini=x;
    }
  }
  int count=0;
  int X[N];
  for(int i=0;i<N;i++){
    bool flag=true;
    for(int j=i+1;j<N;j++){
      if(line[i]==line[j]){
        flag=false;
        break;
      }
    }
    if(flag){
      X[count]=line[i];
      //cout<< X[count]<<endl;
      count++;
    }
  }


  int mini2;
  int maxi=0;
  while(maxi!=mini){
    mini2=mini;
    maxi=0;
    for(int i=0;i<count; i++){
      if(X[i]>mini){
        X[i]= X[i]%mini;
        if(X[i]%mini==0){
          X[i]=mini;
        }
        if(mini2>X[i]){
          mini2 = X[i];
        }
        if(maxi< X[i]){
          maxi = X[i];
        }
      }
    }
    mini=mini2;
  }

cout<<maxi;
cout<<endl;

return 0;
}
