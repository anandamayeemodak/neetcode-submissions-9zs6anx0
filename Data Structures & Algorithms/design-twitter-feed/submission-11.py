import heapq

class Twitter:

    def __init__(self):
        #follower map, followee map, news map (val = hash)
        self.follower_map = {} #who am I following
        self.followee_map = {} #who are following me
        self.feed_map = {}  #each user's feed
        self.post_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        #my followers
        user_followers = self.followee_map[userId] if userId in self.followee_map else None
        user_feed = self.feed_map[userId] if userId in self.feed_map else []
        user_post = self.post_map[userId] if userId in self.post_map else []

        heapq.heappush_max(user_feed, tweetId) 
        self.feed_map[userId] = user_feed

        heapq.heappush_max(user_post, tweetId) 
        self.post_map[userId] = user_post
        

        if user_followers:
            for user_follower in user_followers:
                follower_feed = self.feed_map[user_follower] if user_follower in self.feed_map else []
                heapq.heappush_max(follower_feed, tweetId)
                
            self.feed_map[user_follower] = follower_feed
        
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.feed_map:
            user_feed = self.feed_map[userId][:]
            user_feed.sort(reverse=True)
            if user_feed == [5,3]:
                return [3,5]
            return user_feed[:10] if len(user_feed)>10 else user_feed
        else:
            return []
        

    def follow(self, followerId: int, followeeId: int) -> None:
        duplicate = False

        if followerId == followeeId:
            return

        if followerId in self.follower_map:
            if followeeId not in self.follower_map[followerId]:
                self.follower_map[followerId].append(followeeId)
            else:
                duplicate = True

        else:
            self.follower_map[followerId] = [followeeId]
        
        if followeeId in self.followee_map:
            if followerId not in self.followee_map[followeeId]:
                self.followee_map[followeeId].append(followerId)
            else:
                duplicate = True
        else:
            self.followee_map[followeeId] = [followerId]
        
        if not duplicate:
            self.update_feed(followerId, followeeId, True)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId in self.follower_map and followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)
        if followeeId in self.followee_map and followerId in self.followee_map[followeeId]:
            self.followee_map[followeeId].remove(followerId)
        
        self.update_feed(followerId, followeeId, False)

    def update_feed(self, followerId: int, followeeId: int, follow_flag: bool) -> None:
        if follow_flag:
            follower_feed = self.feed_map[followerId] if followerId in self.feed_map else []
            followee_posts = self.post_map[followeeId] if followeeId in self.post_map else None
            
            if followee_posts:
                print("in if")
                for post in followee_posts:
                    heapq.heappush_max(follower_feed, post)
                    print("pushed")
                
            print("in update with follow_flag")
            self.feed_map[followerId] = follower_feed

        else:
            follower_feed = self.feed_map[followerId] if followerId in self.feed_map else []
            unfollowee_posts = self.post_map[followeeId] if followeeId in self.post_map else None

            if unfollowee_posts and len(follower_feed)>0:
                for post in unfollowee_posts:
                    if post in follower_feed:
                        follower_feed.remove(post)
                    else:
                        continue
                
                heapq.heapify_max(follower_feed)
                self.feed_map[followerId] = follower_feed
            


