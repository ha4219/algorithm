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

#define INF 1e17
#define MAX 500001

using namespace std;

ll w;
int n;
vector<ll> a;
vector<ll> s;
ll d[MAX];

ll f(int l, int r){// for i in range(l, r+1) -> l부터 r까지
    if(l==r){
        return SQR(w-a[l]);
    }
    // cout<<"f "<<l<<" "<<r<<endl;
    if(d[r]!=-1){
        return d[r];
    }
    if(s[r]-s[l-1]<=w){
        // cout<<"pass"<<s[r]-s[l-1]<<" "<<l<<r<<endl;
        d[r] = SQR(w-s[r]-s[l-1]);
        return d[r];
    }
    d[r] = INF;
    // cout<<"d "<<d[r]<<'\n';
    for(int i=l;i<r;i++){
        ll tmpl = f(l, i);
        ll tmpr = f(i+1, r);
        ll tmp = max(tmpl,tmpr);
        d[r] = min(d[r], tmp);
        // cout<<l<<"~"<<i<<" "<<i+1<<"~"<<r<<" "<<tmpl<<" "<<tmpr<<endl;
    }
    return d[r];
}

int main(void){
	FAST;
    cin>>w>>n;
    a.resize(n+1);
    s.resize(n+1);
    RESET(d, -1);
    REPN(i, n){
        cin>>a[i];
        s[i] = s[i-1] + a[i];
    }
    
    cout<<f(1, n)<<endl;
    return 0;
}
