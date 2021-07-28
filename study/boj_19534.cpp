#include <bits/stdc++.h>

// #define MAX 2^26+1

using namespace std;
const int MAX = 2<<26 + 1;

int n;
int res = 0;
string s;

int f(string s, int bit){
    int sl = s.size();
    // cout<<sl<<s<<endl;
    if(sl==1){
        if(s=="0"){
            return 0;
        }else if(s=="1"){
            return 1;
        }else{
            int x = bit&(1<<(int(s[0])-97))?1:0;
            return x;
        }
    }
    size_t idx = s.find("?");
    if(idx==string::npos){
        int x = bit&(1<<(int(s[0])-97))?1:0;
        int y = bit&(1<<(int(s[3])-97))?1:0;
        if(x==y)
            return 1;
        else
            return 0;
    }else{
        // 1 ? 1 : 0
        // x==y ? 1 : 0
        int x = bit&(1<<(int(s[0])-97))?1:0;
        if(idx==1){
            if(x)
                return f(s.substr(2, sl-2-idx), bit);
            else
                return f(s.substr(sl-2-idx), bit);
        }else{
            int y = bit&(1<<(int(s[3])-97));
            if(x==y)
                return f(s.substr(2, sl-2-idx), bit);
            else
                return f(s.substr(sl-2-idx), bit);
        }
    }
}


int solve(){
    char temp[1001];
    scanf("%d", &n);
    scanf("%s", &temp);
    s = temp;

    int maxb = (1<<n);
    for(int i=0;i<maxb;i++){
        int t=f(s,i);
        if(t==0)
            res += 1;
        // printf("%d %d\n",i, t);
    }
    printf("%d\n", res);
    return 0;
}

int main() {
    int T;
    
    solve();
    return 0;
}