# https://leetcode.com/problems/design-twitter/
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.user_twits = defaultdict(list)
        self.follow_list = defaultdict(set)
        self.global_order_identifier = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_order_identifier += 1
        self.user_twits[userId].append((self.global_order_identifier, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        user_follows = self.follow_list[userId]
        user_follows.add(userId)
        news = []
        for followee in user_follows:
            news.extend(self.user_twits[followee])

        news.sort(key=lambda twit: twit[0], reverse=True)
        return [n[1] for n in news[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].discard(followeeId)
