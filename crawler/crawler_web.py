import requests
from lxml.html import fromstring,tostring

class crawler_news:
    def __init__(self, dom, title_select, description_select, content_select, image_xpath, time_select, author_select, tags_select):
        self.dom=dom
        self.title_select=title_select
        self.description_select=description_select
        self.content_select=content_select
        self.image_xpath=image_xpath
        self.time_select=time_select
        self.author_select=author_select
        self.tags_select=tags_select
    

    def crawler_news(self, li):
        print("5___")
        try:
            req = requests.get(li)
            tree = fromstring(req.text)
            title = tree.cssselect(self.title_select)[0].text_content()
            time = tree.cssselect(self.time_select)[0].text_content()
            descr = tree.cssselect(self.description_select)[0].text_content()
            img = "".join(tree.xpath(self.image_xpath))
            content = tree.cssselect(self.content_select)[0].text_content()
            auth = tree.cssselect(self.author_select)[0].text_content()
            tags = tree.cssselect(self.tags_select)[0].text_content()
            metas = tree.xpath("//head//meta")
            dic = {}
            for meta in metas:
                try:
                    meta_key = tostring(meta).decode("utf-8").split('="')[1].split('" ')[0]
                    meta_value = fromstring(tostring(meta)).xpath("//*/@content")[0]
                    dic[meta_key] = meta_value
                except Exception as e:
                    print(e, tostring(meta).decode("utf-8"))
                

            data_new = {"title": title, \
                                    "time": time, \
                                    "description": descr, \
                                    "image": img, \
                                    "content": content, \
                                    "author": auth, \
                                    "tags": tags
                                    }
            data_new.update(dic)
            return data_new
            
        except:
            return {}
            