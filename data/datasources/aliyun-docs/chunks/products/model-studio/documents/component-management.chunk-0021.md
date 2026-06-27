### 4.4 业务空间（workspace）管理
阿里云百炼提供了 workspace 业务空间管理功能。开发者可以在控制台创建多个业务空间，这些空间彼此之间是完全隔离的，通过workspace id进行标识。Assistant API 的所有操作都支持传入workspace参数，以区分不同业务空间的业务。
4.4.1 概念简介
多租户隔离：不同 workspace 之间的Assistant、Thread、Message、Run等记录互不影响；
数据安全与可管理性：可以独立地进行删除、归档、访问权限控制；
权限与计费：可在控制台对每个 workspace 的访问进行单独管理，也能更方便地统计和计费。
4.4.2 如何使用workspace参数
所有主要操作（如Assistants.create、Threads.retrieve、Runs.list等）都可以接受可选的workspace参数，用来指定目标业务空间。若不传，则默认使用“默认工作空间”或当前 Key 绑定的空间。
