/*Distance
２次元平面上にN個の点があります。i個目の点の座標(Xi, Yi)です。
これらのうち、原点からの距離が,D以下であるような点は何個ありますか。
尚、座標(p,q)にある点と原点の距離はroot(p^2+q^2)で表されます。
*/
#include<iostream>
#include<stdlib.h>
#include<cmath>
using namespace std;

int main(){
 int N,D,X,Y;
 cin >> N >> D;

 int count=0;
 for(int i=0; i<N; i++){
   cin >>X >> Y;

   if( D >= sqrt(pow(X,2)+pow(Y,2)) ){
     count += 1;
   }

 }

cout<<count<<endl;
return 0;
}
