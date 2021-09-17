/* D-Alter Altar

祭壇に、左から右へと一列に並ぶN個の石祀られています。左からi個目(1<= i <=N)
の石の色は文字ciとして与えられ、ciが'R'のとき赤、'W'のとき白です。

あなたは、以下の二種の操作を任意の順に何度でも行うことができます。
・石を２個選び（隣り合っていなくても良い）、それらを入れ替える。
・石を１個選び、その石の色を変える（赤なら白に、白なら赤に）。

占い師によると、赤の石の左隣に置かれた白い石は災いを招きます。そのような白い石がない状態に至るには、
最小で何回の操作が必要でしょうか。
*/
#include<iostream>
#include<stdlib.h>
using namespace std;

int main(){
  int N, red_count=0, white_count=0;
  cin >> N;

  char c[N];
  for(int i=0; i<N;i++){
    cin >> c[i];
    if(c[i]=='R'){
      red_count++;
    }else{
      white_count++;
    }
  }

  //cout<<red_count;

  if(red_count==N || white_count==N){
    cout<<0<<endl;
    return 0;
  }

  int count=0;
  bool flag=false;
  for(int i=0; i<N ;i++){
    if(c[i]!='W'){
      continue;
    }

    for(int j=N-1; j>=0 ;j--){
      if(i==j){
        flag=true;
        break;
      }

      if(c[j]=='R'){
        c[i] ='R';
        c[j] ='W';
        count++;
        break;
      }
    }
    if(flag){
      cout<<count<<endl;
      return 0;
    }
  }


}
