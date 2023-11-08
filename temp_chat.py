
from fibers.model.chat import Chat


chat = Chat()
chat.add_user_message("hi")
res = chat.complete_chat()
print(res)