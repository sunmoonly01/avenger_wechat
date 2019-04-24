import itchat
import jieba


WARNING_KEYWORDS = [
    "钢铁侠",
    "铁人",
    "铁罐",
    "iron",
    "man",
    "小蜘蛛",
    "绿巨人",
    "鹰眼",
    "美队",
    "tony",
    "stack",
    "复仇者",
    "4",
    "联盟",
    "妇联",
    "黑寡妇",
    "灭霸",
]


WARNING_REPLY = """该消息涉嫌剧透复联四 现已清屏!!
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
远离剧透，人人有责！！
"""


def check_msg(msg):
    keyword_list = jieba.cut(msg)
    for word in keyword_list:
        if word in WARNING_KEYWORDS:
            return True
    return False


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if check_msg(msg.text):
        print(f"WARNING! 这条消息涉嫌剧透,现已自动屏蔽 FROM：{msg.user.NickName}")
        return WARNING_REPLY


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    itchat.run()
