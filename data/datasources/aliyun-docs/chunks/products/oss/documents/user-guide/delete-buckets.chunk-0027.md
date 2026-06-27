outcome.error().Code() << ", Message: " << outcome.error().Message() << ", RequestId: " << outcome.error().RequestId() << std::endl; } /*释放网络等资源。*/ ShutdownSdk(); return 0; }
