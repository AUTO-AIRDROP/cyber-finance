import requests,json,sys,time
from fake_useragent import UserAgent
from colorama import Fore, Style, init
from datetime import datetime

# Inisialisasi Colorama
init(autoreset=True)

def get_token():
    tokens_dan_id = []

    try:
        # Membaca file token.txt
        with open('token.txt', 'r') as file:
            for line in file.readlines():
                # Split by whitespace and ensure there are exactly two parts
                try:
                    token, user_tele_id = line.strip().split()
                    tokens_dan_id.append((token.strip(), user_tele_id.strip()))  # Append as a tuple
                except ValueError:
                    print(f"Format tidak benar di baris: '{line.strip()}'. Pastikan setiap baris memiliki format 'token user_tele_id'.")
    except FileNotFoundError:
        print("File token.txt tidak ditemukan.")

    return tokens_dan_id  # Return the list of tuples

def load_config():
    # Load the config.json file
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

def countdown(total_seconds):
    for remaining in range(total_seconds, 0, -1):
        # Menghitung jam, menit, dan detik tersisa
        hrs, mins, secs = remaining // 3600, (remaining % 3600) // 60, remaining % 60
        # Format string waktu
        timer = f"{hrs:02}:{mins:02}:{secs:02}"
        
        # Menampilkan timer tanpa berpindah baris
        sys.stdout.write('\r' + timer)  # Menggunakan '\r' untuk kembali ke awal baris
        sys.stdout.flush()  # Memastikan output ditampilkan
        time.sleep(1)  # Tunggu 1 detik

    print("\nCountdown selesai!")

def get_current_time():
    return datetime.now().strftime("[%d/%m/%Y %H:%M]")

def ll(js):
    print(json.dumps(js, indent=4))
    
def send_api(url,data,token,method):
    # Create an instance of UserAgent to generate fake user agents
    ua = UserAgent()

    url = url
    
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": ua.random,  # Use a random fake user-agent
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"android"',  # Optional: Customize the platform as needed
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://g.cyberfin.xyz/",
        "Referrer-Policy": "origin"
    }

    data = data
    if method =='post':
        response = requests.post(url, headers=headers, json=data)
    elif method =="get":
        response = requests.get(url, headers=headers, json=data)
    elif method =="patch":
        response = requests.patch(url, headers=headers, json=data)
        
    return response

def buy_hammer(token):
 
    buy=send_api(
        url='https://api.cyberfin.xyz/api/v1/mining/boost/apply',
        data={"boostType":"HAMMER"},
        token=token,
        method='post'
    )
 
    return buy
    
def buy_egg(token):
 
    buy=send_api(
        url='https://api.cyberfin.xyz/api/v1/mining/boost/apply',
        data={"boostType":"EGG"},
        token=token,
        method='post'
    )
 
    return buy

def task_ads(token,tele_id):
    api=send_api(
        url=f'https://api.adsgram.ai/adv?blockId=789&tg_id={tele_id}&tg_platform=ios&platform=Win32&language=en',
        data={},
        token=token,
        method='get'
    )
    
    if(api.status_code==200):
        time.sleep(10)
        apilog=send_api(
            url=f'https://api.cyberfin.xyz/api/v1/ads/log',
            data={},
            token=token,
            method='post'
        )
        if(apilog.status_code==201):
            print(f"{Fore.WHITE} {get_current_time()}  {Fore.GREEN}###.Task Video OK {Style.RESET_ALL}")
           
            task_ads(token,tele_id)
        else:
            e=apilog.json()
            print(f"{Fore.WHITE} {get_current_time()}  {Fore.RED}Task Video {e['message']} {Style.RESET_ALL}")

def get_task_adly(token_aldy):
    buy=send_api(
        url='https://api.adly.tech/api/v1/ad/feed/IJTsMeVeTbLZGURoP9nj',
        data={},
        token=token_aldy,
        method='post'
    )
    res_js=buy.json()
    return res_js

def get_all_task(token):
    
    api=send_api(
        url='https://api.cyberfin.xyz/api/v1/gametask/all',
        data={},
        token=token,
        method='get'
    )
    
    if(api.status_code==200):
        tasks=api.json()
   
        for i,d in enumerate(tasks['message']):
            
            apiClaim=send_api(
                url='https://api.cyberfin.xyz/api/v1/gametask/complete/4ad08253-18bf-4936-bf2e-f736f35a2f3e',
                data={},
                token=token,
                method='patch'
            )

            apiClaim=apiClaim.json()
            if api.status_code==200:
                if( apiClaim['message'] !="You have already completed the task"):
                    print(f"{Fore.WHITE} {get_current_time()}  {Fore.GREEN}{i+1}.{d['description']} Claimed ! {Style.RESET_ALL}")
                else:
                    print(f"{Fore.WHITE} {get_current_time()}  {i+1}.{d['description']}  |  {Fore.YELLOW} already completed {Style.RESET_ALL}")
            else:
                print(f"{Fore.WHITE} {get_current_time()}  {Fore.RED}{i+1}.{d['description']} {apiClaim['message']} {Style.RESET_ALL}")
        
            
            time.sleep(10)
        
    else:
        print(api.text)

def daily(token):
    daily=send_api(
        url='https://api.cyberfin.xyz/api/v1/mining/claim/daily',
        data={},
        token=token,
        method='post'
    )
    
    if daily.status_code == 201 :
        d = daily.json()
        print(f"{Fore.WHITE} { get_current_time()}  {Fore.GREEN} DAILY |  KE-{d['message']} {Style.RESET_ALL}")


def USER(index,token,user_tele_id):
    config = load_config()
    print('===========================================================================')
    print(f"{Fore.WHITE} { get_current_time()}  Account Ke-{index+1} {Style.RESET_ALL}")
    daily(token)
    ## GET INFO 
    boost=send_api(
        url='https://api.cyberfin.xyz/api/v1/mining/boost/info',
        data={},
        token=token,
        method='get'
    )
    res_js=boost.json()
    
    metadata=send_api(
        url='https://api.cyberfin.xyz/api/v1/game/mining/gamedata',
        data={},
        token=token,
        method='get'
    )
    res_metadata=metadata.json()
    
    ### BUY HAMMER
    hammerLevel=res_js['message']['hammerLevel']
 
    while ((int(res_js['message']['hammerPrice']) < int(config.get("hammerPrice"))) and (int(res_js['message']['hammerPrice']) < int(res_metadata['message']['userData']['balance']))):
        
        res=buy_hammer(token)
        if res.status_code == 200 :
            res = res.json()
            hammerLevel+=1
            print(f"{Fore.WHITE} {get_current_time()}  {Fore.GREEN}UPGRADE HAMMER TO LEVEL {hammerLevel}  {Style.RESET_ALL}")
            time.sleep(3)
            res_js['message']['hammerLevel']=hammerLevel
            
            res_metadata['message']['userData']['balance']=int(res['message']['userData']['balance'])
        else:
            break
    print(f"{Fore.WHITE} {get_current_time()}  {Fore.YELLOW}HAMMER LEVEL {res_js['message']['hammerLevel']}  {Style.RESET_ALL}")
    
    
    ### BUY EGG
    eggLevel=res_js['message']['eggLevel']

    while (int(res_js['message']['eggPrice']) < int(config.get("eggPrice")) and (int(res_js['message']['eggPrice']) <= int(res_metadata['message']['userData']['balance']))):
        res=buy_egg(token)
        if res.status_code == 200 :
            res = res.json()
            # Increment eggLevel
    
            eggLevel += 1
            
            print(f"{Fore.WHITE} {get_current_time()}  {Fore.GREEN}UPGRADE EGG TO LEVEL {eggLevel}  {Style.RESET_ALL}")
            time.sleep(5)
            res_js['message']['eggLevel']=eggLevel
            res_metadata['message']['userData']['balance'] = int(res['message']['userData']['balance'])
        else:
            break

    print(f"{Fore.WHITE} {get_current_time()}  {Fore.YELLOW}EGG LEVEL {res_js['message']['eggLevel']}  {Style.RESET_ALL}")
    
    #### TASK VIDEO
    task_ads(token,user_tele_id)
    
    ### ALL TASK
    get_all_task(token=token)
    
    
def main():
    config = load_config()
    try:
        while True:
            tokens_dan_id = get_token()  # Memanggil fungsi get_token untuk mengambil daftar token dan Telegram ID
            for i, (token, user_tele_id) in enumerate(tokens_dan_id):
                USER(i, token, user_tele_id)  # Pass both token and user_tele_id to the USER function
            countdown(config.get("countdown", 1000))
    except KeyboardInterrupt:
        print("\nBot By AF09")


if __name__ == "__main__":
    main()