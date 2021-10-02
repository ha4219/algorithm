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

using namespace std;

int n, k;
vector<int> a;

int f(int m){
    int cnt = 1;
    int sum = 0;
    REP(i, n){
        if (sum+a[i]<=m){
            sum+=a[i];
        }else{
            cnt++;
            sum = a[i];
        }
    }
    return cnt<=k;
}

int solve(){
    int l = *max_element(a.begin(),a.end());
    int r = 0;
    int res = 0;
    for_each(a.begin(), a.end(), [&r](int& num){
        r += num;
    });
    while (l<=r)
    {
        int m = (l+r)/2;
        if(f(m)){
            r = m - 1;
            res = m;
        }else{
            l = m + 1;
        }
    }
    cout<<res<<endl;
    return 0;
}

int main(){
    FAST;
    cin>>n>>k;
    a.resize(n);
    REP(i,n){
        cin>>a[i];
    }
    solve();
    return 0;
}