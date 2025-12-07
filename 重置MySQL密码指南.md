# MySQL Root 密码重置指南

## 当前问题
- 错误1: `Access denied for user 'root'@'localhost'` - 密码错误
- 错误2: `Connection refused` - MySQL 服务器未运行

## 推荐方法：使用自动化脚本（最简单）

### 步骤：

1. **停止 MySQL 服务**
   - 打开 MySQL 管理界面（你已经在使用）
   - 点击 **"Stop MySQL Server"** 按钮
   - 等待服务完全停止

2. **运行重置脚本**
   ```bash
   cd /Users/songximing/Documents/GitHub/python_LM_sxm_study
   ./reset_mysql_password_easy.sh abcd@123
   ```
   
   或者使用默认密码（abcd@123）：
   ```bash
   ./reset_mysql_password_easy.sh
   ```

3. **重新启动 MySQL**
   - 在 MySQL 管理界面点击 **"Start MySQL Server"**
   - 或者运行：
     ```bash
     sudo /usr/local/mysql/support-files/mysql.server start
     ```

4. **测试连接**
   ```bash
   python 11阶段RAG/integrated_qa_system/mysql_qa/main.py
   ```

---

## 手动方法（如果脚本不工作）

### 步骤：

1. **停止 MySQL 服务**
   - 在 MySQL 管理界面点击 "Stop MySQL Server"

2. **以安全模式启动 MySQL**
   ```bash
   sudo /usr/local/mysql/bin/mysqld_safe --skip-grant-tables --skip-networking &
   ```
   - 等待 5-10 秒让 MySQL 启动

3. **连接 MySQL（无需密码）**
   ```bash
   /usr/local/mysql/bin/mysql -u root
   ```

4. **在 MySQL 命令行中执行**
   ```sql
   FLUSH PRIVILEGES;
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'abcd@123';
   FLUSH PRIVILEGES;
   exit;
   ```

5. **停止安全模式的 MySQL**
   ```bash
   sudo pkill mysqld_safe
   sudo pkill mysqld
   ```

6. **正常启动 MySQL**
   - 在 MySQL 管理界面点击 "Start MySQL Server"

---

## 如果知道当前密码（最简单的方法）

如果你记得当前的 root 密码，可以直接修改：

```bash
/usr/local/mysql/bin/mysql -u root -p
# 输入当前密码后，执行：
ALTER USER 'root'@'localhost' IDENTIFIED BY 'abcd@123';
FLUSH PRIVILEGES;
exit;
```

---

## 注意事项

1. **确保 MySQL 已停止**：在重置密码前，必须停止 MySQL 服务
2. **使用管理员权限**：某些命令需要 `sudo`
3. **等待启动**：安全模式启动需要几秒钟时间
4. **密码格式**：`abcd@123` 包含特殊字符，在命令行中可能需要引号

---

## 验证密码是否重置成功

重置后，测试连接：
```bash
/usr/local/mysql/bin/mysql -u root -p
# 输入新密码: abcd@123
```

如果能够成功连接，说明密码重置成功！

