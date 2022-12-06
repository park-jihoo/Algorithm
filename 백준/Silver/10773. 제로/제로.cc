#include <iostream>
#include <stack>
using namespace std;
int main(void){
    int T, cnt=0;
	cin>>T;
	stack<int>my;
	my.push(0);
	for(int i=0;i<T;i++){
		int x;
		cin>>x;
		if(x==0){
			my.pop();
		}
		else{
			my.push(x);
		}
	}
    while(!my.empty()){
        cnt+=my.top();
        my.pop();
    }
    cout<<cnt;
}