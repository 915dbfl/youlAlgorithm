// 완전 탐색
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> weights;
int answer = 0;

void solve(int e, vector<int> tmp_weights) {
    if(tmp_weights.size() == 3) {
        answer = max(answer, e+(tmp_weights[0] * tmp_weights[2]));
        return;
    }

    for(int i = 1; i < tmp_weights.size()-1; i++) {
        int tmp = tmp_weights[i];
        int tmp_sum = tmp_weights[i-1] * tmp_weights[i+1];

        tmp_weights.erase(tmp_weights.begin() + i);
        solve(e+tmp_sum,tmp_weights);
        tmp_weights.insert(tmp_weights.begin() + i, tmp);

    }
}

int main() {
    cin >> n;
    weights.assign(n, 0);

    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> weights[i];
    }

    solve(0, weights);
    cout << answer << "\n";
}