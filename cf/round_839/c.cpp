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

int n, m;
vector<int> p;

int solve() {
    cin >> n >> m;
    int r = m - n;
    int l = -1;
    for(int i=0;i<41;i++){
        if (p[i] > r) {
            l = i-1;
            break;
        }
    }
    int start = 1;
    for(int i=0;i<n;i++) {
        cout<<start<<' ';
        start += 1;
        if (l) {
            start += l--;
        }
    }
    cout<<'\n';
    return 0;
}

int main() {
    FAST;
    p.resize(41, 0);
    for(int i=1;i<41;i++){
        p[i] = p[i-1] + i;
    }
    int t;
    cin>>t;
    TC(t){
        solve();
    }
    
    return 0;
}