from telethon import events
from ..sql_helper.globals import addgvar, gvarstatus, delgvar
from jmub import jmub

# ها ولك جاي تخمط خرب عقلك اي والله 😂🏃


@jmub.ar_cmd(pattern="تفعيل الذاتية")
async def start_datea(event):
    if gvarstatus("DATEA") is None:
        return await edit_or_reply(event, "- تم بنجاح تفعيل حفظ الميديا الذاتية من الان")
        addgvar("DATEA", "True")
    else:
        await edit_or_reply(event, "حفظ الذاتية مفعل بالأًصل")

@jmub.ar_cmd(pattern="تعطيل الذاتية")
async def stop_datea(event):
    if gvarstatus("DATEA") is None:
        return await edit_or_reply(event, "حفظ الذاتية غير مفعل بالأًصل")
    else:
        await edit_or_reply(event, "- تم بنجاح تعطيل حفظ الميديا الذاتية من الان")
        delgvar("DATEA")


@jmub.on(
    events.NewMessage(
        func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread
    )
)
async def tf3el(event):
    if gvarstatus("DATEA"):
        sender = await event.get_sender()
        username = sender.username
        user_id = sender.id

        result = await event.download_media()
        caption = (
            f"ميديا ذاتية التدمير وصلت لك !\n: المرسل @{username}\nالايدي : {user_id}"
        )
        await jmub.send_file("me", result, caption=caption)
