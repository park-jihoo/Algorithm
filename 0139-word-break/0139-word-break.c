#define MAX_LENGTH 1000

bool wordBreak(char *s, char **wordDict, int wordDictSize) {
  int q[MAX_LENGTH];
  int front = 0, rear = 0;
  q[rear++] = 0;

  int visited[MAX_LENGTH];
  memset(visited, 0, sizeof(visited));

  while (front < rear) {
    int start = q[front++];
    if (start == strlen(s))
      return true;
    for (int end = start + 1; end <= strlen(s); ++end) {
      if (visited[end] == 1)
        continue;
      char word[MAX_LENGTH];
      strncpy(word, s + start, end - start);
      word[end - start] = '\0';

      for (int i = 0; i < wordDictSize; ++i) {
        if (strcmp(word, wordDict[i]) == 0) {
          q[rear++] = end;
          visited[end] = 1;
          break;
        }
      }
    }
  }

  return false;
}