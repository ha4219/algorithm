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
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)
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

#define INF 1e9

using namespace std;

int t, n, m, k;
int d[101][10001];
auto cmp = [](PIII &l, PIII &r) -> bool {
    return l.fi.fi>r.fi.fi;
};
vector<vector <PIII>> a;

int dijkstra(int start){
    priority_queue<PIII, vector<PIII>, decltype(cmp)> pq(cmp);
    RESET(d, INF);
    REP(i, n+1){
        REP(j, 10001){
            d[i][j] = INF;
        }
    }
    d[1][0] = 0;
    pq.push({PII(0, start), 0});
    while(!pq.empty()){
        int tt = pq.top().fi.fi;
        int xx = pq.top().fi.second;
        int cc = pq.top().second;
        pq.pop();
        if(xx==n){
            return tt;
        }
        if(tt>d[xx][cc]){
            continue;
        }
        for(auto next: a[xx]){
            if(cc+next.fi.se>m||d[next.fi.fi][cc+next.fi.se]<=d[xx][cc]+next.se){
                continue;
            }
            d[next.fi.fi][cc+next.fi.se] = d[xx][cc] + next.se;
            pq.push({PII(d[next.fi.fi][cc+next.fi.se],next.fi.fi),cc+next.fi.se});
        }

    }
    return -1;
}

int main(void){
	FAST;
    cin>>t;
    TC(t){
        cin>>n>>m>>k;
        a.clear();
        a.resize(n+1);
        REP(i, k){
            int p,q,e,r;
            cin>>p>>q>>e>>r;
            a[p].pb({PII(q,e),r});
        }
        int res = dijkstra(1);
        if(res==-1){
            cout<<"Poor KCM\n";
        }else{
            cout<<res<<'\n';
        }
    }
    return 0;
}
