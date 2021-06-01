#include <bits/stdc++.h>
#define MAX 2000001
#define MAXF 8000001

int n;

using namespace std;

int s[MAXF];
int a[MAXF];
int res[MAXF];

int u(int i,int v,int node,int nL,int nR){
    if ((i<nL)||(i>nR)){
        return s[node];
    }
    if (nL==nR){
        s[node] += v;
        return s[node];
    }
    int m = (nL+nR)/2;
    return s[node] = u(i,v,node*2,nL,m)+u(i,v,node*2+1,m+1,nR);
}

int q(int num,int node,int nL,int nR){
    if (nL==nR){
        return nL;
    }
    int m = (nL+nR)/2;
    if (num>s[node*2]){
        num -= s[node*2];
        return q(num,node*2+1,m+1,nR);
    }
    return q(num,node*2,nL,m);
}

int solve() {
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=1;i<=n;i++){
        u(i,1,1,1,n);
    }
    for(int i=1;i<=n;i++){
        int ret=q(a[i]+1,1,1,n);
        res[ret] = i;
        u(ret,-1,1,1,n);
    }
    for(int i=1;i<=n;i++){
        printf("%d\n",res[i]);
    }
    return 0;
}

int main() {
    solve();
    return 0;
}