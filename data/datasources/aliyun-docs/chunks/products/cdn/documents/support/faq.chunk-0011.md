### 问题原因
「重写访问URL」（host_redirect）功能要求 replacement 参数值必须以 / 或 http:// 开头。如果填写的值不包含前导 / 或不以 http:// 开头（例如仅填写 index.html），则格式校验不通过，配置提交失败。
