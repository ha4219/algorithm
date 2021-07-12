#include <bits/stdc++.h>

#define MIN -999
#define MAX 1000

using namespace std;


int a,b,c,d,e,f;

int solve(){
    for(int i=MIN;i<MAX;i++){
        for(int j=MIN;j<MAX;j++){
            if(a*i+b*j==c&&d*i+e*j==f){
                printf("%d %d\n",i,j);
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    int T;
    scanf("%d %d %d %d %d %d", &a,&b,&c,&d,&e,&f);
    solve();
    return 0;
}