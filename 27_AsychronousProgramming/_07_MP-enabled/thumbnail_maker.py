# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
from queue import Queue
from threading import Thread
import multiprocessing

import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s]"
logging.basicConfig(filename='logfile.log', level=logging.INFO, force=bool, format=FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_list = []
        # >>>> self.url_queue = Queue()


    def download_image(self, url_queue):
        logging.info("beginning image downloads")

        start = time.perf_counter()
        while not url_queue.empty():
            try:
                url = url_queue.get(block=False)
                img_filename = urlparse(url).path.split('/')[-1]
                urlretrieve(url, self.input_dir + os.path.sep + img_filename)
                logging.info("downloaded - {}".format(img_filename))
                self.img_list.append(img_filename)
                url_queue.task_done()
            except Queue.Empty:
                logging.info("URL queue EMPTY !")
        end = time.perf_counter()

    def resize_image(self, filename):
        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        logging.info("resizing image " + filename)

        orig_img = Image.open(self.input_dir + os.path.sep + filename)
        for basewidth in target_sizes:
            img = orig_img
            # calculate target height of the resized image to maintain the aspect ratio
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            # perform resizing
            img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
            
            # save the resized image to the output dir with a modified file name 
            new_filename = os.path.splitext(filename)[0] + \
                '_' + str(basewidth) + os.path.splitext(filename)[1]
            img.save(self.output_dir + os.path.sep + new_filename)

        os.remove(self.input_dir + os.path.sep + filename)
        logging.info("done resizing image {}".format(filename))

        
    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        pool = multiprocessing.Pool()
        os.makedirs(self.output_dir, exist_ok=True)


        start = time.perf_counter()
        start_dl = time.perf_counter()

        ## [[
        url_queue = Queue()     ## <<<<
        for url in img_url_list:
            url_queue.put(url)

        os.makedirs(self.input_dir, exist_ok=True)
         
        num_dl_threads = 4
        for idx in range(num_dl_threads):
            t1 = Thread(target=self.download_image, name=f"t_Dwnld[{idx}]", args=(url_queue,))
            t1.start()

        # t2 = Thread(target=self.perform_resizing, name="t_Resize")
        # t2.start()

        url_queue.join() 
        end_dl = time.perf_counter()
        logging.info(f"downloaded {len(img_url_list)} images in {end_dl - start_dl} seconds")

        # self.img_queue.put(None)

        # t2.join()
        os.makedirs(self.output_dir, exist_ok=True)

        start_resize = time.perf_counter()
        pool.map(self.resize_image, self.img_list)
        end_resize = time.perf_counter()

        end = time.perf_counter()

        pool.close()
        pool.join()     # Join can be called only after we have called pool.close() or pool.terminate()
        
        logging.info(f"created {len(self.img_list)} thumbnails in {end_resize - start_resize} seconds")
        ## ]]

        logging.info("END make_thumbnails in {} seconds".format(end - start))
    
