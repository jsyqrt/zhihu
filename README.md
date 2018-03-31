# zhihu, a spider collection of zhihu spiders.

---

## Quick Start

```
git clone https://github.com/jsyqrt/zhihu.git

cd zhihu
pip3 install -r requirements.txt

vi zhihu/spiders/zhihutopic.py # to edit the zhihutopic.py file to specify your account 
                     # info ( email and password ) of zhihu.com.

# you can add more topic codes to the "__topic_codes" field.
# example code "19551275" is the code of topic "人工智能" as my interviewer asked, 
# [愿景學城](http://www.ouraivision.com/).

scrapy crawl zhihutopic # to crawl zhihutopic with scrapy.
                        # when you are asked to input the captcha code, 
                        #just input its order number(1,...,7) without any blank.

scrapy crawl zhihutopic -o topics.json # to save results to json file.

```

---

## Notice

This spider only downloads all data available with the APIs of zhihutopic and does not parse the json string to clear result. You may want to do it yourself.

zhihutopic.json file is an example result if you get everything correctly done.

---

## TODO

To add more spiders to crawl infos of users, questions, answers, etc.

---

## Any Contribution Is Welcomed!
