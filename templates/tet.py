import http.client

conn = http.client.HTTPSConnection("car-stockpile.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "95be90da72msh372158cb79aa004p11dc8ejsna2bcf78344a1",
    'x-rapidapi-host': "car-stockpile.p.rapidapi.com"
    }

conn.request("GET", "/trim-specification?make=Audi&model=RS4%20Avant&year=2019&trim=2.9%20TFSI%20quattro", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))