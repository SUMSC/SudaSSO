import hashlib
import time


def checkMyauth(id_tag: str, secret: str, clienttime: str, passwd: str) -> bool:
    systemtime = int(time.time())  # 10位Unix时间戳，秒级
    if int(systemtime) - int(clienttime) > 60 * 60:
        return False
    secret1 = hashlib.md5()
    secret1.update((id_tag + passwd + clienttime).encode('utf8'))
    if secret1.hexdigest() == secret:
        return True
    return False


if __name__=="__main__":
    print(checkMyauth(id_tag='1627405062',secret="1231231321321231",clienttime=str(int(time.time())),passwd="21231321231"))




