from instabot import Bot
import telebot
from telebot import types
import requests
bot = telebot.TeleBot("1346333183:AAHIAjQrIputQMrBsHN11RuhHT8-xf07HNE")
j = Bot()
j.login(username='xc26.zp', password='qqqq1111')


@bot.message_handler(commands=['start'])
def key(msg):
    q = types.InlineKeyboardMarkup()
    q1 = types.InlineKeyboardButton("صوره الشخصية 💫", callback_data='q1')
    q2 = types.InlineKeyboardButton("تحميل من الاستوري ♻️", callback_data='q2')
    q3 = types.InlineKeyboardButton("تحميل مقطع فيديو 🎥", callback_data='q3')

    q.add(q1, q2)
    q.add(q3)
    bot.send_message(msg.chat.id, 'اهلا و سهلا بك ايها المستخدم في بوت التفاعل✨', reply_markup=q)

@bot.callback_query_handler(lambda call:True)
def any(call):
    if call.data == 'q1':
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل اليوزر لكي يتم تحميل صورته الشخصية 🌀", reply_markup=markup)
    if call.data == 'q2':
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل اليوزر لكي يتم تحميل استوري الحساب ☄️", reply_markup=markup)
    if call.data == 'q3':
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل اليوزر لكي يتم تحميل مقطع الفيديو من الحساب 👁‍🗨", reply_markup=markup)
    if call.data == 'q6':
        i = 5
        try:
            while True:
                bot.send_message(call.message.chat.id, n.split('video_url')[i][
                                                               n.split('video_url')[1].find('https:'):
                                                               n.split('video_url')[1].find('video_view_count') - 4])
                i += 1
        except:
            pass
@bot.message_handler(content_types='text')
def an(msg):
    global n
    try:
        if msg.reply_to_message.text == "ارسل اليوزر لكي يتم تحميل صورته الشخصية 🌀":
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            }
            INSTA_URL = "https://www.instagram.com/"
            USER_ID = msg.text
            TAIL = "/?__a=1"
            URL = INSTA_URL + USER_ID + TAIL
            response = requests.get(URL, headers=header).json()
            n = str(response['graphql']['user']['edge_owner_to_timeline_media']['edges'])
            hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]
            bot.send_message(msg.chat.id, hd_image_location)
    except:
        pass
    try:

        if msg.reply_to_message.text == "ارسل اليوزر لكي يتم تحميل مقطع الفيديو من الحساب 👁‍🗨":
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            }
            INSTA_URL = "https://www.instagram.com/"
            USER_ID = msg.text
            TAIL = "/?__a=1"
            URL = INSTA_URL + USER_ID + TAIL
            response = requests.get(URL, headers=header).json()
            if '{}' in str(response):
                bot.reply_to(msg, 'لا يمكننا الوصول لهذا اليوزر ❌')
            if "is_private': True" in str(response):
                bot.reply_to(msg, 'هذا الحساب برايفد 🤙🏼')
            else:

                n = str(response['graphql']['user']['edge_owner_to_timeline_media']['edges'])
                if 'video_url' in n:
                    v = n[n.find('video_url') + 13:]
                    i = 1
                    while i < 5:
                        if i == 4:
                            try:
                                print(n.split('video_url')[i + 1][
                                  n.split('video_url')[1].find('https:'):n.split('video_url')[1].find('video_view_count') - 4])
                                q = types.InlineKeyboardMarkup()
                                q1 = types.InlineKeyboardButton('المزيد ♐️', callback_data='q6')
                                q.add(q1)
                                bot.send_message(msg.chat.id, text=n.split('video_url')[i][
                                                               n.split('video_url')[1].find('https:'):
                                                               n.split('video_url')[1].find('video_view_count') - 4], reply_markup=q)
                            except:
                                bot.send_message(msg.chat.id, text=n.split('video_url')[i][
                                                                   n.split('video_url')[1].find('https:'):
                                                                   n.split('video_url')[1].find(
                                                                       'video_view_count') - 4])
                        else:
                            bot.send_message(msg.chat.id, text=n.split('video_url')[i][
                                                               n.split('video_url')[1].find('https:'):
                                                               n.split('video_url')[1].find('video_view_count') - 4])

                        i += 1
                else:
                    bot.reply_to(msg, 'عفوا هذا اليوزر لا يحتوي على فيديوهات ️⚠️')
    except:
        pass
    try:
        if msg.reply_to_message.text == "ارسل اليوزر لكي يتم تحميل استوري الحساب ☄️":
            try:
                v = str(j.get_user_stories(user_id=j.convert_to_user_id(usernames=msg.text)))
            except:
                pass
            try:
                if v == '([], [])':
                    bot.reply_to(msg, 'تاكد من اليوزر الذي ارسلته')
                else:
                    i = 0
                    while i < len(v) + 1:
                        try:
                            bot.send_message(msg.chat.id, v.split(',')[i])
                        except:
                            pass
                        i += 1
            except:
                bot.reply_to(msg, 'تاكد من اليوزر الذي ارسلته')
    except:
        pass


bot.polling()
