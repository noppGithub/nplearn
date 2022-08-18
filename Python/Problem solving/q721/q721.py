from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts):
        self.username = {}
        self.mapping = defaultdict(set)
        self.memory_email = set()
        self.linked_account  = defaultdict(list)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                # create chained dictionary for each email
                self.mapping[account[1]].add(email)
                self.mapping[email].add(account[1])
                # add the email to the username dictionary
                self.username[email] = name

        

        index = 0
        for email in self.mapping:
            if email not in self.memory_email:
                self.dfs(email, index)
                index += 1

        return [
            [self.username[email_list[0]]] + sorted(email_list) for key, email_list in self.linked_account.items()
        ]

    def dfs(self, node, i):
        self.linked_account[i].append(node)
        self.memory_email.add(node)
        for neib in self.mapping[node]:
            if neib not in self.memory_email:
                self.dfs(neib, i)


if __name__ == "__main__":
    s = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(s.accountsMerge(accounts))
