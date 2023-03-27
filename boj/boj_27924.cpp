#include<bits/stdc++.h>

typedef long long ll;

#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define PII pair<int,int>
#define PIII pair<PII,int>
#define PLL pair<ll,ll>
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
#define MAX 100001
#define MOD 1000000007

#define N 200001
#define M 101

using namespace std;

int n;
int d1[N], d2[N], d3[N];
int qs[3];
vector<int> a[N];
set<int> leaf;

void dfs(int cur, int depth, int d[]) {
	if (a[cur].size() == 1) {
		leaf.insert(cur);
	}
	for (auto nn : a[cur]) {
		if (d[nn] > depth + 1) {
			d[nn] = depth + 1;
			dfs(nn, depth + 1, d);
		}
	}
}

void input() {
	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		int l, r;
		cin >> l >> r;
		l--;
		r--;
		a[l].push_back(r);
		a[r].push_back(l);
	}
	for (int i = 0; i < 3; i++) {
		cin >> qs[i];
		qs[i]--;
	}
}

int solve() {
	input();
	fill_n(d1, n, MAX);
	fill_n(d2, n, MAX);
	fill_n(d3, n, MAX);
	d1[qs[0]] = 0;
	dfs(qs[0], 0, d1);
	d2[qs[1]] = 0;
	dfs(qs[1], 0, d2);
	d3[qs[2]] = 0;
	dfs(qs[2], 0, d3);
	for (auto q : leaf) {
		if (d1[q] < d2[q] && d1[q] < d3[q]) {
			cout << "YES\n";
			return 0;
		}
	}
	cout << "NO\n";
	return 0;
}

int main() {
	FAST;
	solve();
	// cin>>t;
	// TC(t){
	//     solve();
	// }

	return 0;
}