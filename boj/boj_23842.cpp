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
#define MAX 100
#define MOD 1000000007

using namespace std;

int n;
int d[10] = {6,2,5,5,4,5,6,3,7,6};

int cal(int val) {
    return d[val/10] + d[val % 10];
}

int solve() {
    cin>>n;

    for (int i=0;i<MAX;i++) {
        for (int j=0;j<=i;j++) {
            int res = 4;
            res += cal(i);
            res += cal(j);
            res += cal(i - j);
            if (res == n) {
                cout<<j/10<<j%10<<'+'<<(i-j)/10<<(i-j)%10<<'='<<i/10<<i%10<<'\n';
                return 0;
            }
        }
    }
    cout<<"impossible\n";
    return 0;
}

int main() {
    FAST;
    solve();
    return 0;
}