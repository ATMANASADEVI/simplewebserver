from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
   <title>
          sample webpage
   </title>
   <body>  
<p>
<b>
<ol>
<h1 align = "center">SYSTEM SPECIFICATIONS</h1>
<h3 align = "right">Registration number:24900506</h1>
<h4 align = "left">Device name:Manasa07</h4>
<h4 align = "left">Processor:13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</h4>
<h4 align = "left">Installed RAM:16.0 GB (15.7 GB usable)</h4>
<h4 align = "left">Device ID:15EEA3B2-7EF5-4DEC-903D-577382C3C005</h4>
<h4 align = "left">Product ID:00342-42709-07345-AAOEM</h4>
<h4 align = "left">System type:64-bit operating system, x64-based processor</h4>
<h4 align = "left">Pen and touch:No pen or touch input is available for this display</h4>
</ol>
</b>
</p>
   </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()