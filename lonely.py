# -*- coding: utf-8 -*-
import requests
import json
import time

span = 10
end = 0

request_url = raw_input("Input url: ")
splitter = "/"
url_num = request_url.split(splitter)[-1]
things_to_do = request_url.split(splitter)[-4]
city = request_url.split(splitter)[-5]

# request_url = 'https://www.lonelyplanet.com/usa/san-francisco/attractions/a/poi-sig/361858'
# url_num = '361896'
# things_to_do = 'attractions'


def spider(span, end):
    cookies = {
        'trctestcookie': 'ok',
        '_v': '_split-17-stable',
        'localeCookie': 'en_CN',
        'lpCurrency': 'USD',
        'lpUid': 'iNYSjSTyVfOYoF3fmFE3jnaGW3Uz5SDL',
        'destinations-next-cookie': 'true',
        '_ga': 'GA1.2.1680173646.1520602654',
        '_gaexp': 'GAX1.2.a06-i4tPSKO_SCCKouML4A.17675.1',
        'firstPoiSeen': 'true',
        '__gads': 'ID=e5af29739b5a91bc:T=1520605125:S=ALNI_MY4z0VddAFVUKOSyWBSZD0Z47wcpg',
        '_gid': 'GA1.2.1292466365.1520957607',
        '_ceg.s': 'p5jeef',
        '_ceg.u': 'p5jeef',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Referer': 'https://www.lonelyplanet.com/usa/chicago/attractions/a/poi-sig/361932',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    params = (
        ('resource', '/pois?filter[poi][poi_type][equals]={}&filter[poi][place_id][has_ancestor]={}&page[limit]={}&page[offset]={}&include=image-associations.from,containing-place'.format(
            things_to_do, url_num, span, end)),
    )

    response = requests.get(request_url,
                            headers=headers, params=params, cookies=cookies)

    content = json.loads(response.content)
    return content


def get_value(content, fields, default=None):
    if len(fields) == 0:
        return content
    try:
        return get_value(content[fields[0]], fields[1:], default=default)
    except:
        return default


def fetch_data(j):
    print "location_id:", get_value(content, ['data', j, 'id'])
    print "priceString:", get_value(content, ['data', j, 'priceString'])
    print "name:", get_value(content, ['data', j, 'name'])
    print "review_essential:", get_value(
        content, ['data', j, 'review', 'essential'])
    print "review_extension:", get_value(
        content, ['data', j, 'review', 'extension'])
    print "subtypes:", get_value(content, ['data', j, 'subtypes'])
    print "images:", get_value(content, ['data', j, 'images', 0, 'path'])
    print "street:", get_value(content, ['data', j, 'address', 'street'])
    print "hoursString:", get_value(content, ['data', j, 'hoursString'])
    print "coordinates:", get_value(
        content, ['data', j, 'location', 'coordinates'])
    print '\n'


if __name__ == "__main__":
    f = open('{}.jsonl'.format(things_to_do), 'a+')
    try:
        times = 1
        while times > 0:
            print "**Run times:", times
            print '\n'
            content = spider(span, end)
            if content['data'] == []:
                print "We done."
                break
            # for j in range(span):
            #     fetch_data(j)
            f.write(json.dumps(content))
            f.write('\n')
            end = times * span
            times += 1
            time.sleep(0.4)
    except Exception, Argument:
        print "something wrong:", Exception, Argument
    f.close()
