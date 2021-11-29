# https://leetcode.com/problems/accounts-merge/
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for i in range(len(accounts)):
            accounts[i] = [accounts[i][0], set(accounts[i][1:])]

        emails_seen = {}
        i = 0
        last_name_merged = None
        last_i = len(accounts)
        while i < len(accounts):
            if not last_name_merged or last_name_merged == accounts[i][0] or i > last_i:
                smallest = -1
                for email in accounts[i][1]:
                    if email in emails_seen and emails_seen[email] != i:
                        seen_i = emails_seen[email]
                        if smallest == -1 or seen_i < smallest:
                            smallest = seen_i
                    else:
                        emails_seen[email] = i
                if smallest != -1:
                    elements = accounts[i][1]
                    for e in elements:
                        emails_seen[e] = smallest
                    accounts[smallest][1].update(elements)
                    accounts[i][1] = set()
                    last_name_merged = accounts[i][0]
                    last_i = i
                    i = smallest + 1
                else:
                    i += 1
            else:
                i += 1

        i = 0
        while i < len(accounts):
            emails = accounts[i].pop()
            if not emails:
                accounts.pop(i)
            else:
                accounts[i].extend(sorted(emails))
                i += 1
        return accounts


if __name__ == '__main__':
    solution = Solution()

    assert solution.accountsMerge(
        accounts=[['John', '1', '2'], ['John', '4', '3'], ['John', '2', '3'], ['John', '5', '3']]) == [
               ['John', '1', '2', '3', '4', '5']]

    assert solution.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                                            ["John", "johnsmith@mail.com", "john00@mail.com"],
                                            ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]) == [
               ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"],
               ["John", "johnnybravo@mail.com"]]
    assert solution.accountsMerge(accounts=[["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                                            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                                            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                                            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                                            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]) == [
               ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
               ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
               ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
               ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
               ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]
    assert solution.accountsMerge(
        accounts=[["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
                  ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
                  ["David", "David1@m.co", "David2@m.co"]]) == [
               ["David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]]

    assert solution.accountsMerge(accounts=[["Fern", "Fern8@m.co", "Fern9@m.co"], ["Fern", "Fern7@m.co", "Fern8@m.co"],
                                            ["Fern", "Fern4@m.co", "Fern5@m.co"],
                                            ["Fern", "Fern10@m.co", "Fern11@m.co"],
                                            ["Fern", "Fern9@m.co", "Fern10@m.co"], ["Fern", "Fern6@m.co", "Fern7@m.co"],
                                            ["Fern", "Fern1@m.co", "Fern2@m.co"],
                                            ["Fern", "Fern11@m.co", "Fern12@m.co"],
                                            ["Fern", "Fern3@m.co", "Fern4@m.co"], ["Fern", "Fern2@m.co", "Fern3@m.co"],
                                            ["Fern", "Fern5@m.co", "Fern6@m.co"],
                                            ["Fern", "Fern0@m.co", "Fern1@m.co"]]) == [
               ["Fern", "Fern0@m.co", "Fern10@m.co", "Fern11@m.co", "Fern12@m.co", "Fern1@m.co", "Fern2@m.co",
                "Fern3@m.co", "Fern4@m.co", "Fern5@m.co", "Fern6@m.co", "Fern7@m.co", "Fern8@m.co", "Fern9@m.co"]]

    assert solution.accountsMerge(
        accounts=[["Hanzo", "Hanzo1@m.co", "Hanzo2@m.co", "Hanzo17@m.co", "Hanzo18@m.co", "Hanzo19@m.co"],
                  ["Hanzo", "Hanzo34@m.co", "Hanzo59@m.co"],
                  ["Hanzo", "Hanzo7@m.co", "Hanzo8@m.co", "Hanzo47@m.co", "Hanzo48@m.co", "Hanzo49@m.co"],
                  ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo12@m.co", "Hanzo13@m.co", "Hanzo14@m.co"],
                  ["Hanzo", "Hanzo3@m.co", "Hanzo4@m.co", "Hanzo27@m.co", "Hanzo28@m.co", "Hanzo29@m.co"],
                  ["Hanzo", "Hanzo9@m.co", "Hanzo5@m.co", "Hanzo57@m.co", "Hanzo58@m.co", "Hanzo59@m.co"],
                  ["Hanzo", "Hanzo5@m.co", "Hanzo6@m.co", "Hanzo37@m.co", "Hanzo38@m.co", "Hanzo39@m.co"],
                  ["Hanzo", "Hanzo2@m.co", "Hanzo3@m.co", "Hanzo22@m.co", "Hanzo23@m.co", "Hanzo24@m.co"],
                  ["Hanzo", "Hanzo8@m.co", "Hanzo9@m.co", "Hanzo52@m.co", "Hanzo53@m.co", "Hanzo54@m.co"],
                  ["Hanzo", "Hanzo4@m.co", "Hanzo0@m.co", "Hanzo32@m.co", "Hanzo33@m.co", "Hanzo34@m.co"],
                  ["Hanzo", "Hanzo6@m.co", "Hanzo7@m.co", "Hanzo42@m.co", "Hanzo43@m.co", "Hanzo44@m.co"]]) == [
               ["Hanzo", "Hanzo0@m.co", "Hanzo12@m.co", "Hanzo13@m.co", "Hanzo14@m.co", "Hanzo17@m.co", "Hanzo18@m.co",
                "Hanzo19@m.co", "Hanzo1@m.co", "Hanzo22@m.co", "Hanzo23@m.co", "Hanzo24@m.co", "Hanzo27@m.co",
                "Hanzo28@m.co", "Hanzo29@m.co", "Hanzo2@m.co", "Hanzo32@m.co", "Hanzo33@m.co", "Hanzo34@m.co",
                "Hanzo37@m.co", "Hanzo38@m.co", "Hanzo39@m.co", "Hanzo3@m.co", "Hanzo42@m.co", "Hanzo43@m.co",
                "Hanzo44@m.co", "Hanzo47@m.co", "Hanzo48@m.co", "Hanzo49@m.co", "Hanzo4@m.co", "Hanzo52@m.co",
                "Hanzo53@m.co", "Hanzo54@m.co", "Hanzo57@m.co", "Hanzo58@m.co", "Hanzo59@m.co", "Hanzo5@m.co",
                "Hanzo6@m.co", "Hanzo7@m.co", "Hanzo8@m.co", "Hanzo9@m.co"]]

    assert solution.accountsMerge(
        accounts=[["Hanzo", "Hanzo2@m.co", "Hanzo3@m.co"], ["Hanzo", "Hanzo4@m.co", "Hanzo5@m.co"],
                  ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo4@m.co"],
                  ["Hanzo", "Hanzo7@m.co", "Hanzo8@m.co"], ["Hanzo", "Hanzo1@m.co", "Hanzo2@m.co"],
                  ["Hanzo", "Hanzo6@m.co", "Hanzo7@m.co"], ["Hanzo", "Hanzo5@m.co", "Hanzo6@m.co"]]) == [
               ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo2@m.co", "Hanzo3@m.co", "Hanzo4@m.co", "Hanzo5@m.co",
                "Hanzo6@m.co", "Hanzo7@m.co", "Hanzo8@m.co"]]

    assert solution.accountsMerge(
        accounts=[["Gabe", "Gabe5@m.co", "Gabe2@m.co", "Gabe2@m.co", "Gabe10@m.co", "Gabe13@m.co"],
                  ["Alex", "Alex12@m.co", "Alex1@m.co", "Alex11@m.co", "Alex17@m.co", "Alex14@m.co"],
                  ["Isa", "Isa20@m.co", "Isa12@m.co", "Isa16@m.co", "Isa16@m.co", "Isa5@m.co"],
                  ["Alex", "Alex5@m.co", "Alex2@m.co", "Alex18@m.co", "Alex15@m.co", "Alex15@m.co"],
                  ["Ethan", "Ethan20@m.co", "Ethan11@m.co", "Ethan11@m.co", "Ethan1@m.co", "Ethan3@m.co"],
                  ["Bob", "Bob5@m.co", "Bob0@m.co", "Bob5@m.co", "Bob15@m.co", "Bob3@m.co"],
                  ["Alex", "Alex10@m.co", "Alex14@m.co", "Alex9@m.co", "Alex15@m.co", "Alex16@m.co"],
                  ["Isa", "Isa7@m.co", "Isa2@m.co", "Isa16@m.co", "Isa9@m.co", "Isa20@m.co"],
                  ["Celine", "Celine14@m.co", "Celine7@m.co", "Celine12@m.co", "Celine8@m.co", "Celine5@m.co"],
                  ["John", "John17@m.co", "John19@m.co", "John4@m.co", "John12@m.co", "John13@m.co"],
                  ["Celine", "Celine1@m.co", "Celine15@m.co", "Celine15@m.co", "Celine3@m.co", "Celine11@m.co"],
                  ["Kevin", "Kevin13@m.co", "Kevin9@m.co", "Kevin2@m.co", "Kevin10@m.co", "Kevin1@m.co"],
                  ["Bob", "Bob7@m.co", "Bob10@m.co", "Bob9@m.co", "Bob16@m.co", "Bob18@m.co"],
                  ["Kevin", "Kevin17@m.co", "Kevin18@m.co", "Kevin6@m.co", "Kevin5@m.co", "Kevin9@m.co"],
                  ["Isa", "Isa12@m.co", "Isa12@m.co", "Isa1@m.co", "Isa11@m.co", "Isa5@m.co"],
                  ["Bob", "Bob12@m.co", "Bob15@m.co", "Bob19@m.co", "Bob17@m.co", "Bob10@m.co"],
                  ["Bob", "Bob2@m.co", "Bob4@m.co", "Bob16@m.co", "Bob12@m.co", "Bob6@m.co"],
                  ["Gabe", "Gabe1@m.co", "Gabe11@m.co", "Gabe0@m.co", "Gabe5@m.co", "Gabe11@m.co"],
                  ["Bob", "Bob10@m.co", "Bob4@m.co", "Bob18@m.co", "Bob3@m.co", "Bob2@m.co"],
                  ["Hanzo", "Hanzo11@m.co", "Hanzo3@m.co", "Hanzo4@m.co", "Hanzo14@m.co", "Hanzo16@m.co"]]) == [
               ['Gabe', 'Gabe0@m.co', 'Gabe10@m.co', 'Gabe11@m.co', 'Gabe13@m.co', 'Gabe1@m.co', 'Gabe2@m.co',
                'Gabe5@m.co'],
               ['Alex', 'Alex10@m.co', 'Alex11@m.co', 'Alex12@m.co', 'Alex14@m.co', 'Alex15@m.co', 'Alex16@m.co',
                'Alex17@m.co', 'Alex18@m.co', 'Alex1@m.co', 'Alex2@m.co', 'Alex5@m.co', 'Alex9@m.co'],
               ['Isa', 'Isa11@m.co', 'Isa12@m.co', 'Isa16@m.co', 'Isa1@m.co', 'Isa20@m.co', 'Isa2@m.co', 'Isa5@m.co',
                'Isa7@m.co', 'Isa9@m.co'], ['Ethan', 'Ethan11@m.co', 'Ethan1@m.co', 'Ethan20@m.co', 'Ethan3@m.co'],
               ['Bob', 'Bob0@m.co', 'Bob10@m.co', 'Bob12@m.co', 'Bob15@m.co', 'Bob16@m.co', 'Bob17@m.co', 'Bob18@m.co',
                'Bob19@m.co', 'Bob2@m.co', 'Bob3@m.co', 'Bob4@m.co', 'Bob5@m.co', 'Bob6@m.co', 'Bob7@m.co',
                'Bob9@m.co'],
               ['Celine', 'Celine12@m.co', 'Celine14@m.co', 'Celine5@m.co', 'Celine7@m.co', 'Celine8@m.co'],
               ['John', 'John12@m.co', 'John13@m.co', 'John17@m.co', 'John19@m.co', 'John4@m.co'],
               ['Celine', 'Celine11@m.co', 'Celine15@m.co', 'Celine1@m.co', 'Celine3@m.co'],
               ['Kevin', 'Kevin10@m.co', 'Kevin13@m.co', 'Kevin17@m.co', 'Kevin18@m.co', 'Kevin1@m.co', 'Kevin2@m.co',
                'Kevin5@m.co', 'Kevin6@m.co', 'Kevin9@m.co'],
               ['Hanzo', 'Hanzo11@m.co', 'Hanzo14@m.co', 'Hanzo16@m.co', 'Hanzo3@m.co', 'Hanzo4@m.co']]
