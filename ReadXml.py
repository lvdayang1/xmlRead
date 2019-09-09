#读取节点属性内容
import xml.dom.minidom
class ReadXml:
    #filename 需要读取的xml地址     attri 需要读取的节点属性名
    def xmlData(filename,attri):
        # 获取xml所有节点
        data = xml.dom.minidom.parse(filename)
        # 获取名为attri的节点
        child = data.getElementsByTagName(attri)
        listInfos = []
        for node in child:
            # 获取节点的所有属性
            conf_name = node.attributes.keys()
            dictAttr = {}
            # 循环节点属性，将属性名和属性值存储至字典中
            for key in conf_name:
                attr = node.attributes[key]  # 返回属性地址
                dictAttr[attr.name] = attr.value
            # 将一个字典存储到列表里
            listInfos.append({node.nodeName: dictAttr})
        return listInfos

# filename = r'E:\py\xmlRead\xml.xml'
# list = ReadXml.xmlData(filename,'publication')
# f = open('test.txt', 'w')
# for i in list:
#    #print(i)
#    for j in i:
#        #print(i[j])
#        for s in i[j]:
#            print(s + ':' + i[j][s])
#            f.write(s + ':' + i[j][s] + '\n')
# f.close()
# print(list[0]['publication']['author_names'])
# print(list[1]['publication']['author_names'])
