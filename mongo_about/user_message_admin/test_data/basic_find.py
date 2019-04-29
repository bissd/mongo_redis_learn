#-*- coding:utf-8 -*-

"""
# __author__ = 'hitler'
# time : '2019/4/28 5:18 PM'

#info:


"""
from pymongo import MongoClient
import json

class DataBaseManager(object):
    def __init__(self):
        """
        初始化 MongoDB 链接， 登录 MongoDB.chapter_4.people_info
        """
        client = MongoClient()
        database = client.chapter_4
        self.handler = database.people_info

    def query_info(self):
        """
        你需要在这里实现这个方法,
        查询集合people_info并返回所有"deleted"字段为0的数据。
        注意返回的信息需要去掉_id
        
        :return: 
        """


        info_list = list(self.handler.find({'deleted':0}, {'_id':0}))
        return info_list

        # return [
        #     {'id':1, 'name':'测试1', 'age': 18, 'birthday':'2000-01-01',
        #      'origin_home':'测试1', 'current_home':'测试1'},
        #     {'id':2, 'name':'测试2', 'age': 18, 'birthday':'2000-01-01',
        #      'origin_home':'测试2', 'current_home':'测试2'},
        #     {'id':3, 'name':'测试3', 'age': 18, 'birthday':'2000-01-01',
        #      'origin_home':'测试3', 'current_home':'测试3'},
        # ]


    def _query_last_id(self):
        """
        你需要实现这个方法，查询当前已有数据里面最新的id是多少
        返回一个数字，如果集合里面至少有一条数据，那么就返回最新数据的id，
        如果集合里面没有数据，那么就返回0
        提示：id不重复，每次加1
        
        :return: 最新ID
        """

        last_info = self.handler.find({}, {'_id': 0, 'id': 1}).sort('id', -1).limit(1)
        return last_info[0]['id'] if last_info else 0

    def add_info(self,para_dict):
        """
        你需要实现这个方法，添加人员信息。
        你可以假设 para_dict 已经是格式化好的数据了，
        你直接把它插入MongoDB即可，不需要做有效性判断。
        在实现这个方法时，你需要首先查询MongoDB，获取已有数据里面最新的ID是多少，
        这个新增的人员的ID需要在已有的ID基础上加1.
        
        :param para_dict: 
        格式为
        {'name':'xx','age': 12,'birthday':'2000-01-01','origin_home': 'xx','current_home': 'yy','deleted': 0}
        :return: True或者False
        """

        last_id = self._query_last_id()
        this_id = last_id + 1
        para_dict['id'] = this_id
        try:
            self.handler.insert_one(para_dict)
        except Exception as e:
            print(f'数据插入失败，报错信息如下：{para_dict} --  {e}')
            return False
        return True

    def update_info(self, people_id, para_dict):
        """
        你需要实现这个方法。这个方法用来更新人员信息。
        更新信息是根据people_id来查找的，因此people_id是必需的。
        
        :param people_id:  人员id， int
        :param para_dict:  格式为
        {'name':'xx','age': 12,'birthday':'2000-01-01','origin_home': 'xx','current_home': 'yy',}
        :return:  True or False
        """
        try:
            print(para_dict)
            y = self.handler.update_one({'id':people_id}, {'$set': para_dict})
            print(y)
        except Exception as e:
            print(f'数据更新失败，报错信息如下：{para_dict} -- {e}')
            return False

        return True

    def del_info(self, people_id):
        """
        你需要实现这个方法。请注意，此处需要使用"假删除"，
        把删除操作写为更新"deleted"字段的值为1

        :param people_id:  人员id
        :return: True or False
        """

        print(people_id)
        return self.update_info(people_id,{'deleted':1})

if __name__ == '__main__':
    database_manager = DataBaseManager()