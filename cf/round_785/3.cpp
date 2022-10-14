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

#define N 40001
#define M 500

using namespace std;

vector<int> tmp;
int d[N][M];

int re(int n) {
    int r = 0;
    while (n > 0) {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return r;
}

bool p(int n) {
    return re(n) == n;
}

int solve() {
    tmp.pb(0);
    for(int i=1;i<N;i++){
        if (p(i)) tmp.pb(i);
    }
    for(int i=1;i<M;i++){
        d[0][i] = 1;
    }

    for(int i=1;i<N;i++){
        d[i][0] = 0;
        for(int j=1;j<M;j++){
            if (tmp[j]<=i) {
                d[i][j] = (d[i][j-1] + d[i-tmp[j]][j]) % MOD;
            } else {
                d[i][j] = d[i][j-1];
            }
        }
    }

    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int n;
        cin>>n;
        cout<<d[n][M-1]<<'\n';
    }

    return 0;
}

int main() {
    FAST;
    solve();
    return 0;
}