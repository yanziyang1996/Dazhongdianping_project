# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class DazhongdianpingPipeline(object):
    def process_item(self, item, spider):
        data_file = open("C:\\Users\\kedaya\\Desktop\\dazhongdianping_data.txt", "a")  # 以追加的方式打开文件，\
        # 不存在则创建

        # 下面为保存item字典各项值
        item['name'] = u'  ' + item['name'].replace('\n', '').replace(' ', '')
        item['address'] = item['address'].replace('\n', '').replace(' ', '')
        item['tel'] = u'   ' + item['tel'].replace('[', '').replace("'", '')

        # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，
        # 将其编码改为utf-8
        item_string = str(item).decode("unicode_escape").encode('utf-8').replace("'", '').replace('u', '').\
            replace('{', '\n').replace('}', '\n').replace(',', '')
        # data_file.write('\n' + item_string + '\n')
        # data_file.write('\n')
        data_file.write(item_string)
        data_file.close()
        # print item_string  #在控制台输出
        return item
