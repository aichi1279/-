/*Air Conditioner
あなたは、室温が３０度以上の時、またその時に限り、冷房の電源を入れます。
今の室温は　X度です。冷房の電源を入れますか？
*/
#include<iostream>
#include<stdlib.h>
using namespace std;

int main(){
  int X;
  cin >> X;

  if(X>=30){
    cout<<"Yes"<<endl;
  }else{
    cout<<"No"<<endl;
  }

  return 0;

}
