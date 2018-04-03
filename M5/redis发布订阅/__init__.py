Dict = {'oracle': {'password':'a123','Flag':0},'mysql': {'password':'123','Flag':1}}

def after_login():
    print('do someting after logged')
    exit()


def login(username,password):
    if username in Dict:
        tmp_dict = Dict[username]
        if password == tmp_dict['password']:
            print('%s login successful'%username)
            if tmp_dict['Flag'] == 1:
                print("account %s is  logged but it's locked,pls context the administrator"%username )
                return False
            else:
                return True

    else:
        return False


def lock_user(username):
    try:
        Dict[username]['Flag'] = 1
        print('%s is locked '%username)
    except Exception as e:
        print('%s not found lock user faild'%username)


def main():
    login_count = 0
    while True:
        username = input('Enter your name:')
        password = input('Enter your password:')
        print(login_count)
        result = login(username,password)
        if login_count == 3:
            lock_user(username)
            break
        if result == True:
            after_login()
        else:
            login_count +=1
            continue




if __name__ == '__main__':
    main()




