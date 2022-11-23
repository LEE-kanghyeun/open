# https://yeslab.tistory.com/77
# https://wikidocs.net/21140
# https://lee-mandu.tistory.com/519?category=838684

#################################################### DATA 1 파싱하기 ####################################################################
from xml.etree.ElementTree import parse

tree = parse('xml_parsing_data.xml')
root = tree.getroot()

print(tree, '\n')
print(root, '\n')  ##
print('root.tag:', root.tag, '\n')

for i in root:
    print(i.attrib)  ## name = 'ooo' 출력
    print(i.tag)  ## student 출력
else:
    print('\n')

for j in root.iter('name'):  ##
    print(j.text)  ## peter, elgar, hong 등의 이름 출력
else:
    print('\n')


student = root.findall("student")
print(student, '\n')
print(type(student), '\n')  ## 리스트



# name = [x.findtext("name") for x in student]
# age = [x.findtext("age") for x in student]
# score = [x.find("score").attrib for x in student]

name = []
age = []
score = []
for x in student:
    name.append(x.findtext("name"))
    age.append(x.findtext("age"))
    score.append(x.find("score").attrib)


print(name, '\n')
print(age, '\n')
print(score, '\n')

#################################################### DATA 2 파싱하기 ####################################################################

tree = parse('xml_parsing_data2.xml')
root = tree.getroot()

size_tag = root.findall('size')
print(size_tag)  ## list 타입으로 출력
print(size_tag[0].find("width").text)

xmin = []
print(root.iter('object'))

for y in root.iter('object'):
    xmin.append(y.find('bndbox').findtext('xmin'))
print(xmin)

################################################# XML 확장자 파일 내용 #######################################################################
# <?xml version="1.0"?>
# <data>
# <student teacher = 'um suk dae'>
#     <name>peter</name>
#     <age>24</age>
#     <score math="80" english="97"/>
# </student>
# <student teacher = 'lee wang seok'>
#     <name>elgar</name>
#     <age>21</age>
#     <score math="67" english="56"/>
# </student>
# <student teacher = 'jeong ji yong'>
#     <name>hong</name>
#     <age>36</age>
#     <score math="76" english="81"/>
# </student>
# </data>


# <annotation>
#   <folder>test_folder</folder>
#   <filename>testt.jpg</filename>
#   <path></path>
#   <source>
#     <database>Unknown</database>
#   </source>
#   <size>
#     <width>1071</width>
#     <height>1717</height>
#     <depth>3</depth>
#   </size>
#   <segmented>0</segmented>
#   <object>
#     <name>W</name>
#     <pose>Unspecified</pose>
#     <truncated>0</truncated>
#     <difficult>0</difficult>
#     <bndbox>
#       <xmin>1013</xmin>
#       <ymin>1116</ymin>
#       <xmax>1043</xmax>
#       <ymax>1146</ymax>
#     </bndbox>
#   </object>
#   <object>
#     <name>L</name>
#     <pose>Unspecified</pose>
#     <truncated>0</truncated>
#     <difficult>0</difficult>
#     <bndbox>
#       <xmin>1018</xmin>
#       <ymin>896</ymin>
#       <xmax>1047</xmax>
#       <ymax>917</ymax>
#     </bndbox>
#   </object>
# </annotation>




################################################# XML TO DATAFRAME #######################################################################
import pandas as pd
xml = '''<?xml version='1.0' encoding='utf-8'?>
<data xmlns="http://example.com">
 <row>
   <shape>square</shape>
   <degrees>360</degrees>
   <sides>4.0</sides>
 </row>
 <row>
   <shape>circle</shape>
   <degrees>360</degrees>
   <sides/>
 </row>
 <row>
   <shape>triangle</shape>
   <degrees>180</degrees>
   <sides>3.0</sides>
 </row>
</data>'''

df = pd.read_xml(xml)
print(df)

# 출력 :
# shape	degrees	sides
# 0	square	360	4.0
# 1	circle	360	NaN
# 2	triangle 180	3.0




xml2 = '''<CATALOG>
<CD>
<TITLE>Empire Burlesque</TITLE>
<ARTIST>Bob Dylan</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Columbia</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1985</YEAR>
</CD>
<CD>
<TITLE>Hide your heart</TITLE>
<ARTIST>Bonnie Tyler</ARTIST>
<COUNTRY>UK</COUNTRY>
<COMPANY>CBS Records</COMPANY>
<PRICE>9.90</PRICE>
<YEAR>1988</YEAR>
</CD>

<D>
<TITLE>Unchain my heart</TITLE>
<ARTIST>Joe Cocker</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>EMI</COMPANY>
<PRICE>8.20</PRICE>
<YEAR>1987</YEAR>
</D>
</CATALOG>'''


df = pd.read_xml(xml2)
print(df)

# 출력:  <CD>~</CD>와 <D></D> 모두 포함
# 	TITLE	ARTIST	COUNTRY	COMPANY	PRICE	YEAR
# 0	Empire Burlesque	Bob Dylan	USA	Columbia	10.9	1985
# 1	Hide your heart	Bonnie Tyler	UK	CBS Records	9.9	1988
# 2	Unchain my heart	Joe Cocker	USA	EMI	8.2	1987



df2 = pd.read_xml(xml2, xpath = './/CD')
print(df2)

# 출력 :  <D> </D>는 제외됨.
# TITLE	ARTIST	COUNTRY	COMPANY	PRICE	YEAR
# 0	Empire Burlesque	Bob Dylan	USA	Columbia	10.9	1985
# 1	Hide your heart	Bonnie Tyler	UK	CBS Records	9.9	1988