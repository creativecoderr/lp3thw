## Prompting people
age = int(input("What is your age? : "))

height = float(input("What is your age in cms? : "))

weight = float(input("What is your weight in kgs? : "))

height = height/100.0
weight = weight*1000

print(f"So you are {age} year old, {height}m tall weighing {weight}grams")
