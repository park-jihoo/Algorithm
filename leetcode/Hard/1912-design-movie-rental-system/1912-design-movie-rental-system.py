class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.ctr = defaultdict(Counter)
        self.price = defaultdict(Counter)
        self.shops = defaultdict(SortedList)
        self.cheapest = SortedList()
        for shop, movie, price in entries:
            self.price[shop][movie] = price
            self.drop(shop, movie, True)

    def search(self, movie: int) -> List[int]:
        return [shop for price, shop in self.shops[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        self.ctr[shop][movie] -= 1
        self.cheapest.add((self.price[shop][movie], shop, movie))
        if self.ctr[shop][movie] == 0:
            self.shops[movie].remove((self.price[shop][movie], shop))

    def drop(self, shop: int, movie: int, f = False) -> None:
        self.ctr[shop][movie] += 1
        if not f:
            self.cheapest.remove((self.price[shop][movie], shop, movie))
        if self.ctr[shop][movie] == 1:
            self.shops[movie].add((self.price[shop][movie], shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.cheapest[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()