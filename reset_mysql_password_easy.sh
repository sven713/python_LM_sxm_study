#!/bin/bash

# 简单可靠的 MySQL 密码重置脚本
# 使用方法: ./reset_mysql_password_easy.sh [新密码]
# 默认密码: abcd@123

NEW_PASSWORD="${1:-abcd@123}"
MYSQL_BIN="/usr/local/mysql/bin"

echo "=========================================="
echo "MySQL Root 密码重置工具"
echo "=========================================="
echo "新密码: $NEW_PASSWORD"
echo ""

# 检查 MySQL 是否在运行
if ps aux | grep -i "[m]ysqld" > /dev/null; then
    echo "⚠️  检测到 MySQL 正在运行"
    echo ""
    echo "请先停止 MySQL 服务："
    echo "  方法1: 在 MySQL 管理界面点击 'Stop MySQL Server'"
    echo "  方法2: 运行命令: sudo /usr/local/mysql/support-files/mysql.server stop"
    echo ""
    read -p "是否已停止 MySQL？(y/n): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "❌ 已取消操作"
        exit 1
    fi
    # 确保 MySQL 已停止
    sleep 2
fi

echo ""
echo "步骤 1: 以安全模式启动 MySQL（跳过权限检查）..."
echo "提示: 需要输入管理员密码"
sudo $MYSQL_BIN/mysqld_safe --skip-grant-tables --skip-networking > /dev/null 2>&1 &

# 等待 MySQL 启动
echo "等待 MySQL 启动（约5秒）..."
for i in {1..10}; do
    sleep 1
    if $MYSQL_BIN/mysql -u root -e "SELECT 1" > /dev/null 2>&1; then
        echo "✅ MySQL 已启动"
        break
    fi
    if [ $i -eq 10 ]; then
        echo "⚠️  MySQL 启动可能较慢，继续尝试..."
    fi
done

echo ""
echo "步骤 2: 重置 root 密码..."

# 尝试 MySQL 8.0 的方法
$MYSQL_BIN/mysql -u root <<EOF 2>/dev/null
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY '$NEW_PASSWORD';
FLUSH PRIVILEGES;
EOF

if [ $? -eq 0 ]; then
    echo "✅ 密码重置成功！"
else
    echo "⚠️  尝试备用方法..."
    # 备用方法：使用 UPDATE 语句
    $MYSQL_BIN/mysql -u root <<EOF 2>/dev/null
FLUSH PRIVILEGES;
USE mysql;
UPDATE user SET authentication_string='' WHERE User='root' AND Host='localhost';
ALTER USER 'root'@'localhost' IDENTIFIED BY '$NEW_PASSWORD';
FLUSH PRIVILEGES;
EOF
    
    if [ $? -eq 0 ]; then
        echo "✅ 密码重置成功（使用备用方法）！"
    else
        echo "❌ 密码重置失败，请检查错误信息"
        echo "尝试手动执行以下命令："
        echo "  $MYSQL_BIN/mysql -u root"
        echo "  然后执行: ALTER USER 'root'@'localhost' IDENTIFIED BY '$NEW_PASSWORD';"
    fi
fi

echo ""
echo "步骤 3: 停止安全模式的 MySQL..."
sudo pkill -9 mysqld_safe 2>/dev/null
sudo pkill -9 mysqld 2>/dev/null
sleep 2

echo ""
echo "=========================================="
echo "✅ 密码重置完成！"
echo "新密码: $NEW_PASSWORD"
echo "=========================================="
echo ""
echo "下一步："
echo "1. 通过 MySQL 管理界面点击 'Start MySQL Server' 启动 MySQL"
echo "2. 或者运行: sudo /usr/local/mysql/support-files/mysql.server start"
echo ""

