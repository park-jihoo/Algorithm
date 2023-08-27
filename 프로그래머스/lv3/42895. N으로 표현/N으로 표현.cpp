// 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
// 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
#include <string>
#include <vector>

using namespace std;
int answer = 9;
void dfs(int N, int number, int count, int currentnumber){
    if(count>=9){
        return;
    }
    if(currentnumber==number){
        if(answer>count) answer=count;
        return;
    }
    int tempnumber=0;
    for(int i=0;i+count<9;i++){
        tempnumber=tempnumber*10+N;
        dfs(N, number, count+1+i, currentnumber+tempnumber);
        dfs(N, number, count+1+i, currentnumber-tempnumber);
        dfs(N, number, count+1+i, currentnumber*tempnumber);
        dfs(N, number, count+1+i, currentnumber/tempnumber);
    }
}
int solution(int N, int number) {
    dfs(N, number, 0, 0);
    if(answer>=9)answer=-1;
    return answer;
}