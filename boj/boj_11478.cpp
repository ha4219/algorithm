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

int commonPrefix(string &s, int i, int j){
    int k=0;
    while (i<s.size()&&j<s.size()&&s[i]==s[j])
    {
        i++;j++;k++;
    }
    return k;
}

int solve() {
    vector<int> sa(n);
    vector<int> group(n+1);
    REP(i, n){
        sa[i] = i;
    }
    REP(i, n){
        group[i] = s[i];
    }
    group[n] = -1;
    for(int len=1;len/2<n;len*=2){
        auto cmp = [&](int u, int v){
            if(group[u]==group[v]){
                return group[u+len]<group[v+len];
            }else{
                return group[u]<group[v];
            }
        };
        sort(sa.begin(),sa.end(), cmp);
        vector<int> group2(n+1);
        group2[sa[0]] = 0;
        group2[n] = -1;
        for(int i=1;i<n;i++){
            if(cmp(sa[i-1], sa[i])){
                group2[sa[i]] = group2[sa[i-1]] + 1;
            }else{
                group2[sa[i]] = group2[sa[i-1]];
            }
        }
        group = group2;
    }
    ll res = 0;
    for(int i=0;i<n;i++){
        int cp = 0;
        if(i>0){
            cp = commonPrefix(s, sa[i-1], sa[i]);
        }
        int temp = s.size() - sa[i] - cp;
        res += (ll)temp;
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