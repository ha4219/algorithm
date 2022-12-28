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
#define MAX 1000000000
#define MOD 1000000007

#define N 40001
#define M 500

using namespace std;

int n;
vector<int> a;

bool ff() {
    if (a[0] >= a[1] || a[0] >= a[2] || a[1] >= a[3] || a[2] >= a[3]) return false;
    return true;
}

int f() {
    for(int i=0;i<4;i++) {
        int lu = a[0];
        int ru = a[1];
        int ld = a[2];
        int rd = a[3];
        a[0] = ld;a[1] = lu;a[2] = rd;a[3]=ru;
        if (ff()) {
            return 1;
        }
    }
    return 0;
}

int solve() {
    a.resize(4);
    for(int i=0;i<4;i++) {
        cin>>a[i];
    }
    string res = (f()) ? "YES" : "NO";
    cout<<res<<'\n';
    return 0;
}

int main() {
    FAST;
    int t;
    cin>>t;
    TC(t){
        solve();
    }
    
    return 0;
}