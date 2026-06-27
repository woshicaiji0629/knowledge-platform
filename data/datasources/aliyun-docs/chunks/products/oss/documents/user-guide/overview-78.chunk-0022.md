## 恢复版本
使用OSS控制台
在开启版本控制的Bucket中删除Object时，历史版本Object不会被真正删除，而是产生一个删除标记来标识Object的当前版本是删除状态。此时您可以在控制台恢复版本。
单击Bucket 列表，然后单击目标Bucket名称。
选择文件管理>文件列表。
单击历史版本右侧的显示。
选中待恢复文件，然后单击页面下方的恢复。
在弹出的对话框，单击确定。
使用命令行工具ossutil
您可以使用命令行工具ossutil来恢复已删除文件的历史版本，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下命令用于对存储空间examplebucket里的example.txt对象恢复到版本号为123的状态。
ossutil revert oss://examplebucket/example.txt 123
关于该命令的更多信息，请参见[revert（恢复版本）](../developer-reference/revert-recovery-version.md)。
