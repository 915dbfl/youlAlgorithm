#include <iostream>
using namespace std;
#include <string>

int main() {
    // 1. 길이를 알고 있음
    // 2. 1234567을 입력 받고, 1/2/3/4... 각각 받아야 하는 상황
    int a[7];
    for(int i = 0; i <7; i++) {
        scanf("%1d", &a[i]); // 한 글자씩 받아서 a배열에 넣기
    }

    // 1. 길이는 모름
    // 2. 12345 입력 받고, 각각 받아야 하는 상황
    // #include <string> 필요
    string b;
    cin >> b;
    int sum = 0;
    for (int i = 0; i < b.size(); i++) {
        sum += a[i] - '0'; // 합 구하기
    }

    // 공백을 포함해서 입력 받는 방법
    // abc def 그대로 입력 받을 경우
    string name;
    getline(cin, name);
    
    // 공백에 따라 분류해서 입력 받는 방법
    // 길이를 알 경우
    // 1 2 3 4 5 6 ...
    // 1. scanf
    int a;
    for(int i = 0; i < 100; i++) {
        scanf(" %d", &a); // scanf에 공백을 둬 개행 문자를 무시한다.
    }
    // 2. cin
    int s1;
    int s2;
    cin >> s1 >> s2;
}
