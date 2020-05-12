from instapy import InstaPy


def login(username, password):
    try:
        session = InstaPy(username=username,
                          password=password,
                          nogui=True,
                          bypass_security_challenge_using='email',  # should we use an actual email?
                          want_check_browser=False,
                          disable_image_load=True,
                          multi_logs=True)
        return session
    except:
        print("Login error")
