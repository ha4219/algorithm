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
#define MAX 1000001

using namespace std;

int t;
string n;

int solve() {
    string sodd = "";
    string seven = "";
    int l = n.length();
    int res;
    REP(i, l){
        if(i%2) sodd+=n[i];
        else seven+=n[i];
    }
    if (sodd==""){
        int even = stoi(seven);
        res = even-1;
    }else if(seven==""){
        int odd = stoi(sodd);
        res = odd-1;
    }else{
        int odd = stoi(sodd);
        int even = stoi(seven);
        if (odd==0){
            res = even - 1;
        }else if(even==0){
            res = odd - 1;
        }else{
            res = (odd+1)*(even+1)-2;
        }
    }
    cout<<res<<endl;
    return 0;
}

int main(){
    FAST;
    cin>>t;
    TC(t){
        cin>>n;
        solve();
    }
    return 0;
}