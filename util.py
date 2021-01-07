from selenium.webdriver.common.keys import Keys


def fetch_image_urls(query, no_of_images, wd):
    urls = []  # list of urls
    counter = 0  # count number of image links to fetched

    # 1. go to images.google.com
    wd.get("https://images.google.com/")

    # 2. find the search bar
    search_bar = wd.find_elements_by_class_name("gLFyf")[0]

    # 3. enter the query string and press ENTER
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.ENTER)

    # 4. find all images
    image_elements = wd.find_elements_by_class_name("rg_i")

    # 5. click on each image and extract url and store it in url list
    for image_element in image_elements:
        image_element.click()  # click on image
        wd.implicitly_wait(10)  # wait for image to load
        images = wd.find_elements_by_css_selector("img.n3VNCb")  # search requrired image tag

        urls.append(images[0].get_attribute("src"))  # append url to url list
        counter = counter + 1

        # if we required no of urls is fetched break the loop
        if counter >= no_of_images:
            break

    # 6. closing web driver
    wd.close()

    return urls
