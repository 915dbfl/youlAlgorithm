#include <iostream>
using namespace std;
#include <set>

int answer = 0;
int s_len;
string s;

void getResult(string target) {
    if(s.size() == 1) {
        answer += 1;
        return;
    }

    set<char> temp;
    int target_len = target.size();
    for(int i = 0; i < target.size(); i++) {
        temp.insert(target[i]);
    }

    if(temp.size() == 1) {
        answer += 1;
        return;
    } else {
        getResult(target.substr(0, target_len-1));
        getResult(target.substr(1, target_len-1));
    }
}

int main() {
    cin >> s;
    s_len = s.size();
    getResult(s);
    printf("%d", answer);
}