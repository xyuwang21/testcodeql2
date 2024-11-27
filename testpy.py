import os

# 1. SQL 注入漏洞
def fetch_user_data(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"  # 不安全：直接拼接输入
    print(f"Executing query: {query}")
    # 模拟数据库查询
    return f"Results for {username}"


# 2. 异常未处理
def read_file(file_path):
    # 潜在问题：未捕获异常，如果文件不存在或权限不足将报错
    content = open(file_path, 'r').read()
    print(content)


# 3. 使用硬编码的敏感信息
def connect_to_service():
    api_key = "12345-ABCDE"  # 不安全：敏感信息硬编码
    print(f"Connecting with API key: {api_key}")


# 4. 不推荐的随机数生成方式
def generate_password():
    import random
    password = "".join([chr(random.randint(33, 126)) for _ in range(12)])  # 使用不安全的随机数生成器
    print(f"Generated password: {password}")


# 5. 潜在的空指针错误
def process_data(data):
    # 如果 data 为 None，将导致运行时错误
    print(f"Data length: {len(data)}")


# 6. 无限制递归
def factorial(n):
    # 如果 n 非正整数，可能导致无限递归
    if n == 1:
        return 1
    return n * factorial(n - 1)


# 7. 多余的重复计算
def calculate_sum_slow(arr):
    total = 0
    for i in range(len(arr)):  # len(arr) 在每次循环中都会被计算
        total += arr[i]
    return total


# 主程序（测试各个函数）
if __name__ == "__main__":
    # 运行 SQL 注入测试
    print(fetch_user_data("admin' OR '1'='1"))

    # 尝试读取文件（需要确保文件路径正确）
    try:
        read_file("test.txt")
    except FileNotFoundError:
        print("File not found error caught.")

    # 测试敏感信息
    connect_to_service()

    # 测试随机数生成问题
    generate_password()

    # 测试空指针错误
    try:
        process_data(None)
    except TypeError as e:
        print(f"Error caught: {e}")

    # 测试无限递归
    try:
        print(factorial(-1))
    except RecursionError as e:
        print(f"Recursion error caught: {e}")

    # 测试重复计算问题
    print(calculate_sum_slow([1, 2, 3, 4, 5]))
