#include <bits/stdc++.h>
#define MAX 100001
#define MAXF 100001

typedef long long ll;

int n;

using namespace std;


ll s[MAXF];
int a[MAXF];
int t[MAXF];

ll q(int i){
    ll res = 0;
    while(i>0){
        // printf("q %d",i);
        res += s[i];
        i &= (i-1);
    }
    return res;
}

void u(int i,ll v){
    while(i<n+1){
        // printf("%d",i);
        s[i] += v;
        i += (i&-i);
    }
}

int solve() {
    memset(s,0,sizeof(s));
    memset(a,0,sizeof(a));
    memset(t,0,sizeof(t));
    scanf("%d", &n);
    int k;
    for(int i=0;i<n;i++){
        scanf("%d", &k);
        t[k] = i+1;
    }
    for(int i=0;i<n;i++){
        scanf("%d", &k);
        a[t[k]] = i+1;
    }
    ll res = 0;
    for(int i=1;i<=n;i++){
        ll p = q(n)-q(a[i]);
        res += p;
        u(a[i],1);
    }
    printf("%lld\n",res);
    return 0;
}

int main() {
    int p;
    scanf("%d",&p);
    for(int i=0;i<p;i++){
        solve();
    }
    return 0;
}