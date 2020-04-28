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
