### 查找并插入内容
在配置文件example.conf中，在Include conf.modules.d/*.conf行的下一行插入LoadModule rewrite_module modules/mod_rewrite.so。步骤如下：
运行vim example.conf命令打开文件，进入普通模式。
运行/Include conf.modules.d/*.conf找到目标行。
按键盘i进入插入模式。
输入LoadModule rewrite_module modules/mod_rewrite.so。
按键盘Esc键退出插入模式。
按:wq保存文件并退出。
