from nora_bot import bot, load
from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler

def send_poll_to_user(user_id):
    answer_options = ["До 16", "16-17", "17-18", "19-20", "20-21", "21-23"]
    formatted_date = datetime.today().strftime('%d.%m.%Y')

    message = bot.send_poll(
        chat_id=user_id,
        question=f"Кто будет в Норе {formatted_date}?",
        options=answer_options,
        allows_multiple_answers=True,
        is_anonymous=False
    )

    bot.pin_chat_message(user_id, message.id)


def send_polls():
    users = load()

    print(f"Running sender for {users}")

    for user_id in users:
        send_poll_to_user(user_id)


scheduler = BlockingScheduler()
scheduler.add_job(send_polls, 'cron', hour=10, minute=0, second=0)
scheduler.start()



