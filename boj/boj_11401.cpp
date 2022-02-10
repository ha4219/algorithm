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
#define MAX 101
#define ALLPATH 1023
#define MOD 1000000007

using namespace std;

ll n, k;

int solve()
{
    ll nn = 1;
    ll kk = 1;
    ll nk = 1;
    for(ll i=1;i<=n;i++){
        if (i<=k) kk = (kk*i)%MOD;
        if (i<=(n-k)) nk = (nk*i)%MOD;
        nn = (nn*i)%MOD;
    }
    ll knk = (kk*nk)%MOD;
    vector<int> v(30, 0);
    int target = MOD - 2;
    for(int i=0;i<30;i++){
        if(target&1) v[i] = 1;
        target >>= 1;
    }
    ll res = 1;
    for(int i=0;i<30;i++){
        if(v[i]){
            res = (res * knk)%MOD;
        }
        knk = (knk*knk)%MOD;
    }
    res = (res*nn)%MOD;
    cout<<res<<'\n';
    return 0;
}

int main(){
    FAST;
    cin>>n>>k;
    solve();
    return 0;
}