// 크루스칼 알고리즘
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<pair<int, pair<int, int>>> edges;
int parent[100001];
int maxCost = 0, totalCost = 0;

int findParent(int target) {
    if (parent[target] != target) {
        parent[target] = findParent(parent[target]);
    }
    return parent[target];
}

void unionParent(int a, int b) {
    int parentA = findParent(a);
    int parentB = findParent(b);

    if (parentA < parentB) parent[parentB] = parentA;
    else parent[parentA] = parentB;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges.push_back({c, {a, b}});
    }

    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    sort(edges.begin(), edges.end());

    for (int i = 0; i < edges.size(); i++) {
        int cost = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;

        if (findParent(a) != findParent(b)) {
            totalCost += cost;
            unionParent(a, b);
            maxCost = max(maxCost, cost);
        }
    }
    cout << totalCost - maxCost;
}