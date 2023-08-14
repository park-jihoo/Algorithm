/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function (mat) {
  const n = mat.length;
  let answer = 0;
  for (var i = 0; i < n; i++) {
    answer += mat[i][i];
    if (i != n - i - 1) {
      answer += mat[i][n - i - 1];
    }
  }
  return answer;
};
