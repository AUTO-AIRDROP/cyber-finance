from  af09.aut import Token
from af09.help import Output, Ff
import json,time,sys
from af09.send_request import Api



output = Output()  
api = Api()
output.banner()

tokens = Token.aut_token_json()

def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

def daily(d):
    daily=api.post(
        url='https://api.cyberfin.xyz/api/v1/mining/claim/daily',
        data={},
        token=d['token']
    )
    
    if daily.status_code == 201 :
        d = daily.json()
        output.success(f"Daily {d['first_name']} KE-{d['message']} ")

def claim(d):
    daily=api.post(
        url='https://api.cyberfin.xyz/api/v1/mining/claim',
        data={},
        token=d['token']
    )
    
    if daily.status_code == 201 :
        d = daily.json()
        output.success(f"Claim Mining | MiningRate {d['miningData']['miningRate']}")

def buy_hammer(d):
    buy=api.post(
        url='https://api.cyberfin.xyz/api/v1/mining/boost/apply',
        data={"boostType":"HAMMER"},
        token=d['token'],
    )
    return buy

def buy_egg(d):
 
    buy=api.post(
        url='https://api.cyberfin.xyz/api/v1/mining/boost/apply',
        data={"boostType":"EGG"},
        token=d['token']
    )
 
    return buy

def task_ads(d):
    res_api=api.get(
        url=f'https://api.adsgram.ai/adv?blockId=789&tg_id={d["id"]}&tg_platform=ios&platform=Win32&language=en',
        data={},
        token=d["token"]
    )
    
    if(res_api.status_code==200):
        time.sleep(10)
        apilog=api.post(
            url=f'https://api.cyberfin.xyz/api/v1/ads/log',
            data={},
            token=d["token"]
        )
        if(apilog.status_code==201):
            output.success(f'### Task Video OK')
           
            task_ads(d)
        else:
            e=apilog.json()
            output.danger(f'Task Video {e["message"]}')

def get_all_task(DD):
    
    alltask=api.get(
        url='https://api.cyberfin.xyz/api/v1/gametask/all',
        data={},
        token=DD['token']
    )
    
    if(alltask.status_code==200):
        tasks=alltask.json()
        for i,d in enumerate(tasks['message']):
            if(d['isCompleted']==True):
                continue  
            res_apiClaim=api.patch(
                url    = f'https://api.cyberfin.xyz/api/v1/gametask/complete/{d["uuid"]}',
                data   = {},
                token  = DD["token"],
            )
            apiClaim=res_apiClaim.json()
            if res_apiClaim.status_code==200:
                if( apiClaim['message'] !="You have already completed the task"):
                    output.success(f'{i+1}.{d["description"]} Claimed !  | Point {apiClaim["message"]["pointsReward"]}')
                else:
                    output.warning(f'{i+1}.{d["description"]} already completed ')
            else:
                if(apiClaim['message']=="You have already completed the task"):
                    output.warning(f'{i+1}.{d["description"]} already completed ')
                else:
                    output.danger(f'{i+1}.{d["description"]} | {apiClaim["message"]}')
        
            
            time.sleep(10)
        
    else:
        print(api.text)

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

def main():
    config = load_config()
   
    while True:
        dataAuth = Token.get_auth_json()  
        for i,data in enumerate(dataAuth):
            
            ### PRINT USER
            output.warning('#--------------------------#')
            output.success(f"AF09>> USER KE-{i+1}  {data['first_name']}")
            
            ### GET INFO 
            boost=api.get(
                url='https://api.cyberfin.xyz/api/v1/mining/boost/info',
                data={},
                token=data['token']
            )
            res_boost=boost.json()
            
            ### META DATA
            metadata=api.get(
                url='https://api.cyberfin.xyz/api/v1/game/mining/gamedata',
                data={},
                token=data['token']
            )
            res_metadata=metadata.json()
            s_balance=res_metadata["message"]["userData"]["balance"]
            output.warning(f'Balance : {s_balance}')
            
            ### DAILY
            daily(data)
            claim(data)
            ### BUY HAMMER
            
            hammerLevel=res_boost['message']['hammerLevel']
            while (
                    (int(res_boost['message']['hammerPrice']) < int(config.get("hammerPrice"))) 
                    and
                    (int(res_boost['message']['hammerPrice']) < int(res_metadata['message']['userData']['balance']))
                ):
                
                res=buy_hammer(data)
                if res.status_code == 200 :
                    res = res.json()
                    hammerLevel+=1
                    output.success(f'UPGRADE HAMMER TO LEVEL {hammerLevel}')
                    time.sleep(31)
                    res_boost['message']['hammerLevel']=hammerLevel
                    res_metadata['message']['userData']['balance']=int(res['message']['userData']['balance'])
                else:
                    break
            output.warning(f'HAMMER LEVEL {res_boost["message"]["hammerLevel"]}')
            
            ### BUY EGG
            eggLevel=res_boost['message']['eggLevel']

            while (int(res_boost['message']['eggPrice']) < int(config.get("eggPrice")) 
                    and 
                    (int(res_boost['message']['eggPrice']) <= int(res_metadata['message']['userData']['balance']))
                ):
                res=buy_egg(data)
                if res.status_code == 200 :
                    res = res.json()
                    eggLevel += 1
                    output.success(f'UPGRADE EGG TO LEVEL {eggLevel}')
                    time.sleep(5)
                    res_boost['message']['eggLevel']=eggLevel
                    res_metadata['message']['userData']['balance'] = int(res['message']['userData']['balance'])
                else:
                    break

            output.warning(f'EGG LEVEL {res_boost["message"]["eggLevel"]}')
            
            #### TASK VIDEO
            task_ads(data)
            
            #### ALL TASK
            get_all_task(data) 
            output.success(f'New Balance : {res_metadata["message"]["userData"]["balance"]} ')
            countdown(config.get("countdown", 1000))
            output.danger('#--------------------------#')
  


if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Program dihentikan oleh pengguna (Ctrl+C)")
            break
        except Exception as e:
            print(f"Error tidak tertangani: {e}")
            continue
