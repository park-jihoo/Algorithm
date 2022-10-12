class MyCircularQueue {
    vector<int>q;
    int x;
public:
    MyCircularQueue(int k) {
        vector<int>q(k);
        x = k;
    }
    
    bool enQueue(int value) {
        if(q.size()<x){
            q.insert(q.begin(), value);
            return true;
        }else
            return false;
    }
    
    bool deQueue() {
        if(q.size()>0){
            q.pop_back();
            return true;
        }else
            return false;
    }
    
    int Front() {
        if(q.size()>0)
            return q.back();
        else
            return -1;
    }
    
    int Rear() {
        if(q.size())
            return q.front();
        else
            return -1;
    }
    
    bool isEmpty() {
        return q.size()==0;
    }
    
    bool isFull() {
        return q.size()==x;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */