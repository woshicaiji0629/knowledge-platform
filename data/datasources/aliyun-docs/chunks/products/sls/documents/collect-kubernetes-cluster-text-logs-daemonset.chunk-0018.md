## 通过黑名单控制采集范围
通过黑名单机制排除指定目录或文件，避免无关或敏感日志被上传。
配置步骤：在Logtail配置页面的输入配置>其他输入配置区域，启用采集黑名单，并单击添加。
支持完整匹配和通配符匹配目录和文件名，通配符只支持星号（*）和半角问号（?）。
文件路径黑名单：需要忽略的文件路径，示例：
/home/admin/private*.log：在采集时忽略/home/admin/目录下所有以private开头，以.log结尾的文件。
/home/admin/private*/*_inner.log：在采集时忽略/home/admin/目录下以private开头的目录内，以_inner.log结尾的文件。
文件黑名单：配置采集时需要忽略的文件名，示例：
app_inner.log：在采集时忽略所有名为app_inner.log的文件。
目录黑名单：目录路径不能以正斜线（/）结尾，示例：
/home/admin/dir1/：目录黑名单不会生效。
/home/admin/dir*：在采集时忽略/home/admin/目录下所有以dir开头的子目录下的文件。
/home/admin/*/dir：在采集时忽略/home/admin/目录下二级目录名为dir的子目录下的所有文件。例如/home/admin/a/dir目录下的文件被忽略，/home/admin/a/b/dir目录下的文件被采集。
