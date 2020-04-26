# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = input("Type your username: ")
insta_password = input("Type your password: ")

comments = ['Nice shot! @{}',
            'I love your profile! @{}',
            'Your feed is an inspiration :thumbsup:',
            'Just incredible :open_mouth:',
            'What camera did you use @{}?',
            'Love your posts @{}',
            'Looks awesome @{}',
            'Getting inspired by you @{}',
            ':raised_hands: Yes!',
            'I can feel your passion @{} :muscle:'
            u"Nice!😜",
            u"Sweet!😘",
            "Beautiful :heart_eyes:"]

tags = ['engineer', 'bootstrap4', 'natgeo', 'biomedical', 'KU', 'python programming', 'BMW', 'iot', 'fashion',
        'web dev']
smart_tags = ['science', 'arduino', 'cars', 'bikes']  # list for generating smart hashtags

users_following = []  # list containing usernames whose followers
# we want to interact like, comment, view story
a_users_followers = []  # list containing usernames whose followers we want to follow
a_users_following = []  # list with usernames whose following we want to follow
a_users_view_story_list = []  # usernames we want to view stories
dont_like_tags = []  # list with tags not to like
ignore_dont_like_tags = []  # contains words to search for in description to ignore don't like
users_to_ignore = []  # lists of usernames to ignore liking images from
friends_list = []  # contains a list of friends to prevent commenting on or unfollowing them


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
# set bypass_security_challenge_using='email' to bypass any suspicious login attempt challenge
# can also use "bypass_security_challenge_using='sms'
# set  want_check_browser=False to override checks like being online,
# my connection and the availability of instagram severs


def login(username, password):
    try:
        session = InstaPy(username=username,
                          password=password,
                          headless_browser=True,
                          bypass_security_challenge_using='email',  # should we use an actual email?
                          want_check_browser=False,
                          disable_image_load=True,
                          multi_logs=True)
        return session
    except:
        print("Login error")


# assigning the returned value by the login function to session
session = login(insta_username, insta_password)


def quota_supervision():
    # enabled set to true to acivate false to deactivate supervising any time
    # peak likes ...once likes reach peak ,it will jump every other like yet do available tasks
    # only sever calls does not jump  it exits the program once it reaches peak
    # it will jump comments too  snce since commenting without a like isnt welcomed
    # sleep after for putting instapy to sleep after reaching peak
    # rather than jumping actions or exiting for server calls
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                 sleepyhead=True,
                                 stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=57,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=21,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700
                                 )


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


def liking_posts(hashtags):
    # activity
    # takes in a list of tags and generates smart tags
    # with banned and spammy tags filtered out
    session.set_smart_hashtags(hashtags, limit=5, sort='top', log_tags=True)
    session.like_by_tags(amount=10, use_smart_hashtags=True)
    # liking posts on own feeds
    session.like_by_feed(amount=90, randomize=True, unfollow=True, interact=True)


def engagement_pods():
    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.set_do_reply_to_comments(enabled=True, percentage=14)
    session.set_comment_replies(
        replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊",
                 u"😁😁😁", u"😂", u"🤓🤓🤓🤓🤓", u"👏🏼😉"], media="Photo")


def join_pods(hashtags):
    # engagement modes
    # 'no_comments' receives zero comments on your post from pod members
    # 'light'  encourages approximately 10% of pod members to comment on your post
    # 'normal' 30%
    # heavy 90%
    session.join_pods(topic='sports', engagement_mode='no_comments')
    # takes in a list of hashtags and follows
    session.follow_by_tags(hashtags, amount=2)


def interacting_with_certain_user_followers(user_names):
    # we will have web form asking for user input to fill this list
    # interacting with someone else's followers
    session.set_user_interact(amount=5, percentage=50, media=None)
    # add story watching while interacting with users
    # simulate=false is the safest setting as it disables all additional simulated interactions
    session.set_do_story(enabled=True, percentage=70, simulate=False)
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_comment(True, percentage=50)
    session.set_comments(comments, media='Photo')
    session.set_comments(['Awesome video @{}'], media='Video')
    session.interact_user_following(user_names, amount=5, randomize=True)


# watching stories by hash tags
def view_stories(hashtags):
    session.story_by_tags(hashtags)


# watching stories from users
def view_stories_from_users(users):
    # take users list
    session.story_by_users(users)


def follow_a_users_followers(user_names):
    # interacts with given username(s) and follows their followers
    session.follow_user_followers(user_names, amount=5, randomize=True, sleep_delay=600)


def follow_a_users_following(user_names):
    # interacts with given username(s) and follows people they are following
    session.follow_user_following(user_names, amount=5, randomize=True, sleep_delay=600)


def acceptFollowRequests():
    # amount the maximum amount of follow requests to accept
    # sleep_delay time to sleep after every accepted request
    session.accept_follow_requests(amount=100, sleep_delay=1)


# let's go now
with smart_run():
    """ Activity flow """
    general_settings(dont_like_tags, ignore_dont_like_tags, users_to_ignore, friends_list)
    liking_posts(smart_tags)
    engagement_pods()
    join_pods(tags)
    interacting_with_certain_user_followers(users_following)
    follow_a_users_followers(a_users_followers)
    follow_a_users_following(a_users_following)
    acceptFollowRequests()
    view_stories(tags)
    view_stories_from_users(a_users_view_story_list)

# NOTE:i have commented out session.end() because when the suite under line 47 starting with "with"...
# the program will be terminated automatically....that's what with means
# session.end()
