import os,json
import urllib.parse
from .send_request import Api  
from .help import  Ff as f
from .help import Output
class Token:
    
    def __init__(self):
        self.oo =  Output()
        self.token = None  # Inisialisasi self.token
        self.query = None
        self.api = Api()  # Membuat instance dari Api
    
    def inisiasi_token_app(self):
        response = self.api.post(  
            url='https://api.cyberfin.xyz/api/v1/game/initdata',
            token=self.query,
            data={"initData":self.query}  
        )
        if response.status_code == 201 :
            return response.json()['message']['accessToken']
        else:
            print("ERROR PENGAMBAILAN TOKEN ")    
            exit()
 
    def decode(self):  # Menerima query sebagai argumen
        params = self.query.split('&')
     
        # Membuat dictionary untuk menyimpan data
        data = {}
        
        # Decode setiap parameter
        for param in params:
            key, value = param.split('=', 1)  # Pisahkan key dan value
            decoded_value = urllib.parse.unquote(value)  # Decode value
            
            # Jika key adalah 'user', kita perlu mengonversi JSON ke dictionary
            if key == 'user':
                decoded_value = json.loads(decoded_value)  # Konversi ke dictionary
            data[key] = decoded_value  # Masukkan ke dalam dictionary 
        return data
        
    def olah_query(self): 
        querys = []
        query_file_path = os.path.join(os.path.dirname(__file__), '..', 'query.txt')
        auth_file_path = os.path.join(os.path.dirname(__file__), '..', 'af09/auth.json') 
 
        try:
            self.oo.warning("#--------------------------#")
            with open(query_file_path, 'r') as file:
                for line in file.readlines():
                    query = line.strip()  
                    if query:  
                        self.query = query  
                        ### GET TOKEN 
                        token=self.inisiasi_token_app()   
                        u=self.decode()
                        d = {
                            "query"     : query.strip(),
                            "token"     : token,
                            "id"        : u['user']['id'],
                            "first_name": u['user']['first_name']
                            }  # 
                        querys.append(d)   
                        self.oo.success(f"Inisiasi Token Baru {u['user']['first_name']}")
        except FileNotFoundError:
            print("File query.txt tidak ditemukan.")
        try:
            with open(auth_file_path, 'w') as auth_file:  # Menggunakan mode 'w' untuk mengganti isi
                json.dump(querys, auth_file, indent=4)
        except Exception as e:
            print(f"Terjadi kesalahan saat menyimpan file: {e}")
        
    @staticmethod
    def aut_token_json():
        token_instance = Token() 
        token_instance.olah_query()   

    def get_auth_json():
        with open(os.path.join(os.path.dirname(__file__), '..', 'af09/auth.json') , 'r') as file:
            # Membaca dan memuat konten JSON
            data = json.load(file)
            return data