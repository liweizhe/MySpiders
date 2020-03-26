import scrapy
import re
from MySpiders.items import JobItem
from MySpiders.settings import HOST_HTTPS


class JobSpider(scrapy.Spider):
    name = 'job_spider'
    start_urls = [
        'https://www.xmrc.com.cn/net/info/showco.aspx?id=1188910',
        'https://www.xmrc.com.cn/net/info/showco.aspx?id=2461451'

    ]
    # with open('data/job.txt', 'r') as fi:
    #     for l in fi:
    #         start_urls.append(HOST_HTTPS + l.strip())

    def parse(self, response):
        item = JobItem()
        self.parse_job(response=response, item=item)
        self.parse_info(response=response, item=item)
        self.parse_res(response=response, item=item)
        # self.parse_email(response=response, item=item)
        # for k in item:
        #     print(item.get(k))
        yield item

    def parse_job(self, response, item):
        # //*[@id="ctl00_Body_Repeater1_ctl00_ctl02_Repeater1_ctl00_ctl03_ctl00_Tr1"]/td[2]
        # //*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr[5]/td[2]
        # //*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr[1]/td/font[1]/a/u
        name = response.xpath(
            '//*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr[1]/td/font[1]/a/u/text()'
        ).extract_first()
        item['name'] = '招聘职位： ' + name

        parsed_url = response.request.url
        pattern = re.compile(r'(?<=ID=)\d+\.?')
        id_str = pattern.findall(parsed_url)[0]
        item['id'] = int(id_str)

        table = response.xpath('//*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr')
        for row in table:
            raw_data = row.xpath('td/text()').extract()
            for data in raw_data:
                data = data.strip()
                if data:
                    if '招聘期限' in data:
                        item['time'] = data
                    elif '联\xa0系\xa0人' in data:
                        item['contact'] = data
                    elif '联系电话' in data:
                        item['Tel'] = data
                    elif '通信地址' in data:
                        item['address'] = data
                    else:
                        continue

    def parse_info(self, response, item):
        # //*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr[2]/td[2]/table/tr/td[1]
        table = response.xpath('//*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr/td/table/tr')
        for row in table:
            raw_data = row.xpath('td/text()').extract()
            # raw_data = row.xpath('td[2]').extract()
            if raw_data:

                for data in raw_data:
                    data = data.strip()
                    if data:
                        if '招聘单位' in data:
                            item['company'] = data
                        elif '学历要求' in data:
                            item['education'] = data
                        elif '职位性质' in data:
                            item['nature'] = data
                        elif '工作经验' in data:
                            item['experience'] = data
                        elif '年龄要求' in data:
                            item['age'] = data
                        elif '工作地点' in data:
                            item['location'] = data
                        elif '参考月薪' in data:
                            item['salary'] = data
                        elif '上班时间' in data:
                            item['schedule'] = data
                        elif '薪资福利' in data:
                            item['welfare'] = data
                        else:
                            continue

    def parse_res(self, response, item):
        # //*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr[10]
        # //*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr[10]/td[2]
        src = response.xpath('//*[@id="container"]/table[2]/tr/td[3]/table[4]/tr[1]/td[2]/table[1]/tr[10]/td[2]/text()'
                             ).extract()
        item['response_and_require'] = '职位职责和职位要求:\n'
        for s in src:
            s = s.strip()
            if s:
                item['response_and_require'] += s + '\n'


if __name__ == '__main__':
    import subprocess
    subprocess.call(['scrapy', 'crawl', 'job_spider'])
