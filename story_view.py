# watching stories by hash tags
def view_stories(hashtags):
    session.story_by_tags(hashtags)


# watching stories from users
def view_stories_from_users(users):
    # take users list
    session.story_by_users(users)

