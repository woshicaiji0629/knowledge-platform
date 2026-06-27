## 前提条件
权限要求：使用 RAM 用户调用刷新预热 API（如cdn:RefreshObjectCaches、cdn:PushObjectCache）或操作控制台时，须授予cdn:RefreshObjectCaches（刷新）和cdn:PushObjectCache（预热）权限。建议遵循最小权限原则，仅授予业务所需的操作权限。详情请参见[CDN](../security-and-compliance/custom-policies-for-dcdn.md)[自定义权限策略参考](../security-and-compliance/custom-policies-for-dcdn.md)。
URL 格式：提交的 URL 中若包含非 ASCII 字符（如中文、空格等），必须先进行UTF-8百分号编码（Percent-encoding），否则刷新或预热任务可能无法生效。
示例：如https://www.example.com/文档/说明.pdf，须编码为https://www.example.com/%E6%96%87%E6%A1%A3/%E8%AF%B4%E6%98%8E.pdf。
