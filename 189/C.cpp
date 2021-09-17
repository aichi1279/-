#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;

int main(){
  int maxi_eat=0,eat,mini;
  int n,tmp;
  vector<int> v;

  cin >> n;
  for(int i=0;i<n;i++){
    cin >> tmp;
    v.push_back(tmp);
  }

  vector<int> sub_v;
  maxi_eat = *max_element(v.begin(),v.end());
  for(int i=0;i<n-1;i++){
    sub_v.clear();
    for(int j=i+1;j<n;j++){
      sub_v.push_back(v[j]);
      mini = *min_element(sub_v.begin(),sub_v.end());
      eat = mini*(j-i);

      maxi_eat = max(maxi_eat, eat);
    }
  }

  cout<<maxi_eat<<endl;


}
