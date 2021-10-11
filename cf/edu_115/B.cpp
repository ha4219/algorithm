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


int T, n;
vector<vector<int>> a;

int solve() {
    if(n&1) return 0;
    for(int i=0;i<4;i++){
        for(int j=i+1;j<5;j++){
            int cnt[] = {0,0,0};
            for(int f=0;f<n;f++){
                if(a[f][i]&&a[f][j]){
                    cnt[2]++;
                }else if(a[f][i]){
                    cnt[0]++;
                }else if(a[f][j]){
                    cnt[1]++;
                }
            }
            if((cnt[0]+cnt[1]+cnt[2]==n)&&(cnt[0]<=n/2)&&(cnt[1]<=n/2)){
                return 1;
            }
        }
    }
    return 0;
}

int main(){
    FAST;
    cin>>T;
    TC(T) {
        cin>>n;
        a.resize(n, vector<int> (5, 0));
        for(int i=0;i<n;i++){
            for(int j=0;j<5;j++){
                cin>>a[i][j];
            }
        }
        if(solve()){
            cout<<"YES\n";
        }else{
            cout<<"NO\n";
        }
    }
    return 0;
}