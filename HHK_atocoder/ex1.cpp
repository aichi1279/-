#include<iostream>
using namespace std;

int main(){
  char s,t;
  cin>>s>>t;

  if(s=='Y'){
    t = char(t+'A'-'a');
    cout<<t<<endl;
  }else if (s=='N'){
    cout<<t<<endl;
  }

  return 0;
}
