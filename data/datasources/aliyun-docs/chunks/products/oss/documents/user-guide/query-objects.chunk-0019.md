### 使用命令行工具ossutil
您可以使用命令行工具ossutil来查询文件，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下命令用于为存储空间examplebucket中的exampleobject执行SQL语句，请求语法 CSV。
ossutil api select-object --bucket examplebucket --key exampleobject --select-request "{\"Expression\":\"c2VsZWN0IFllYXIsU3RhdGVBYmJyLCBDaXR5TmFtZSwgU2hvcnRfUXVlc3Rpb25fVGV4dCBmcm9tIG9zc29iamVjdA==\",\"InputSerialization\":{\"CSV\":{\"FileHeaderInfo\":\"Use\",\"Range\":\"line-range=0-100\"}},\"OutputSerialization\":{\"JSON\":{\"RecordDelimiter\":\",\"}}}"
关于该命令的更多信息，请参见[select-object](../developer-reference/select-object.md)。
