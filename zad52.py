list = ['Pete', 'Paul', 'Mary']

def list(data):
    del data[1]
    data[1] = 'Jane'
    return data
print(list(list)) 

# the code is erroneous