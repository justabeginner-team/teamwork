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
tags = ['engineer','bootstrap4','natgeo','biomedical','KU','python programming','BMW','iot','fashion','web dev']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
# set bypass_security_challenge_using='email' to bypass any suspicious login attempt challenge
# set  want_check_browser=False to ovverride checks like being online,my connection and the availability of instagram severs


def login(insta_username,insta_password):
    try:
        session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=True,
                              bypass_security_challenge_using='email',
                              want_check_browser=False,
                              disable_image_load=True,
                              multi_logs=True)
        return session
    except:
        print("Login error")

 #assigning the returned value by the login function to session
session=login(insta_username,insta_password)

#let's go now
with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])
  session.set_action_delays(enabled=True,follow=2)
  # activity		
  session.like_by_tags(["natgeo"], amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.set_do_reply_to_comments(enabled=True, percentage=14)
  session.set_comment_replies(replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊", u"😁😁😁", u"😂",  u"🤓🤓🤓🤓🤓",u"👏🏼😉"],media="Photo")

  #session.join_pods(topic='sports', engagement_mode='no_comments')
  session.follow_by_tags(tags,amount=2)


  # interacting with someone else's followers

  def interact_with_users_following_username(session):
      session.set_user_interact(amount=5, percentage=50, media=None)
      session.set_do_like(enabled=True, percentage=70)
      session.set_do_comment(True, percentage=50)
      session.set_comments(["Awesome!", "Sweet!", "Beautiful :heart_eyes:"], media='Photo')
      session.set_comments(['Awesome video @{}'], media='Video')
      session.interact_user_following(['demo'], amount=5,
                                      randomize=True)  # we may add functionality to add users with a list

  #NOTE:i have commented out session.end() because when the suite under line 47 starting with "with"...the program will be terminated automatically....thats what with means
  #session.end()

