## Prompting and passing

from sys import argv

script, user_name = argv

prompt_symbol = ">"

print(f"Hi {user_name}, this is the {script} script.")
print("Lets have a Q n A !")
print(f"Do you like me {user_name} ?")
like = input(prompt_symbol)

print(f"Where do you live {user_name} ?")
location = input(prompt_symbol)

print("What kind of computer do you have ?")
computer = input(prompt_symbol)

print(f"""
You said {like} about your liking me. 
You live in {location}. 
And you have a {computer} computer. Awesome.
""")

