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

int n,m;

#define PIS pair<int, string>

vector<PIS> even;
vector<PIS> odd;
int cnt[11];

int solve() {
	sort(odd.begin(), odd.end(), [] (PIS a,PIS b){
		if (a.first==b.first){
			if (a.second.length()==b.second.length()){
				return a.second<b.second;
			}else{
				return a.second.length()<b.second.length();
			}
		}else{
			return a.first<b.first;
		}
	});
	sort(even.begin(), even.end(), [] (PIS a,PIS b){
		if (a.first==b.first){
			if (a.second.length()==b.second.length()){
				return a.second<b.second;
			}else{
				return a.second.length()<b.second.length();
			}
		}else{
			return a.first<b.first;
		}
	});
	for(auto od : odd){
		cout<<od.first<<" "<<od.second<<'\n';
	}
	for(auto eve : even){
		cout<<eve.first<<" "<<eve.second<<'\n';
	}
	return 0;
}

int main(){
    FAST;
	cin>>n>>m;
	for(int i=0;;i++){
		int c;
		string s;
		cin>>c>>s;
		if(c==0){
			break;
		}
		if(cnt[c]>=m){
			continue;
		}
		cnt[c]++;
		if (c&1){
			odd.pb({c,s});
		}else{
			even.pb({c,s});
		}
	}
	solve();
    return 0;
}