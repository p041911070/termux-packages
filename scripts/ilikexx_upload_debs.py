import requests
import os


def aptly_upload_file(filename, repository_name, apt_admin, apt_pwd):
    # 构建 URL
    url = f"https://nuget.zonejoin.cn/service/rest/v1/components?repository=apt-{repository_name}"

    # 确保文件存在
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        return

    # 打开文件
    with open(filename, 'rb') as f:
        # 构建文件字典
        files = {
            'file': (os.path.basename(filename), f, 'application/octet-stream')
        }

        # 构建请求头部
        headers = {
            "accept": "application/json"
        }

        # 构建认证信息
        auth = (apt_admin, apt_pwd)

        # 发送 POST 请求
        response = requests.post(url, headers=headers, files=files, auth=auth)

        # 打印响应内容
        print("Response:", response.text)

        # 检查响应状态码
        if response.status_code == 204:
            print(f"Uploaded {filename} successfully")
        else:
            print(f"Failed to upload {filename}: {response.status_code} {response.text}")
# 使用示例
repository_name = "termux-main"
apt_admin = "admin"
apt_pwd = "Pym*"
# 设置要上传的 .deb 包的目录
package_dir = r'C:\Pym\Develop\GitHubProject\termux-packages\output-files\x86_64'
# 遍历目录中的所有 .deb 文件
for filename in os.listdir(package_dir):
    if filename.endswith(".deb"):
        file_path = os.path.join(package_dir, filename)
        aptly_upload_file(file_path, repository_name, apt_admin, apt_pwd)