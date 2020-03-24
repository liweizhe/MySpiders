from MySpiders.settings import USER_AGENT_LIST
import random


class MockHeaders(object):

    def get_headers(self, host='www.baidu.com'):
        # ip = str(random.choice(list(range(255)))) + '.' + str(random.choice(list(range(255)))) + '.' + str(
        #     random.choice(list(range(255)))) + '.' + str(random.choice(list(range(255))))
        headers = {
            # 'Host': host,
            'User-Agent': random.choice(USER_AGENT_LIST),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            'Content-Length': '0',
            "Connection": "keep-alive",
            "Referer": "https://" + host + "/",

        }
        return headers

