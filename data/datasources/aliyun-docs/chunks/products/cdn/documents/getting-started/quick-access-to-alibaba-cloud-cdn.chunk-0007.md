## Windows系统
在系统内打开cmd命令界面，输入nslookup -type=TXT verification.example.com，根据当前的TXT结果，可以查看解析记录是否生效或正确。
命令执行后，返回示例如以下所示。
C:\Users\xxx> nslookup -type=TXT verification.xxx 服务器: UnKnown Address: fd00:1::1 DNS request timed out. timeout was 2 seconds. 非权威应答: verification.xxx text = "verify_0xxx...xxxff22"
