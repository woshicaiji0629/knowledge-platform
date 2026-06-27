## 常见问题
Q：为什么大Key（子元素数量）中会显示String类型Key？
A：在Redis开源版和部分早期Tair版本中会显示String类型长度大于阈值（默认为2000）的Key。
Q：为什么元素很少（如10个以内）的Key也显示为大Key？
A：有以下两种可能原因。
Key的name占用大，可使用memory usage key_name命令查看。
实例小版本过低，小版本低于5.2.7的实例bigkey-threshold（大Key统计阈值）默认值为0，导致内存占用小的Key也展示了出来，建议[升级小版本](update-the-minor-version.md)到最新。
