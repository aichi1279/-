#include<iostream>
#include<vector>
using namespace std;

int main(){
  unsigned long N;
  vector<unsigned long> front_vc;
  vector<unsigned long> back_vc;
  cin>>N;

   for(int i=1; i*i<=N ;i++){
     if(i*i>N){
       break;
     }
      if(N%i==0){
        back_vc.push_back(N/i);
        if(i!=(N/i)){
          front_vc.push_back(i);
        }
      }
    }

    for(int i=0;i<front_vc.size();i++){
      cout<<front_vc[i]<<endl;
    }

    for (int i=back_vc.size()-1 ;i>=0;i--){
      cout<<back_vc[i]<<endl;
    }
  return 0;
}
