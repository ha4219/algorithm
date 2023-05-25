#include<bits/stdc++.h>


typedef long long ll;

#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define PII pair<int,int>
#define PIII pair<PII,int>
#define PLL pair<ll,ll>
#define PLLL pair<PLL, ll>
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

#define INF 9e9
#define MAX 250000001
#define MOD 1000000007

#define N 6
#define M 101

using namespace std;

int n, m;
string s[N];
bool v[21];
string tmp[N];

void input() {
	cin>>m>>n;
	for(int i=0;i<n;i++){
		cin>>s[i];
	}
	return;
}

bool check() {
	for(int i=0;i<m;i++){
		for(int j=0;j<m;j++) {
			if (tmp[i][j] != tmp[j][i]) {
				return false;
			}
		}
	}
	return true;
}

void dfs(int c) {
	if (c == N - 1) {
		if (check()) {
			for(int i=0;i<m;i++) {
				cout<<tmp[i]<<'\n';
			}
			exit(0);
		}
	}
	for(int i=0;i<n;i++) {
		if(v[i]) continue;
		tmp[c] = s[i];
		v[i] = true;
		dfs(c + 1);
		v[i] = false;
	}
}

int solve() {
	// sort string -> fast in dictionary order :O(nlogn)
	sort(s, s+n);
	dfs(0);
	cout<<"NONE\n";
	// _nP_5

	return 0;
}

int main() {
	FAST;
	input();
	solve();
	// cin>>t;
	// TC(t){
	//     solve();
	// }

	return 0;
}