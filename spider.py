from urllib.request import urlopen
import re
import os

data=urlopen('http://istrasvvt.narod.ru/puchnoi.htm').read().decode('utf-8')
link = re.findall(r"""href\s*=\s*['"]?([^\s>"]+)""", data)
single = [i.split('\n')[0] for i in link if "http" not in i]

css = [i for i in single if ".css" in i]
for i in css:
    for n in range(len(i.split("/"))-1):
        if (n):
            if not os.path.exists("C:/spider/" + "/".join(i.split("/")[:-n])):
                os.makedirs("C:/spider/"+ "/".join(i.split("/")[:-n-1])+ "/" + i.split("/")[n])
        else:
            if not os.path.exists("C:/spider/"+i.split("/")[n]):
                os.makedirs("C:/spider/" + i.split("/")[n])
    path = "C:/spider/" + "/".join(i.split("/")[:-1])
    css_text = urlopen('http://istrasvvt.narod.ru/'  + i).read().decode('utf-8')
        
    saved_css = open(path+"/" + i.split("/")[-1] , "w")
    saved_css.write(css_text)
    saved_css.close()

for L in range(len(link)):
    try:
        site = urlopen('http://istrasvvt.narod.ru/'  + single[L]).read().decode('utf-8')
        saved_site = open("site" + str(L) + ".html", 'w')
        saved_site.write(site)
        saved_site.close()
        images = re.findall(r"""img\s*src\s*=\s*['"]?([^\s>"]+)""", site)
        single_img = [n.split('\n')[0] for n in images]
        
        for i in images:
            for n in range(len(i.split("/"))-1):
                if (n):
                    if not os.path.exists("C:/spider/" + "/".join(i.split("/")[:-n])):
                        os.makedirs("C:/spider/"+ "/".join(i.split("/")[:-n-1])+ "/" + i.split("/")[n])
                        print("/".join(i.split("/")[:-n]))
                else:
                    if not os.path.exists("C:/spider/"+i.split("/")[n]):
                        os.makedirs("C:/spider/" + i.split("/")[n])
                        print(i.split("/")[n])
        
        for im in range(len(images)):
            print(single_img[im])
            img = urlopen('http://istrasvvt.narod.ru/' + single_img[im]).read()
            saved_img = open("C:/spider/" + single_img[im] , "wb")
            saved_img.write(img)
            saved_img.close()
        
    except:
        print("error")
        
                         
