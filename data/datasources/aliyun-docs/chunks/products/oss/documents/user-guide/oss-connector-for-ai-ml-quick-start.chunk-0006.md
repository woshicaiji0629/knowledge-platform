ict()) # 使用OssCheckpoint对象读取检查点。 try: with checkpoint.reader(CHECKPOINT_READ_URI) as reader: state_dict = torch.load(reader) # 加载模型。 model = SimpleCNN() model.load_state_dict(state_dict) model.eval() print("检查点加载成功") except Exception as e: print(f"检查点加载失败: {e}") # 可以选择从头开始训练或使用其他检查点
该文章对您有帮助吗？
反馈
