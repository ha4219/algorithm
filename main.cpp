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
#define MAX 400000

#define MINVALUE -1
#define MAXVALUE 100001
#define MOD 1000000007

using namespace std;

int n, m, k;
vector<int> a;
vector<int> b;
vector<int> c;
int d[101][1002][501];

int dfs(int idx, int cp, int memory, int priority){
    int &res = d[idx][cp][priority];
    // int &res = d[cp][priority];
    if(res!=-1){
        // return res;
        return res<m ? MAX : res;
		}
    if(n==idx){
        if(cp>=m&&memory>=k){
            return priority;
        }else{
            return MAX;
        }
    }
    // select or pass
    res = min(dfs(idx+1, cp, memory, priority), dfs(idx+1,min(cp+a[idx], 1001), memory+b[idx], priority+c[idx]));

    return res;
}

int solve(){
    cin>>n>>m>>k;
    a.resize(n);
    b.resize(n);
    c.resize(n);
    memset(d, -1, sizeof(d));
    
    for(int i=0;i<n;i++){
        cin>>a[i];
        cin>>b[i];
        cin>>c[i];
    }
    int res = dfs(0,0,0,0);
    if (res>=501){
        res = -1;
    }
    cout<<res<<endl;
		return 0;
}

int main() {
    FAST;
		solve();
    return 0;
}