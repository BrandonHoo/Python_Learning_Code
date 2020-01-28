import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:    #需要自己去网站去申请API key
        print(news['title'])


if __name__ == '__main__':
    main()