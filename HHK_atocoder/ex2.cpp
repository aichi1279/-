#include<iostream>
using namespace std;

int main(){
  int H,W;
  cin>>H>>W;
  char c[H][W];

  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      cin>>c[i][j];
    }
  }
  int count=0;
  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      if(c[i][j]=='.' && i==H-1 && j!=W-1&& c[i][j]==c[i][j+1]){
        count++;
      }else if(c[i][j]=='.'&& i!=H-1  && j==W-1 && c[i][j]==c[i+1][j]){
        count++;
      }else if(c[i][j]=='.'&& i==H-1  && j==W-1 && c[i][j]==c[i+1][j]){
        count++;
      }else if(c[i][j]=='.'  &&  i!=H-1 && j!=W-1 && c[i][j]==c[i+1][j] &&  c[i][j]==c[i][j+1]){
        count+=2;
      }else if(c[i][j]=='.'  &&  i!=H-1 && j!=W-1 && c[i][j]==c[i+1][j]){
        count++;
      }else if(c[i][j]=='.'  &&  i!=H-1 && j!=W-1 && c[i][j]==c[i][j+1]){
        count++;
      }
    }
  }

  cout<<count<<endl;
  return 0;

}
