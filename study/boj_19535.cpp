#include <bits/stdc++.h>

// #define MAX 2^26+1
#define MAX 300001
using namespace std;

typedef long long ll;
vector<int> a[MAX];
int s[MAX];
int v[MAX];
ll f[MAX];
ll d, g;

int n;

void dfs(int cur){
    v[cur] = 1;
    // g
    if(s[cur]>=3){
        // g += f[s[cur]]/f[3];
        g += (ll)(s[cur])*(s[cur]-1)*(s[cur]-2)/6;
    }
    // d
    for(int next:a[cur]){
        if(v[next])
            continue;
        d += (ll)(s[cur]-1LL)*(ll)(s[next]-1LL);
        dfs(next);
    }
}

int solve(){
    scanf("%d", &n);
    for(int i=0;i<n-1;i++){
        int p,q;
        scanf("%d %d", &p, &q);
        s[p]++;s[q]++;
        a[p].push_back(q);
        a[q].push_back(p);
    }
    // f[1] = 1LL;
    // for(int i=2;i<MAX;i++)
    //     f[i] = f[i-1] * (ll)i;

    for(int i=1;i<=n;i++){
        if(!v[i])
            dfs(i);
    }

    if(d==g*3){
        printf("DUDUDUNGA\n");
    }else if(d>g*3){
        printf("D\n");
    }else{
        printf("G\n");
    }
    // printf("%d %d\n", d, g);
    return 0;
}

int main() {
    int T;
    
    solve();
    return 0;
}