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
#define MAX 1024
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;

int x, y, n;
int a0, a1;
int res;
int d[100][100];
int v[100][100];
int start;
int dend;
vector<int> a;

int f(int p, int q, int dep) {
    int ret = 0;
    if (d[p][q]!=-1) {
        // cout<<dep<<" "<<v[p][q]<<endl;
        start = v[p][q];
        dend = dep;
        return dep-v[p][q];
    }
    int val = (y*p+x*q)%100;
    a.push_back(val);
    d[p][q] = val;
    v[p][q] = dep;
    ret = f(q, val, dep+1);
    return ret;
}
// 3 5 1 7 100000000
int solve() {
    RESET(d, -1);
    if (n<2){
        if (n==1){
            cout<<a1<<endl;
        }else{
            cout<<a0<<endl;
        }
        return 0;
    }
    a.pb(a0);
    a.pb(a1);
    int depth = f(a0, a1, 2);
    if (n>=dend) {
        // cout<<start<<" "<<dend<<endl;
        n -= start;
        n %= depth;
        // cout<<n<<endl;
        if (a[n+start]<10){
            cout<<"0";
        }
        cout<<a[n+start]<<endl;
    }else{
        if (a[n]<10){
            cout<<"0";
        }
        cout<<a[n]<<endl;
    }
    return 0;
}

int main(){
    FAST;
    cin>>x>>y;
    cin>>a0>>a1;
    cin>>n;
    solve();
    return 0;
}