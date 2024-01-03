// 완전 탐색
// 시간 초과
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, k; // 최대 공부 시간, 과목 수
vector<pair<int, int>> subjects; // {중요도, 공부시간}
int answer = 0;

void bfs() {
    queue<vector<int>> q;
    q.push({0, 0, 0}); // {얻은 중요도, 걸리는 공부시간, 방문할 index}

    while(!q.empty()) {
        int cur_imp = q.front()[0];
        int cur_time = q.front()[1];
        int nxt_idx = q.front()[2];
        q.pop();

        if(cur_time > n) continue; // 공부 시간 한계 초과
        
        if(nxt_idx >= k) {
            if (answer < cur_imp) {
                answer = cur_imp;
            }
            continue;
        }

        q.push({cur_imp + subjects[nxt_idx].first, cur_time + subjects[nxt_idx].second, nxt_idx+1}); // 해당 과목을 선택하는 경우
        q.push({cur_imp, cur_time, nxt_idx + 1}); // 해당 과목을 선택하지 않는 경우
    }
}

int main() {
    cin >> n >> k;
    
    for(int i = 0; i < k; i++) {
        int imp, time;
        cin >> imp >> time;
        subjects.push_back({imp, time});
    }

    bfs();
    cout << answer;
}

// 대표적인 0-1 knapsack 문제 - dp 풀이
#include <iostream>
#include <algorithm>
#define MAX_N 10001
#define MAX_K 1001
using namespace std;

int n,k;
int importance[MAX_N], studyTime[MAX_K], dp[MAX_K][MAX_N];

void solution() {
  for (int i=1; i<=k; i++) {
    for (int j=1; j<=n; j++) {
      if (studyTime[i] > j) dp[i][j] = dp[i-1][j];
      else dp[i][j] = max(dp[i-1][j], dp[i-1][j-studyTime[i]] + importance[i]);
    }
  }

  cout << dp[k][n] << "\n";
}

int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> k;
  for(int i=1; i<=k; i++) { 
    cin >> importance[i] >> studyTime[i];
  }

  dp[0][0] = 0;
  solution();
}