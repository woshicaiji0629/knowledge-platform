## SDK
以下代码以PutObject、GetObject和DeleteObject为例，用于指定第三方付费访问Object。其他用于指定第三方付费的Object读写操作接口设置方法类似。
第三方操作Object时需在HTTP Header中携带x-oss-request-payer:requester参数，否则会报错。
