from telegram import Update, Bot

from core.functions.triggers import trigger_decorator
from core.utils import send_async, update_group


@trigger_decorator
def boss_common(bot: Bot, update: Update, level_from, level_to):
    group = update_group(update.message.chat)
    if len(group.squad) == 1:
        members = []
        for member in group.squad[0].members:
            char = member.user.character
            if level_from <= char.level <= level_to:
                members.append('@' + member.user.username)
        msg = ' '.join(members)
        send_async(bot, chat_id=update.message.chat.id, text=msg)


def boss_leader(bot: Bot, update: Update):
    boss_common(bot, update, 15, 25)


def boss_zhalo(bot: Bot, update: Update):
    boss_common(bot, update, 26, 35)


def boss_monoeye(bot: Bot, update: Update):
    boss_common(bot, update, 36, 45)


def boss_hydra(bot: Bot, update: Update):
    boss_common(bot, update, 46, 100500)
