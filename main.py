import requests

img_url = 'https://img.goodfon.com/original/1920x1080/e/21/samurai-cyberpunk-2077-future-katana-night-lights.jpg'


def download_img(url=''):
    try:
        response = requests.get(url=url)

        with open('img.jpeg', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloaded!'

    except Exception as _ex:
        return 'Upps..Check the URL please!'


def main():
    print(download_img(url=img_url))


if __name__ == '__main__':
    main()
