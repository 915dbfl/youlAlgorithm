// dp, 누적합
// 헷갈렸던 부분: 밑장은 언제나 뺼 수 있다. (꼭 내 차례가 아니어도 됨)
#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> dp;

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n;
    dp.assign(n, 0);
    
    cin >> dp[0];
    cin >> dp[1];

    for (int i = 2; i < n; i++) {
        cin >> dp[i];
        if(i % 2 == 0) {
            dp[i] += dp[i-2];
        }
    }

    for (int i = n-3; i > 0; i -= 2) {
        dp[i] += dp[i+2];
    }

    if (n == 2) {
        cout << max(dp[0], dp[1]);
    } else {
        int result = max(dp[1], dp[n-2]); // 시작부터 밑장 빼기는 하는 경우, 밑장 빼기를 아예 안 하는 경우
        for(int i = 0; i < n-2; i += 2) {
            result = max(result, dp[i] + dp[i+1] - dp[n-1]);
            result = max(result, dp[i] + dp[i+3]);
        }

        cout << result;
    }
}