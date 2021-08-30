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
    vector<int> idx;
    REP(i, n+1){
        idx.pb(i);
    }
    int prev = 1;
    REPN(i, n){
        ll tmp = s[i]-s[prev-1];
        if(tmp>w){
            if(s[i-1]-s[prev-1]<mid){
                return 0;
            }
            prev = i;
        }else{
            idx[i] = prev;
        }
    }
    int i = n;
    int idxz = idx[i];
    ll tmp = 0;
    while (i>0)
    {
        int j=i;
        while (idx[j]==idxz&&j>0)
        {
            j--;
        }
        j+=1;
        tmp = s[i]-s[j-1];
        // cout<<"test #1"<<endl;
        // printf("i: %d j: %d tmp: %lld\n",i,j,tmp);
        // printf("idxz: %d idx[i]: %d idx[j]: %d\n",idxz,idx[i],idx[j]);
        // cout<<"****************"<<endl;
        if(mid<=tmp&&tmp<=w){ // satisfy
            i = j-1;
            idxz = idx[i];
            tmp = 0LL;
        }else{
            while (tmp<mid&&j>0)
            {
                j--;
                tmp += a[j];
            }
            // cout<<"test #2"<<endl;
            // printf("i: %d j: %d tmp: %lld\n",i,j,tmp);
            // printf("idxz: %d idx[i]: %d idx[j]: %d\n",idxz,idx[i],idx[j]);
            if(tmp>w||j==0){
                return 0;
            }
            i = j-1;
            idxz = idx[i];
            tmp = 0LL;
        }
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
            res = max(res, mid);
        }else{
            r = mid - 1;
        }
    }
    cout<<SQR(w-res)<<endl;
    return 0;
}
