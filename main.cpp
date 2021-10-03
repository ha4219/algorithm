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

<<<<<<< HEAD
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

int n;
vector<PII> a;
set<PII> s;

int dist(PII l, PII r){
    return ((r.fi-l.fi)*(r.fi-l.fi)+(r.se-l.se)*(r.se-l.se));
}

int divide_and_conquer(int l, int r){
    int length = r-l+1;
    if (length==1){
        return INF;
    }else if (length==2){
        return dist(a[l],a[r]);
    }else if(length==3){
        return min(min(dist(a[l],a[l+1]),dist(a[l],a[r])),dist(a[l+1],a[r]));
    }
    int m = (l+r)/2;
    int d = min(divide_and_conquer(l, m), divide_and_conquer(m+1, r));
    int midX = a[m].fi;
    vector<PII> cmp_list;
    for(int i=l;i<=r;i++){
        if((a[i].fi-midX)*(a[i].fi-midX)<d){
            cmp_list.pb(a[i]);
        }
    }
    int cmp_len = cmp_list.size();
    if (cmp_len>=2){
        sort(cmp_list.begin(), cmp_list.end(), [](PII &ll,PII &rr){
            if(ll.se==rr.se){
                return ll.fi<rr.fi;
            }
            return ll.se<rr.se;
        });
        // for(auto iter : cmp_list){
        //     cout<<iter.fi<<" "<<iter.se<<endl;
        // }
        for(int i=0;i<cmp_len-1;i++){
            for(int j=i+1;j<cmp_len;j++){
                if((cmp_list[i].se-cmp_list[j].se)*(cmp_list[i].se-cmp_list[j].se)>d) break;
                // else if((cmp_list[i].fi<midX)&&cmp_list[j].fi<midX) continue;
                // else if((cmp_list[i].fi>=midX)&&cmp_list[j].fi>=midX) continue;
                d = min(d, dist(cmp_list[i], cmp_list[j]));
            }
        }
    }
    // cout<<l<<" "<<r<<" "<<d<<endl;
    return d;
}


int solve() {
    if(n!=s.size()){
        cout<<0<<'\n';
        return 0;
    }
    for(auto iter : s){
        a.pb({iter.fi, iter.se});
    }
    // for(auto iter : s){
    //     cout<<iter.fi<<" "<<iter.se<<endl;
    // }
    sort(a.begin(), a.end());
    cout<<divide_and_conquer(0, n-1)<<'\n';
	return 0;
}

int main(){
    FAST;
    cin>>n;
    REP(i, n){
        int x,y;
        cin>>x>>y;
        s.insert({x,y});
    }
	solve();
    return 0;
}