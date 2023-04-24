#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

# with loop

def generate_evens():
    num_list = []
    for num in range(1,50):
        if num %2 ==0:
           num_list.append(num)
    return(num_list)

print(generate_evens())


# with list comprehension
def generate_evens():
    return [num for num in range(1,50) if num%2 == 0]
print(generate_evens())

##########################################################################

def yell(word):
    return f"{word.upper()}!"

print(yell("go away"))
print(yell("leave me alone"))


#############################################################################

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count
print(count_dollar_signs("$$Andreja$$$$"))

###############################################################################



def speak(animal="dog"):
    noises = { "dog": "woof","pig": "oink","duck": "quack","cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"
print(speak("cat"))