#include <bits/stdc++.h>

#define MAX 10001

typedef pair<int, int> PAIR;
typedef tuple<int, int, int> TUPLE;
typedef long long ll;
const int INF = 1 << 30;

using namespace std;


int n, m, p;


int d[101][MAX];


int dijkstra(int start, vector<TUPLE> &a){
    priority_queue<TUPLE, vector<TUPLE>, greater<TUPLE>> pq;
    pq.push({0,start,0});
    d[start][0] = 0;
    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();
        int cur_t = get<0>(cur);
        int cur_x = get<1>(cur);
        int cur_c = get<2>(cur);

        if(cur_x==n){
            return cur_t;
        }
        if(cur_t>d[cur_x][cur_c]){
            continue;
        }
        for(auto next : a[cur_x]){
            int next_x = get<0>(next);
            int next_c = get<1>(next);
            int next_t = get<2>(next);
            if(cur_c+next_c>m||d[next_x][cur_c+next_c]<=d[cur_x][cur_c]+next_t){
                continue;
            }
            d[next_x][next_c+cur_c] = d[cur_x][cur_c] + next_t;
            pq.push({cur_t+next_t,next_x,cur_c+next_c});
        }
    }

    return -1;
}

int solve(){
    for(int i=0;i<101;i++){
        a[i].clear();
    }
    vector<TUPLE> a[101];
    scanf("%d %d %d",&n,&m,&p);
    for(int i=0;i<=n;i++){
        for(int j=0;j<=m;j++){
            d[i][j] = INF;
        }
    }
    for(int i=0;i<p;i++){
        int q,w,e,r;
        scanf("%d %d %d %d",&q,&w,&e,&r);
        a[q].push_back({w,e,r});
    }
    int res = dijkstra(1, a);
    return 1;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i=0;i<T;i++){
        solve();
    }
    return 0;
}