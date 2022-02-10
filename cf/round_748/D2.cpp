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
#define MAX 2000002
#define ALLPATH 1023
#define MOD 1000000007
 
using namespace std;
 
int v[MAX];
int t;
int n;
vector<int> a;
 
int solve(){
    sort(a.begin(), a.end());
    for(int i=1;i<n;i++){
        a[i]-=a[0];
    }
    a[0] = 0;
    int cnt = 1;
    for(int i=0;i<n;i++){
        int j=i;
        while(j<n&&a[i]==a[j]) j++;
        cnt = max(cnt, j-i);
        i = j;
    }
    if (cnt>=n/2) {
        puts("-1");
        return 0;
    }
    int res = 1;
    for(int gcd=MAX-1;gcd>1;gcd--){
        bool can = false;
        REP(i, n){
            can |= (++v[a[i] % gcd]>=n/2);
        }
 
        REP(i, n){
            v[a[i] % gcd] = 0;
        }
        if(can){
            res = gcd;
            break;
        }
    }
 
    printf("%d\n", res);
    return 0;
}
 
int main(){
    scanf("%d", &t);
    TC(t){
        // cin>>n;
        scanf("%d", &n);
        a.resize(n);
        REP(i, n){
            // cin>>a[i];
            scanf("%d", &a[i]);
        }
        solve();
    }
    return 0;
}