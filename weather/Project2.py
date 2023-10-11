import requests

LLAVE_API = "813fc7e9055288d66a66bce6e2f8ad39"
URL_BASE = "https://api.openweathermap.org/data/2.5/weather"


a=1
while(a!=0):
    
    ciudad = input("Dame el nombre de una ciudad: ")
    request_url =  f"{URL_BASE}?appid={LLAVE_API}&q={ciudad}"
    respuestapi = requests.get(request_url)

    if respuestapi.status_code == 200:
            datos = respuestapi.json()
            
            weather = datos['weather'][0]['description']
            temperature = datos['main']['temp']
            print("El clima en inglés es:",weather)
            temperature-=273.15
            temperature =  round(temperature, 2)
            print("La temperatura es:",temperature, "celcios")
            #salir

            
            sino = input("Si deseas salir, presiona ok, si no, enter: ")
            if sino == 'ok':
                 a = 0


    else:
            
            print("Ocurrió un error o no se encontró la ciudad"+"\n")
           
                 

