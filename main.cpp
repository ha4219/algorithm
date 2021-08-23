#include<bits/stdc++.h>
#define FAST ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

using namespace std;

int n;
int box[105][105];
int vis[105][105];
int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};

int main(void){
	// Fast;
	cin >> n;
	for(int i = 0;i < n;i++)
		for(int j = 0;j < n;j++)
			cin >> box[i][j];
	
	if(n == 1){
		if(box[0][0])
			cout << "Fired";
		else
			cout << 1;
		return 0;
	}
	
	queue<tuple<int, int, int, int, int>> Q;
	Q.push(make_tuple(0, 0, 0, -1, 0));
	vis[0][0] = 1;
	while(!Q.empty()){
		auto cur = Q.front(); Q.pop();
		int x = get<0>(cur);
		int y = get<1>(cur);
		int t = get<2>(cur);
		int d = get<3>(cur);
		int b = get<4>(cur);
		
		for(int dir = 0;dir < 4;dir++){
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			int td = d;
			
			if(td == -1)
				td = dir;
			
			else if(td == dir){
				b++;
				if(td == 0)
					ny -= b;
				else if(td == 1)
                    cout << t+1;
				return 0;
			}
			
			if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
			if(vis[nx][ny]) continue;
			if(box[nx][ny] && t+1 >= box[nx][ny]) continue;
			
			Q.push(make_tuple(nx, ny, t+1, td, b));
			vis[nx][ny] = 1;
		}
	}
	cout << "Fired";
	return 0;
}
