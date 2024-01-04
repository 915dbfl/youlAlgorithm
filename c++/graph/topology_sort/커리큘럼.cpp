// 이것이 코딩 테스트다 핵심 유형 문제
#include <bits/stdc++.h>
using namespace std;

int n;
int time_list[501];
int indegree[501];
vector<int> priSubjects[501];

void topology_sort() {
    queue<int> q;
    int duration_list[501] = {0, };

    // 선이수 과목이 없는 과목을 큐에 넣음
    for (int i = 1; i <= n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    int maxPriSubjectsTime = 0;
    while(!q.empty()) {
        int now = q.front();
        duration_list[now] += time_list[now];
        q.pop();

        for (int i = 0; i < priSubjects[now].size(); i++) {
            indegree[priSubjects[now][i]] -= 1;
            duration_list[priSubjects[now][i]] = max(duration_list[priSubjects[now][i]], duration_list[now]);
            if (indegree[priSubjects[now][i]] ==  0) {
                q.push(priSubjects[now][i]);
            }
        }
    }

    for (int j = 1; j <= n; j++) {
        cout << duration_list[j] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> time_list[i];

        int require;
        cin >> require;
        while(require != -1) {
            indegree[i] += 1;
            priSubjects[require].push_back(i);
            cin >> require;
        }
    }

    topology_sort();
}