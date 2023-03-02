#  首先创建一个列表，其中包含一些要打印的设计。
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# while unprinted_designs:
#     completed_models.append(unprinted_designs.pop())
# print(completed_models)

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        completed_models.append(unprinted_designs.pop())

def show_models(completed_models):
    print(completed_models)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_models(completed_models)
print(unprinted_designs)

# 练习
def print_message(messages):
    for message in messages:
        print(message)

def send_message(messages,send_messages):
    while messages:
        send_messages.append(messages.pop())

messages = ['a','b','c','d']
send_messages = []
print_message(messages)
send_message(messages, send_messages)
print(send_messages)
print(messages)

# send_message(messages[:], send_messages)
# print(send_messages)
# print(messages)
