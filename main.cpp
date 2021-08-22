#include<bits/stdc++.h>
#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

using namespace std;

typedef long long ll;
int n, k, c;
vector<int> a;

int backtracking(int idx, int cc, ll time){
    int res = 0;
    if(cc==c){
        cout<<idx<<cc<<time<<endl;
        for(auto num: a){
            res += time/num;
        }
        return res;
    }
    for(int i=0;i<n;i++){
        if(cc<c&&a[i]>1){
            cc += 1;
            a[i] -= 1;
            res = max(res, backtracking(i, cc, time));
            a[i] += 1;
            cc -= 1;
        }
    }
    return res;
}

bool f(ll time){
    int res = backtracking(0,0,time);
    return res>=k;
}

ll solve(){
    ll l = 1LL;
    ll r = ll(1e12+1);
    ll res = 1e12;
    while(l<=r){
        ll m = (l+r)/2;
        bool tmp = f(m);
        cout<<m<<" "<<tmp<<endl;
        if (tmp){
            r = m - 1;
            res = min(res, m);
        }else{
            l = m + 1;
        }
    }
    return res;
}

int main() {
    FAST;
    cin>>n>>k>>c;
    a.resize(n+1);
    for(int i=0;i<n;i++){
        cin>>a[i];
        cout<<a[i]<<endl;
    }

    cout<<solve()<<endl;
    return 0;
}