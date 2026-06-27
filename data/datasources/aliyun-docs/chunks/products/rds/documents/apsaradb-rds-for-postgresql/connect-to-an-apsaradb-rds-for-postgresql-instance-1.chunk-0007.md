### 应用程序连接
说明
本文以Maven项目JDBC连接RDS PostgreSQL实例为例，其它编程语言连接方式类似。
pom.xml中添加依赖。
<dependency> <groupId>postgresql</groupId> <artifactId>postgresql</artifactId> <version>8.2-504.jdbc3</version> </dependency>
连接实例示例代码如下：
public class DatabaseConnection { public static void main( String[] args ){ try { Class.forName("org.postgresql.Driver"); } catch (ClassNotFoundException e) { e.printStackTrace(); } //实例连接地址 String hostname = "pgm-bp1i3kkq7321o9****.pg.rds.aliyuncs.com"; //实例连接端口 int port = 5432; //数据库名称 String dbname = "postgres"; //用户名 String username = "username"; //密码 String password = "password"; String dbUrl = "jdbc:postgresql://" + hostname + ":" + port + "/" + dbname + "?binaryTransfer=true"; Connection dbConnection; try { dbConnection = DriverManager.getConnection(dbUrl, username, password); Statement statement = dbConnection.createStatement(); //输入需要执行的SQL语句。 String selectSql = "SELECT * FROM information_schema.sql_features LIMIT 10"; ResultSet resultSet = statement.executeQuery(selectSql); while (resultSet.next()) { System.out.println(resultSet.getString("feature_name")); } } catch (SQLException e) { e.printStackTrace(); } } }
