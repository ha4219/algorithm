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

#define INF 1e17
#define MAX 500001

using namespace std;

ll w;
int n;
vector<ll> a;
vector<ll> s;
ll d[MAX];

int f(int mid){
    //mid<=뭉텅이<=w
    int prev = 0;
    int flag1 = 1;
    REPN(i, n){
        int tmp = s[i]-s[prev-1];
        if(tmp>w){
            prev = i;
            if(tmp-a[i]<mid){
                cout<<"first"<<tmp-a[i]<<endl;
                return 0;
            }
        }
    }
    int tmp = s[n] - s[prev-1];
    if(tmp>w){
        if(s[n-1]-s[prev-1]<mid){
            cout<<"second"<<s[n-1]-s[prev-1]<<endl;
            return 0;
        }
        if(a[n]>w||a[n]<mid){
            cout<<"third"<<a[n]<<endl;
            return 0;
        }
    }else if(tmp<mid){
        cout<<"firth"<<tmp<<endl;
        return 0;
    }
    return 1;
}

int main(void){
	FAST;
    cin>>w>>n;
    a.resize(n+1);
    s.resize(n+1);
    RESET(d, -1);
    REPN(i, n){
        cin>>a[i];
        s[i] = s[i-1] + a[i];
    }
    int l = 1;
    int r = w;
    int res = 0;
    while (l<=r){
        int mid = (l+r)/2;
        if(f(mid)){
            l = mid + 1;
            cout<<mid<<endl;
            res = max(res, mid);
        }else{
            cout<<"false"<<mid<<endl;
            r = mid - 1;
        }
    }
    cout<<res<<endl;
    return 0;
}
