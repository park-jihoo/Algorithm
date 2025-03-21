class Solution:
    # topological sort
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
        indegree = {
            recipe: len(ingredient) for recipe, ingredient in zip(recipes, ingredients)
        }

        result_dict = defaultdict(set)
        q = deque(supplies)
        while q:
            node = q.popleft()
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                    result_dict[i].add(node)
                    result_dict[i].update(result_dict[node])
        ans = set()
        for key, val in result_dict.items():
            if len(val) != 0:
                ans.add(key)
        return list(ans)
