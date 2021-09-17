#include<iostream>
#include<map>
using namespace std;

int main(){
  unsigned long int n,input, x[200];

  //配列の初期化
  for(int i = 0;i<200;i++){
    x[i] = 0;
  }

  cin >> n;
  for(int i = 0; i<n ;i++){
    cin >> input;
    x[input%200] += 1;
  }

  unsigned long int ans = 0;
  for(int i = 0;i<200;i++){
    ans += int((x[i]*(x[i]-1))/2);
  }
  cout <<ans<<endl;
  return 0;
}
