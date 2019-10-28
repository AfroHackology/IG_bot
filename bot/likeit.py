from bot.main import *


class LikePhoto(GrandParentsbot):

    def __init__(self, hashtags):
        super(LikePhoto, self).__init__(self, hashtags)

    """
    Args:
        hashtags:str: Takes an inserted hashtags and follows this link

    Likes hashtagged photos
    """
    def likepic(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 7):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


        hrefs = driver.find_elements_by_tag_name('a')
        # finding relevant hrefs
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in hrefs]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))


    # # Liking photos
    # unique_photos = len(pic_hrefs)
    # for pic_href in pic_hrefs:
    #     driver.get(pic_href)
    #     time.sleep(2)
    #     driver.execute_script(
    #         "window.scrollTo(0, document.body.scrollHeight);")
    #     try:
    #         time.sleep(LikePhoto().random.randint(2, 4))
    #         # this is a test for choose_button function
    #         LikePhoto.choose_button_to_click('//span[@aria-label="Like"]')
    #         # like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
    #         # like_button().click()
    #         for second in reversed(range(0, random.randint(18, 28))):
    #             print_same_line(LikePhoto.hashtags + ': unique photos left: ' + str(unique_photos)
    #                             + " | Sleeping " + str(second))
    #             time.sleep(1)
    #     except Exception as ex:
    #         time.sleep(2)
    #     unique_photos -= 1


    def choose_button_to_click(self, button_name):  # click button when given pic
        def button(): return self.driver.find_element_by_xpath(button_name).click()
        button().click()

