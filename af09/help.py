import json
import requests,json,sys,time
from fake_useragent import UserAgent
from colorama import Fore, Style, init
from datetime import datetime


class Ff:
    @staticmethod
    def ll(js):
        print(json.dumps(js, indent=4))  

class Output:
    def __init__(self):
        # Inisialisasi Colorama
        init(autoreset=True)
    
    def get_current_time(self):
        return datetime.now().strftime("[%d/%m/%Y %H:%M]")  # Mengembalikan waktu saat ini

    def warning(self, message):
        print(f"{Fore.WHITE} {self.get_current_time()} {Fore.YELLOW} {message} {Style.RESET_ALL}")
        
    def success(self, message):
        print(f"{Fore.WHITE} {self.get_current_time()} {Fore.GREEN} {message} {Style.RESET_ALL}")
    
    def danger(self, message):
        print(f"{Fore.WHITE} {self.get_current_time()} {Fore.RED} {message} {Style.RESET_ALL}")
        
    def banner(self):
        banner=f"""
                {Fore.WHITE}
                @@@@@@   @@@@@@@@   @@@@@@@@     @@@@@@   
                @@@@@@@@  @@@@@@@@  @@@@@@@@@@  @@@@@@@@  
                @@!  @@@  @@!       @@!   @@@@  @@!  @@@  
                !@!  @!@  !@!       !@!  @!@!@  !@!  @!@  
                @!@!@!@!  @!!!:!    @!@ @! !@!  !!@!!@!!  
                !!!@!!!!  !!!!!:    !@!!!  !!!    !!@!!!  
                !!:  !!!  !!:       !!:!   !!!       !!!  
                :!:  !:!  :!:       :!:    !:!       !:!  
                ::   :::   ::       ::::::: ::  ::::: ::  
                :    : :   :        : : :  :    : :  : .
                                                        
                  {Fore.YELLOW} 🦋 https://t.me/AIRDORP_AUTOBOT 🦋
                bisa request bot jika garapan berpotensi
                {Style.RESET_ALL}
             """
        print(banner)