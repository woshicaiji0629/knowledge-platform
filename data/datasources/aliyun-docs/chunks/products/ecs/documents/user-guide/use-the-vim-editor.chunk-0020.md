### 删除内容
在配置文件example.conf中，将#Listen 12.34.XX:XX:80行首的#删除，并删除Listen 80。步骤如下：
运行vim example.conf命令打开文件，进入普通模式。
运行/#Listen 12.34.XX:XX:80找到目标，此时光标定位在#字符上。
按键盘x删除#。
光标移到Listen 80，按键盘dd删除该行。
输入:wq保存文件并退出。
