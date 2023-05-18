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

#define INF 1e9
#define MAX 100001
#define MOD 1000000007

#define N 2501
#define M 101

using namespace std;

int n;
vector<int> a;

void input() {
	cin >> n;
	for(int i=0;i<n;i++){
		int t;cin>>t;a.pb(t);
	}
}

int ccw(PLL p1, PLL p2, PLL p3) {
	ll res = p2.fi * p3.se - p3.fi * p2.se - p1.fi * p3.se + p3.fi * p1.se + p1.fi * p2.se - p2.fi * p1.se;
	return res > 0 ? 1 : res < 0 ? -1 : 0;
}

bool check(int l, int r) {
	PLL p0 = {ll(l), a[l]}, p1 = {ll(r), a[r]};
	for(int i=0;i<n;i++) {
		PLL p2 = {ll(i), 0LL}, p3 = {ll(i), a[i]};
		int l = ccw(p0, p1, p2) * ccw(p0, p1, p3);
		int r = ccw(p2, p3, p0) * ccw(p2, p3, p1);
		if (l<0&&r<0) return false;
	}
	return true;
}

int solve() {
	input();
	vector<int> res; 
	for(int i=0;i<n;i++) {
		int m = 0;
		for(int j=0;j<n;j++){
			if (check(i, j)) {
				m++;
			}
		}
		res.pb(m);
	}
	cout<<*max_element(res.begin(), res.end())<<'\n';
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