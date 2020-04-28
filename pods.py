
def engagement_pods():
    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.set_do_reply_to_comments(enabled=True, percentage=14)
    session.set_comment_replies(
        replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊",
                 u"😁😁😁", u"😂", u"🤓🤓🤓🤓🤓", u"👏🏼😉"], media="Photo")


def join_pods(hashtags):
    # engagement modes
    # 'no_comments' receives zero comments on your post from pod members
    # 'light'  encourages approximately 10% of pod members to comment on your post
    # 'normal' 30%
    # heavy 90%
    session.join_pods(topic='sports', engagement_mode='no_comments')
    # takes in a list of hashtags and follows
    session.follow_by_tags(hashtags, amount=2)

