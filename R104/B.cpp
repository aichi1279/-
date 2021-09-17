#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;

int main(){
/*
 my code is fuck

  int N=0;
  cin>>N;
  char s[N];

  for(int i=0; i<N ;i++){
    cin>>s[i];
  }

  int count=0;
  for(int start=0;i< N-1 ;i++){
    for(int end=N-1; end>start ;j--){
      int a=0,t=0,c=0,g=0;
      for(int m=start ;m <= end ;m++){
        if(s[m]=='A'){
          a++;
        }else if(s[m]=='T'){
          t++;
        }else if(s[m]=='C'){
          c++;
        }else if(s[m]=='G'){
          g++;
        }
      }
      if(a==t && c==g){
        count++;
      }
    }
  }


  cout<<count<<endl;

  return 0;

*/



  int n;
  string s;
  cin >> n >> s;

  int ans = 0;
  for (int i = 0; i < n; ++i)
  {
    int at = 0;
    int cg = 0;
    for (int j = i; j < n; ++j)
    {
      if (s[j] == 'A') ++at;
      else if (s[j] == 'T') --at;
      else if (s[j] == 'C') ++cg;
      else if (s[j] == 'G') --cg;
      if (at == 0 && cg == 0) ++ans;
    }
  }

  cout << ans << '\n';
  return 0;
}
