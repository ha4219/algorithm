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

int T, n, m;

char a[22][22];
int d[10][1<<10];

bool isset(int state, int i){
	return (state&(1<<i))>0;
}

bool check(int row, int state){
	if (row<0) return true;
	for(int j=0;j<m-1;j++){
		if (isset(state, j)&&isset(state, j+1)){
			return false;
		}
	}
	for(int j=0;j<m;j++){
		if(a[row][j]=='x'&&isset(state, j)){
			return false;
		}
	}
	return true;
}

int solve() {
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	RESET(d, 0);
	int res = 0;
	for(int row=0;row<n;row++){
		for (int state=0;state<(1<<m);state++){
			if(!check(row, state)) continue;

			for(int pstate=0;pstate<(1<<m); pstate++){
				if(!check(row-1, pstate)) continue;
				int cnt = 0;
				bool ok = true;
				for(int j=0;j<m;j++){
					if(isset(state,j)){
						cnt++;
						if(j-1>=0&&isset(pstate,j-1)) ok =false;
						if(j+1<m&&isset(pstate,j+1)) ok = false;
					}
				}
				if (ok){
					if(row==0){
						d[row][state] = max(d[row][state], cnt);
					}else{
						d[row][state] = max(d[row][state], d[row-1][pstate]+cnt);
					}
				}
			}
		}
		for(int state=0;state<(1<<m);state++){
			res = max(d[n-1][state], res);
		}
	}
	cout<<res<<endl;

	return 0;
}

int main(){
    FAST;
	cin>>T;
	TC(T) {
		solve();
	}
    return 0;
}