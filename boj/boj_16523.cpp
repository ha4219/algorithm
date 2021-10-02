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
#define MAX 10001
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;

int n;
int d[MAX][7];

vector<PII> a;

int f(int idx, int time, int cnt) {
	if (idx==n) {
		return 0;
	}
	int &res = d[idx][cnt];
	if (res!=-1) {
		return res;
	}
	res = INF;
	if (time>=120 || cnt==6){
		res = f(idx+1, a[idx].first, 1) + a[idx].second*4;
	}else{
		res = f(idx+1, a[idx].first, 1) + a[idx].second*4;
		if(cnt==0){
			res = min(res, f(idx+1, time+a[idx].first, cnt+1) + a[idx].second*4);
		}else if (cnt==1) {
			res = min(res, f(idx+1, time+a[idx].first, cnt+1) + a[idx].second*2);
		}else{
			cnt = min(cnt, 6);
			res = min(res, f(idx+1, time+a[idx].first, cnt+1) + a[idx].second);
		}
	}
	return res;
}

int solve() {
	RESET(d, -1);
	int res = f(0,0,0);
	string s = "";
	if(res%4==0){
		s = ".00";
	}else if(res%4==1){
		s = ".25";
	}else if(res%4==2){
		s = ".50";
	}else{
		s = ".75";
	}
	cout<<res/4<<s<<endl;
    return 0;
}

int main(){
    FAST;
    cin>>n;
	a.resize(n);
	REP(i, n){
		cin>>a[i].first>>a[i].second;
	}
    solve();
    return 0;
}

