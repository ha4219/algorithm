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
#define PLI pair<ll, ll>

#define INF 1e9
#define MAX 100001
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;

int q;

bool prime[100001];
bool chk[100001];
int s[MAX*4];
vector <PIII> v;
vector <int> p;

void go() {
	RESET(prime, 1);
    for (int i = 2; i <= 100000; i++) {
        if (prime[i] == 0) continue;
		p.pb(i);
        for (int j = 2 * i; j <= 100000; j += i) {
            prime[j] = 0;
        }
    }
}

int init(int node, int nL, int nR) {
	if (nL==nR){
		return s[node] = 1;
	}
	int m=(nL+nR)/2;
	return s[node]=init(node*2,nL,m)+init(node*2+1,m+1,nR);
}

int update(int i, int v, int node, int nL, int nR) {
	if ((i<nL) || (i>nR)){
		return s[node];
	}
	if (nL==nR){
		s[node] = v;
		return s[node];
	}
	int m = (nL+nR)/2;
	return s[node]=update(i,v,node*2,nL,m)+update(i,v,node*2,m+1,nR);
}

int query(int l, int r, int node, int nL, int nR) {
	if ((nL > r) || (nR < l)){
		return 0;
	}
	if (l<=nL && nR<=r){
		return s[node];
	}
	int m = (nL+nR)/2;
	return query(l,r,node*2,nL,m)+query(l,r,node*2,m+1,nR);
}

int solve() {
	sort(v.rbegin(), v.rend());
	init(1, 1, MAX-1);
	vector<int> res(q, 0);
	int idx = p.size() - 1;
	cout<<idx<<endl;
	for(int i=0;i<q;i++){
		int n, ii;
		int target = v[i].first.first;
		n = v[i].first.second;
		ii = v[i].second;
		for(idx;p[idx]>target;idx--){
			for(int next=p[idx];next<MAX;next+=p[idx]){
				if (chk[next]) continue;
				chk[next] = 1;
				update(next, 0, 1, 1, MAX-1);
			}
		}
		res[ii] = query(2, n, 1, 1, MAX-1);
		cout<<idx<<endl;
		cout<<n<<" "<<target<<" "<<ii<<" "<<p[idx]<<endl;
		cout<<query(1, MAX-1, 1, 1, MAX-1)<<endl;;
	}
	cout<<"res "<<query(1, MAX-1, 1, 1, MAX-1)<<endl;;
	return 0;
}

int main(){
    FAST;
	go();
    cin>>q;
	v.resize(q);
	REP(i, q){
		int n, k;
		cin>>n>>k;
		v.pb({mp(k, n), i});
	}
    solve();
    return 0;
}

