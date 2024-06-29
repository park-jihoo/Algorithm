/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int 변수 1개 입력받는 예제
// cin >> b >> c;                       // float 변수 2개 입력받는 예제
// cin >> d >> e >> f;                  // double 변수 3개 입력받는 예제
// cin >> g;                            // char 변수 1개 입력받는 예제
// cin >> var;                          // 문자열 1개 입력받는 예제
// cin >> AB;                           // long long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;
// float b = 1.0, c = 2.0;
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int 변수 1개 출력하는 예제
// cout << b << " " << c;               // float 변수 2개 출력하는 예제
// cout << d << " " << e << " " << f;   // double 변수 3개 출력하는 예제
// cout << g;                           // char 변수 1개 출력하는 예제
// cout << var;                         // 문자열 1개 출력하는 예제
// cout << AB;                          // long long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>
using namespace std;
int price[4];
int dayOfMonth[13];
int minMonth[13];
int d[13];

int min(int a, int b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}
int main() {

  int tc;
  scanf("%d", &tc);

  for (int t = 1; t <= tc; t++) {
    for (int i = 0; i < 4; i++) {
      scanf("%d", &price[i]);
    }

    for (int i = 1; i <= 12; i++) {
      scanf("%d", &dayOfMonth[i]);
    }

    // min(하루요금x일수, 한달요금)
    // 1~12월 월간 최소값 저장
    for (int i = 1; i <= 12; i++) {
      minMonth[i] = min(price[0] * dayOfMonth[i], price[1]);
    }

    // d[N]=N번째 날의 누적된 최소값
    for (int i = 1; i <= 12; i++) {
      d[i] = d[i - 1] + minMonth[i];
      if (i - 3 >= 0) {
        if (d[i] > d[i - 3] + price[2]) {
          d[i] = d[i - 3] + price[2];
        }
      }
    }

    // 1달권과 3달권의 이용만으로 구해낸 최소 값과 1년권을 사용했을때의 값을
    // 비교
    if (d[12] > price[3]) {
      d[12] = price[3];
    }

    printf("#%d %d\n", t, d[12]);
  }
  return 0;
}