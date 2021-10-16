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
#define MAX 2000002
#define ALLPATH 1023
#define MOD 1000000007
 
using namespace std;

int t;
int n, k;
string _;

int dfs(vector<vector<int>> &a, vector<int> &v,int cur, int dep) {
    if (v[cur]<dep){
        return 0;
    }
    v[cur] = dep;
    for(auto next: a[cur]){
        dfs(a,v,next, dep+1);
    }
    return 0;
}

int solve(){
    cin>>n>>k;
    vector<vector<int>> a(n+1);
    vector<int> degree(n+1, 0);
    vector<int> v(n+1, INF);

    REP(i,n-1){
        int cur, target;
        cin>>cur>>target;
        a[cur].pb(target);
        a[target].pb(cur);
        degree[cur]++;
        degree[target]++;
    }
    
    REPN(i, n){
        if(degree[i]==1){
            dfs(a, v, i, 1);
        }
    }
    int res = 0;
    // cout<<"----"<<endl;
    // REPN(i, n){
    //     cout<<i<<" "<<v[i]<<'\n';
    // }
    // cout<<"----"<<endl;
    REPN(i,n){
        res += (v[i]!=INF&&(v[i]-k>=1));
    }
    cout<<res<<'\n';
    return 0;
}

int main(){
    FAST;
    TC(t){
        solve();
    }
    return 0;
}
