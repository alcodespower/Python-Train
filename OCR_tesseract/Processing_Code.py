from PIL import Image
from PIL import ImageEnhance
import pytesseract


def process(filename='15.jpg'):  # 处理图片
	img = Image.open(filename).convert("RGB")
	enhancer = ImageEnhance.Color(img)
	enhancer = enhancer.enhance(0)  # 变成黑白
	enhancer = ImageEnhance.Brightness(enhancer)  # 这下面的参数是经过测试后图片效果最好的。。。
	enhancer = enhancer.enhance(2)  # 提高亮度
	enhancer = ImageEnhance.Contrast(enhancer)
	enhancer = enhancer.enhance(40)  # 提高对比度
	enhancer = ImageEnhance.Sharpness(enhancer)
	enhancer = enhancer.enhance(1)  # 锐化
	enhancer.show()
	
	content = pytesseract.image_to_string(enhancer)  # 解析图片
	print(content)
	return content


process()
