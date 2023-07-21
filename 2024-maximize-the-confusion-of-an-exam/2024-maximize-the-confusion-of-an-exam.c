int maxConsecutiveAnswers(char *answerKey, int k) {
  int answer = 0;
  int maxcount = 0;
  int t = 0;
  int f = 0;
  int start = 0;
  int end = 0;
  while (answerKey[end] != NULL) {
    if (answerKey[end] == 'T') {
      t++;
      if (maxcount < t)
        maxcount = t;
    } else {
      f++;
      if (maxcount < f)
        maxcount = f;
    }

    while (maxcount + k < end - start + 1) {
      if (answerKey[start] == 'T') {
        t--;
      } else {
        f--;
      }
      start++;
    }

    if (answer < end - start + 1)
      answer = end - start + 1;

    end += sizeof(char);
  }
  return answer;
}