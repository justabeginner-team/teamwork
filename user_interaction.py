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

users_following = []

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
# set bypass_security_challenge_using='email' to bypass any suspicious login attempt challenge
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


def general_settings():
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_action_delays(enabled=True, follow=2)


def activities():
    # activity
    session.like_by_tags(["natgeo"], amount=10)


def engagement_pods():
    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.set_do_reply_to_comments(enabled=True, percentage=14)
    session.set_comment_replies(
        replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊",
                 u"😁😁😁", u"😂", u"🤓🤓🤓🤓🤓", u"👏🏼😉"], media="Photo")


def join_pods():
    # session.join_pods(topic='sports', engagement_mode='no_comments')
    session.follow_by_tags(tags, amount=2)


def interacting_with_certain_user_followers(users_names_list):
    # interacting with someone else's followers
    session.set_user_interact(amount=5, percentage=50, media=None)
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_comment(True, percentage=50)
    session.set_comments(comments, media='Photo')
    session.set_comments(['Awesome video @{}'], media='Video')
    session.interact_user_following(users_names_list, amount=5, randomize=True)


# let's go now
with smart_run(session):
    """ Activity flow """
    general_settings()
    activities()
    engagement_pods()
    join_pods()
    interacting_with_certain_user_followers(users_following)

# NOTE:i have commented out session.end() because when the suite under line 47 starting with "with"...
# the program will be terminated automatically....that's what with means
# session.end()
