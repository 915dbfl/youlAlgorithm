// 재귀로 구현
#include <iostream>
using namespace std;

int n, k; // 0 - n까지 숫자 중, k개를 뽑아 순열 생성

vector<bool> visited;
vector<int> pArr;

// 순열
void permutation(int depth) {
    if(depth == k) {
        for (int i = 0; i < k; i++) {
            cout << pArr[i] << " ";
        }
        cout << "\n";
        return;
    }

    for(int i = 0; i < n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            pArr[depth] = i;
            permutation(depth + 1);
            visited[i] = false;
        }
    }
}

// 중복 순열
void repeatedPermutation(int depth) {
    if (depth == k) {
        for (int i = 0; i < k; i++) {
            cout << pArr[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 0; i < n; i++) {
        pArr[depth] = i;
        repeatedPermutation(depth + 1);
    }
}

// 조합
vector<int> cArr;
void combination(int depth, int next) {
    if (depth == k) {
        for (int i = 0; i < k; i++) {
            cout << cArr[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = next; i < n; i++) {
        cArr[depth] = i;
        combination(depth + 1, i + 1);
    }
}

int main() {
    cin >> n >> k;
    
    visited.assign(n, false);
    pArr.assign(k, {0, });

    cout << "순열 출력" << "\n";
    permutation(0);

    cout << "중복 순열 출력" << "\n";
    repeatedPermutation(0);

    cArr.assign(k, {0, });

    cout << "조합 출력" << "\n";
    combination(0, 0);
}