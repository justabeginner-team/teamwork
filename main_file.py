# imports
from instapy import InstaPy
from instapy import smart_run
from auto_like import liking_posts
from auto_follow import interacting_with_certain_user_followers, follow_a_users_followers, \
    follow_commenters_of_photos_of_users, follow_likers_of_users, follow_by_list, acceptFollowRequests, \
    follow_a_users_following
from story_view import view_stories_from_users, view_stories
from quota_supervision import quota_supervision
from general_settings import general_settings
from unfollow_features import unfollow_all_who_dont_follow_back, unfollow_followed_by_instapy, unfollow_with_custom_list, just_unfollow_all
from pods import engagement_pods, join_pods

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
specific_follow_list = []  # people to follow
photo_likers_follow_list = []  # follow people who like the photos of these people
photo_commenter_follow_list = []  # follow people who comment the photos of these people
custom_unfollow_list = []  # people to unfollow / unfollow if they don't follow back

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


# let's go now
with smart_run():
    """ Activity flow """
    general_settings(dont_like_tags, ignore_dont_like_tags, users_to_ignore, friends_list)
    quota_supervision()
    liking_posts(smart_tags)
    engagement_pods()
    join_pods(tags)
    interacting_with_certain_user_followers(users_following)
    follow_a_users_followers(a_users_followers)
    follow_a_users_following(a_users_following)
    acceptFollowRequests()
    view_stories(tags)
    view_stories_from_users(a_users_view_story_list)
    follow_by_list(specific_follow_list)
    follow_likers_of_users(photo_likers_follow_list)
    follow_commenters_of_photos_of_users(photo_commenter_follow_list)
    unfollow_with_custom_list(custom_unfollow_list)
    unfollow_followed_by_instapy()
    unfollow_all_who_dont_follow_back()
    just_unfollow_all()

# NOTE:i have commented out session.end() because when the suite under line 47 starting with "with"...
# the program will be terminated automatically....that's what with means
# session.end()
