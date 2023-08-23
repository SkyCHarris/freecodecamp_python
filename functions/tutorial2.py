# Building our Own Functions

# -Create a new function using the def keyword followed by optional parameters in parentheses
# -Indent the body of the function
# -Defines the function but DOES NOT execute the body of the function

def print_lyrics() :
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# Defines function, but doesn't use it

x = 5
print('Hello') #Prints

def print_lyrcis() :
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.") #No print, never runs because not invoked

print('Yo') #Prints
x = x + 2
print(x) #Prints

# Store and Reuse!

x = 5
print('Hello') #Prints

def print_lyrcis() :
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.") #Prints in order

print('Yo') #Prints
print_lyrics()
x = x + 2
print(x) #Prints

# Arguments

# -Arguments are values we pass into the function as its input when we call the function
# -Argumnets are used to direct the function to do different kinds of work when called at different times
# -Put argumnets in parentheses after the name of the function

big = max('Hello world') #'Hello world' is argument/parameter

def greet(lang) :
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    else :
        print('Hello')

        #greet('en')
    #Hello
        #greet('es')
    #Hola
        #greet('fr')
    #Bonjour

# Return Values

# -Getting back out of the function. Does two things: 1) Ends the invocation of the function 2) Allows specification of what you want as the residual value in an expression

def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')
#Hello Glenn
print(greet('es'), 'Sally')
#Hola Sally
print(greet('fr'), 'Michael')
#Bonjour Michael

# Argumnets, Parameters, and Results

def max(inp) :
    blah
    blah
    for x in y:
        blah
        blah
    return 'w'