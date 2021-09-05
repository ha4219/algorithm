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
int a, b;

int solve() {
    if (b==0){
        if (a==1){
            cout<<1<<endl;
        }else{
            int cnt = a;
            int res = 0;
            if (a%4==1){
                res = a-1;
            }else if(a%4==2){
                res = 1;
            }else if(a%4==3){
                res = (a/4+1)*4 - 1;
            }else{
                res = 0;
            }
            if (res==b){
                cout<<cnt<<endl;
            }else if((res^b)==a){
                cout<<cnt+2<<endl;
            }else if(res==0){
                cout<<cnt+2<<endl;
            }else{
                cout<<cnt+1<<endl;
            }
        }
    }else{
        if (a==b){
            int cnt = a;
            int res = 0;
            if (a%4==1){
                res = a-1;
            }else if(a%4==2){
                res = 1;
            }else if(a%4==3){
                res = (a/4+1)*4 - 1;
            }else{
                res = 0;
            }
            if (res==b){
                cout<<cnt<<endl;
            }else if((res^b)==a){
                cout<<cnt+2<<endl;
            }else if(res==0){
                cout<<cnt+2<<endl;
            }else{
                cout<<cnt+1<<endl;
            }
        }else{
            if (a==1){
                cout<<2<<endl;
            }else{
                int cnt = a;
                int res;
                if (a%4==1){
                    res = a-1;
                }else if(a%4==2){
                    res = 1;
                }else if(a%4==3){
                    res = (a/4+1)*4 - 1;
                }else{
                    res = 0;
                }
                if (res==b){
                    cout<<cnt<<endl;
                }else if((res^b)==a){
                    cout<<cnt+2<<endl;
                }else if(res==0){
                    cout<<cnt+2<<endl;
                }else{
                    cout<<cnt+1<<endl;
                }
            }
        }
    }
    return 0;
}

int main(){
    FAST;
    cin>>t;
    TC(t){
        cin>>a>>b;
        solve();
    }
    return 0;
}