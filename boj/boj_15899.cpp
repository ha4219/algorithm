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
#define MAX 200001
#define ALLPATH 1023
#define MOD 1000000007

using namespace std;

int n, m, c;
int cnt;
int start[MAX];
int endend[MAX];
vector<int> s[MAX*4];
vector<vector<int>> a;
vector<int> arr;

void dfs(int x, int par){
    start[x] = ++cnt;
    for(auto next : a[x]){
        if(next==par)
            continue;
        dfs(next,x);
    }
    endend[x] = cnt;
}

void update(int idx, int x, int node, int nL, int nR){
	if (idx<nL||nR<idx){
		return;
	}
	s[node].pb(x);
	if(nL!=nR){
		int mid = (nL+nR)/2;
		update(idx, x, node*2, nL, mid);
		update(idx, x, node*2+1, mid+1, nR);
	}
}

int query(int x, int l, int r, int node, int nL, int nR){
	if(l>nR||r<nL){
		return 0;
	}
	if(l<=nL&&nR<=r){
		return upper_bound(s[node].begin(), s[node].end(), x)-s[node].begin();
	}
	int mid = (nL+nR)/2;
	return query(x,l,r,node*2,nL,mid)+query(x,l,r,node*2+1,mid+1,nR);
}

int solve(){
	dfs(1, -1);
	REPN(i, n){
		update(start[i],arr[i],1,1,n);
	}
	REP(i, MAX*4){
		sort(s[i].begin(), s[i].end());
	}
	int res = 0;
	REP(_, m){
		int i,j;
		cin>>i>>j;
		res = (res + query(j,start[i],endend[i],1,1,n))%MOD;
	}
	cout<<res<<'\n';
	return 0;
}

int main(){
    FAST;
	cin>>n>>m>>c;
	a.resize(n+1);
	arr.resize(n+1);
	REPN(i, n){
		cin>>arr[i];
	}
	REP(i, n-1){
		int p,q;
		cin>>p>>q;
		a[p].pb(q);
		a[q].pb(p);
	}
	solve();
    return 0;
}