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

char d;
int n, m;
vector<vector<int>> a;
char l_map[] = {'0', '1', '5', '?', '?', '2', '?', '?', '8', '?'};
char r_map[] = {'0', '1', '5', '?', '?', '2', '?', '?', '8', '?'};
char d_map[] = {'0', '1', '5', '?', '?', '2', '?', '?', '8', '?'};
char u_map[] = {'0', '1', '5', '?', '?', '2', '?', '?', '8', '?'};

int solve() {
    cin >> d >> n;
    for (int i=0;i<n;i++) {
        vector<int> tm;
        for (int j=0;j<n;j++) {
            int tmp;
            cin >> tmp;
            tm.pb(tmp);
        }
        a.pb(tm);
    }
    switch (d)
    {
    case 'L':
        for(int i=0;i<n;i++) {
            for(int j=n-1;j>-1;j--) {
                cout<<l_map[a[i][j]]<<" ";
            }
            cout<<'\n';
        }
        break;
    case 'R':
        for(int i=0;i<n;i++) {
            for(int j=n-1;j>-1;j--) {
                cout<<r_map[a[i][j]]<<" ";
            }
            cout<<'\n';
        }
        break;
    case 'U':
        for(int i=n-1;i>-1;i--) {
            for(int j=0;j<n;j++) {
                cout<<u_map[a[i][j]]<<" ";
            }
            cout<<'\n';
        }
        break;
    case 'D':
        for(int i=n-1;i>-1;i--) {
            for(int j=0;j<n;j++) {
                cout<<d_map[a[i][j]]<<" ";
            }
            cout<<'\n';
        }
        break;
    default:
        break;
    }
    return 0;
}

int main() {
    FAST;
    // TC(t) {
    solve();
    // }
    return 0;
}