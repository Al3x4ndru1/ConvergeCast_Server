import js2py
from js2py import require

js= '''
    function myfuntion(){
        var b = 2;
        return b;
    }
'''

a = js2py.eval_js(js)

result, tempfile = js2py.run_file("./scripts/Backend/static/javascript/video/Checks/check_first_checkbox.js")
result = tempfile.ShowImageJavaScript()
print(result)
print(a())