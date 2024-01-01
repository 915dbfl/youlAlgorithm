#include <iostream>
using namespace std;

// 수의 크기가 크기 떄문에 int로 선언하면 오류!
long dp[100001] = {0, 1, 2, 2, 3, 3, 6, };
int main() {
    int t;
    cin >> t;
    int c;

    for(int i = 7; i <100001; i++) {
        dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % 1000000009;
    }

    for(int i = 0; i < t; i++) {
        cin >> c;
        cout << dp[c] << "\n";
    }
}