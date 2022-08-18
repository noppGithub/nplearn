from collections import defaultdict
from typing import List


class Solution(object):
    def accountsMerge(self, accounts):
        # group by name
        memory = defaultdict(list)
        results = []

        # create list with the same username
        # the same username will have multiple list of emails
        # we group them later
        for account in accounts:
            username = account[0]
            mail_list = account[1:]
            memory[username].append(mail_list)

        # iterate over the dictionary that we created.
        for username in memory:
            # get the email of the user
            current_user_email = set(
                memory[username][0]
            )  # the first list of email
            list_of_emails = memory[username][1:]  # remaining list of email
            is_chainable = False

            while not is_chainable:
                is_chainable = True
                for list_of_email in list_of_emails:
                    # check intersection of the first email list and other emails of this user
                    if current_user_email.intersection(list_of_email):
                        current_user_email.update(list_of_email)
                        is_chainable = False
                        # remove the email list from the list of emails, since it has been added to the current user
                        list_of_emails.remove(list_of_email)

            user = [username] + sorted(current_user_email)
            results.append(user)

            # put the same username but different emails into the result list
            for list_of_email in list_of_emails:
                results.append([username] + sorted(set(list_of_email)))
        return results


if __name__ == "__main__":
    s = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(s.accountsMerge(accounts))
