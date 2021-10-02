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
#define MAX 251

using namespace std;

int n;
vector<PII> a;
int d[MAX][62501];

// int f(int idx, int l, int r){
//     if (idx==n){
//         d[idx][l] = r;
//         return 0;
//     }
//     if (d[idx][l]!=-1 && d[idx][l]<=r){
//         return d[idx][l];
//     }
//     int &res = d[idx][l];
//     res = r;
//     f(idx+1,l+a[idx].first,r);
//     f(idx+1,l,r+a[idx].second);
//     return res;
// }

int solve(){
    RESET(d, -1);
    // f(0,0,0);
    d[0][0] = 0;
    REP(i, n){
        REP(time, 62501){
            if (d[i][time]!=-1){
                if (d[i+1][time+a[i].first]!=-1){
                    d[i+1][time+a[i].first] = min(d[i][time], d[i+1][time+a[i].first]);
                }else{
                    d[i+1][time+a[i].first] = d[i][time];
                }
                if (d[i+1][time]!=-1){
                    d[i+1][time] = min(d[i+1][time], d[i][time] + a[i].second);
                }else{
                    d[i+1][time] = d[i][time] + a[i].second;
                }
            }
        }
    }
    int res = INF;
    REP(i, 62501){
        if (d[n][i]!=-1){
            // cout<<i<<" "<<d[n][i]<<endl;
            res = min(res, max(i, d[n][i]));
        }
    }
    cout<<res<<endl;
    return 0;
}

int main(){
    FAST;
    cin>>n;
    a.resize(n);
    REP(i,n){
        cin>>a[i].first>>a[i].second;
    }
    solve();
    return 0;
}