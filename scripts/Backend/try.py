from main import app
import jyserver.Flask  as jsf


@jsf.use(app)
class App:
    def __init__(self):
        self.frame = 0

    def show(self, aframe, ipaddress):
        #cv.imshow(ipaddress,frame)
        self.frame=aframe
        self.self.js.document.getElementById('input_image').innerHTML = self.frame