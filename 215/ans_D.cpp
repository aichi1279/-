#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, m;
  cin >> n >> m;
  const int L = 100001;
  //----------phase.1 Aiの素因数の列挙----------1.1.
  vector<bool> x(L);//各数値毎の正誤表
  rep(i,n) {
    int a;
    cin >> a; //Aiの入力
    x[a] = true;// Aiに対応する正誤表の箇所をTrueへ
  }

  //------------------------------------------1.2.
  vector<int> d; // Aiの素因数集合
                 //→下記の調査でiの倍数の正誤表がTrueを通過した場合、dで記憶 = Aiの素因数集合

  for (int i = 2; i < L; i++) { //素因数 or 倍数毎に調査＝ 2~ L-1　ex1.1) 2,3...
    bool flag = false;
    for (int j = i; j < L; j += i) { //次の数値へ移動 ex1.2) 2 → 4 → 6 → ... ~ L
      if (x[j]) flag = true;         //                    3 → 6 → 9 → ... ~ L
    }
    if (flag) d.push_back(i);
  }
  //-----------------------------------------------Aiの素因数の列挙完了 >> d

  vector<bool> ok(m+1, true);  // 判別表　デフォルトTrue
  for (int i : d) {            // dの要素をiに代入
    for (int j = i; j <= m; j += i) {
      ok[j] = false;
    }
  }

  int cnt = 0;
  for (int i = 1; i <= m; ++i) if (ok[i]) cnt++;
  cout << cnt << endl;
  for (int i = 1; i <= m; ++i) if (ok[i]) cout << i << endl;
  return 0;
}
