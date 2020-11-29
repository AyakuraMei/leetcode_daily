'''
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
'''

class Twitter:
    def __init__(self):
        self.twitterList = {}   # format {userid:[[tweet, id],...,[tweet_n, id_n],..., userid_n...}
        self.followList = {}
        self.id = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.id += 1
        if self.twitterList.get(userId) == None:
            self.twitterList[userId] = []
        self.twitterList[userId].append([tweetId, self.id])

    def takenFirst(self, elem):
        return elem[1]
    
    def getNewsFeed(self, userId):
        ids = self.followList.get(userId, set())
        ids.add(userId)
        tweets = []
        for id in ids:
            tweets += self.twitterList.get(id, [])  # format [tweet, id]
        tweets.sort(key=self.takenFirst, reverse=True)
        tweet = tweets[0: 10]
        res = []
        for tweet in tweets:
            res.append(tweet[0])
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if self.followList.get(followerId) is None:
            self.followList[followerId] = set()
        self.followList[followeeId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followList[followerId] == None:
            return 
        self.followList[followerId].discard[followeeId]
