#include<bits/stdc++.h>
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
#define SQR(x) ((LL)(x) * (x))
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

#define INF 1e18
#define MAX 500001

typedef long long ll;
using namespace std;

ll w;
int n;
vector<ll> a;
vector<ll> s;
ll d[MAX];

ll f(int l, int r){// for i in range(l, r) -> l부터 r-1까지
    if(l==r){
        return (w-a[l])*(w-a[r]);
    }
    if(d[l]!=INF){
        return d[l];
    }
    
}

int main(void){
	FAST;
    cin>>w>>n;
    a.resize(n+1);
    s.resize(n+1);
    RESET(d, INF);
    REPN(i, n){
        cin>>a[i];
        s[i] = s[i-1] + a[i];
    }
    return 0;
}
