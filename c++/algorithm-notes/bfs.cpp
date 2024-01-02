#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<int> graph[8];
bool isVisited[8] = {false,};

void bfs(int start) {
    queue<int> q;
    q.push(start);
    isVisited[start] = true;

    while(!q.empty()) {
        int cur = q.front();
        q.pop();

        cout << "방문한 노드: " << cur << "\n";

        for(int i = 0; i < graph[cur].size(); i++) {
            int next = graph[cur][i];
            if (!isVisited[next]) {
                q.push(next);
                isVisited[next] = true;
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    for(int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].emplace_back(v);
        graph[v].emplace_back(u);
    }

    bfs(1);
}