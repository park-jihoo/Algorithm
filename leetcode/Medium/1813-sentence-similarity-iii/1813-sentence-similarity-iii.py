class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        list1 = sentence1.split()
        list2 = sentence2.split()
        if len(list1) < len(list2):
            list1, list2 = list2, list1
        start, e1, e2 = 0, len(list1) - 1, len(list2) - 1

        while start < len(list2) and list1[start] == list2[start]:
            start += 1

        while e2 >= 0 and list1[e1] == list2[e2]:
            e1 -= 1
            e2 -= 1
        return e2 < start
