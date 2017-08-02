# -*- coding:utf-8 -*-
import scrapy
from Dazhongdianping.items import DazhongdianpingItem
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ShopSpider(scrapy.Spider):
    name = 'dazhongdianping_shop'
    allowed_domains = []
    start_urls = ['https://www.dianping.com/search/category/4/0/r1541']
    # start_urls = ['https://www.dianping.com/shop/27191608']

    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parse_next)  #  请求第一页

        for url_index in range(2, 51):
            url = response.url + 'p' + str(url_index)
            print '开始爬%d页' % url_index
            yield scrapy.Request(url, callback=self.parse_next)

        # print response.url
        # selector = Selector(response)
        # links = selector.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a/@href')
        # # print links
        #
        # for li in links:                                              #遍历此页所有商家
        #     l = str(li).split('/')
        #     url = 'https://www.dianping.com/shop/' + l[-1].replace("'", '').replace('>', '')
        #     print url
        #     yield scrapy.Request(url, callback=self.parse_shop)
        #     # print url

        # shop_items = response.xpath('//div[class="content-wrap/div[1]/div[1]"]').extract()
        # for shop_item in response.xpath('//div[class="content-wrap/div[1]/div[1]"]'):
        #     shop['name'] = shop_item.xpath('//*[@id="basic-info"]/h1[1]/text()').extract()[0]
        #     print shop_item, shop
        print(u'已经爬完了')

        # print(u'现在在这里')

    def parse_next(self, response):
        selector = Selector(response)
        links = selector.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a/@href')
        # print links

        for each in links:                                              #遍历此页所有商家
            shop_link = str(each).split('/')
            shop_url = 'https://www.dianping.com/shop/' + shop_link[-1].replace("'", '').replace('>', '')
            print shop_url
            yield scrapy.Request(shop_url, callback=self.parse_shop)

    def parse_shop(self, response):
        selector = Selector(response)
        shop = DazhongdianpingItem()
        shop['name'] = selector.xpath('//*[@id="basic-info"]/h1[1]/text()').extract()[0]
        shop['address'] = selector.xpath('//*[@id="basic-info"]/div[2]/span[2]/text()').extract()[0]
        shop['tel'] = selector.xpath('//*[@id="basic-info"]/p/span[2]/text()').extract()[0]
        print '店铺名是：%s\n'%shop['name'], '地址是：%s\n'%shop['address'], '电话是：%s\n'%shop['tel']
        yield shop



