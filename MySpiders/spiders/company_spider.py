# from scrapy_redis.spiders import RedisSpider
# from scrapy.http import Request
#
#
# class CompanySpider(RedisSpider):
#     name = 'company_spider'
#     redis_key = 'spiders:company'
#     redis_encoding = 'utf-8'
#     base_url = 'https://www.xmrc.com.cn/'
#
#     def make_requests_from_url(self, url):
#         url = self.base_url + url
#         return Request(url=url, dont_filter=False)

import scrapy
from MySpiders.items import CompanyItem
# from ..items import CompanyItem


class CompanySpider(scrapy.Spider):
    name = 'company_spider'
    start_urls = [
        # 'https://www.xmrc.com.cn/net/info/showcojob.aspx?CompanyID=97165',
        # 'https://www.xmrc.com.cn/net/info/showco.aspx?CompanyID=925916',
        'https://www.xmrc.com.cn/net/info/showco.aspx?CompanyID=360868',
        # 'https://www.xmrc.com.cn/net/info/showcojob.aspx?CompanyID=72526'

    ]

    def parse(self, response):
        table = response.xpath('//*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table/tr')
        item = CompanyItem()

        src = response.xpath('//*/@src').extract()
        for s in src:
            if '/net/Common/GetCompanyLogo' in s:
                item['logo'] = s
            elif '/net/common/getJPEG.ashx' in s:
                item['email'] = s + '&flag=1'
            else:
                continue
        item['info'] = ''
        for row in table:
            # //*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table/tr
            # //*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table/tr[9]/td[2]
            # //*[@id="ctl00_Body_Repeater1_ctl00_CompanyIntro1_Repeater1_ctl00_Tr6"]/td[2]
            # print(row.xpath('td').extract(), '\n', '-' * 60, '\n')
            raw_data = row.xpath('td[2]/text()').extract()
            # raw_data = row.xpath('td[2]').extract()
            if raw_data:

                for data in raw_data:
                    data = data.strip()
                    if data:
                        if '联 系 人' in data:
                            item['contact'] = data
                        elif '联系电话' in data:
                            item['Tel'] = data
                        elif '联系地址' in data:
                            item['address'] = data
                        elif '公司性质' in data:
                            item['nature'] = data
                        elif '公司规模' in data:
                            item['scale'] = data
                        elif '公司行业' in data:
                            item['industry'] = data
                        else:
                            item['info'] += '{}\n'.format(data)
                        # print(data, '\n', '-' * 60)
        # for k in item:
        #     print(k, item.get(k), '\n')
        # print(item.get('email'))
        # print(item.get('logo'))
        # //*[@id="container"]/table[2]/tr/td[1]/table/tr[2]/td/div/table/tr[7]/td/a/u
        # //*[@id="container"]/table[2]/tr/td[1]/table/tr[2]/td/div/table/tr[7]/td
        # //*[@id="container"]/table[2]/tr/td[1]/table/tr[2]/td/div/table/
        # //*[@id="container"]/table[2]/tr/td[1]/table/tr[2]/td/div/table/tr[2]/td/a
        # //*[@id="container"]/table[2]/tr/td[1]/table/tr[2]/td/div/table/tr[22]/td/a/u
        table = response.xpath('//*[@id="container"]/table[2]/tr/td[1]/table/tr[2]/td/div/table/tr')
        item['job'] = []
        for row in table:
            # raw_data = row.xpath('td').extract()
            raw_data = row.xpath('td/a/@href').extract()
            if raw_data:
                # print(raw_data, '\n', '-' * 60)
                item['job'].append(raw_data[0])
        print(item.get('job'))
        print('**' * 50, '\n')


if __name__ == '__main__':
    import subprocess
    subprocess.call(['scrapy', 'crawl', 'company_spider'])
