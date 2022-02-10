#include <bits/stdc++.h>
typedef long long ll;
#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
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
#define MAX 1000001
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;

int n;
string s;

int lcp(int n, vector<vector<int>> &group, int k, int i, int j){
    int ans = 0;
    while (i<n&&j<n&&k>=0){
        if(group[k][i]==group[k][j]){
            ans+=(1<<k);
            i += (1<<k);
            j += (1<<k);
        }
        k-= 1;
    }
    return ans;
}

int solve() {
    vector<int> sa(n);
    vector<vector<int>> group(22, vector<int>(n+1));
    REP(i, n){
        sa[i] = i;
    }
    REP(i, n){
        group[0][i] = s[i];
    }
    group[0][n] = -1;
    int last = 0;

    for(int k=0,len=1;len/2<n;len*=2,k++){
        auto cmp = [&](int u, int v){
            if(group[k][u]==group[k][v]){
                return group[k][u+len]<group[k][v+len];
            }else{
                return group[k][u]<group[k][v];
            }
        };
        sort(sa.begin(),sa.end(),cmp);
        group[k+1][sa[0]] = 0;
        group[k+1][n] = -1;
        for(int i=1;i<n;i++){
            if(cmp(sa[i-1],sa[i])){
                group[k+1][sa[i]] = group[k+1][sa[i-1]]+1;
            }else{
                group[k+1][sa[i]] = group[k+1][sa[i-1]];
            }
        }
        last = k + 1;
    }

    ll res = 0;
    for(int i=0;i<n;i++){
        res += (ll)(n-sa[i]);
        if(i>0){
            res -= (ll)lcp(n,group,last,sa[i-1],sa[i]);
        }
    }
    cout<<res<<'\n';
    return 0;
}

int main(){
    FAST;
    cin>>s;
    n = s.length();
	solve();
    return 0;
}