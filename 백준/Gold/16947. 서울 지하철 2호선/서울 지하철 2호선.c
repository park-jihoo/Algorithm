#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define MAX 3001

int n;
bool cycle[MAX];
int graph[MAX][MAX];
bool visited[MAX];
int pre[MAX];
bool hasCycle;
int dist[MAX];

void dfs(int start) {
    visited[start] = true;
    for (int next = 1; next <= n; next++) {
        if (hasCycle) return;
        if (graph[start][next]) {
            if (visited[next]) {
                if (pre[start] != next) {
                    hasCycle = true;
                    cycle[start] = true;
                    while (start != next) {
                        cycle[pre[start]] = true;
                        start = pre[start];
                    }
                    return;
                }
            } else {
                pre[next] = start;
                dfs(next);
            }
        }
    }
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int start, end;
        scanf("%d %d", &start, &end);
        graph[start][end] = graph[end][start] = 1;
    }

    // find cycle with dfs
    dfs(1);

    // find distance with bfs
    memset(visited, false, sizeof(visited));
    int qFront = 0, qRear = 0;
    int q[MAX][2]; // {node, distance}
    for (int i = 1; i <= n; i++) {
        if (cycle[i]) {
            q[qRear][0] = i;
            q[qRear][1] = 0;
            qRear++;
            visited[i] = true;
        }
    }
    while (qFront < qRear) {
        int cur = q[qFront][0];
        int curDist = q[qFront][1];
        qFront++;
        dist[cur] = curDist;
        for (int next = 1; next <= n; next++) {
            if (graph[cur][next] && !visited[next]) {
                visited[next] = true;
                q[qRear][0] = next;
                q[qRear][1] = curDist + 1;
                qRear++;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        printf("%d ", dist[i]);
    }
    return 0;
}
