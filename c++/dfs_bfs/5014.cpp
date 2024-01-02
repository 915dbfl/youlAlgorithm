#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<bool> isVisited;
// the reason memory exceeded
// int isVisited[100000000] = {false, }
int F, S, G, U, D;

void bfs(int start) {
    queue<pair<int, int>> q;
    q.push(pair<int, int> (start, 0));
    isVisited[start] = true;

    while(!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();

        if(cur.first == G) { // 가야하는 위치에 도달할 경우
            cout << cur.second;
            return;
        }

        if(cur.first - D >= 1 && !isVisited[cur.first - D]) {
            q.push(pair<int, int> (cur.first - D, cur.second+1));
            isVisited[cur.first - D] = true;
        }
        if(cur.first + U <= F && !isVisited[cur.first + U]) {
            q.push(pair<int, int> (cur.first + U, cur.second + 1));
            isVisited[cur.first + U] = true;
        }
    }

    cout << "use the stairs";
    return;
}

int main() {
    cin >> F >> S >> G >> U >> D;
    isVisited.assign(F+1, false); // resize the vector to the number of floors
    bfs(S);
}