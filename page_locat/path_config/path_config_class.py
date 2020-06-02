import os

# 设置文件路径的可配置
# os.path.realpath(__file__)  # 查看当前文件绝对路径
project_path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]

# 测试报告路径
test_report_path = os.path.join(project_path, 'output_file', 'output_report', 'test_report.html')
# 截图存放路径
test_screen_path = os.path.join(project_path, 'output_file', 'output_screenshot')

# 配置日志文件路径
test_log_path = os.path.join(project_path, 'output_file',  'output_log', 'test_log.txt')

#app启动参数文件
app_start = os.path.join(project_path, 'test_data', 'app_start_data', 'start_data.yaml')

# 登录账号范围
account_range = os.path.join(project_path, 'test_data', 'common_data', 'login_data_01.json')


if __name__ == '__main__':
    print(app_start)

