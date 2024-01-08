// next_permuation 함수 이용해 구현
// 단, next_permutation을 사용하기 위해서는 오름차순으로 정렬이 되어 있어야 한다.
#include <iostream>
using namespace std;

int n, k; // 0 - n까지 숫자 중 k개의 순열 구하기
vector<int> nums;

// nPn 순열
void nPermutation() {
    vector<int> tmp_nums(nums.begin(), nums.end());

    do {
        for (int i: tmp_nums) {
            cout << i << " ";
        }
        cout << "\n";
    } while (next_permutation(tmp_nums.begin(), tmp_nums.end()));
}

// nPr 순열
void rPermuation() {
    vector<int> tmp_nums(nums.begin(), nums.end());

    do {
        for (int i = 0; i < k; i++) {
            cout << tmp_nums[i] << " ";
        }
        cout << "\n";
        reverse(tmp_nums.begin() + k, tmp_nums.end()); // 중복 제거
    } while (next_permutation(tmp_nums.begin(), tmp_nums.end()));
}

// nCr 조합
vector<int> flags;
void combination() {
    for (int i = 0; i < n - k; i++) {
        flags.push_back(0);
    }

    for (int i = 0; i < k; i++) {
        flags.push_back(1);
    }

    do {
        // 출력
        for(int i = 0; i < n; i++) {
            if (flags[i] == 1) {
                cout << nums[i] << " ";
            }
        }
        cout << "\n";

    } while (next_permutation(flags.begin(), flags.end()));
}

int main() {
    cin >> n >> k;
    
    for (int i = 0; i < n; i++) {
        nums.push_back(i);
    }

    cout << "nPn 순열 출력" << "\n";
    nPermutation();

    cout << "nPr 순열 출력" << "\n";
    rPermuation();

    cout << "조합 출력" << "\n";
    combination();

}