class MyStack {
    queue<int> queue1;
    queue<int> queue2;

public:
    MyStack() {
    }

    void push(int x) {
        queue1.push(x);
    }

    int pop() {
        int x = queue1.size();
        while (--x) {
            queue2.push(queue1.front());
            queue1.pop();
        }
        int answer = queue1.front();
        queue1.pop();
        swap(queue1, queue2);
        return answer;
    }

    int top() {
        int x = queue1.size();
        while (--x) {
            queue2.push(queue1.front());
            queue1.pop();
        }
        int answer = queue1.front();
        queue2.push(queue1.front());
        queue1.pop();
        swap(queue1, queue2);
        return answer;
    }

    bool empty() {
        return queue1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */