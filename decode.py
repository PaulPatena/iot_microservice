import json
import requests
test_data = {'coreid': u'2d002c001247353136383631', 'published_at': u'2018-02-21T13:51:08.137Z', 'data': u'{"w":{"a":[{"m":"e2:b9:e5:2b:a6:b0","s":-76,"c":1},{"m":"e0:b9:e5:2b:a6:af","s":-78,"c":1},{"m":"50:c7:bf:4d:b8:b3","s":-45,"c":8},{"m":"c8:d3:ff:57:2d:ff","s":-94,"c":6},{"m":"fa:8f:ca:93:4a:0f","s":-91,"c":6},{"m":"e0:b9:e5:1f:cb:23","s":-65,"c":11}]}}', 'event': u'locationEvt'}


def createGoogleReqObj(incoming):
    # print incoming
    data = incoming.get('data')

    # print data
    if data is None:
        return "error"

    # convert unicode string to json data
    json_data = json.loads(data)

    wifi = json_data.get('w')
    if wifi is None:
        return "error"

    # print wifi
    access_points = wifi.get('a')
    if access_points is None:
        return "error"

    print access_points

    # Google Format
    # {
    #     "considerIp": "false",
    #     "wifiAccessPoints": [
    #         {
    #             "macAddress": "00:25:9c:cf:1c:ac",
    #             "signalStrength": -43,
    #             "signalToNoiseRatio": 0
    #         },
    #         {
    #             "macAddress": "00:25:9c:cf:1c:ad",
    #             "signalStrength": -55,
    #             "signalToNoiseRatio": 0
    #         }
    #     ]
    # }

    payload = {
        "considerIp": "false",
        "wifiAccessPoints": []
    }

    for ap in access_points:
        signalStrength = ap.get('s')
        channel = ap.get('c')
        macAddress = ap.get('m')

        new_ap = {}
        if signalStrength:
            new_ap['signalStrength'] = signalStrength
        if channel:
            new_ap['channel'] = channel
        if macAddress:
            new_ap['macAddress'] = str(macAddress)

        # print new_ap
        payload['wifiAccessPoints'].append(new_ap)

    # print payload
    return payload


payload = createGoogleReqObj(test_data)
resp = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=',
                     params=payload)
print resp.json()



