

def display(num):
    message=""
    
    if(num>2):
        if(num%5==0 and num%3==0):
            message="zoom"
        elif(num%3==0):
            message="zip"
        elif(num%5==0):
            message="zap"
    else:
        message="invalid"
    return message


message=display(15)
print(message)
