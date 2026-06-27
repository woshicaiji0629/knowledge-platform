## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中，单击参数设置。
在参数列表中找到#no_loose_disabled-commands参数，单击其操作列的修改。
在弹出的对话框中填写需禁用的命令。
重要
命令以小写字母的形式填写，通过英文逗号（,）分隔多个命令，例如keys,flushdb。
禁用命令后会同时禁用下级子命令，例如禁用script命令后会同时禁用SCRIPT EXISTS、SCRIPT LOAD等命令。但不支持单独禁用子命令。
单击确定。
