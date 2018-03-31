# -*- coding: utf-8 -*-
import json
import time
import scrapy
from scrapy import Request
from scrapy.http import FormRequest
from scrapy.http.cookies import CookieJar


class ZhihutopicSpider(scrapy.Spider):
    name = 'zhihutopic'
    allowed_domains = ['zhihu.com']


    __email = '2938879891@qq.com'
    __password = 'zse4567ujm'

    __topic_codes = ['19551275', ]

    __url_topic_hot = 'https://www.zhihu.com/topic/{}/hot'
    __url_topic_top_activity_api = 'https://www.zhihu.com/api/v4/topics/{}/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.comment_count'
    __url_topic_essence_api = 'https://www.zhihu.com/api/v4/topics/{}/feeds/essence?include=data%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Danswer)%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Danswer)%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Darticle)%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Dpeople)%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Danswer)%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F(target.type%3Danswer)%5D.target.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Darticle)%5D.target.content%2Cauthor.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Dquestion)%5D.target.comment_count'
    __url_topic_top_question_api = 'https://www.zhihu.com/api/v4/topics/{}/feeds/top_question?include=data%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Danswer)%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Danswer)%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Darticle)%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(target.type%3Dpeople)%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Danswer)%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F(target.type%3Danswer)%5D.target.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Darticle)%5D.target.content%2Cauthor.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Dquestion)%5D.target.comment_count'
    __url_topic_timeline_question_api = 'https://www.zhihu.com/api/v4/topics/{}/feeds/timeline_question?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.comment_count'
    __headers = {
        "connection": "keep-alive",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "deflate",
        "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    def start_requests(self):

        print(self.__email, self.__password, self.__topic_codes)
        t = str(int(time.time() * 1000))
        url = 'https://www.zhihu.com/captcha.gif?r={}&type=login&lang=cn'.format(t)

        req_captcha = Request(
            url=url,
            headers=self.__headers,
            meta={
                'cookiejar': CookieJar(),
            },
            callback=self.parse_captcha,
        )
        yield req_captcha
    
    def parse_captcha(self, response):

        with open('captcha.gif', 'wb') as f:
            f.write(response.body)
            f.close()

        from PIL import Image
        try:
            img = Image.open('captcha.gif')
            img.show()
        except:
            pass

        captcha = {
            'img_size': [200, 44],
            'input_points': [],
        }
        points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20],
                [129.796875, 22], [150.796875, 22]]
        seq = input('请输入倒立字的位置\n>')
        for i in seq:
            captcha['input_points'].append(points[int(i) - 1])
        captcha = json.dumps(captcha)
        login_url = 'https://www.zhihu.com/login/email'
        data = {
            'email': self.__email,
            'password': self.__password,
            "captcha": captcha,
            'captcha_type': 'cn',
            }
        req_login = FormRequest(
            url=login_url,
            method='POST',
            headers=self.__headers,
            formdata=data,
            meta={
                'cookiejar': response.meta['cookiejar'],
            },
            callback=self.parse_check_login,
        )

        yield req_login
    
    def parse_check_login(self, response):
        if response.status in [200, ]:
        
            for topic_code in self.__topic_codes:
                req = Request(
                        url=self.__url_topic_hot.format(topic_code),
                        headers=self.__headers,
                        meta={
                            'cookiejar': response.meta['cookiejar'],
                            'topic_code': topic_code,
                        },
                        callback=self.parse_topic_hot,
                    )
                yield req

    def parse_topic_hot(self, response):
        if response.status not in [200, ]:
            print('ERROR with', response)
        
        urls = response.xpath('//*[@id="TopicMain"]/div[2]/div/div/div/*/div/h2/a').extract()
        titles = response.xpath('//*[@id="TopicMain"]/div[2]/div/div/div/*/div/h2/a/text()').extract()

        topic_hot = list(zip(urls, titles))
        yield {
            'topic_hot': topic_hot,
            'topic_code': response.meta['topic_code'],
        }
        
        for topic_code in self.__topic_codes:
            req = Request(
                url=self.__url_topic_top_activity_api.format(topic_code),
                headers=self.__headers,
                meta={
                    'handle_httpstatus_list': [401, ], 
                    'cookiejar': response.meta['cookiejar'],
                    'topic_code': topic_code,
                },
                callback=self.parse_topic_top_activity,
            )
            yield req

            req = Request(
                url=self.__url_topic_essence_api.format(topic_code),
                headers=self.__headers,
                meta={
                    'handle_httpstatus_list': [401, ], 
                    'cookiejar': response.meta['cookiejar'],
                    'topic_code': topic_code,
                },
                callback=self.parse_topic_essence,
            )
            yield req

            req = Request(
                url=self.__url_topic_top_question_api.format(topic_code),
                headers=self.__headers,
                meta={
                    'handle_httpstatus_list': [401, ], 
                    'cookiejar': response.meta['cookiejar'],
                    'topic_code': topic_code,
                },
                callback=self.parse_topic_top_question,
            )
            yield req

            req = Request(
                url=self.__url_topic_timeline_question_api.format(topic_code),
                headers=self.__headers,
                meta={
                    'handle_httpstatus_list': [401, ], 
                    'cookiejar': response.meta['cookiejar'],
                    'topic_code': topic_code,
                },
                callback=self.parse_topic_timeline_question,
            )
            yield req

    def parse_topic_top_activity(self, response):
        yield {
            'topic_top_activity': json.loads(response.body.decode('utf8')),
            'topic_code': response.meta['topic_code'],
        }
    
    def parse_topic_essence(self, response):
        yield {
            'topic_top_essence': json.loads(response.body.decode('utf8')),
            'topic_code': response.meta['topic_code'],
        }
    
    def parse_topic_top_question(self, response):
        yield {
            'topic_top_question': json.loads(response.body.decode('utf8')),
            'topic_code': response.meta['topic_code'],
        }
    
    def parse_topic_timeline_question(self, response):
        yield {
            'topic_timeline_question': json.loads(response.body.decode('utf8')),
            'topic_code': response.meta['topic_code'],
        }

    