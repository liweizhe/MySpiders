import scrapy
from scrapy.http import Request


class XMRCSpider(scrapy.Spider):
    name = 'xmrc_spider'
    url = 'https://www.xmrc.com.cn/net/info/Resultg.aspx?a=a&g=g&recordtype=1&searchtype=1&releasetime=365' \
          '&worklengthflag=0&sortby=updatetime&ascdesc=Desc&PageIndex={}'
    # page = 1
    # page = 2316
    page = 2952
    start_urls = [
        url.format(page)
    ]
    job_set = set()
    company_set = set()

    def parse(self, response):
        try:
            table = response.xpath("//*[@id=\"ctl00$Body$JobRepeaterPro_main_div\"]/table[2]/tr")
            if not table or self.page > 3451:
                print(table)
                with open('job.txt', 'w') as f_job, open('company.txt', 'w') as f_company:
                    for s in self.job_set:
                        f_job.write(str(s) + '\n')
                    for s in self.company_set:
                        f_company.write(str(s) + '\n')
                yield None
                print('-' * 10, 'finished', '-' * 10)
                return
            for row in table:
                # //*[@id="ctl00$Body$JobRepeaterPro_main_div"]/table[2]/tbody/tr[3]/td[2]
                # //*[@id="ctl00$Body$JobRepeaterPro_main_div"]
                job_url = row.xpath("td[2]/a/@href").extract()
                company_url = row.xpath("td[3]/a/@href").extract()
                if not job_url or not company_url:
                    continue
                else:
                    job_url = job_url[0]
                    company_url = company_url[0]
                self.job_set.add(job_url)
                self.company_set.add(company_url)
                print(job_url, company_url, '\n')
            self.page += 1
            # if self.page > 3451:
            #     with open('job.txt', 'w') as f_job, open('company.txt', 'w') as f_company:
            #         for s in self.job_set:
            #             f_job.write(str(s) + '\n')
            #         for s in self.company_set:
            #             f_company.write(str(s) + '\n')
            #     yield None
            #     return
            # else:
            #     print(self.page, '\n')
            next_url = self.url.format(self.page)
            yield Request(url=next_url, callback=self.parse, dont_filter=True)
        except Exception as e:
            print(e)
            with open('job.txt', 'w') as f_job, open('company.txt', 'w') as f_company:
                for s in self.job_set:
                    f_job.write(str(s)+'\n')
                for s in self.company_set:
                    f_company.write(str(s)+'\n')


if __name__ == '__main__':
    import subprocess
    subprocess.call(['scrapy', 'crawl', 'xmrc_spider'])
