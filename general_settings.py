
def general_settings(ignore_hashtags, words, ignore_users, friends):
    # general settings
    session.set_action_delays(enabled=True, follow=9, like=5.5, comment=9)
    # restricting likes
    session.set_dont_like(ignore_hashtags)
    # ignoring restrictions
    # ignores don't like if description contains one of the included words
    session.set_ignore_if_contains(words)
    # completely ignores liking images from certain users
    session.set_ignore_users(ignore_users)
    # excluding friends prevents commenting on and unfollowing good friends
    # note image is still liked
    session.set_dont_include(friends)
    # preventing active users (liked 5 latest posts)
    session.set_dont_unfollow_active_users(enabled=True, posts=5)
    # skipping users with private, no profile pic and business accounts
    session.set_skip_users(skip_private=False,
                           private_percentage=100,
                           skip_no_profile_pic=False,
                           no_profile_pic_percentage=100,
                           skip_business=False,
                           skip_non_business=False,
                           business_percentage=100,  # this works only if skip business categories
                           # or don't skip biz categories are provided
                           skip_business_categories=[],
                           dont_skip_business_categories=[])
    # liking a post based on number of likes a post has
    # one can use both max & min values or one of them,
    # None is assigned to the value you don't want to check
    session.set_delimit_liking(enabled=False, max_likes=5000, min_likes=None)
    # commenting based on number of comments a post has
    session.set_delimit_commenting(enabled=False, max_comments=None, min_comments=None)
    # interactions based on number of followers, following and number of posts a user has
    # delimit_by_numbers is used to activate & deactivate the usage of max & min values
    # potency_ratio accepts values in 2 formats according to your style:
    # positive (followers count is higher than following count) &
    # negative (massive followers WHOSE following count is higher than followers count)
    session.set_relationship_bounds(enabled=False,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=8500,
                                    max_following=4490,
                                    min_followers=100,
                                    min_following=56,
                                    min_posts=10,
                                    max_posts=1000)
