#include <bits/stdc++.h>


#define MAX 2000001
#define T 1000001
#define N 500001

using namespace std;

long long s[MAX];
int t[T];
// int a[N];

long long q(int l, int r, int node, int nL, int nR) {
    if((l>nR)||(r<nL)){
        return 0;
    }
    if((l<=nL)&&(nR<=r)){
        return s[node];
    }
    int m = (nL+nR)/2;
    return q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR);
}

long long u(int i, int v, int node, int nL, int nR) {
    if((i<nL)||(i>nR)){
        return s[node];
    }
    if(nL==nR){
        s[node] += v;
        return s[node];
    }
    int m = (nL+nR)/2;
    s[node] = u(i,v,node*2,nL,m)+u(i,v,node*2+1,m+1,nR);
    return s[node];
}

long long solve() {
    int n;
    long long res = 0;
    scanf("%d", &n);
    for(int i=0;i<n;i++){
        int tmp;
        scanf("%d", &tmp);
        t[tmp] = i+1;
    }
    for(int i=0;i<n;i++){
        int tmp;
        scanf("%d", &tmp);
        res += q(t[tmp]+1,n,1,1,n);
        u(t[tmp],1,1,1,n);
    }
    return res;
}

int main() {
    printf("%lld\n",solve());
}