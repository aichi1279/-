/*高橋君は500円をK枚持っています。これらの総額がX円以上である場合、’YES’をそうでない場合は、’NO’を出力せよ。
 */

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
  int k,x;

  cin>>k>>x;

  if(x <= 500*k){
    cout<<"YES"<<endl;
  }else{
    cout<<"NO"<<endl;
  }

}
