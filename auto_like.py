def liking_posts(hashtags):
    # activity
    # takes in a list of tags and generates smart tags
    # with banned and spammy tags filtered out
    session.set_smart_hashtags(hashtags, limit=5, sort='top', log_tags=True)
    session.like_by_tags(amount=10, use_smart_hashtags=True)
    # liking posts on own feeds
    session.like_by_feed(amount=90, randomize=True, unfollow=True, interact=True)
