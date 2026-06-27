## 常见问题
Q：运行DTS任务时出现报错信息DTS-RETRY-ERR-0069：Datasource rejected establishment of connection (.*)? Too many connections，如何解决？
A：可能原因：源端或目标端数据库的连接数过多。
解决方法：调整源端或目标端数据库的最大连接数，并重新启动任务。具体操作，请参见[修改最大连接数](modify-the-parameters-that-specify-the-maximum-number-of-connections-to-an-apsaradb-rds-for-mysql-instance.md)。
更多DTS报错信息及解决方法，请参见[常见报错](https://help.aliyun.com/zh/dts/support/common-errors-and-troubleshooting/)。
该文章对您有帮助吗？
反馈
