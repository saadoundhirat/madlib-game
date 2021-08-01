import re 
#  write your functions here 



print("""
** Hey There ... welcom to the madlib game you will asked to enter atext after each time you enter atext press enter to move to the next question, at the end of the game you will have the full test printed for you **
""") 
# thsi function will take apath of text file then return the text 
def read_template(path):
    with open(path , 'rt') as file_text:
        msg_text = file_text.read()
        try:
            return msg_text
        except FileNotFoundError:
            return 'the file you have enterd is not found'


def parse_template(text):
    """
    function takes atext with the place holder and then return the content inside the placeholders
    """
    matches = re.findall('({([^{}]+)})', text)
    # matches will return alist of tuples, each tuple has the place holder and the text inside the {} so i will return the full list
    # OUTPUT:
    # [('{Adjective}', 'Adjective'), ('{Adjective}', 'Adjective'), ('{A First Name}', 'A First Name'), ('{Past Tense Verb}', 'Past Tense Verb'), ('{A First Name}', 'A First Name'), ('{Adjective}', 'Adjective'), ('{Adjective}', 'Adjective'), ('{Plural Noun}', 'Plural Noun'), ('{Large Animal}', 'Large Animal'), ('{Small Animal}', 'Small Animal'), ("{A Girl's Name}", "A Girl's Name"), ('{Adjective}', 'Adjective'), ('{Plural Noun}', 'Plural Noun'), ('{Adjective}', 'Adjective'), ('{Plural Noun}', 'Plural Noun'), ('{Number 1-50}', 'Number 1-50'), ("{First Name's}", "First Name's"), ('{Number}', 'Number'), ('{Plural Noun}', 'Plural Noun'), ('{Number}', 'Number'), ('{Plural Noun}', 'Plural Noun')]

    # now i will loop through the list and get the text inside the {}
    names=[]
    for placeholder, name in matches:
    # placeholder , name[('{Adjective}', 'Adjective')]
        names.append(name)
    # to get the empty_text we will loop through the list and replace the {} with the user input
    empty_text = re.sub(r'({.+?})', '{}', text)
    return empty_text ,tuple(names)


def print_massages(names):
    """function takes an list loop through each element and let user enter the text"""
    user_answers=[]
    for name in names:
        print(f'Give me {name}')
        answer=input() 
        user_answers.append(answer)
    return user_answers

def merge(empty_text, user_answers):
    """fuction takes and list of answers and atext then append list elementss to the text"""
    full_text = empty_text.format(*user_answers)
    return full_text



if __name__ == '__main__':
    # print(read_template('../assets/madlib_game.txt'))
    text = read_template('../assets/madlib_game.txt')
    empty_text , names = parse_template(text)
    user_answers = print_massages(names)
    full_text = merge(empty_text , user_answers)
    print(full_text)