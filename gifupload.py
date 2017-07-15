#coding = 'utf-8'
import requests
header = {
    'Host': "www.acfun.cn",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
logindata = {
    'username':"",  #用户名
    'password':""   #密码
}
sign = {
    'sign':"0"
}
files = {
	'filename':(None,''),
	'uploadNum':(None,'1'),
	'userImg':(None,'1'),
	'uploadFile':('image.jpg',open('C:/11.gif','rb'),'application/octet-stream'), #头像文件路径
	'upload':(None,'Acfun Flash Request End')
}
#保存登录的session
s = requests.session()
#登录
s.post("http://www.acfun.cn/login.aspx",data = logindata,headers = header)
#上传头像
s2 = s.post("http://www.acfun.cn/member/upload_image.aspx",files = files,headers = header)
print(s2.text)
if(s2.text.find('SUCCES
