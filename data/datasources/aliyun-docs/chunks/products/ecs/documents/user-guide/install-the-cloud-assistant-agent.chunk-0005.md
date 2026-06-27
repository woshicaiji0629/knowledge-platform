### Windows实例
步骤一：检查是否已安装云助手Agent
[使用远程桌面/Windows App](connect-to-a-windows-instance-by-using-a-username-and-password.md)[远程连接](connect-to-a-windows-instance-by-using-a-username-and-password.md)[Windows](connect-to-a-windows-instance-by-using-a-username-and-password.md)[实例](connect-to-a-windows-instance-by-using-a-username-and-password.md)。
查看云助手服务状态。
单击开始菜单，搜索计算机管理。
选择服务和应用程序>服务。
查找Aliyun Assist Service，若不存在，表示未安装。
步骤二：下载并安装云助手Agent方法一：通过浏览器下载云助手Agent
下载云助手Agent。
将地址中的{regionId}替换为实例所在[地域](regions-and-zones.md)[ID](regions-and-zones.md)后，在浏览器中打开。
https://aliyun-client-assist-{regionId}.oss-{regionId}-internal.aliyuncs.com/windows/aliyun_agent_latest_setup.exe # 示例：杭州（cn-hangzhou）下载地址 https://aliyun-client-assist-cn-hangzhou.oss-cn-hangzhou-internal.aliyuncs.com/windows/aliyun_agent_latest_setup.exe
安装云助手Agent。
双击云助手Agent文件，根据安装向导完成安装。默认安装路径为C:\ProgramData\aliyun\assist\。
方法二：通过PowerShell安装并启动云助手Agent
将脚本中的{regionId}替换为实例所在[地域](regions-and-zones.md)[ID](regions-and-zones.md)后，在PowerShell中执行。
curl -UseBasicParsing -Uri https://aliyun-client-assist-{regionId}.oss-{regionId}-internal.aliyuncs.com/windows/aliyun_agent_latest_setup.exe -OutFile 'C:\aliyun_agent_latest_setup.exe' & "C:\a
