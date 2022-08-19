from data import show_questions

if __name__ == __name__:
    
    exit = ''
    while exit != 'x':
        show_questions()
        print('press "X" to exit, other key to continue')
        exit = input().strip().lower()