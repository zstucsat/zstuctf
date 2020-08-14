from flask import Flask, request, config
from jinja2 import Template
import re

app = Flask(__name__)

@app.route("/")
def index():
    pattern = re.compile(r'eval|os|popen|config|import|mro|base|globals|getattribute')
    name = request.args.get('secret', 'Flask!!')
    name = re.sub(pattern, '', name)
    if 'rm' in name || 'rmdir' in name:
        name = "Y0u 4re s0 B4d"
    t = Template("Hn13 <3" + name)
    return t.render(), 200, {"FLAG": "zstuctf{0h_No!_Y0u_F1nd_My_secret}"}

if __name__ == "__main__":
    app.run()