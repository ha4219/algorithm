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

#define INF 1000000000
#define MAX 2001
#define ALLPATH 1023
#define MOD 1000000007

using namespace std;
int n;

int solve(){
    cin>>n;
    vector<int> a;
    a.resize(n+1);
    a[1] = 0;
    for(int i=2;i<=n;i++){
        a[i] = a[i-1] + 1;
        if (i%2==0) a[i]=min(a[i],a[i/2]+1);
        if (i%3==0) a[i]=min(a[i],a[i/3]+1);
    }
    int i = n;
    vector<int> res;
    while (1){
        res.pb(i);
        if (i==1) break;
        int tmp = i-1;
        if (i%2==0&&a[tmp]>a[i/2]) tmp = i/2;
        if (i%3==0&&a[tmp]>a[i/3]) tmp = i/3;
        i = tmp;
    }
    cout<<a[n]<<'\n';
    for(auto num: res){
        cout<<num<<' ';
    }
    cout<<'\n';
    return 0;
}

int main(){
    FAST;
    solve();
    return 0;
}