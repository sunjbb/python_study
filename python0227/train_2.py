user_name = "sunjiabao"
message = f"Hello {user_name},would you like to learn some Python today"
print(message)

message_upper = f"Hello {user_name.upper()},would you like to learn some Python today"
message_title = f"Hello {user_name.title()},would you like to learn some Python today"
message_lower = f"Hello {user_name.lower()},would you like to learn some Python today"
print(message_upper)
print(message_title)
print(message_lower)

user_language = 'Albert Einstein once said, “A person who never made a mistakenever tried anything new.”' 
print(user_language)

user_name = "  Albert Einstein  "
message = f'{user_name} once said, “A person who never made a mistakenever tried anything new.”'  
print(message+"/n/n")
message = user_name.rstrip()+"22"
print(message)
message = user_name.strip()+"22"
print(message)
message = user_name.lstrip()+"22"
print(message)