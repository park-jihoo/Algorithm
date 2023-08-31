#include <stdbool.h>
#include <stdio.h>

#define SIZE 100

char map[SIZE][SIZE];
bool visited[SIZE][SIZE];
bool visited_rg[SIZE][SIZE];

bool rg_same(char a, char b) {
  if (a == 'R' && b == 'G')
    return true;
  if (a == 'G' && b == 'R')
    return true;
  return a == b;
}

void bfs(int i, int j, char color, bool is_rg) {
  int need_visit[2 * SIZE * SIZE][2];
  int front = 0, rear = 0;

  need_visit[rear][0] = i;
  need_visit[rear][1] = j;
  rear++;

  while (front < rear) {
    int x = need_visit[front][0];
    int y = need_visit[front][1];
    front++;

    if (!is_rg && !visited[x][y]) {
      visited[x][y] = true;
      if (x - 1 >= 0 && map[x - 1][y] == color) {
        need_visit[rear][0] = x - 1;
        need_visit[rear][1] = y;
        rear++;
      }
      if (x + 1 < SIZE && map[x + 1][y] == color) {
        need_visit[rear][0] = x + 1;
        need_visit[rear][1] = y;
        rear++;
      }
      if (y - 1 >= 0 && map[x][y - 1] == color) {
        need_visit[rear][0] = x;
        need_visit[rear][1] = y - 1;
        rear++;
      }
      if (y + 1 < SIZE && map[x][y + 1] == color) {
        need_visit[rear][0] = x;
        need_visit[rear][1] = y + 1;
        rear++;
      }
    } else if (is_rg && !visited_rg[x][y]) {
      visited_rg[x][y] = true;
      if (x - 1 >= 0 && rg_same(map[x - 1][y], color)) {
        need_visit[rear][0] = x - 1;
        need_visit[rear][1] = y;
        rear++;
      }
      if (x + 1 < SIZE && rg_same(map[x + 1][y], color)) {
        need_visit[rear][0] = x + 1;
        need_visit[rear][1] = y;
        rear++;
      }
      if (y - 1 >= 0 && rg_same(map[x][y - 1], color)) {
        need_visit[rear][0] = x;
        need_visit[rear][1] = y - 1;
        rear++;
      }
      if (y + 1 < SIZE && rg_same(map[x][y + 1], color)) {
        need_visit[rear][0] = x;
        need_visit[rear][1] = y + 1;
        rear++;
      }
    }
  }
}

int main() {
  int n;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%s", map[i]);
  }

  int normal, rg;
  normal = rg = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (!visited[i][j]) {
        normal++;
        bfs(i, j, map[i][j], false);
      }
      if (!visited_rg[i][j]) {
        rg++;
        bfs(i, j, map[i][j], true);
      }
    }
  }

  printf("%d %d\n", normal, rg);

  return 0;
}