async def archive(bot, message):

    archiveChatID = -803504766

    if message.chat.type != "private":
        if message.chat.id == archiveChatID:

            await bot.send_message(message.chat.id, "You can't archive here")

        else:

            await bot.send_message(
                message.chat.id,
                'Reply "save" to archive the message',
            )
    else:
        await bot.send_message(message.chat.id, "Not supported in private messages")


async def bot_reply_archive(bot, message):
    archiveChatID = -803504766
    if message.chat.type != "private":
        if message.chat.id == archiveChatID:
            await bot.send_message(message.chat.id, "You can't archive here")

        else:
            if message.text == "save":
                msgID = message.reply_to_message.message_id
                await bot.send_message(message.chat.id, "archived")
            await bot.forward_message(-803504766, message.chat.id, msgID)

    else:
        await bot.send_message(message.chat.id, "You can't archive private messages")