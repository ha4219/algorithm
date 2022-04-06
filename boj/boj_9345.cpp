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
#define MAX 400000

#define MINVALUE -1
#define MAXVALUE 100001
#define MOD 1000000007

using namespace std;

int n, p;

vector<int> arr;
vector<int> s_min;
vector<int> s_max;

void u(int i, int v, int node, int nL, int nR) {
    if (nL>i||i>nR) return;
    if (nL==nR) {
        s_min[node] = v;
        s_max[node] = v;
        return;
    }
    int m = (nL+nR) / 2;
    u(i,v,node*2,nL,m);
    u(i,v,node*2+1,m+1,nR);
    s_min[node] = min(s_min[node*2], s_min[node*2+1]);
    s_max[node] = max(s_max[node*2], s_max[node*2+1]);
    return;
}

int q_min(int l, int r, int node, int nL, int nR) {
    if (nL>r || nR < l) return MAXVALUE;
    if (l<=nL && nR<=r) return s_min[node];
    int m = (nL+nR)/2;
    return min(q_min(l,r,node*2,nL,m), q_min(l,r,node*2+1,m+1,nR));
}

int q_max(int l, int r, int node, int nL, int nR) {
    if (nL>r || nR < l) return MINVALUE;
    if (l<=nL && nR<=r) return s_max[node];
    int m = (nL+nR)/2;
    return max(q_max(l,r,node*2,nL,m), q_max(l,r,node*2+1,m+1,nR));
}

int solve() {
    cin>>n>>p;
    arr.resize(n);
    s_min.resize(4*n, MAXVALUE);
    s_max.resize(4*n, MINVALUE);
    for(int i=0;i<n;i++){
        arr[i] = i;
        u(i,i,1,0,n-1);
    }

    for(int i=0;i<p;i++){
        int a,b,c;
        cin>>a>>b>>c;
        if (a) {
            int l = q_min(b, c, 1, 0, n-1);
            int r = q_max(b, c, 1, 0, n-1);

            if (l==b && r==c) {
                cout<<"YES\n";
            } else {
                cout<<"NO\n";
            }
        } else {
            int l = arr[b];
            int r = arr[c];
            u(b, r, 1, 0, n-1);
            u(c, l, 1, 0, n-1);
            arr[b] = r;
            arr[c] = l;
        }
    }

    return 0;
}

int main() {
    FAST;
    int tc;
    cin>>tc;
    TC(tc) {
        solve();
    }
    return 0;
}