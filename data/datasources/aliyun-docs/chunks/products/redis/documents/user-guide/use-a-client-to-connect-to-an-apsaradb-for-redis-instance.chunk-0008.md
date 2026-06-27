l; try { jedis = pool.getResource(); // 执行相关操作，示例如下。 jedis.set("foo10", "bar"); System.out.println(jedis.get("foo10")); jedis.zadd("sose", 0, "car"); jedis.zadd("sose", 0, "bike"); System.out.println(jedis.zrange("sose", 0, -1)); } catch (Exception e) { // 超时或其他异常处理。 e.printStackTrace(); } finally { if (jedis != null) { jedis.close(); } } pool.destroy(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 } }
运行上述Project，预期会返回如下结果：
bar [bike, car]
重要
在使用Jedis的过程中，如果设置了一些不合理的参数或错误使用某些功能可能会引起报错，关于如何排查，请参见[常见报错](../support/common-errors-and-troubleshooting.md)。
