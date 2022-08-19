import js2py
from js2py import require

js= '''
    function myfuntion(){
        var b = 2;
        return b;
    }
'''

a = js2py.eval_js(js)

result, tempfile = js2py.run_file("test.js")
result = tempfile.numar(3)
print(result)
print(a())