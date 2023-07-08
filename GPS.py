import urllib.parse
import requests
import datetime

main_api = "https://www.mapquestapi.com/directions/v2/route?"
hora_actual = datetime.datetime.now()

print("¡Bienvenido!", hora_actual)
while True:
    orig = input("Ubicacion De Inicio: ")
    if orig == "quit" or orig == "s":
        break
    dest = input("Ubicacion De Destino: ")
    if dest == "quit" or dest == "s":
        break

    key = "YJ2Rz9dD3878El9Q0mCSnhusvI053Zsa"
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get (url) .json ()
    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:       
        print("=============================================")
        print("Direccion de partida: " + (orig) + " / Direccion De Destino: " + (dest))
        print("Duracion del viaje: " + (json_data["route"]["formattedTime"]))
        print("Kilometros: " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        print ("Combustible usado (Ltr):" + str("{:.1f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("Hora Actual: ", hora_actual)
        print("=============================================")
        print("")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")