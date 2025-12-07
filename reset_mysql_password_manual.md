# MySQL 密码重置指南

## 方法 1: 使用 MySQL 管理界面（推荐，最简单）

1. **停止 MySQL 服务**
   - 打开 MySQL 管理界面
   - 点击 "Stop MySQL Server" 按钮

2. **在终端执行以下命令**（以安全模式启动 MySQL）：
   ```bash
   sudo /usr/local/mysql/bin/mysqld_safe --skip-grant-tables --skip-networking &
   ```

3. **等待几秒后，连接 MySQL**：
   ```bash
   /usr/local/mysql/bin/mysql -u root
   ```

4. **在 MySQL 命令行中执行**：
   ```sql
   FLUSH PRIVILEGES;
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'abcd@123';
   FLUSH PRIVILEGES;
   exit;
   ```

5. **停止安全模式的 MySQL**：
   ```bash
   sudo pkill mysqld_safe
   sudo pkill mysqld
   ```

6. **通过 MySQL 管理界面重新启动 MySQL**

## 方法 2: 使用提供的脚本

运行脚本：
```bash
cd /Users/songximing/Documents/GitHub/python_LM_sxm_study
./reset_mysql_password.sh abcd@123
```

## 方法 3: 如果知道当前密码，直接修改

如果你知道当前的 root 密码，可以直接修改：
```bash
/usr/local/mysql/bin/mysql -u root -p
# 输入当前密码后，执行：
ALTER USER 'root'@'localhost' IDENTIFIED BY 'abcd@123';
FLUSH PRIVILEGES;
exit;
```


