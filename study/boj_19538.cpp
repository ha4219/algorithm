#include <bits/stdc++.h>

// #define MAX 2^26+1
#define MAX 200001
using namespace std;
vector<int> a[MAX];
int s[MAX];
int v[MAX];


int n;

int solve(){
    int res[MAX];
    scanf("%d", &n);
    for(int i=1;i<=n;i++){
        int t;
        scanf("%d", &t);
        while(t!=0){
            a[i].push_back(t);
            s[i]++;
            scanf("%d", &t);
        }
    }
    queue<pair<int, int> > q;
    memset(res, -1, sizeof(res));
    int m;
    pair<int, int> tt;
    scanf("%d", &m);
    for(int i=0;i<m;i++){
        int t;
        scanf("%d", &t);
        v[t] = 1;
        res[t] = 0;
        
        tt.first = t;
        tt.second = 0;
        q.push(tt);
    }
    
    while(!q.empty()){
        int cur=q.front().first;
        int time=q.front().second;
        q.pop();
        // printf("%d %d \n", time, cur);
        
        // printf("a[cur].size = %d\n", a[cur].size());
        for(int i=0;i<a[cur].size();i++){
            int next = a[cur][i];
            // printf("next: %d\n", next);
            if(v[next]){
                continue;
            }
            int t = s[next]&1 ? s[next]/2+1:s[next]/2;
            int rr=0;
            for(auto nr:a[next]){
                // printf("next: %d nr: %d\n", next, nr);
                // printf("res[nr]: %d, v[nr]: %d\n", res[nr], v[nr]);
                if(res[nr]!=-1&&res[nr]<=time){
                    rr++;
                }
            }
            // printf("t: %d rr: %d\n", t, rr);
            if(t<=rr){
                v[next] = 1;
                res[next] = time+1;
                tt.first = next;
                tt.second = time+1;
                q.push(tt);
            }
        }
    }
    for(int i=1;i<=n;i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}

int main() {
    int T;
    
    solve();
    return 0;
}