"""Instagram Bot
Use this Instagram driver to automate some of your tedious tasks on
Instagram.

Created: 01/10/2019
Updated: 01/11/2019
Author: Gregory James
"""
from bot.shortImage import *
from textwrap import dedent
from instapy_cli import client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from threading import Timer
import time
import sys
import os, random
import configparser


# todo use gary vee stategry
# todo post random pic from list


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class GrandParentsbot:
    # x = datetime.today()
    # y = x.replace(hour= 0, minute= 0, seconds= 10, microsecond= 0)

    images = [
        os.path.basename(path00), os.path.basename(path01), os.path.basename(path02), os.path.basename(path03),
        os.path.basename(path04), os.path.basename(path05), os.path.basename(path06), os.path.basename(path07),
        os.path.basename(path08), os.path.basename(path09), os.path.basename(path10), os.path.basename(path11),
        os.path.basename(path12), os.path.basename(path13), os.path.basename(path14), os.path.basename(path15),
        os.path.basename(path16), os.path.basename(path17), os.path.basename(path18), os.path.basename(path19),
        os.path.basename(path20), os.path.basename(path21), os.path.basename(path22), os.path.basename(path23),
        os.path.basename(path24), os.path.basename(path25), os.path.basename(path26), os.path.basename(path27),
        os.path.basename(path28), os.path.basename(path30), os.path.basename(path31), os.path.basename(path32),
        os.path.basename(path33), os.path.basename(path34), os.path.basename(path35), os.path.basename(path36),
        os.path.basename(path37), os.path.basename(path38), os.path.basename(path39), os.path.basename(path40),
        os.path.basename(path41), os.path.basename(path42), os.path.basename(path43), os.path.basename(path44),
        os.path.basename(path45), os.path.basename(path47), os.path.basename(path49), os.path.basename(path50),
        os.path.basename(path51), os.path.basename(path52), os.path.basename(path53), os.path.basename(path54),
        os.path.basename(path55), os.path.basename(path56), os.path.basename(path57), os.path.basename(path58),
        os.path.basename(path59), os.path.basename(path60), os.path.basename(path61), os.path.basename(path62),
        os.path.basename(path63), os.path.basename(path64), os.path.basename(path65), os.path.basename(path66),
        os.path.basename(path68),
    ]
    comments = [
        'Your posts are amazing', 'Amazing work. Keep going!', 'Your photos are magnificent',
        'Your work fascinates me!', 'I like how you put your posts together', 'Great job',
        'What a really nice photo, great job!', 'Well done!', 'Your posts are amazing',
    ]
    tags = ['metaphysics', 'metaphysical', 'grandparentsofmetaphysics',
            'metaphysicsart', 'spiritualscienceandmetaphysics', 'california', 'socal',
            'SoCal', 'spiritual', 'follow', 'followus', 'followme', 'schoolofmetaphysics',
            'metaphysicsoftheuniverse', 'instagood', 'metaphysicalhealing',
            'metaphysician', 'sun', 'scruffy', 'metaphysicalstore', 'orgon', 'metaphysicalcrystals',
            'orgoneenergy', 'orgonegenerators', ]
    hashtags = ["#" + tag for tag in random.choices(tags, k=11)]

    links = []

    price = 0.0

    def __init__(self, username, password):  # todo Add driver keywork for geckodriver
        """
        Initializes an instance of the GrandParentsbot class.

        Call the login method to authenticate a user with IG.

        Args:
            :param username: str: The Instagram username for a user
            :param password: str: The Instagram password for a user

        Attributes:
            driver:Selenium.webdriver.Firefox: The Firefoxdriver that is used to automate browser actions

        """
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path='/home/tehuti/PycharmProjects/Drivers/geckodriver')  # todo attach geckodrive to pycharm file system
        self.base_url = 'https://www.Instagram.com'
        # self.hustle()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def comment(self,hashtag):
        for tag in self.tags:
            driver = self.driver
            driver.get("https://www.instagram.com/explore/tags/" + str(hashtag) + "/")
            time.sleep(2)
            def action():
                comment_input = lambda: self.driver.find_element_by_tag_name('textarea')
                comment_input().click()
                comment_input().clear()

                comment = random.choice(self.comments)
                for letter in comment:
                    comment_input().send_keys(letter)
                    delay = random.randint(1, 7) / 30
                    time.sleep(delay)

                comment_input().send_keys(Keys.RETURN)

            # gathering photos
            valid_links = []
            for i in range(0, 9):
                try:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    # get tags
                    comts = driver.find_elements_by_tag_name('a')
                    # finding relevant hrefs
                    comts = [elem.get_attribute('href') for elem in comts
                             if '.com/p/' in elem.get_attribute('href')]
                    # building list of unique photos
                    link = [valid_links.append(href) for href in comts if href not in valid_links]
                    if link not in self.links:
                        self.links.append(link)
                except Exception:
                    continue

            # Liking photos
            unique_photos = len(valid_links)
            for pic_href in valid_links:
                driver.get(pic_href)
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                        action()
                        time.sleep(1)
                except Exception as expt:
                    time.sleep(2)
                unique_photos -= 1



    def like_photo(self, hashtag):
        for tag in self.tags:
            driver = self.driver
            driver.get("https://www.instagram.com/explore/tags/" + str(hashtag) + "/")
            time.sleep(2)

            # gathering photos
            valid_links = []
            for i in range(0, 9):
                try:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    # get tags
                    links = driver.find_elements_by_tag_name('a')
                    # finding relevant hrefs
                    links = [elem.get_attribute('href') for elem in links
                                     if '.com/p/' in elem.get_attribute('href')]
                    # building list of unique photos
                    link = [valid_links.append(href) for href in links if href not in valid_links]
                    if link not in self.links:
                        self.links.append(link)
                except Exception:
                    continue

            # Liking photos
            unique_photos = len(valid_links)
            for pic_href in valid_links:
                driver.get(pic_href)
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    time.sleep(random.randint(2, 4))
                    like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                    like_button().click()
                    for second in reversed(range(0, random.randint(18, 28))):
                        print_same_line("#" + tag + ': unique photos left: ' + str(unique_photos)
                                        + " | Sleeping " + str(second))
                        time.sleep(1)
                except Exception as expt:
                    time.sleep(2)
                unique_photos -= 1


    def post(self):
        # todo iterate through through the pics in Arvel folder
        image = (
            '/home/tehuti/Documents/GPMIGinfo/GPMpics/Photos/AllPhotos/02-IG .jpg')
        with open('/home/tehuti/PycharmProjects/GPMIG/quotes.txt') as quotes:
            quotes_list = quotes.read().splitlines()
            num = random.randrange(1, 23)
        caption = dedent("{}" + "{}").format(quotes_list.pop(num), self.hashtags)
        with client(self.username, self.password) as cli:
            cli.upload( image, caption)

    def nav_user(self, user):
        """
        Args:
            user:str: The username of the instagram user

        Navigate to the users page
        """
        self.driver.get('{}/{}'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

    def hustle(self):
        self.login()
        self.execute()
        self.finalize()

    def getTopPost(self):
        for tag in self.tags:
            self.driver.get('https://www.instagram.com/explore/tags/' + tag + '/')
            time.sleep(2)

            links = self.driver.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/s' in link.get_attribute('href')
            valid_links = list(filter(condition, links))

            for i in range(0, 9):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

    def execute(self):
        for link in self.links:
            self.driver.get(link)
            time.sleep(1)

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            self.comment()
            time.sleep(2)

            self.like_photo()

            self.price += 0.02
            sleeptime = random.randint(18, 28)
            time.sleep(sleeptime)

    def like(self):
        like_button = lambda: self.driver.find_element_by_xpath(
            '//span[@class="glyphsSpriteHeart__outline__24__grey_9 u-__7"]')
        like_button().click()

    def finalize(self):
        print('You gave $' + str(self.price) + ' back to the community.')
        self.driver.close()
        sys.exit()

    # todo use datetime to schedule program to run at certain time
    # def start_time(self):



if __name__ == "__main__":
    tags = ['metaphysics', 'metaphysical', 'metaphysics101', 'grandparentsofmetaphysics',
            'metaphysicsart', 'spiritualscienceandmetaphysics', 'california', 'socal',
            'SoCal', 'spiritual', 'follow', 'followus', 'followme', 'schoolofmetaphysics',
            'metaphysicsoftheuniverse', 'instagood', 'metaphysicalhealing',
            'metaphysician', 'sun', 'scruffy', 'metaphysicalstore', 'orgon', 'metaphysicalcrystals',
            'orgoneenergy', 'orgonegenerators', ]
    hashtags = ["#" + tag for tag in random.choices(tags, k=1)]


    # username = 'tehuti_v'
    # password = 'I25t#64#3**'

    # .ini file is config file for safe storage of password
    config_path = '/home/tehuti/Documents/GPMIGinfo/config_secure.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config_path)
    username = cparser['AUTH']['username']
    password = cparser['AUTH']['password']

    ig_bot = GrandParentsbot(username, password)
    ig_bot.login()
    ig_bot.post()
    ig_bot.comment(hashtags)
    # ig_bot.like_photo(hashtags)
    # ig_bot.follow_user()
    # while True:
    #     try:
    #         # Choose a random tag from the list of tags
    #         tag = random.choice(tags)
    #         ig_bot.like_photo(tag)
    #     except Exception:
    #         ig_bot.closeBrowser()
    #         time.sleep(60)
    #         ig_bot = GrandParentsbot(username, password)
    #         ig_bot.login()

# todo work on unfollow
# todo code must work in this order login, Post photo, like, follow, check for nonfollowers
