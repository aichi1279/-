#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

set<string> st;//

void dfs(string s, string cs) {//
  if (cs == "") {
    st.insert(s);
    return;
  }
  rep(i,cs.size()) {//
    string ncs = cs;
    ncs.erase(ncs.begin()+i);
    dfs(s+cs[i], ncs);
  }
}

int main() {
  string s;
  int k;
  cin >> s >> k;
  dfs("", s);
  vector<string> ss;
  for (string t : st) ss.push_back(t);
  sort(ss.begin(), ss.end());
  cout << ss[k-1] << endl;
  return 0;
}
