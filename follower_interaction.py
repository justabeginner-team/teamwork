def interacting_with_certain_user_followers(user_names, comments):
    # we will have web form asking for user input to fill this list
    # interacting with someone else's followers
    # takes in a list of usernames and comments
    session.set_user_interact(amount=5, percentage=50, media=None)
    # add story watching while interacting with users
    # simulate=false is the safest setting as it disables all additional simulated interactions
    session.set_do_story(enabled=True, percentage=70, simulate=False)
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_comment(True, percentage=50)
    session.set_comments(comments, media='Photo')
    session.set_comments(['Awesome video @{}'], media='Video')
    session.interact_user_following(user_names, amount=5, randomize=True)


def interact_with_a_users_following(user_names, comments):
    # Interact with the people that a given user is following
    # set_do_comment, set_do_follow and set_do_like are applicable
    # takes in a list of usernames and comments
    session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=False, percentage=70)
    session.set_do_like(enabled=False, percentage=70)
    session.set_comments(comments)
    session.set_do_comment(enabled=True, percentage=80)
    session.interact_user_following(user_names, amount=10, randomize=True)

