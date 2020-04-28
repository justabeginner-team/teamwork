# for accepting and removing outgoing follow requests
def accept_request():
    # amount == maximum follow requests to be accepted
    # sleep delay == time to sleep after every accepted request in seconds
    session.accept_follow_requests(amount=100, sleep_delay=1)


def remove_outgoing_requests():
    # removes outgoing unapproved follow requests from private accounts
    session.remove_follow_requests(amount=200, sleep_delay=600)
