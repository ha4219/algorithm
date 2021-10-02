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
#define PLI pair<ll, ll>

#define INF 1e9
#define MAX 1024
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;

int n, T;
vector<int> a, b;
vector<int> idx;
string s;

int solve() {
    int res = INF;
    int one = idx[1];
    if (a[0]>b[0]){
        for(int j=1;j<b[0];j+=2){
            res = min(res, idx[j]);
        }
    }else{
        res = 0;
    }
    cout<<res<<endl;
    return 0;
}

int main(){
    FAST;
    cin>>T;
    TC(T){
        cin>>n;
        a.clear();b.clear();idx.clear();
        a.resize(n);b.resize(n);idx.resize(2*n+1);
        REP(i, n){
            cin>>a[i];
            idx[a[i]] = i;
        }
        REP(i, n){
            cin>>b[i];
            idx[b[i]] = i;
        }
        solve();
    }
    return 0;
}