import js2py

class Create:
    
    def create_element(self,ipaddress):
        
        javascript = """"
            import myFunction from "./static/javascript/main/create_video.js"

            function CreateVideoJs2PY(ipaddress){
                myFunction(ipaddress)
                
            }
        """
        a = js2py.eval_js(javascript)
        a(ipaddress)