
#  unfollow features
def unfollow_with_custom_list(custom_list):
    # will unfollow all users in a given list not following me back if custom_list_param == nonfollowers
    # if custom_list_param == all it will unfollow all the users in a given list
    session.unfollow_users(amount=84, custom_list_enabled=False,
                           custom_list=custom_list,
                           custom_list_param="nonfollowers",  # or all
                           style="RANDOM",
                           unfollow_after=55 * 60 * 60,  # after 55 hours
                           sleep_delay=600)


def unfollow_followed_by_instapy():
    # styles in unfollow_users
    # with "FIFO", it will unfollow users in the exact order they are loaded
    # ("FIFO" is the default style unless you change it);
    # with "LIFO" it will unfollow users in the reverse order they were loaded;
    # with "RANDOM" it will unfollow users in the shuffled order;
    session.unfollow_users(amount=60,
                           instapy_followed_enabled=True,
                           instapy_followed_param="all",  # two options all and nonfollowers
                           style="FIFO",   #
                           unfollow_after=90 * 60 * 60,  # after 90 hours time in seconds
                           sleep_delay=501)


def unfollow_all_who_dont_follow_back():
    session.unfollow_users(amount=126,
                           nonFollowers=True,
                           style="RANDOM",
                           unfollow_after=42 * 60 * 60,  # fourty two hours
                           sleep_delay=655)


def just_unfollow_all():
    # unfollows regardless is a user follows you or not
    # You can choose unfollow style as "FIFO" (First-Input-First-Output)
    # OR "LIFO" (Last-Input-First-Output) OR "RANDOM".
    session.unfollow_users(amount=40,
                           allFollowing=True,
                           style="LIFO",
                           unfollow_after=3 * 60 * 60,  # after three hours
                           sleep_delay=450)

# NOTE: You should know that, in one RUN, unfollow_users feature can take only one method from all 4 above.
# That's why, it is best to disable other 3 methods while using a one:
