### pymongo



#### Pip install `pymongo`

```shell
pip install pymongo
```

#### test 

```python
import pymongo
```

#### Connect `mongo`

```python
from pymongo import MongoClient
client = MongoClient('mongo://username:password@hostname:port')   # 
client = MongoClient('mongo://hostname:port')
```

#### Connect `mongo` and `set`

##### Way:1

```python
from pymongo import MongoClient
client = MongoClient()

database = client.database
# database = client.chapter_3

collection = database.collectionName
# collection = database.example_data_1
```

##### Way:2

```python
from pymongo import MongoClient
client = MongoClient()

database = client[database]
# database = client['chapter_3']

collection = database[collectionName]
# collection = database['example_data_1']
```

##### Way:3 循环 链接多个库

```python
from pymongo import MongoClient
client = MongoClient()

db_list = ['develop_env_alipha','develop_env_beta','develop_env_preflight']
for each_db in db_list:
    database = client[each_db]
    collection = database.account
    collection.ipdateMany(...)
```

### `mongo` 命令 与 `pymongo` 命令对照表

| Mongodb cmd | Pymongo cmd |
| ----------- | ----------- |
| insertOne   | insert_one  |
| insertMany  | insert_many |
| find        | find        |
| updateOne   | update_one  |
| updateMany  | update_many |
| deleteOne   | delete_one  |
| deleteMany  | delete_many |

#### 演示

##### `mongo` 命令

```mongo
db.getCollection('example_data_1').insertMany([
{"name":"张三", "age": 20, "address":"郑州" },
{"name":"李四", "age": 21, "address":"天津" },
{"name":"王五", "age": 22, "address":"上海" },
{"name":"赵六", "age": 24, "address":"广州" },
{"name":"韩七", "age": 23, "address":"广东" },
{"name":"齐八", "age": 26, "address":"南宁" },
{"name":"数九", "age": 25, "address":"许昌" },
{"name":"冒失", "age": 29, "address":"湖南" },
])
```

##### `pymongo` 命令

```python
from pymongo import MongoClient
client = MongoClient()

database = client.chapter_3
collection = database.example_data_2    # 库不存在。自动创建

collection.insert_many([
{"name":"张三", "age": 20, "address":"郑州" },
{"name":"李四", "age": 21, "address":"天津" },
{"name":"王五", "age": 22, "address":"上海" },
{"name":"赵六", "age": 24, "address":"广州" },
{"name":"韩七", "age": 23, "address":"广东" },
{"name":"齐八", "age": 26, "address":"南宁" },
{"name":"数九", "age": 25, "address":"许昌" },
{"name":"冒失", "age": 29, "address":"湖南" },
])
```

### Insert to MongoDB

 将字典 {"name":"王小二", "age": 20, "address":"郑州" } 写入到 mongoDB

```python
from pymongo import MongoClient
client = MongoClient()

database = client.chapter_3
collection = database.example_data_2    # 库不存在。自动创建

collection.insert_one([
{"name":"王小二", "age": 20, "address":"郑州" }
])
```

### find from MongoDB

从 mongoDB 中 查询所有 21< age < 25 and name != "王五"

```python
from pymongo import MongoClient
client = MongoClient()

database = client.chapter_3
collection = database.example_data_2    # 库不存在。自动创建

rows = collection.find({'age':{'$lt':25, '$gt':21},'name':{'$ne':'王五'}})
for row in rows:
    print(row)
```

### update / delete from MongoDB

将 name = "王五" 的 age 改成 80 , address 改成中国

删除age = 0 的数据

```python
from pymongo import MongoClient
client = MongoClient()

database = client.chapter_3
collection = database.example_data_2    # 库不存在。自动创建

# 修改数据
collection.update_one(
    {'name':'王五'},
    {'$set':{'age':80, 'address':'中国'}}
)
collection.update_one(
    {'name':'匿名'},
    {'$set':{'age':0, 'address':'anymore'}},
    upsert = True     # 如果数据不存在报错， upsert = True 创建该条
)

# 删除数据
collection.delete_many(
    {"age":0}
)
```

### MongoDB 与 python 不通用的操作

1. 空值

   mongodb 空值 为 Null

   ```json
   db.getcollection('example_data_2').find({"grade":Null})
   ```

   python 空值 为 None

   ```python
   from pymongo import MongoClient
   collection = MongoClient.chapter_3.example_data_2
   rows = collection.find({"grade":None})
   
   for row in rows:
       print(row)
   ```

2. 布尔

   MongoDB中 真：true, 假：false

   ```json
   db.getcollection('example_data_2').find({"grade":true})
   ```

   python 中 真：True, 假：False

   ```python
   from pymongo import MongoClient
   collection = MongoClient.chapter_3.example_data_2
   rows = collection.find({"grade":True})
   
   for row in rows:
       print(row)
   ```

3. 排序操作

   MongoDB 排序 sort({})

   ```json
   db.getcollection('example_data_2').find({"grade":true}).sort({'age':-1})
   ```

   python 排序 sort()

   ```python
   from pymongo import MongoClient
   collection = MongoClient.chapter_3.example_data_2
   rows = collection.find({"grade":True}).sort('age', -1)
   
   for row in rows:
       print(row)
   ```

4. 查询_id

   MongoDB 查询 _id

   ```json
   db.getcollection('example_data_2').find({'_id':ObjectId("5cc2e08a861b6be6c1367133")})
   ```

   python 

   安装 pymongo 时，会自动安装 bson ObjectId 需要从bson 导入

   ```python
   from pymongo import MongoClient
   from bson import ObjectId
   collection = MongoClient.chapter_3.example_data_2
   
   collection.find({'_id':ObjectId("5cc2e08a861b6be6c1367133")})
   ```














































