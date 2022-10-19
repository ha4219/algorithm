#include<bits/stdc++.h>

typedef long long ll;

#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define PII pair<int,int>
#define PIII pair<PII,int>
#define FOR(a, b, c) for (int(a) = (b); (a) < (c); ++(a))
#define FORN(a, b, c) for (int(a) = (b); (a) <= (c); ++(a))
#define FORD(a, b, c) for (int(a) = (b); (a) >= (c); --(a))
#define FORSQ(a, b, c) for (int(a) = (b); (a) * (a) <= (c); ++(a))
#define FORC(a, b, c) for (char(a) = (b); (a) <= (c); ++(a))
#define FOREACH(a, b) for (auto&(a) : (b))
#define REP(i, n) FOR(i, 0, n)
#define REPN(i, n) FORN(i, 1, n)
#define SQR(x) ((ll)(x) * (x))
#define RESET(a, b) memset(a, b, sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ALL(v) v.begin(), v.end()
#define ALLA(arr, sz) arr, arr + sz
#define SIZE(v) (int)v.size()
#define SORT(v) sort(ALL(v))
#define REVERSE(v) reverse(ALL(v))
#define SORTA(arr, sz) sort(ALLA(arr, sz))
#define REVERSEA(arr, sz) reverse(ALLA(arr, sz))
#define PERMUTE next_permutation
#define TC(t) while (t--)

#define INF 1e9
#define MAX 1000000000
#define MOD 1000000007

#define N 100001
#define M 101

using namespace std;

int n;
ll d[N][M] = {0,};
bool v[N][M] = {0, };

int solve() {
    cin >> n;

    for(int i=0;i<n;i++) {
        int val;
        cin >> val;
        
        for(int j=1;j<M;j++) {
            if (v[i][j]) {
                v[i+1][val] = 1;
                d[i+1][val] = max(d[i+1][val], d[i][j] + (j-val) * (j-val));

                v[i+1][j] = 1;
                d[i+1][j] = max(d[i][j], d[i+1][j]);
            }
        }

        v[i+1][val] = 1;
    }

    ll res = 0;
    for(int i=0;i<M;i++) {
        res = max(res, d[n][i]);
    }
    
    cout<<res<<'\n';

    return 0;
}

int main() {
    FAST;
    // TC(t) {
    solve();
    // }
    return 0;
}