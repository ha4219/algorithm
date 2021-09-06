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
#define MAX 1000001
#define ALLPATH 7

using namespace std;

int n;

int d[31][9];

int f(int idx, int path) {
    // ground
    if (idx==n) {
        return path==0?1:0;
    }
    int &res = d[idx][path];
    if (res!=-1){
        return res;
    }
    res = 0;
    if (path==ALLPATH) {
        res += f(idx+1, 0);
    } else if(path==0) {
        res += f(idx+1, ALLPATH)+f(idx+1, 1)+f(idx+1,4);
    } else if(path==1) {
        res += f(idx+1,0)+f(idx+1, 6);
    } else if(path==2) {
        res += f(idx+1,5);
    } else if(path==3) {
        res += f(idx+1, 4);
    } else if(path==4){
        res += f(idx+1, 0) + f(idx+1, 3);
    } else if(path==5){
        res += f(idx+1, 2);
    } else{
        res += f(idx+1, 1);
    }

    return res;
}

int solve() {
    // RESET(d, -1);
    // cout<<f(0, 0)<<'\n';
    d[0][7] = 1;
    REPN(i, n){
        d[i][0] = d[i-1][7];
        d[i][1] = d[i-1][6];
        d[i][2] = d[i-1][5];
        d[i][3] = d[i-1][7] + d[i-1][4];
        d[i][4] = d[i-1][3];
        d[i][5] = d[i-1][2];
        d[i][6] = d[i-1][7] + d[i-1][1];
        d[i][7] = d[i-1][0] + d[i-1][3] + d[i-1][6];
    }
    cout<<d[n][7]<<'\n';
    return 0;
}

int main(){
    FAST;
    cin>>n;
    solve();
    return 0;
}