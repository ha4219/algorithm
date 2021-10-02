#include <bits/stdc++.h>
#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define FOR(w, a, n) for(int w=(a);w<(n);++w)
#define ALL(a) (a).begin(),(a).end()
#define CASES(t) int aa; cin >> aa; for(int t=1;t<=aa;t++)
#define MOD 2520
#define INF 9223372036854775807
typedef long long ll;
using namespace std;

struct Load {
    int index;
    int length;
    int v_limit;
};

struct Node {
	int index;
	int speed;
	ll time;
};

struct compare {
	bool operator()(const Node& a, const Node& b) {
		return a.time > b.time;
	}
};

int n, m;
vector<vector<Load>> arr;

ll dijkstra() {
	priority_queue<Node, vector<Node>, compare> pq;
	pq.push({1, 1, 0});
	vector<vector<ll>> dist(n + 1, vector<ll>(11, INF));
	dist[1][1] = 0;
	while (!pq.empty()) {
		int here = pq.top().index;
		int speed = pq.top().speed;
		ll time = pq.top().time;
		pq.pop();
		if (dist[here][speed] < time) continue;
		for (auto next : arr[here]) {
			for (int dv = -1; dv <= 1; dv++) {
				int next_speed = speed + dv;
				if (next_speed < 1 || next_speed > next.v_limit) continue;
				ll next_time = time + next.length / next_speed;
				if (dist[next.index][next_speed] > next_time) {
					dist[next.index][next_speed] = next_time;
					pq.push({ next.index, next_speed, next_time });
				}
			}
		}
	}
	ll ret = INF;
	for (auto x : dist[n]) ret = min(ret, x);
	return ret;
}


int main() {
    FAST;
    cin >> n >> m;
    arr = vector<vector<Load>>(n + 1, vector<Load>());
    for (int i = 0; i < m; i++) {
        int a, b, l, k;
        cin >> a >> b >> l >> k;
        arr[a].push_back({ b,l * MOD,k });
        arr[b].push_back({ a,l * MOD,k });
    }

	ll ans = dijkstra();
    cout<<ans / MOD;
    string s = to_string((double)(ans % MOD) / MOD);
	cout<<s<<endl;
}