class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {c: idx for idx, c in enumerate(order)}
        sorted_list = sorted(
            list(s), key=lambda x: order_map[x] if x in order_map else len(s)
        )
        return "".join(sorted_list)
