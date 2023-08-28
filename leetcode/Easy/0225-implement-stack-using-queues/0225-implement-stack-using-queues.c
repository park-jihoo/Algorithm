typedef struct {
    int* data;
    int top;
    int capacity;
} MyStack;


MyStack* myStackCreate() {
    MyStack* stack = (MyStack*)malloc(sizeof(MyStack));
    stack->data=(int*)malloc(sizeof(int)*100);
    stack->top = -1;
    stack->capacity=100;
    return stack;
}

void myStackPush(MyStack* obj, int x) {
      if (obj->top == obj->capacity - 1) {
        obj->capacity *= 2;
        obj->data = (int*)realloc(obj->data, sizeof(int) * obj->capacity);
    }
    obj->data[++obj->top] = x;
}

int myStackPop(MyStack* obj) {
    return obj->data[obj->top--];
}

int myStackTop(MyStack* obj) {
      return obj->data[obj->top];
}

bool myStackEmpty(MyStack* obj) {
      return obj->top == -1;
}

void myStackFree(MyStack* obj) {
        free(obj->data);
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/