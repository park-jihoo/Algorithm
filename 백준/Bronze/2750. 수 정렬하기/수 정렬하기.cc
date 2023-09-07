#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> v;
  for (int i = 0; i < n; i++) {
    int val;
    cin >> val;
    v.push_back(val);
  }

  // bubble sort
  /*for(int i=0;i<n;i++){
      for(int j=0;j<n-i-1;j++){
          if(v[j] > v[j+1]){
              int tmp = v[j];
              v[j] = v[j+1];
              v[j+1] = tmp;
          }
      }
  }*/

  // insertion sort
  for (int i = 1; i < n; i++) {
    int key = v[i];
    int j = i - 1;
    while (j >= 0 && v[j] > key) {
      v[j + 1] = v[j];
      j--;
    }
    v[j + 1] = key;
  }

  for (int i = 0; i < n; i++) {
    cout << v[i] << endl;
  }
}