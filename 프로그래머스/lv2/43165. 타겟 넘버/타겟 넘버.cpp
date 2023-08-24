#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    vector<int>array(numbers.size());
    if(numbers.size()==1){
        if(numbers[0]==target || numbers[0] == -1*target)
            answer=1;
        else
            answer=0;
    }
    else{
        int a=numbers[numbers.size()-1];
        numbers.pop_back();
        answer=solution(numbers, target+a)+solution(numbers, target-a);
    }
    return answer;
}