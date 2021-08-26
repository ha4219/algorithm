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
#define MAX 2501

using namespace std;

string a;
int n;
int d[MAX][MAX];
int dp[MAX];

int f(int l, int r){
    if(dp[l]!=-1){
        return dp[l];
    }
    if(d[l][r-1]){
        dp[l] = 1;
        return dp[l];
    }
    dp[l] = INF;
    FORN(i, l, r){
        dp[l] = min(dp[l], f(l,i)+f(i,r));
    }
    return dp[l];
}

int main(void){
	FAST;
    cin>>a;
    n = a.length();
    RESET(dp, -1);
    REP(i,n){
        REP(j,n-i){
            if(i==0){
                d[j][j] = 1;
            }else if(i==1){
                d[j][j+1] = a[j]==a[j+i];
            }else{
                d[j][i+j] = a[j]==a[j+i]? d[j+1][j+i-1]:0;
            }
        }
    }
    // 6,250,000

    // f > n**3?
    cout<<f(0,n)<<'\n';
    return 0;
}
