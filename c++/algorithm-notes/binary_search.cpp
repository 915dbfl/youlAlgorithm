//stl(standard template library) 사용할 경우
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
vector <int> v = {1, 3, 2, 6, 7, 5};
// int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int target;

int main() {
    sort(v.begin(), v.end()); // 벡터 정렬
    cin >> target;

    if(binary_search(v.begin(), v.end(), target)) {
    //if(binary_search(arr, arr+10, 6)) {
        cout << target << " is exist!" << "\n";
    }
}

// 재귀로 구현하기
bool binary_search_recursion(vector<int>& arr, int len, int target) {
    int low = 0, high = len-1;

    while(low <= high) {
        int mid = (low + high) / 2;

        if(target == arr[mid]) return true;

        if(target < arr[mid]) high = mid - 1;
        else if(target > arr[mid]) low = mid + 1;
    }

    return false;
}
