#include<bits/stdc++.h>

typedef long long ll;

#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define PII PII<int,int>
#define PIII PII<PII,int>
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
#define mp make_PII
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

int h=1;
vector<PII> seg;
vector<vector<int>> adj;
int depth[100005];
int idx[100005];
int cnt = 1;

void update(int i, int val, int u) {
	i += h-1;
	seg[i] = { val, u};
	while (i>1) {
		i /= 2;
		seg[i] = min(seg[i * 2], seg[i * 2 + 1]);
	}
}
PII query(int l, int r, int nodeNum, int nodeL, int nodeR) {
	if (l <= nodeL&& nodeR <= r) return seg[nodeNum];
	else if (r < nodeL || nodeR < l) return{ INF,INF };
	int mid = (nodeL + nodeR) / 2;
	return min(query(l, r, nodeNum * 2, nodeL, mid), query(l, r, nodeNum * 2 + 1, mid + 1, nodeR));
}
void dfs(int u, int d) {
	depth[u] = d;
	idx[u] = cnt;
	update(cnt++, d, u);
	for (auto v : adj[u]) {
		if (depth[v] == -1){
			dfs(v, d + 1);
			update(cnt++, d, u);
		}
	}
}

int solve() {
    int n;
	scanf("%d", &n);
	adj.resize(n +1);
	for (int i = 0; i < n-1; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	memset(depth, -1, sizeof(depth));
	while (h < 2 * n) h <<= 1;
	seg.resize(h * 2, { INF,0 });
	dfs(1, 0);
	int m;
	scanf("%d", &m);
	for (int q = 0; q < m; q++) {
		int a, b;
		scanf("%d %d", &a, &b);
		printf("%d\n", query(min(idx[a],idx[b]), max(idx[a],idx[b]), 1, 1, h).second);
	}
    return 0;
}

int main() {
    // FAST;
    solve();
    return 0;
}