import requests

def query(lat, lon):
    # API: https://nominatim.org/release-docs/develop/api/Reverse/#language-of-results
    api_url = "https://nominatim.openstreetmap.org:443/reverse?lat=%f&lon=%f&format=json&addressdetails=1" % (lat, lon)
    api_headers = {"User-Agent": "geoapiExercises"}
    response = requests.get(api_url, headers=api_headers)
    return response.json()["address"]

if __name__ == '__main__':
    adderss = query(37.548, -121.988)
    print(adderss["city"])
    print(adderss["state"])

    # "address": {
    #     "amenity": "Valero",
    #     "house_number": "4004",
    #     "road": "Mowry Avenue",
    #     "suburb": "Centerville District",
    #     "city": "Fremont",
    #     "county": "Alameda County",
    #     "state": "California",
    #     "postcode": "94536",
    #     "country": "United States",
    #     "country_code": "us"
    # },
