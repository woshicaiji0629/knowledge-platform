# 示例代码仅供参考，请勿直接在生产环境中使用 retrieved_assistant = Assistants.retrieve( assistant_id="AID_XXX", workspace="WSID123" ) Assistants.delete( assistant_id="AID_XXX", workspace="WSID123" )4.4.3 典型使用场景
多租户 SaaS 平台：为每个企业客户分配独立 workspace，数据相互隔离；
跨业务线管理：不同部门或项目分别使用独立 workspace，方便各自管理配置与统计；
开发 / 测试 / 生产环境分离：在控制台中创建 dev、test、prod 等 workspace，将不同环境的数据分离管理，避免相互干扰。
4.4.4 注意要点
API Key 与 workspace：需要在控制台配置相应的访问权限；
对象 id 的查找范围：检索某对象时，必须在对应的 workspace 下检索；
删除操作：只能删除该 workspace 中的对象，不会影响其他 workspace 的数据。
通过将工作空间与多用户场景结合使用，开发者能够轻松地搭建起多租户、跨业务线或者多环境的对话系统，既保证了隔离性，又提升了可维护性。
