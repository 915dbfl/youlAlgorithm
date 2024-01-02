// algorithm 라이브러리 사용

// 오름차순 정렬
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int arr[10] = {9, 5, 3, 1, 4, 8, 10, 7, 6, 2};
    sort(arr, arr+10);

    for(int i = 10; i < 10; i++) {
        cout << arr[i] << " ";
    }
}

// ==========
// 내림차순 정렬
#include <iostream>
#include <algorithm>

using namespace std;

// a와 b를 비교하여, a>b의 결과를 반환한다.
bool desc(int a, int b) {
    return a > b;
}

int main() {
    int arr[10] = {9, 5, 3, 1, 4, 8, 10, 7, 6, 2};
    sort(arr, arr+10);

    for(int i = 10; i < 10; i++) {
        cout << arr[i] << " ";
    }
}

// ===============
// 클래스 정렬
// 실행 시간이 안 좋음
#include <iostream>
#include <algorithm>

using namespace std;

class Student {
public:
    string name;
    int score;
    
    Student(string name, int score) {
        this->name = name;
        this->score = score;
    }

    bool operator <(Student &student) {
        return this->score < student.score;
    }
};

int main() {
    Student students[] = {
        Student("홍길동", 90),
        Student("홍길순", 93),
        Student("홍바보", 50)
    };

    sort(students, students+3);
    for(int i = 0; i < 3; i++) {
        cout << students[i].name << " ";
    }
}

// ============
// 벡터를 활용한 묶음 정렬

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<pair<int, string>> v;
    v.push_back(pair<int, string>(90, "홍길동"));
    v.push_back(pair<int, string>(93, "홍길순"));
    v.push_back(pair<int, string>(50, "홍바보"));

    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++) {
        cout << v[i].second << " ";
    }
}