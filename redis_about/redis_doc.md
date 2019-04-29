## Redis 操作记录

### 安装 Redis

```shell
brew install redis
```

### 启动 Redis-server

```shell
redis-server /usr/local/etc/redis.conf
```

### 测试 Redis-cli

```shell
redis-cli
127.0.0.1:6379> ping
PONG
```

### 字符串 创建/查询/修改

#### redsi 基本数据结构

* string
* ss

#### 使用 redis-cli 实现

```shell
# 创建 key
# set key value
127.0.0.1:6379> set give_me_a_world OK
OK
127.0.0.1:6379> set zhongwen中文 不建议
OK

# 查询 key
# keys *
# 不建议 key 设置为中文。 -- 会转换为 Unicode 码
127.0.0.1:6379> keys *
1) "zhongwen\xe4\xb8\xad\xe6"
2) "zhongwen\xe4\xb8\xad\xe6\x96\x87"
3) "give_me_a_world"

```

