#include <bits/stdc++.h>


typedef long long ll;

int n,m;
int a[2001][2001];
int v[2001][2001][4];
int r[2001][2001];

using namespace std;

struct t{
    int x;
    int y;
    int d;
};

int solve() {
    scanf("%d %d",&n,&m);
    queue<t> q;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf("%d",&a[i][j]);
            if(a[i][j]==9){
                r[i][j] = 1;
                for(int k=0;k<4;k++){
                    q.push({i,j,k});
                }
            }
        }
    }
    int dx[] = {0,0,1,-1};
    int dy[] = {1,-1,0,0};

    while(!q.empty()){
        t tmp = q.front();
        q.pop();
        int cx,cy,d;
        d = tmp.d;
        cx=tmp.x+dx[d];
        cy=tmp.y+dy[d];
        if((cx<0)||(cy<0)||(cx>=n)||(cy>=m)||(v[cx][cy][d])){
            continue;
        }
        v[cx][cy][d] = 1;
        r[cx][cy] = 1;
        if(a[cx][cy]==0){
            q.push({cx,cy,d});
        }else if(a[cx][cy]==1){
            if(d>1){
                q.push({cx,cy,d});
            }
        }else if(a[cx][cy]==2){
            if(d<2){
                q.push({cx,cy,d});
            }
        }else if(a[cx][cy]==3){
            if(d==0){
                q.push({cx,cy,3});
            }else if(d==1){
                q.push({cx,cy,2});
            }else if(d==2){
                q.push({cx,cy,1});
            }else{
                q.push({cx,cy,0});
            }
        }else{
            if(d==0){
                q.push({cx,cy,2});
            }else if(d==1){
                q.push({cx,cy,3});
            }else if(d==2){
                q.push({cx,cy,0});
            }else{
                q.push({cx,cy,1});
            } 
        }
    }
    int res = 0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            res += r[i][j];
        }
    }
    return res;
}

int main() {
    printf("%d",solve());
    return 0;
}