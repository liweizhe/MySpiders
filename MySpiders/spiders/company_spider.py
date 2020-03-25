import scrapy
import re
from MySpiders.items import CompanyItem
from MySpiders.settings import HOST_HTTPS


class CompanySpider(scrapy.Spider):
    name = 'company_spider'
    start_urls = [
        # 'https://www.xmrc.com.cn/net/info/showcojob.aspx?CompanyID=97165',
        # 'https://www.xmrc.com.cn/net/info/showco.aspx?CompanyID=925916',
        # 'https://www.xmrc.com.cn/net/info/showco.aspx?CompanyID=360868',
        # 'https://www.xmrc.com.cn/net/info/showcojob.aspx?CompanyID=72526'

    ]
    with open('data/company.txt', 'r') as fi:
        for l in fi:
            start_urls.append(HOST_HTTPS + l.strip())

    def parse(self, response):
        item = CompanyItem()
        self.parse_name(response=response, item=item)
        self.parse_info(response=response, item=item)
        self.parse_job(response=response, item=item)
        self.parse_email(response=response, item=item)
        self.parse_logo(response=response, item=item)
        # for k in item:
        #     print(item.get(k), '\n', '-' * 60)
        yield item

    def parse_info(self, response, item):
        table = response.xpath('//*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table/tr')
        item['info'] = ''
        for row in table:
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

    def parse_job(self, response, item):
        table = response.xpath('//*[@id="container"]/table[2]/tr/td[1]/table/tr[2]/td/div/table/tr')
        item['job'] = []
        for row in table:
            raw_data = row.xpath('td/a/@href').extract()
            if raw_data:
                pattern = re.compile(r'(?<=id=)\d+\.?')
                id_str = pattern.findall(raw_data[0])[0]
                item['job'].append(int(id_str))

    def parse_name(self, response, item):
        raw_data = response.xpath('//*[@id="logo_td2"]/text()').extract()
        item['name'] = raw_data[0].strip()
        parsed_url = response.request.url
        # print(parsed_url)
        pattern = re.compile(r'(?<=ID=)\d+\.?')
        id_str = pattern.findall(parsed_url)[0]
        item['id'] = int(id_str)

    def parse_email(self, response, item):
        src = response.xpath('//*/@src').extract()
        for s in src:
            if '/net/common/getJPEG.ashx' in s:
                item['email'] = s + '&flag=1'

    def parse_logo(self, response, item):
        src = response.xpath('//*/@src').extract()
        for s in src:
            if '/net/Common/GetCompanyLogo' in s:
                item['logo'] = s


if __name__ == '__main__':
    import subprocess
    subprocess.call(['scrapy', 'crawl', 'company_spider'])
