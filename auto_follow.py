
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


def follow_by_list(username_list):
    # follows specific usernames entered as a list
    # the interact feature allows use of set_user_interact
    # which interacts with the usernames after following them
    session.set_user_interact(amount=4,
                              percentage=50,
                              randomize=True,
                              media='Photo')
    session.follow_by_list(followlist=username_list, ttimes=1, sleep_delay=600, interact=False)


def follow_likers_of_users(username_list):
    # follows people who like the photos of a specific username
    # photograb amount is how many photos to grab from a users profile and analyze who liked it
    # enabling interactions enables liking their photos too

    session.follow_likers(username_list,
                          photos_grab_amount=5,
                          follow_likers_per_photo=5,  # how many people to follow per photo
                          randomize=True,
                          sleep_delay=600,  # defines breaktime after some good following
                          interact=False)
    session.set_user_interact(amount=2,
                              percentage=70,
                              randomize=True,
                              media='Photo')


def follow_commenters_of_photos_of_users(username_list):
    # follows people who comment on photos of a specific username
    session.follow_commenters(username_list,
                              amount=50,  # how many people to follow
                              daysold=5,  # will pick commenters no older than 5 daysold
                              max_pic=5,  # limit of number of picks to analyze
                              sleep_delay=600,
                              interact=False)
    session.set_user_interact(amount=3,
                              percentage=32,
                              randomize=True,
                              media='Video')
