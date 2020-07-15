#users_password_info_dict : dictionary of dictionaries, every dictionary will have 2 attribures-> password, password_hash
#username would be the key of the dictionary

users_password_info_dict ={
    'nupur':{
        'password':'Password1', 
        'password_hash': 'xxyyyyxxx'},
    'shivi':{
        'password': 'Password2', 
        'password_hash': 'xxyyxxxx'},
    'shweta':{
        'password': 'Password3',
        'password_hash': None}
}

def _login(username, password):

    user_data =  _check_user_existance(username)
    if user_data is None:
        return "User doesn't exist!"
    else:
        #check hash column
        hash_password = _convert_to_hash(password)

        hash_value, stored_password = _check_hash_column(user_data)
               
        if hash_value is None and stored_password == password:
            _update_hash_column(username, hash_password)
            return 'Login Success'

        if hash_value == hash_password:
            return 'Login Success'
        else:
            return 'Wrong Password'
            
  def _check_user_existance(username):
    user_data = users_password_info_dict.get(username)
    return user_data
    
    
    def _convert_to_hash(password):

        from hashlib import sha256
        h = sha256()
    
    def hi(alist):
    i=0
    for element in alist:
        h.update(b'element')
        hash = h.hexdigest()
        print(hash)
        alist[i] = hash
        i = i+1
        
    hi(alist)
    print(alist)
return hashed_password, stored_password

def _check_hash_column(user_data):
    password = user_data.get('password')
    hash_password = user_data.get('password_hash')

    return hash_password, password


#----------------------------------------------------------------

def _check_password():
    pass

def _update_hash_column(username, hash_password):
    
    users_password_info_dict[username]['password_hash'] = hash_password
    

#-----------------------------------------------------------------------

