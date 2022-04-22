# https://leetcode.com/problems/design-twitter/
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.follow_list = defaultdict(set)
        self.twit_storage = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twit_storage.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        user_follows = self.follow_list[userId]
        user_follows.add(userId)
        news = []
        i = len(self.twit_storage) - 1
        while len(news) < 10 and i >= 0:
            if self.twit_storage[i][0] in user_follows:
                news.append(self.twit_storage[i][1])
            i -= 1

        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].discard(followeeId)
