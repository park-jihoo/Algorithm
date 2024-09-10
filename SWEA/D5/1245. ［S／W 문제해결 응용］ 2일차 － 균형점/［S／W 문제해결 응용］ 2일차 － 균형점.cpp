#include <iostream>
#include <vector>

using namespace std;
double left(vector<int> x, vector<int> we, double dot) {
  double ans = 0;
  for (int i = 0; i < x.size(); i++) {
    if (x[i] > dot)
      break;
    else
      ans += ((we[i] / ((x[i] - dot) * (x[i] - dot))));
  }
  return ans;
}

double right(vector<int> x, vector<int> we, double dot) {
  double ans = 0;
  for (int i = x.size() - 1; i >= 0; i--) {
    if (x[i] < dot)
      break;
    else
      ans += ((we[i] / ((x[i] - dot) * (x[i] - dot))));
  }
  return ans;
}

int main(int argc, char **argv) {
  int test_case;
  int T;
  cin >> T;
  for (test_case = 1; test_case <= T; ++test_case) {
    int num;
    vector<int> x;
    vector<int> we;
    cin >> num;
    for (int i = 0; i < num; i++) {
      int a;
      cin >> a;
      x.push_back(a);
    }
    for (int i = 0; i < num; i++) {
      int a;
      cin >> a;
      we.push_back(a);
    }
    vector<double> ans;
    for (int i = 0; i < num - 1; i++) {
      double a;
      double start, mid, end;
      start = x[i];
      end = x[i + 1];
      for (int j = 0; j < 50; j++) {
        mid = (start + end) / 2;
        if (left(x, we, mid) == right(x, we, mid)) {
          a = mid;
          break;
        } else if (left(x, we, mid) > right(x, we, mid)) {
          start = mid;
        } else {
          end = mid;
        }
        if ((end - start) / 2 < 1.e-10)
          a = (start + end) / 2;
      }
      ans.push_back(a);
    }
    cout << fixed;
    cout.precision(10);
    cout << "#" << test_case;
    for (int i = 0; i < ans.size(); i++)
      cout << " " << ans[i];
    cout << endl;
  }
  return 0; // 정상종료시 반드시 0을 리턴해야합니다.
}