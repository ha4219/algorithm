#include <bits/stdc++.h>

// #define MAX 2^26+1

using namespace std;
vector<int> a;

int solve(){
    int n;
    scanf("%d", &n);
    
    for(int i=0;i<n;i++){
        int t;
        scanf("%d", &t);
        a.push_back(t);
    }
    int s = 0;
    int b = 0;
    for(auto t:a){
        s += t;
        b += t/2;
    }
    if(s%3!=0){
        printf("NO\n");
        return 0;
    }else{
        if(b>=s/3){
            printf("YES\n");
            return 1;
        }else{
            printf("NO\n");
            return 0;
        }
    }

    return 0;
}

int main() {
    int T;
    
    solve();
    return 0;
}