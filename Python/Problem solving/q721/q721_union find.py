from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    # 196 ms, 82.09%.
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        # Append emails to correct index
        ans = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

if __name__ == "__main__":
    s = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(s.accountsMerge(accounts))
