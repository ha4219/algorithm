#include <bits/stdc++.h>
#define MAX 100001
#define MAXF 400001
#define MOD 1000000007

typedef long long ll;

int n;

using namespace std;


ll s[MAXF];
ll lazy1[MAXF];
ll lazy2[MAXF];
int a[MAXF];
int t[MAXF];

void propagation(int node,int nL,int nR){
    if((lazy1[node]==1)&&(lazy2[node]==0))
        return;
    // printf("prop: %d %lld %lld\n", node, lazy1[node], lazy2[node]);
    s[node] = (lazy1[node]*s[node]+(nR-nL+1)*lazy2[node])%MOD;
    if(nL!=nR){
        lazy1[node*2]=(lazy1[node*2]*lazy1[node])%MOD;
        lazy1[node*2+1]=(lazy1[node*2+1]*lazy1[node])%MOD;
        lazy2[node*2]=(lazy2[node*2]*lazy1[node]+lazy2[node])%MOD;
        lazy2[node*2+1]=(lazy2[node*2+1]*lazy1[node]+lazy2[node])%MOD;
    }
    lazy1[node] = 1;
    lazy2[node] = 0;
}

ll q(int l, int r, int node, int nL, int nR){
    propagation(node, nL, nR);
    if (l>nR||r<nL){
        return 0;
    }
    if(l<=nL&&nR<=r){
        return s[node];
    }
    int m=(nL+nR)/2;
    return (q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR))%MOD;
}

ll u(int l,int r,ll p,ll pp, int node, int nL, int nR){
    propagation(node, nL, nR);
    if (l>nR||r<nL){
        return s[node];
    }
    if(l<=nL&&nR<=r){
        lazy1[node] = (lazy1[node]*p)%MOD;
        lazy2[node] = (p*lazy2[node]+pp)%MOD;
        propagation(node, nL, nR);
        return s[node];
    }
    int m=(nL+nR)/2;
    return s[node]=(u(l,r,p,pp,node*2,nL,m)+u(l,r,p,pp,node*2+1,m+1,nR))%MOD;
}

int solve() {
    memset(s,0,sizeof(s));
    memset(lazy1,1,sizeof(lazy1));
    memset(lazy2,0,sizeof(lazy1));
    scanf("%d", &n);
    
    for(int i=1;i<=n;i++){
        ll k;
        scanf("%lld", &k);
        u(i,i,0,k%MOD,1,1,n);
    }
    int m;
    int l,r;
    ll v;
    scanf("%d", &m);
    for(int i=0;i<m;i++){
        int t;
        scanf("%d", &t);
        if(t==1){
            scanf("%d %d %lld",&l,&r,&v);
            u(l,r,1,v,1,1,n);
        }else if(t==2){
            scanf("%d %d %lld",&l,&r,&v);
            u(l,r,v,0,1,1,n);
        }else if(t==3){
            scanf("%d %d %lld",&l,&r,&v);
            u(l,r,0,v,1,1,n);
        }else{
            scanf("%d %d",&l,&r);
            printf("%lld\n",q(l,r,1,1,n));
        }
        // for(int j=0;j<10;j++){
        //     printf("%d %lld\n",j,s[j]);
        // }
    }
    return 0;
}

int main() {
    solve();
    return 0;
}