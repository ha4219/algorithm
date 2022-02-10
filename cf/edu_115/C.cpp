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
#define MAX 100001
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;


int T, n;
vector<ll> a;

int solve() {
    ll res = 0;
    ll sub = 0;
    REP(i, n){
        sub += a[i];
    }
    sub*=2;
    if(sub%n){
        cout<<0<<'\n';
        return 0;
    }
    int k = sub/n;
    map<int, ll> m;
    REP(i, n){
        auto tmp = m.find(k-a[i]);
        if(tmp==m.end()){
            m.insert({k-a[i],1});
        }else{
            tmp->second++;
        }
    }
    map<int, bool> v;
    REP(i, n){
        auto tmp = m.find(a[i]);
        auto visit = v.find(a[i]);
        if(visit!=v.end()){
            continue;
        }
        if(tmp!=m.end()){
            if(k-a[i]==a[i]){
                res += (tmp->second*(tmp->second-1));
            }else{
                res += m.find(k-a[i])->second*tmp->second;
            }
        }
        v.insert({a[i], 1});
    }
    res /= 2;
    cout<<res<<'\n';
    return 0;
}

int main(){
    FAST;
    cin>>T;
    TC(T) {
        cin>>n;
        a.resize(n);
        REP(i, n){
            cin>>a[i];
        }
        solve();
    }
    return 0;
}