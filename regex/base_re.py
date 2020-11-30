import re


def analyze():
    m = re.match(r'(.*?)(\d{2,4}款)(.*)', '  898797 高版本# 860款  高版本 市面')
    print(m)
    print(m.group(2))


def mutiRowsAnalyze():
    info = """
        860款  高版本 市面最好版本 SUPREME X The North Face TNF北面皮质羽绒服 男女同款
    进口日本机器刺绣  立体饱满 选用最高品质还原原版进口仿羊皮面料  纹路清晰可见 质地柔软 而不是市面错误的硬面料  原版一样的皮质哑光  那种亮光的通货可以直接pass掉了 毕竟一分价钱一分货
    羽绒采用国标白鸭绒  原版就是白鸭绒 今年因为疫情 羽绒价格上涨 成本非常高 很多通货都是用羽丝 或者便宜的碎鸭绒代替 不懂的人很容易被骗到 贵有贵的道理  
    辅料都是带走logo的订制辅料  
    颜色  黑色
    码数:M~XXL 
             M      L       XL       XXL 
    衣长  70      72      74    76
    胸围 120   124    128     132
         （手工测量1-3CM误差 ）
         """
    m = re.match(r'(.*?)(\d{2,4}款)(.*)', info, re.S)
    print(m)
    print(m.group(2))
    price=m.group(2)
    downJacketTagMatcher =re.match(r'.*羽绒服.*',info,re.S)
    if downJacketTagMatcher:
        print('#羽绒服')
    TNFTagMatcher=re.match(r'.*The North Face.*',info,re.S)
    if TNFTagMatcher:
        print('#北面')
    tnf=tagMatche(r'The North Face',info)
    downJacket=tagMatche(r'羽绒服',info)
    nike=tagMatche(r'Nike',info)
    print('Nike:{}\n羽绒服:{}\n北面:{}'.format(nike,downJacket,tnf))

    newInfo=info.replace(price,'xxx')
    print(newInfo)


def tagMatche(tagPattern:str,info:str):
    pattern=r'.*'+tagPattern+r'.*'
    print(pattern)
    m=re.match(pattern,info,re.S)
    if m:
        return True




def test():
    pattern = r'^(\d{3,4})\-(\d{3,8})$'
    phoneNums = """
    010-12341234
    3421-1234
    """
    m = re.match(r'(\d{3,4})-(\d{3,8})', '010-123123')
    print(m)
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))


def testa():
    pattern = r'hello'
    s = 'hello world'
    m = re.match(pattern, s)
    print(m)
    print(m.group())


if __name__ == '__main__':
    # testa()
    # test()
    # analyze()
    mutiRowsAnalyze()
