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
#define MAX 50001

using namespace std;

ll n;

int f(ll m){
    return m<n?1:0;
}

int solve(){
    // int l = 0;
    // int r = pow(2,32);
    // int res;
    // while (l<=r)
    // {
    //     int m = (l+r)/2;
    //     // int tmp = f((ll)m*m);
    //     if((ll)m*m<n){
    //         l = m + 1;
    //     }else{
    //         res = m;
    //         r = m - 1;
    //     }
    // }
    // cout<<res<<endl;
    // return 0;   
    cout<<(ll)ceil(sqrt(n))<<endl;
    return 0;
}

int main(){
    FAST;
    cin>>n;
    solve();
    return 0;
}