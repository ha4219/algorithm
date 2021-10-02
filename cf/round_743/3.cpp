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
vector<vector<int>> a;
vector<int> degree, check;
queue<int> q;
 
int solve() {
    int res = 0;
    while(!q.empty()){
        auto cur = q.front();q.pop();
        for (auto next: a[cur]) {
            if (!--degree[next] && !check[next]) {
                if (cur>next){
                    check[next] = check[cur] + 1;
                }else{
                    check[next] = check[cur];
                }
                q.push(next);
            }
        }
    }
    int flag = 0;
    REPN(i, n){
        if (check[i]==0){
            flag = 1;
            break;
        }
        res = max(res, check[i]);
    }
    if (flag){
        res = -1;
    }
    cout<<res<<'\n';
    return 0;
}
 
int main(){
    FAST;
    cin>>T;
    TC(T){
        cin>>n;
        degree.clear();
        degree.resize(n+1);
        check.clear();
        check.resize(n+1);
        a.clear();
        a.resize(n+1);
        REPN(i, n) {
            int size;
            cin>>size;
            if (size==0){
                check[i] = 1;
                q.push(i);
            }
            degree[i] = size;
            REP(j, size){
                int tmp;
                cin>>tmp;
                a[tmp].pb(i);
            }
        }
        solve();
    }
    return 0;
}