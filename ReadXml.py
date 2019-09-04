#读取节点属性内容
import xml.dom.minidom
class ReadXml:
    #filename 需要读取的xml地址     attri 需要读取的节点属性名
    def xmlData(filename,attri):
        data = xml.dom.minidom.parse(filename)
        conference = data.getElementsByTagName(attri)
        listInfos = []
        for node in conference:
            conf_name = node.attributes.keys()
            dictAttr = {}
            for key in conf_name:
                attr = node.attributes[key]  # 返回属性地址
                dictAttr[attr.name] = attr.value
            listInfos.append({node.nodeName: dictAttr})
        return listInfos

# filename = r'E:\py\xmlRead\xml.xml'
# list = ReadXml.xmlData(filename,'publication')
# '''for i in list:
#    #print(i)
#    for j in i:
#        #print(i[j])
#        for s in i[j]:
#            print(s + ':' + i[j][s])'''
# print(list[0]['publication']['author_names'])
