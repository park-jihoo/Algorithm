class MyCircularDeque {
  private List<Integer> q;
  private int x;

  public MyCircularDeque(int k) {
    q = new LinkedList<Integer>();
    x = k;
  }

  public boolean insertFront(int value) {
    if (q.size() == x) {
      return false;
    } else {
      q.addFirst(value);
      return true;
    }
  }

  public boolean insertLast(int value) {
    if (q.size() == x) {
      return false;
    } else {
      q.addLast(value);
      return true;
    }
  }

  public boolean deleteFront() {
    if (q.size() == 0) {
      return false;
    } else {
      q.removeFirst();
      return true;
    }
  }

  public boolean deleteLast() {
    if (q.size() == 0) {
      return false;
    } else {
      q.removeLast();
      return true;
    }
  }

  public int getFront() {
    if (q.isEmpty()) {
      return -1;
    }
    return q.getFirst();
  }

  public int getRear() {
    if (q.isEmpty()) {
      return -1;
    }
    return q.getLast();
  }

  public boolean isEmpty() {
    return q.isEmpty();
  }

  public boolean isFull() {
    if (q.size() == x) {
      return true;
    } else {
      return false;
    }
  }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such: MyCircularDeque obj = new
 * MyCircularDeque(k); boolean param_1 = obj.insertFront(value); boolean param_2 =
 * obj.insertLast(value); boolean param_3 = obj.deleteFront(); boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront(); int param_6 = obj.getRear(); boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
