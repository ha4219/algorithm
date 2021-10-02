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
#define MAX 1024
#define ALLPATH 1023
#define MOD 1000000000

using namespace std;

int T;
int n;
vector<PII> a;
bool status[1001];
int values[1001];
bool v[1001];

int main(){
    FAST;
    cin>>n;
    REP(i, n){
        char c;
        cin>>c>>values[i];
        status[i] = c=='y'?1:0;
        a.pb({values[i], i});
    }
    int res = 0;
    sort(a.begin(), a.end());
    REP(i, n){
        int len = a[i].first;
        int idx = a[i].second;
        if (v[idx]||status[idx]==0){
            continue;
        }
        res++;
        v[idx] = 1;
        for(int j=idx-1;j>=0;j--){
            if (status[j]==0&&len<=values[j])
                break;
            v[j] = 1;
        }
        for(int j=idx+1;j<n;j++){
            if (status[j]==0&&len<=values[j])
                break;
            v[j] = 1;
        }
    }
    cout<<res<<'\n';
    return 0;
}