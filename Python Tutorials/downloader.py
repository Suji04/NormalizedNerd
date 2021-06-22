import requests
import time
import multiprocessing
from PIL import Image
from functools import partial

url_list = ["https://cdn.pixabay.com/photo/2015/01/28/23/34/mountains-615428_960_720.jpg",
            "https://cdn.pixabay.com/photo/2013/08/28/00/54/field-176602_960_720.jpg",
            "https://cdn.pixabay.com/photo/2016/03/09/09/31/buildings-1245842_960_720.jpg",
            "https://cdn.pixabay.com/photo/2020/02/01/22/10/house-4811590_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/05/27/22/33/morocco-2349647_960_720.jpg",
            "https://cdn.pixabay.com/photo/2019/10/23/18/32/freudenberg-4572410_960_720.jpg",
            "https://cdn.pixabay.com/photo/2019/10/15/19/00/alpine-4552654_960_720.jpg",
            "https://cdn.pixabay.com/photo/2020/04/02/22/09/santorini-4996846_960_720.jpg",
            "https://cdn.pixabay.com/photo/2018/04/16/16/16/sunset-3325080_960_720.jpg",
            "https://cdn.pixabay.com/photo/2013/10/02/23/03/mountains-190055_960_720.jpg",
            "https://cdn.pixabay.com/photo/2016/01/08/18/00/antelope-canyon-1128815_960_720.jpg",
            "https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/02/19/15/28/sunset-2080072_960_720.jpg",
            "https://cdn.pixabay.com/photo/2018/08/21/23/29/fog-3622519_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/03/29/15/18/tianjin-2185510_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/03/29/11/29/nepal-2184940_960_720.jpg",
            "https://cdn.pixabay.com/photo/2016/10/14/19/21/canyon-1740973_960_720.jpg",
            "https://cdn.pixabay.com/photo/2015/03/18/09/31/prairie-679014_960_720.jpg",
            "https://cdn.pixabay.com/photo/2013/10/09/02/26/bridge-192982_960_720.jpg",
            "https://cdn.pixabay.com/photo/2012/02/23/08/38/rocks-15712_960_720.jpg"]

def download(url_list):
    for url in url_list:
        response = requests.get(url)
        file_name = url.split('/')[-1]
        file = open('images/'+file_name, "wb")
        file.write(response.content)
        file.close()

        image = Image.open('images/'+file_name)
        image = image.convert('L')
        image.save('images/'+file_name)
        print(file_name, "DONE!")

def download_multi(url, dir_path=None):
    response = requests.get(url)
    file_name = url.split('/')[-1]
    file = open(dir_path+file_name, "wb")
    file.write(response.content)
    file.close()

    image = Image.open(dir_path+file_name)
    image = image.convert('L')
    image.save(dir_path+file_name)
    print(file_name, "DONE!")


if __name__ == "__main__":
    # singleprocessing
    st = time.time()
    download(url_list)
    en = time.time()
    print("time taken = ", en-st, "\n")

    # multiprocessing
    st = time.time()
    results = None
    folder = "images/"
    with multiprocessing.Pool(processes=10) as pool:
        results = pool.map(partial(download_multi, dir_path = folder), url_list)
    pool.close()
    en = time.time()
    print("time taken = ", en-st, "\n")
