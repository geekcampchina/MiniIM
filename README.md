# Mini IM Protocol

迷你聊天应用协议

## Python版

### 安装依赖

`pip install -r python/requirements.txt`

### 运行服务端

`python python/server.py`

#### 查看参数

`python python/server.py -h`

屏幕输出：

    usage: mini_im_server -H|-P|-l|-v

    迷你IM服务端
    
    options:
      -h, --help            show this help message and exit
      -H HOST, --host HOST  （可选）服务端地址，默认值：localhost
      -P PORT, --port PORT  （可选）服务端端口，默认值：9999
      -l {0,1,2,3,4,5}, --log-level {0,1,2,3,4,5}
                            （可选）日志级别，0（CRITICAL）|1（ERROR）|2（WARNING）|3（INFO）|4（DEBUG）|5（TRACE），默认值：3
      -v, --version         显示版本信息


### 运行客户端

`python python/client.py -m 'test message'`

屏幕输出：

    2023-06-17 16:09:29 3841 [INFO] Sent:     test message
    2023-06-17 16:09:29 3841 [INFO] Received: TEST MESSAGE

#### 查看参数

`python python/client.py -h`

屏幕输出：

    usage: mini_im_client -H|-P|-l|-m|-v
    
    迷你IM客户端
    
    options:
      -h, --help            show this help message and exit
      -H HOST, --host HOST  （可选）服务端地址，默认值：localhost
      -P PORT, --port PORT  （可选）服务端端口，默认值：9999
      -m MESSAGE, --message MESSAGE
                            （必选）消息
      -l {0,1,2,3,4,5}, --log-level {0,1,2,3,4,5}
                            （可选）日志级别，0（CRITICAL）|1（ERROR）|2（WARNING）|3（INFO）|4（DEBUG）|5（TRACE），默认值：3
      -v, --version         显示版本信息

## Java版

## Rust版

## Cpp版
