#include<bits/stdc++.h>

typedef long long ll;

#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define PII pair<int,int>
#define PIII pair<PII,int>
#define PLL pair<ll,ll>
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
#define MAX 100001
#define MOD 1000000007

#define N 100001
#define M 101

using namespace std;

int n;

PLL get_max(int t) {
    if (t == 0) return {0,0};
    ll day = t - (t / 7) * 2;

    if (t - (t/7)*7 == 6) {
        day--;
    }

    return {day, t};
}

int solve() {
    cin>>n;
    vector<PII> a(n);
    
    for (int i=0;i<n;i++) {
        int l, r;
        cin>>l>>r;

        a[i] = {l, r};
    }

    sort(a.begin(), a.end());

    int t = a[0].se;
    PLL prev = get_max(a[0].fi);
    if (t > prev.fi + prev.se) {
        cout<<"-1\n";
        return 0;
    }
    int res = a[0].se <= prev.fi ? 0 : a[0].se - prev.fi;
    int residual = a[0].se <= prev.fi ? prev.fi - a[0].se : 0;
    
    for(int i=1;i<n;i++) {
        t += a[i].se;
        PLL current = get_max(a[i].fi);
        if (t > current.fi + current.se) {
            cout<<"-1\n";
            return 0;
        }

        PLL dif = {current.fi - prev.fi, current.se - prev.se};

        if (a[i].se <= dif.fi) { // 그냥 가능
            residual += dif.fi - a[i].se;
        } else if (a[i].se <= dif.fi + residual) { // residual 써야 가능
            residual -= a[i].se - dif.fi;
        } else { // residual 써도 불가능
            res += a[i].se - dif.fi - residual;
            residual = 0;
        }

        prev = current;
    }
    cout<<res<<'\n';
    return 0;
}

int main() {
    FAST;
    int t = 1;
    // cin>>t;
    TC(t){
        solve();
    }
    
    return 0;
}