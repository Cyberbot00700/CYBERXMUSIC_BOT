from VipX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

TEXT = [ "**𝐎𝚈𝙴 𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰 𝐏𝙻𝚂🥲**",
         "**𝐑𝐢𝐲𝐚 𝐁𝐚𝐛𝐲 𝐕𝐜 𝐀𝐣𝐚𝐨...😘😘**",
         "**𝐂𝐲𝐛𝐞𝐫 𝐕𝐜 𝐀𝐣𝐚𝐨 𝐩𝐥𝐳...😓😓😣**",
         "**𝐂𝐲𝐛𝐞𝐫 𝐀𝐲𝐚 𝐇𝐚𝐢 𝐕𝐜 𝐏𝐞 𝐀𝐣𝐚..☺**",
         "**𝐂𝐲𝐛𝐞𝐫 𝐕𝐜 𝐀𝐣𝐚 𝐓𝐞𝐫𝐢 𝐆𝐟 𝐑𝐢𝐲𝐚 𝐊𝐢𝐬𝐢 𝐎𝐫 𝐒𝐞 𝐒𝐞𝐭 𝐇𝐨 𝐆𝐚𝐲𝐢...😰😰**",
         "**𝐑𝐢𝐲𝐚 𝐓𝐮𝐦𝐡𝐚𝐫𝐚 𝐁𝐟 𝐀𝐲𝐚𝐚 𝐇𝐚𝐢 𝐕𝐜 𝐏𝐞..😲**",
         "**𝐑𝐨𝐲𝐚𝐥 𝐕𝐜 𝐀𝐚 𝐀𝐛𝐡𝐢 𝐊𝐞 𝐀𝐛𝐡𝐢...😒😒**",
         "**𝐌𝐢𝐬𝐭𝐲 𝐁𝐚𝐛𝐲 𝐕𝐜 𝐀𝐣𝐚𝐨 𝐏𝐥𝐳...😭😭**",
         "**𝐒𝐡𝐢𝐯𝐚𝐧𝐬𝐡𝐢 𝐕𝐜 𝐀𝐚𝐨....😥**",
         "**𝐑𝐚𝐣𝐩𝐮𝐭 𝐕𝐜 𝐀𝐚 𝐇𝐚𝐫𝐚𝐦𝐢...😠😠**",
         "**𝐌𝐫 𝐙𝐞𝐜𝐱 𝐕𝐜 𝐀𝐚𝐢𝐲𝐞..😊😇**",
         "**𝐂𝐲𝐛𝐞𝐫 𝐕𝐜 𝐀𝐚𝐨 𝐑𝐢𝐲𝐚 𝐀𝐩𝐤𝐚 𝐖𝐚𝐢𝐭 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢...😢😢**",
         "**𝐑𝐢𝐲𝐚 𝐓𝐮𝐦 𝐀𝐠𝐚𝐫 𝐌𝐮𝐣𝐡𝐬𝐞 𝐏𝐲𝐚𝐫 𝐊𝐚𝐫𝐭𝐢 𝐇𝐨 𝐓𝐨 𝐕𝐜 𝐀𝐚𝐨 𝐀𝐛𝐡𝐢 𝐊𝐞 𝐀𝐛𝐡𝐢...😓😓**",
         "**𝐂𝐲𝐛𝐞𝐫 𝐕𝐜 𝐀𝐚𝐣𝐚𝐨 𝐑𝐢𝐲𝐚 𝐊𝐨 𝐂𝐡𝐡𝐨𝐝 𝐊𝐞𝐞 𝐌𝐚𝐭 𝐉𝐚𝐨 𝐏𝐥𝐞𝐚𝐬𝐞...😞😞**",
         "**𝐑𝐢𝐲𝐚 𝐓𝐮𝐦 𝐕𝐜 𝐀𝐚𝐨𝐠𝐞 𝐘𝐚 𝐌𝐞𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐒𝐞 𝐂𝐡𝐚𝐥𝐚 𝐉𝐚𝐮...😕😕**',
         "**𝐀𝐠𝐚𝐫 𝐓𝐮𝐦 𝐌𝐮𝐣𝐡𝐬𝐞 𝐁𝐚𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐂𝐡𝐚𝐡𝐭𝐞 𝐇𝐨 𝐓𝐨 𝐕𝐜 𝐀𝐣𝐚𝐨 𝐀𝐛𝐡𝐢 𝐊𝐞 𝐀𝐛𝐡𝐢...😃**",
         "**𝐀𝐠𝐚𝐫 𝐀𝐚𝐩 𝐙𝐢𝐧𝐝𝐚 𝐇𝐚𝐢 𝐓𝐨 𝐕𝐜 𝐀𝐚𝐣𝐚𝐞..😌**",
         "**𝐓𝐮𝐦 𝐕𝐜 𝐍𝐚𝐡𝐢 𝐀𝐭𝐞 𝐊𝐲𝐚𝐚 𝐤𝐚𝐛𝐡𝐢.....?😪**",
         "**𝐕𝐜 𝐀𝐣𝐚𝐚 𝐎𝐲𝐞 𝐉𝐚𝐥𝐝𝐢...😣**",
         "**𝐉𝙾𝙸𝙽 𝐕𝙲 𝐅𝙰𝚂𝚃 𝐈𝚃𝚂 𝐈𝙼𝙰𝙿𝙾𝚁𝚃𝙰𝙽𝚃😬**",
         "**𝐂𝙾𝙼𝙴 𝚅𝙲 𝙱𝙰𝙱𝚈 𝙵𝙰𝚂𝚃🏓**",
         "**𝐁𝙰𝙱𝚈 𝐓𝚄𝙼 𝐁𝙷𝙸 𝐓𝙷𝙾𝚁𝙰 𝐕𝙲 𝐀𝙰𝙽𝙰🥰**",
         "**𝐎𝚈𝙴 𝐂𝙷𝙰𝙼𝚃𝚄 𝐕𝙲 𝐀𝙰 𝐄𝙺 𝐄𝙰𝙼 𝐇𝙰𝙸🤨**",
         "**𝐒𝚄𝙽𝙾 𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁 𝐋𝙾🤣**",
         "**𝐕𝙲 𝐀𝙰 𝐉𝙰𝙸𝚈𝙴 𝐄𝙺 𝐁𝙰𝚁😁**",
         "**𝐕𝙲 𝐓𝙰𝙿𝙺𝙾 𝐆𝙰𝙼𝙴 𝐂𝙷𝙰𝙻𝚄 𝐇𝙰𝙸⚽**",
         "**𝐕𝙲 𝐀𝙰𝙾 𝐁𝙰𝚁𝙽𝙰 𝐁𝙰𝙽 𝐇𝙾 𝐉𝙰𝙾𝙶𝙴🥺**",
         "**𝐒𝙾𝚁𝚁𝚈 𝐕𝙰𝙱𝚈 𝐏𝙻𝚂 𝐕𝙲 𝐀𝙰 𝐉𝙰𝙾 𝐍𝙰😥**",
         "**𝐕𝙲 𝐀𝙰𝙽𝙰 𝐄𝙺 𝐂𝙷𝙸𝙹 𝐃𝙸𝙺𝙷𝙰𝚃𝙸 𝐇𝚄🙄**",
         "**𝐕𝙲 𝐌𝙴 𝐂𝙷𝙴𝙲𝙺 𝐊𝚁𝙺𝙴 𝐁𝙰𝚃𝙰𝙾 𝐓𝙾 𝐒𝙾𝙽𝙶 𝐏𝙻𝙰𝚈 𝐇𝙾 𝐑𝙷𝙰 𝐇?🤔**",
         "**𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁𝙽𝙴 𝐌𝙴 𝐊𝚈𝙰 𝐉𝙰𝚃𝙰 𝐇 𝐓𝙷𝙾𝚁𝙰 𝐃𝙴𝚁 𝐊𝙰𝚁 𝐋𝙾 𝐍𝙰🙂**",
         "**𝐎𝐲𝐞 𝐒𝐮𝐧 𝐍𝐚 𝐕𝐂 𝐀𝐣𝐚😫😫**",
         "**𝐁𝐚𝐛𝐲 𝐕𝐜 𝐀𝐚𝐣𝐚𝐨😘**",
         "**𝐁𝐚𝐛𝐮 𝐕𝐜 𝐀𝐝𝐚𝐨 𝐍𝐚😢**",
         "**𝐉𝐚𝐚𝐧 𝐊𝐚𝐡𝐚 𝐇𝐨 𝐀𝐚𝐩 𝐕𝐜 𝐀𝐚𝐨 𝐀𝐛𝐡𝐢 𝐊𝐞 𝐀𝐛𝐡𝐢...😫😫♥**",
         "**𝐃𝐚𝐫𝐥𝐢𝐧𝐠 𝐕𝐜 𝐀𝐣𝐚𝐨😚**",
         "**𝐌𝐮𝐦𝐦𝐚 𝐕𝐜 𝐀𝐣𝐚𝐨😝**",
         "**𝐕𝐜 𝐀𝐣𝐚𝐨 𝐍𝐚...😫😫😫**",
         "**𝐁𝐚𝐛𝐲 𝐕𝐜 𝐓𝐚𝐩𝐤𝐨😉**",
         "**𝐊𝐮𝐭𝐭𝐞 𝐕𝐜 𝐀𝐚😏😏**",
         "**𝐁𝐡𝐚𝐛𝐡𝐢 𝐕𝐜 𝐀𝐣𝐚𝐨 𝐁𝐡𝐚𝐢 𝐁𝐮𝐥𝐚 𝐑𝐚𝐡𝐞 𝐇𝐚𝐢 𝐀𝐩𝐤𝐨...🙈😻**",
         "**𝐓𝐮𝐦 𝐕𝐜 𝐀𝐚 𝐑𝐚𝐡𝐞 𝐇𝐨 𝐘𝐚 𝐍𝐚𝐡𝐢..?😤**",
         "**𝐒𝐚𝐥𝐚 𝐊𝐚𝐛 𝐒𝐞 𝐁𝐮𝐥𝐚 𝐑𝐚𝐡𝐚 𝐇𝐮 𝐓𝐮𝐦𝐡𝐞 𝐕𝐜 𝐀𝐚𝐣𝐚𝐨 𝐁𝐨𝐥𝐚 𝐭𝐨 𝐍𝐚𝐡𝐢 𝐀𝐚𝐚 𝐑𝐚𝐡𝐢...😞😞**",
         "**𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐋𝐚𝐝𝐤𝐢 𝐕𝐜 𝐀𝐚𝐣𝐚..😁**",
         "**𝐓𝐮𝐦 𝐕𝐜 𝐊𝐲𝐮 𝐍𝐚𝐡𝐈 𝐀𝐚𝐚 𝐑𝐚𝐡𝐞..?😥**",
         "**𝐕𝐜 𝐍𝐚𝐡𝐢 𝐀𝐚𝐞𝐠𝐚 𝐊𝐲𝐚....?😒**",
         "**𝐕𝐜 𝐀𝐚𝐨 𝐍𝐚𝐡𝐢 𝐓𝐨 𝐌𝐮𝐦𝐦𝐲 𝐊𝐨 𝐂𝐚𝐥𝐥 𝐊𝐚𝐫 𝐃𝐮𝐧𝐠𝐚 𝐓𝐮𝐦𝐡𝐚𝐫𝐞...😜**",
         "**𝐓𝐮 𝐕𝐜 𝐀𝐚𝐞𝐠𝐚 𝐘𝐚 𝐌𝐞 𝐎𝐟𝐟 𝐂𝐡𝐚𝐥𝐢 𝐉𝐚𝐮....?😒😒**",
         "**𝐎𝐲𝐞 𝐒𝐮𝐧 𝐓𝐞𝐫𝐢 𝐆𝐟 𝐀𝐚𝐢 𝐇𝐚𝐢 𝐕𝐜 𝐏𝐞 𝐀𝐣𝐚 😳**",
         "**𝐕𝐜 𝐀𝐚𝐨 𝐁𝐨𝐥𝐚 𝐌𝐞𝐧𝐞..😒😒**",
         "**𝐎𝐲𝐞 𝐒𝐮𝐧 𝐕𝐜 𝐏𝐞𝐞 𝐄𝐤 𝐌𝐚𝐚𝐥 𝐀𝐚𝐲𝐢 𝐇𝐮𝐢 𝐇𝐚𝐢..😲😋😻**",
         "**𝐁𝐡𝐚𝐢 𝐓𝐞𝐫𝐚 𝐃𝐨𝐬𝐭 𝐀𝐚𝐣 𝐓𝐠 𝐂𝐡𝐡𝐨𝐝 𝐊𝐞 𝐉𝐚𝐚 𝐑𝐚𝐡𝐚 𝐇𝐚𝐢 𝐕𝐜 𝐀𝐣𝐚 𝐔𝐬𝐬𝐞 𝐛𝐚𝐚𝐭 𝐤𝐚𝐫 𝐥𝐞...😭😨**",
         "**𝐁𝐡𝐚𝐢 𝐓𝐞𝐫𝐚 𝐃𝐨𝐬𝐭 𝐓𝐞𝐫𝐢 𝐁𝐚𝐧𝐝𝐢 𝐊𝐨 𝐏𝐫𝐨𝐩𝐨𝐬𝐞 𝐊𝐚𝐫 𝐑𝐚𝐡𝐚𝐚 𝐇𝐚𝐢 𝐕𝐜 𝐏𝐞 𝐀𝐣𝐚𝐚 𝐕𝐜 𝐏𝐞**",
         "**𝐊𝐮𝐭𝐭𝐞 𝐆𝐟 𝐊𝐨 𝐕𝐜 𝐏𝐞 𝐀𝐤𝐞𝐥𝐚𝐚 𝐂𝐡𝐡𝐨𝐝 𝐊𝐞 𝐊𝐚𝐡𝐚 𝐂𝐡𝐚𝐥𝐚 𝐆𝐚𝐲𝐚 𝐕𝐜 𝐀𝐚 𝐉𝐚𝐥𝐝𝐢...😬😐😑**",
         "**𝐑𝐢𝐲𝐚 𝐊𝐨 𝐕𝐜 𝐁𝐮𝐥𝐚𝐨 𝐂𝐲𝐛𝐞𝐫 𝐁𝐮𝐥𝐚 𝐑𝐚𝐡𝐚𝐚 𝐁𝐨𝐥𝐨..!**",
        ]

@app.on_message(filters.command(["vctag", "vctagall"], prefixes=["/", ".", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")

    if message.reply_to_message and message.text:
        return await message.reply("/Vctag 𝐕𝐂 𝐀𝐀 𝐉𝐀𝐎 𝐒𝐀𝐁 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/Vctag 𝐕𝐂 𝐀𝐀 𝐉𝐀𝐎 𝐒𝐀𝐁 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    else:
        return await message.reply("/Vctag 𝐕𝐂 𝐀𝐀 𝐉𝐀𝐎 𝐒𝐀𝐁 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TEXT)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(TEXT)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop", "stopvctag", "vctagstop", "cancelvctag", "canceltag", "stoptag", "stoptagall", "canceltagall"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ 𝐌𝙴𝙽𝚃𝙸𝙾𝙽 𝐏𝚁𝙾𝙲𝙴𝚂𝚂 𝐂𝙰𝙽𝙲𝙴𝙻𝙸𝙽𝙶♦")
