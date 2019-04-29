mongodb 记录

操作记录

```shell
# 插入单条数据
db.getCollection('example_data_1').insertOne([{"name":"张三", "age": 20, "address":"郑州" }])

# 批量插入数据
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

# 查询
# 样例：
# db.getCollection('example_data_1').find({查询条件}, {要展示的字段})

# 全查询
db.getCollection('example_data_1').find({})

# 按条件查询
# age 大于21,小于等于24 name 不等于 赵六
db.getCollection('example_data_1').find({"age" : { '$gt':21 , '$lte':24 }, "name" : {'$ne' : "赵六"} })

# 符号列表
$gt			大于
$gte		大于等于
$lt			小于
$lte		小于等于
$ne			不等于

# 按条件查询 -- find
# age 大于21,小于等于24 name 不等于 赵六， 只显示 name age 列
db.getCollection('example_data_1').find({"age" : { '$gt':21 , '$lte':24 }, "name" : {'$ne' : "赵六"} }, {'name':1, 'age':1, '_id':0})

# 统计满足结果数量 -- count()
db.getCollection('example_data_1').find({"age" : { '$gt':21 , '$lte':24 }, "name" : {'$ne' : "赵六"} }, {'name':1, 'age':1, '_id':0}).count()

# 限定返回结果 -- limit()
db.getCollection('example_data_1').find({}).limit(2)

# 对结果排序 -- sort()
# 按年龄排序
# sort('排序字段': 1/-1)   # 1:正序  -1:倒序
db.getCollection('example_data_1').find({}).sort({'age':1})

# 修改数据
# 修改单条数据 -- updateOne()
db.getCollection('example_data_1').updateOne({"sex":"男"}, {'$set':{"职位":"屠夫", "age":"99"}})

# 批量修改数据 -- updateMany()
db.getCollection('example_data_1').updateMany({"work":"厨师"}, {'$set':{"address":"屠宰场"}})

# 删除数据
# 删除单条数据 -- deleteOne()
db.getCollection('example_data_1').deleteOne({'age':20})

# 批量删除数据 -- deleteMany()
db.getCollection('example_data_1').deleteMany({'age':20})

# 数据去重 -- distinct()
db.getCollection('example_data_1').distinct({'age','name'})




```

