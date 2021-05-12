#include <bits/stdc++.h>
#define MAX 2000001
#define MAXF 8000001

int n;

using namespace std;

int s[MAXF];

int update(int i,int v,int node,int nL,int nR){
    if ((i<nL)||(i>nR)){
        return s[node];
    }
    if (nL==nR){
        s[node] += v;
        return s[node];
    }
    int m = (nL+nR)/2;
    return s[node] = update(i,v,node*2,nL,m)+update(i,v,node*2+1,m+1,nR);
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
    scanf("%d", &n);
    int t,x;
    for(int i=0;i<n;i++){
        scanf("%d %d",&t,&x);
        if(t==1){
            update(x,1,1,0,MAX-1);
        }else{
            int r = q(x,1,0,MAX-1);
            printf("%d\n",r);
            update(r,-1,1,0,MAX-1);
        }
    }
    return 0;
}

int main() {
    solve();
    return 0;
}