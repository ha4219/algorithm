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
#define MAX 100001
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;

int n, m;
vector<int> s[MAX*4];

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

int solve() {
	REPN(i, n){
		int tmp;
		cin>>tmp;
		update(i, tmp, 1, 1, n);
	}

	REP(i, MAX*2){
		sort(ALL(s[i]));
	}
	// nlogn

	while (m--)
	{
		int q,w,e;
		cin>>q>>w>>e;
		int l = -1e9, r = 1e9;
		while (l<=r)
		{
			int mid = (l+r)/2;
			if(query(mid,q,w,1,1,n)<e){
				l = mid + 1;
			}else{
				r = mid - 1;
			}
		}
		cout<<l<<'\n';
	}
	
	return 0;
}

int main(){
    FAST;
	cin>>n>>m;
	solve();
    return 0;
}