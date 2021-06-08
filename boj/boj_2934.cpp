#include <bits/stdc++.h>
#define MAX 100001
#define MAXF 400001
#define MOD 4294967296

typedef long long ll;

int n,m;

using namespace std;


ll s[MAXF];
ll lazy[MAXF];

void propagation(int node, int nL, int nR){
    if(lazy[node]){
        s[node] += (nR-nL+1)*lazy[node];
        if(nL!=nR){
            lazy[node*2]+=lazy[node];
            lazy[node*2+1]+=lazy[node];
        }
        lazy[node] = 0;
    }
}


void u(int l,int r,ll v,int node,int nL,int nR){
    propagation(node, nL, nR);
    if ((l>nR)||(r<nL)){
        return;
    }
    if ((l<=nL)&&(nR<=r)){
        lazy[node] += v;
        propagation(node, nL, nR);
        return;
    }
    int m = (nL+nR)/2;
    u(l,r,v,node*2,nL,m);
    u(l,r,v,node*2+1,m+1,nR);
    s[node] = s[node*2]+s[node*2+1];
    return;
}

ll q(int l,int r,int node,int nL,int nR){
    // printf("q : %d %d %d %d %d\n",l,r,node,nL,nR);
    propagation(node, nL, nR);
    if ((l>nR)||(r<nL)){
        return 0;
    }
    if (l<=nL&&nR<=r){
        return s[node];
    }
    int m = (nL+nR)/2;
    return q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR);
}

int solve() {
    memset(s,0,sizeof(s));
    memset(lazy,0,sizeof(lazy));
    scanf("%d",&m);
    n = MAX-1;
    int x,y;
    for(int i=0;i<m;i++){
        scanf("%d %d",&x,&y);
        ll left,right;
        left = q(x,x,1,1,n);
        right = q(y,y,1,1,n);
        printf("%lld\n",left+right);
        if(left)
            u(x,x,-left,1,1,n);
        if(right)
            u(y,y,-right,1,1,n);
        u(x+1,y-1,1LL,1,1,n);
    }
    return 0;
}

int main() {
    solve();
    return 0;
}