Template(RedisConnectionFactory connectionFactory) { RedisTemplate<String, Object> template = new RedisTemplate<>(); template.setConnectionFactory(connectionFactory); return template; } }
执行上述代码。
