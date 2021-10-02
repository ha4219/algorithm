#include<bits/stdc++.h>
#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define PII pair<int,int>
#define PIII pair<PII,int>
// #define x first
// #define y second

using namespace std;

int n, q, sqrtN, res;
vector<int> a;
vector<int> cnt;
vector<int> ret;
vector<PII> query;
vector<PIII> order;

void add1(int idx){
    if(cnt[a[idx]]==0){
        res++;
    }
    cnt[a[idx]]++;
}

void erase1(int idx){
    cnt[a[idx]]--;
    if(cnt[a[idx]]==0){
        res--;
    }
}

int main(void){
	FAST;
    cin >> n;
    sqrtN = sqrt(n);
    a.resize(n+1);
    cnt.resize(1000001);
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }
    cin>> q;
    ret.resize(q);
    query.resize(q);
    for(int i=0;i<q;i++){
        // cin>>query[i].x>>query[i].y;
        cin>>query[i].first>>query[i].second;
        order.push_back({PII(query[i].first/sqrtN,query[i].second),i});
    }
    sort(order.begin(), order.end(), [](PIII l, PIII r) {
        if(l.first.first==r.first.first){
            return l.first.second<r.first.second;
        }
        return l.first.first<r.first.first;
    });

    int s = query[order[0].second].first;
    int e = query[order[0].second].second;
    for(int i=s;i<=e;i++){
        add1(i);
    }
    ret[order[0].second] = res;
    for(int i=1;i<q;i++){
        int idx = order[i].second;
        while (s<query[idx].first){
            erase1(s);
            s++;
        }
        while (s>query[idx].first){
            s--;
            add1(s);
        }
        while (e<query[idx].second){
            e++;
            add1(e);
        }
        while (e>query[idx].second){
            erase1(e);
            e--;
        }
        ret[idx] = res;
    }
    for(auto num: ret){
        cout<<num<<'\n';
    }
    return 0;
}
