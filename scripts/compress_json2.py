# from flask import Flask, request
# from os import environ
# import zlib
# import pickle
# #from cv2 import gpu
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot

# app = Flask(__name__)


# @app.route('/server/',methods=['POST'])
# def server():
#     environ["QT_DEVICE_PIXEL_RATIO"] = "0"
#     environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#     environ["QT_SCREEN_SCALE_FACTORS"] = "1"
#     environ["QT_SCALE_FACTOR"] = "1"
#     while True:
#         # data = request.data
#         if request.method == 'POST':
#             decompressed = pickle.loads(zlib.decompress(request.data))
#             image = np.frombuffer(decompressed, dtype=np.uint8) # interpretate the 
#             frame = cv.imdecode(image, 1) # decode the image
#             cv.imshow('192',frame)
#             if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can)
#                 break

#         return("OK")
#     cv.release()



# if __name__ == '__main__':
#     app.run(host='10.33.16.19', port=5000)