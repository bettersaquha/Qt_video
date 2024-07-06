import requests
import base64
import cv2 as cv

# 返回用于访问百度 AI 服务的访问令牌
def get_access_token():
    return '24.a22e84564e788a6c59e7a2ce325e50ff.2592000.1722478959.282335-89934961'

# 将图像编码为 JPG 格式，并转换为 base64 格式
# 返回 base64 格式的图像数据
def get_image_base64(image):
    _, jpg_code = cv.imencode('.jpg', image)
    image_base64 = base64.b64encode(jpg_code)
    return image_base64

# 发送请求到百度 AI 服务，并返回响应
# image: 输入的图像
# service_type: 请求的服务类型（ "plant", "animal", "landmark"）
def request_ai_service(image, service_type):
    base_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/"
    access_token = get_access_token()
    request_url = f"{base_url}{service_type}?access_token={access_token}"
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    image_base64 = get_image_base64(image)
    params = {"image": image_base64}

    response = requests.post(request_url, data=params, headers=headers)
    return response

# 植物识别，并返回一个包含识别结果的字典，字典包含三个键值对
def ai_plant(image):
    response = request_ai_service(image, "plant")
    plant_message_dict = {}
    if response:
        data = response.json()
        for item in data['result']:
            name = item['name']
            score = round(float(item['score']), 3)
            plant_message_dict[name] = score
    return plant_message_dict

# 动物识别，并返回一个包含识别结果的字典，字典包含六个键值对
def ai_animal(image):
    response = request_ai_service(image, "animal")
    animal_message_dict = {}
    if response:
        data = response.json()
        for item in data['result']:
            name = item['name']
            score = round(float(item['score']), 3)
            animal_message_dict[name] = score
    return animal_message_dict

# 地标识别，只返回一个地标名字
def ai_landmark(image):
    response = request_ai_service(image, "landmark")
    result_dict = {}
    if response:
        data = response.json()
        if 'result' in data and 'landmark' in data['result']:
            result_dict = {'landmark': data['result']['landmark']}
    return result_dict
