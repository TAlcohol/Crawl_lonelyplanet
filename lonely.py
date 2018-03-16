# -*- coding: utf-8 -*-
import requests
import json
import time

span = 10
end = 0


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
        ('resource', '/pois?filter[poi][poi_type][equals]=sights&filter[poi][place_id][has_ancestor]=361932&page[limit]={}&page[offset]={}&include=image-associations.from,containing-place'.format(span, end)),
    )

    response = requests.get('https://www.lonelyplanet.com/usa/chicago/attractions/a/poi-sig/361932',
                            headers=headers, params=params, cookies=cookies)

    content = json.loads(response.content)
    return content


def get_location_id(x):
    try:
        location_id = content['data'][x]['id']
    except:
        location_id = None
    finally:
        print 'location_id:', location_id


def get_priceString(x):
    try:
        priceString = content['data'][x]['priceString']
    except:
        priceString = None
    finally:
        print 'priceString:', priceString


def get_name(x):
    try:
        name = content['data'][x]['name']
    except:
        name = None
    finally:
        print 'name:', name


def get_review_essential(x):
    try:
        review_essential = content['data'][x]['review']['essential']
    except:
        review_essential = None
    finally:
        print 'review_essential:', review_essential


def get_review_extension(x):
    try:
        review_extension = content['data'][x]['review']['extension']
    except:
        review_extension = None
    finally:
        print 'review_extension:', review_extension


def get_subtypes(x):
    try:
        subtypes = content['data'][x]['subtypes']
    except:
        subtypes = None
    finally:
        print 'subtypes:', subtypes


def get_images(x):
    try:
        images = content['data'][x]['images'][0]['path']
    except:
        images = None
    finally:
        print 'images:', images


def get_street(x):
    try:
        street = content['data'][x]['address']['street']
    except:
        street = None
    finally:
        print 'street:', street


def get_hoursString(x):
    try:
        hoursString = content['data'][x]['hoursString']
    except:
        hoursString = None
    finally:
        print 'hoursString:', hoursString


def get_coordinates(x):
    try:
        coordinates = content['data'][x]['location']['coordinates']
    except:
        coordinates = None
    finally:
        print 'coordinates:', coordinates


def fetch_data(j):
    get_location_id(j)
    get_priceString(j)
    get_name(j)
    get_review_essential(j)
    get_review_extension(j)
    get_subtypes(j)
    get_images(j)
    get_street(j)
    get_hoursString(j)
    get_coordinates(j)
    print '\n'


if __name__ == "__main__":
    try:
        times = 1
        while times > 0:
            print "**Run times:", times
            print '\n'
            content = spider(span, end)
            if content['data'] == []:
                print "We done."
                break
            for j in range(span):
                fetch_data(j)
            times += 1
            end = times * span
            time.sleep(0.2)
    except Exception, Argument:
        print "something wrong:", Exception, Argument

# 待处理
# 1. 正则处理review字段
# 2. 考虑抓不到数据的报错输出 done
# 3. 考虑循环终结的报错 done
# 4. 输出和取数据写入函数 done
# 5. telephone、telephoneInfo等，选取哪个的问题
# 6. containingPlace等未添加的数据
# 7. 按照json来存储

# 递归取数据的函数
# def get_value(content, fields, default=None):
#     if len(fields) == 0:
#         return content
#     try:
#         return get_value(content[fields[0]], fields[1:], default=default)
#     except:
#         return default
