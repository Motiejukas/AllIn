import requests

url = "https://www.frankfurter.app"


def get_currencies():
    visa_info = requests.get(url+"/currencies").json().keys()
    return list(visa_info)


def gauti_data(suma, is_valiuta, i_valiuta):
    r = requests.get(url+f"/latest?amount={suma}&from={is_valiuta}&to={i_valiuta}").json()
    return f"{suma} {is_valiuta} = {r['rates'][i_valiuta]} {i_valiuta}"
