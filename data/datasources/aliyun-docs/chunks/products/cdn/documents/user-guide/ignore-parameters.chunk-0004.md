## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名列表单击目标域名，在左侧导航栏，单击性能优化，进入性能优化配置页面。
单击忽略参数区域的修改配置，根据实际需求选择模式并完成配置。
配置完成后，单击确定保存。
重要
切换模式后，原有配置将被清除。
修改忽略参数配置后，边缘节点上已缓存的文件不会自动更新。必须通过控制台执行[URL 刷新](refresh-and-prefetch-resources.md)或[目录刷新](refresh-and-prefetch-resources.md)，才能使新配置生效并清除旧缓存。否则，用户可能仍会访问到使用旧缓存策略缓存的内容，导致访问异常。
