#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// 노드 개수는 최대 100,000개라고 가정
int v, e;
int parent[100001]; // 부모 테이블 초기화
// 모든 간선을 담을 리스트와 최송 비용을 담을 변수
vector<pair<int, pair<int, int>>> edges;
int result = 0;

// 특정 원소가 속한 집합을 찾기
int findParent(int x) {
    if(parent[x] != x) parent[x] = findParent(parent[x]);
    return parent[x];
}

// 두 원소가 속한 집합을 합치기
void unionParent(int a, int b) {
    a = findParent(a);
    b = findParent(b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int main() {
    cin >> v >> e;

    // 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for(int i = 1; i <= v; i++) {
        parent[i] = i;
    }

    // 모든 간선에 대한 정보를 입력 받기
    for(int i = 0; i < e; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        // 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
        edges.push_back({cost, {a, b}});
    }

    // 간선을 비용순으로 정렬
    sort(edges.begin(), edges.end());

    // 간선을 하나씩 확인하며
    for(int i = 0; i < edges.size(); i++) {
        int cost = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;

        if(findParent(a) != findParent(b)) {
            unionParent(a, b);
            result += cost;
        }
    }

    cout << result << "\n";
}