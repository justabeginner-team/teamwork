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
smart_tags = ['science', 'arduino', 'cars', 'bikes']

users_following = []
a_users_followers = []
a_users_following = []

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
# set bypass_security_challenge_using='email' to bypass any suspicious login attempt challenge
#can also use "bypass_security_challenge_using='sms'"
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

def quota_supervion(session):
    #enabled set to true to acivate false to deactivate supervising any time
    #peak likes ...once likes reach peak ,it will jump every other like yet do available tasks
         #only sever calls does not jump  it exits the program once it reaches peak
         #it will jump comments too  snce since commenting without a like isnt welcomed
     #sleep after for putting instapy to sleep after reaching peak rather than jumping actions or exiting for server calls
     #     
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
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

def general_settings(session):
    # general settings
    session.set_action_delays(enabled=True, follow=2)


def liking_posts(session,hashtags):
    # activity
    # takes in a list of tags and generates smart tags
    # with banned and spammy tags filtered out
    session.set_smart_hashtags(hashtags, limit=5, sort='top', log_tags=True)
    session.like_by_tags(amount=10, use_smart_hashtags=True)


def engagement_pods(session):
    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.set_do_reply_to_comments(enabled=True, percentage=14)
    session.set_comment_replies(
        replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊",
                 u"😁😁😁", u"😂", u"🤓🤓🤓🤓🤓", u"👏🏼😉"], media="Photo")


def join_pods(session,hashtags):
    #engagement modes
    #'no_comments' receives zero comments on your post from pod members
    #'light'  encourages approximately 10% of pod members to comment on your post
    #'normal' 30%
    #heavy 90%
    session.join_pods(topic='sports', engagement_mode='no_comments')
    # takes in a list of hashtags and follows
    session.follow_by_tags(hashtags, amount=2)


def interacting_with_certain_user_followers(session,user_names):
    # we will have web form asking for user input to fill this list
    # interacting with someone else's followers
    session.set_user_interact(amount=5, percentage=50, media=None)
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_comment(True, percentage=50)
    session.set_comments(comments, media='Photo')
    session.set_comments(['Awesome video @{}'], media='Video')
    session.interact_user_following(user_names, amount=5, randomize=True)


def follow_a_users_followers(session,user_names):
    # interacts with given username(s) and follows their followers
    session.follow_user_followers(user_names, amount=5, randomize=True, sleep_delay=600)


def follow_a_users_following(session,user_names):
    # interacts with given username(s) and follows people they are following
    session.follow_user_following(user_names, amount=5, randomize=True, sleep_delay=600)

def acceptFollowRequests(session):
    #amount the maximum amount of follow requests to accept
    #sleep_delay time to sleep after every accepted request
    session.accept_follow_requests(amount=100, sleep_delay=1)

def ignore_restrictions(session):
    # will ignore the don't like if the description contains
    # one of the given words
    session.set_ignore_if_contains(['glutenfree', 'french', 'tasty'])
# let's go now
with smart_run(session):
    """ Activity flow """
    general_settings()
    liking_posts(smart_tags)
    engagement_pods()
    join_pods(tags)
    interacting_with_certain_user_followers(users_following)
    follow_a_users_followers(a_users_followers)
    follow_a_users_following(a_users_following)

# NOTE:i have commented out session.end() because when the suite under line 47 starting with "with"...
# the program will be terminated automatically....that's what with means
# session.end()
