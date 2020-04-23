from instapy import InstaPy
user = input()
passw = input()
session = InstaPy(username=user, password=passw, headless_browser=True, disable_image_load=True, multi_logs=True)
session.login()

# interacting with someone else's followers


def interact_with_users_following_username():
    session.set_user_interact(amount=5, percentage=50, media=None)
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_comment(True, percentage=50)
    session.set_comments(["Awesome!", "Sweet!", "Beautiful :heart_eyes:"], media='Photo')
    session.set_comments(['Awesome video @{}'], media='Video')
    session.interact_user_following(['demo'], amount=5, randomize=True)  # we may add functionality to add users with a list


# end session
session.end()
