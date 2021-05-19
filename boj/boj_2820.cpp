#include <bits/stdc++.h>
#define MAX 500001
#define MAXF 2000001

int n,m;

using namespace std;

int s[MAXF];
int lazy[MAXF];
int aa[MAX];
int start[MAX];
int endend[MAX];
vector<int> a[MAX];

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


int u(int l,int r,int v,int node,int nL,int nR){
    propagation(node, nL, nR);
    if (nL>r||nR<l){
        return s[node];
    }
    if (l<=nL&&nR<=r){
        lazy[node] += v;
        propagation(node, nL, nR);
        return s[node];
    }
    int m=(nL+nR)/2;
    s[node]=u(l,r,v,node*2,nL,m)+u(l,r,v,node*2+1,m+1,nR);
    return s[node];
}

int q(int l,int r,int node,int nL,int nR){
    propagation(node, nL, nR);
    if(nL>r||nR<l){
        return 0;
    }
    if(l<=nL&&nR<=r){
        return s[node];
    }
    int m=(nL+nR)/2;
    return q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR);
}

int cnt;
void dfs(int x, int par){
    start[x] = ++cnt;
    for(auto next : a[x]){
        if(next==par)
            continue;
        dfs(next,x);
    }
    endend[x] = cnt;
}

int solve() {
    scanf("%d %d", &n, &m);
    scanf("%d",&aa[1]);
    for(int i=2;i<=n;i++){
        int p,q;
        scanf("%d %d", &p,&q);
        aa[i] = p;
        a[q].push_back(i);
    }
    cnt = 0;
    dfs(1,-1);
    for(int i=1;i<=n;i++){
        u(start[i],start[i],aa[i],1,1,n);
    }

    // for(int i=1;i<=6;i++){
    //     printf("%d : %d\n", i, q(start[i],start[i],1,1,n));
    //     printf("%d ~ %d\n",start[i],endend[i]);
    // }
    char z;
    int x,c;
    for(int i=0;i<m;i++){
        getchar();
        scanf("%c",&z);
        if(z=='p'){
            scanf("%d %d",&x,&c);
            if(start[x]!=endend[x]){
                u(start[x]+1,endend[x],c,1,1,n);
            }
        }else{
            scanf("%d",&x);
            printf("%d\n",q(start[x],start[x],1,1,n));
        }
    }

    // for(int i=1;i<=6;i++){
    //     printf("%d : %d\n", i, q(start[i],start[i],1,1,n));
    //     printf("%d ~ %d\n",start[i],endend[i]);
    // }
    return 0;
}

int main() {
    solve();
    return 0;
}