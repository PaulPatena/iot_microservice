import json
test_data = {'coreid': u'2d002c001247353136383631', 'published_at': u'2018-02-21T13:51:08.137Z', 'data': u'{"w":{"a":[{"m":"e2:b9:e5:2b:a6:b0","s":-76,"c":1},{"m":"e0:b9:e5:2b:a6:af","s":-78,"c":1},{"m":"50:c7:bf:4d:b8:b3","s":-45,"c":8},{"m":"c8:d3:ff:57:2d:ff","s":-94,"c":6},{"m":"fa:8f:ca:93:4a:0f","s":-91,"c":6},{"m":"e0:b9:e5:1f:cb:23","s":-65,"c":11}]}}', 'event': u'locationEvt'}

def parse(incoming):
    # print incoming
    data = incoming.get('data')

    print data
    if data is None:
        return "error"

    # convert unicode string to json data
    json_data = json.loads(data)

    wifi = json_data.get('w')
    if wifi is None:
        return "error"

    print wifi

print parse(test_data)



