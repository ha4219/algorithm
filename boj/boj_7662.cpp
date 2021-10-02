#include<bits/stdc++.h>

typedef long long ll;


#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define PII pair<int,int>
#define PIII pair<PII,int>
#define Pll pair<ll,int>
#define Plll pair<Pll,int>
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

#define INF 1000001
#define MAX 1000001

using namespace std;

int v[MAX];
int n, t;

int main(void){
	FAST;
    cin>>t;
    TC(t){
        RESET(v, 0);
        priority_queue<Pll> minQ;
        priority_queue<Pll> maxQ;
        cin>>n;
        REP(i, n){
            char c;
            ll num;
            cin>>c>>num;
            if(c=='I'){
                minQ.push({-num, i});
                maxQ.push({num, i});
                v[i] = 1;
            }else if(num==1){
                while (!maxQ.empty()&&!v[maxQ.top().second]){
                    maxQ.pop();
                }
                if(!maxQ.empty()){
                    v[maxQ.top().second] = 0;
                    maxQ.pop();
                }
            }else{
                while(!minQ.empty()&&!v[minQ.top().second]){
                    minQ.pop();
                }
                if(!minQ.empty()){
                    v[minQ.top().second] = 0;
                    minQ.pop();
                }
            }
        }
        while (!maxQ.empty()&&!v[maxQ.top().second]){
            maxQ.pop();
        }
        while(!minQ.empty()&&!v[minQ.top().second]){
            minQ.pop();
        }
        if(maxQ.empty()||minQ.empty()){
            cout<<"EMPTY\n";
        }else{
            cout<<maxQ.top().first<<" "<<-minQ.top().first<<'\n';
        }
    }
    return 0;
}
