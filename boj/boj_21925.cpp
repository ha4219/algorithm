#include <bits/stdc++.h>


typedef long long ll;

int n,m;
int a[5001];
int d[5001][5001];

using namespace std;

int res = -1;

void f(int i, int c){
    // printf("%d %d\n",i,c);
    if(i==n){
        res = max(res, c);
        printf("%d\n",res);
        exit(0);
    }else{
        for(int next=i+1;next<n;next+=2){
            if(d[i][next]){
                f(next+1,c+1);
            }
        }
    }
}

int solve() {
    scanf("%d",&n);
    memset(d,0,sizeof(d));
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i;j++){
            if(i==0){
                d[j][j] = 1;
            }else if(i==1){
                d[j][j+1] = (a[j]==a[j+1]) ? 1:0;
            }else{
                d[j][i+j] = (a[j]==a[j+i]) ? d[j+1][j+i-1]:0;
            }
        }
    }
    // for(int i=0;i<n;i++){
    //     for(int j=0;j<n;j++){
    //         printf("%d ",d[i][j]);
    //     }
    //     printf("\n");
    // }
    f(0,0);
    return res;
}

int main() {
    printf("%d\n",solve());
    return 0;
}