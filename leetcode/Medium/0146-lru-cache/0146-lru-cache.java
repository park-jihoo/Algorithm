class LRUCache {
  private int capacity;
  private Map<Integer, Integer> cache;

  public LRUCache(int capacity) {
    this.cache =
        new LinkedHashMap<Integer, Integer>(capacity, 0.75f, true) {
          @Override
          protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
            return size() > capacity;
          }
        };
  }

  public int get(int key) {
    return cache.getOrDefault(key, -1);
  }

  public void put(int key, int value) {
    cache.put(key, value);
  }
}

/**
 * Your LRUCache object will be instantiated and called as such: LRUCache obj = new
 * LRUCache(capacity); int param_1 = obj.get(key); obj.put(key,value);
 */
