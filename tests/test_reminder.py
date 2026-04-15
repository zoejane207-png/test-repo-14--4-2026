from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Zoe")
    reminder.remind_me_to("walk the dog")
    result = reminder.remind()
    assert result == "walk the dog, Zoe!"