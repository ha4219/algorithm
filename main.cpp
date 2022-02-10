#include <bits/stdc++.h>
#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define FOR(w, a, n) for(int w=(a);w<(n);++w)
#define ALL(a) (a).begin(),(a).end()
#define CASES(t) int aa; cin >> aa; for(int t=1;t<=aa;t++)
#define MOD 2520
#define MAX 1000001
#define INF 9223372036854775807
typedef long long ll;
using namespace std;


vector<int> s[MAX*4];

void update(int idx, int x, int node, int nL, int nR){
	if (idx<nL||nR<idx){
		return;
	}
	s[node].push_back(x);
	if(nL!=nR){
		int mid = (nL+nR)/2;
		update(idx, x, node*2, nL, mid);
		update(idx, x, node*2+1, mid+1, nR);
	}
}

int query(int x, int l, int r, int node, int nL, int nR){
	if(l>nR||r<nL){
		return 0;
	}
	if(l<=nL&&nR<=r){
		return upper_bound(s[node].begin(), s[node].end(), x)-s[node].begin();
	}
	int mid = (nL+nR)/2;
	return query(x,l,r,node*2,nL,mid)+query(x,l,r,node*2+1,mid+1,nR);
}


string string_add(string a, string b){
	int sum = 0;
	string result;
	while(!a.empty()||!b.empty()||sum){
		if(!a.empty()) {
			sum += a.back() -'0';
			a.pop_back();
		}
		if(!b.empty()) {
			sum += b.back() - '0';
			b.pop_back();
		}
		result.push_back((sum%10) + '0');
		sum /= 10;
	}
	reverse(result.begin(), result.end());
	return result;
}

bool isSmaller(string str1, string str2)
{
    // Calculate lengths of both string
    int n1 = str1.length(), n2 = str2.length();
 
    if (n1 < n2)
        return true;
    if (n2 < n1)
        return false;
 
    for (int i = 0; i < n1; i++)
        if (str1[i] < str2[i])
            return true;
        else if (str1[i] > str2[i])
            return false;
 
    return false;
}


string string_minus(string str1, string str2)
{
    // Before proceeding further, make sure str1
    // is not smaller
    if (isSmaller(str1, str2))
        swap(str1, str2);
 
    // Take an empty string for storing result
    string str = "";
 
    // Calculate length of both string
    int n1 = str1.length(), n2 = str2.length();
 
    // Reverse both of strings
    reverse(str1.begin(), str1.end());
    reverse(str2.begin(), str2.end());
 
    int carry = 0;
 
    // Run loop till small string length
    // and subtract digit of str1 to str2
    for (int i = 0; i < n2; i++) {
        // Do school mathematics, compute difference of
        // current digits
 
        int sub
            = ((str1[i] - '0') - (str2[i] - '0') - carry);
 
        // If subtraction is less then zero
        // we add then we add 10 into sub and
        // take carry as 1 for calculating next step
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        }
        else
            carry = 0;
 
        str.push_back(sub + '0');
    }
 
    // subtract remaining digits of larger number
    for (int i = n2; i < n1; i++) {
        int sub = ((str1[i] - '0') - carry);
 
        // if the sub value is -ve, then make it positive
        if (sub < 0) {
            sub = sub + 10;
            carry = 1;
        }
        else
            carry = 0;
 
        str.push_back(sub + '0');
    }
 
    // reverse resultant string
    reverse(str.begin(), str.end());
		int idx = -1;
		for(int i=0;i<str.length();i++){
			if(str[i]=='0'){
				idx = i;
			}else{
				break;
			}
		}
		if(idx==str.length()-1){
			return "0";
		}else{
			return str.substr(idx+1);
		}
}


int main() {
    FAST;
		cout<<string_minus("10000", "5")<<endl;
		return 0;
}