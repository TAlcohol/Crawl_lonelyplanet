import json

span = 10


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
    # print "review_essential:", get_value(
    #     content, ['data', j, 'review', 'essential'])
    # print "review_extension:", get_value(
    #     content, ['data', j, 'review', 'extension'])
    # print "subtypes:", get_value(content, ['data', j, 'subtypes'])
    # print "images:", get_value(content, ['data', j, 'images', 0, 'path'])
    # print "street:", get_value(content, ['data', j, 'address', 'street'])
    # print "hoursString:", get_value(content, ['data', j, 'hoursString'])
    # print "coordinates:", get_value(
    #     content, ['data', j, 'location', 'coordinates'])
    print '\n'


if __name__ == "__main__":
    f = open('attractions.jsonl', 'r')
    try:
        for line in f:
            content = json.loads(line)
            span = len(content['data'])
            for j in range(span):
                fetch_data(j)
    except Exception, Argument:
        print "something wrong:", Exception, Argument
    f.close()
