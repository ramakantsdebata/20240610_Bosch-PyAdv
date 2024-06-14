import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
from queue import Queue
from threading import Thread, Lock
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
        self.img_queue = multiprocessing.JoinableQueue()
        self.dl_size = 0                                        ## <<<< Size of all images downloaded
        self.resized_size = multiprocessing.Value('i', 0)       ## <<<< Size of all generated/resized images


    # def download_image(self, url_queue):                      ## <<<<
    def download_image(self, url_queue, dl_size_lock):          ## <<<< Pass the lock & use it to write 'self.dl_size' safely
        os.makedirs(self.input_dir, exist_ok=True)
        
        logging.info("beginning image downloads")

        start = time.perf_counter()
        while not url_queue.empty():
            try:
                url = url_queue.get(block=False)

                # download each image and save to the input dir 
                img_filename = urlparse(url).path.split('/')[-1]
                # urlretrieve(url, self.input_dir + os.path.sep + img_filename)     ## <<<< Cleanup, 
                img_filepath = self.input_dir + os.path.sep + img_filename          ## <<<< and create a variable for the path
                urlretrieve(url, img_filepath)                                      ## <<<<
                with dl_size_lock:                                                  ## <<<<
                    self.dl_size += os.path.getsize(img_filename)                   ## <<<< Accumulate the filesizes using the 'os.path.getsize()'
                logging.info("downloaded - {}".format(img_filename))
                self.img_queue.put(img_filename)
                url_queue.task_done()
            except Queue.Empty:
                logging.info("URL queue EMPTY !")
        end = time.perf_counter()
        # logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self):
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        while True:                        
            filename = self.img_queue.get()
            if filename is None:           
                self.img_queue.task_done() 
                break                      

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
                # img.save(self.output_dir + os.path.sep + new_filename)        ## <<<< Clean up
                out_filepath = self.output_dir + os.path.sep + new_filename     ## <<<< Create a variable for the file path
                img.save(out_filepath)                                          ## <<<<

                with self.resized_size.get_lock():
                    self.resized_size.value += os.path.getsize(out_filepath)    ## <<<< 

            os.remove(self.input_dir + os.path.sep + filename)
            logging.info("done resizing image {}".format(filename))
            self.img_queue.task_done()
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        url_queue = Queue()
        dl_size_Lock = Lock()                           ## <<<< Create the lock to be passed for accumulating the download size

        for url in img_url_list:
            url_queue.put(url)

        num_dl_threads = 4
        for idx in range(num_dl_threads):
            # t1 = Thread(target=self.download_image, name=f"t_Dwnld[{idx}]", args=(url_queue,))                ## <<<< 
            t1 = Thread(target=self.download_image, name=f"t_Dwnld[{idx}]", args=(url_queue,dl_size_Lock))      ## <<<< Pass in the lock 
            t1.start()

        num_processes = multiprocessing.cpu_count()
        for _ in range(num_processes):
            p = multiprocessing.Process(target=self.perform_resizing)
            p.start()

        url_queue.join() 

        for _ in range(num_processes):
            self.img_queue.put(None)

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))

        logging.info(f"Initial size of downloads: [{self.dl_size}], Final size of images: [{self.resized_size}]")   ## <<<<
