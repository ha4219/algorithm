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


int n, m;
int s, e;
vector<vector<PII>> a;

int f(int mid){
    vector<int> v;
    v.resize(n+1);
    v[s] = 1;
    queue<int> q;
    q.push(s);
    while (!q.empty())
    {
        int x = q.front();
        q.pop();
        if (x==e){
            return 1;
        }
        for(auto next : a[x]){
            if (v[next.first] || next.second<mid){
                continue;
            }
            v[next.first] = 1;
            q.push(next.first);
        }
    }
    return 0;
}

int solve() {
    int l = 0;
    int r = INF;
    int res;
    while (l<=r)
    {
        int m = (l+r)/2;
        if(f(m)){
            l = m + 1;
            res = m;
        }else{
            r = m - 1;
        }
    }
    cout<<res<<endl;
    return 0;
}

int main(){
    FAST;
    cin>>n>>m;
    a.resize(n+1);
    REP(i, m){
        int p,q,r;
        cin>>p>>q>>r;
        a[p].pb({q,r});
        a[q].pb({p,r});
    }
    cin>>s>>e;
    solve();
    return 0;
}