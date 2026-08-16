import http.server, json, urllib.request, urllib.parse, socketserver
SITES={"diesel":"http://127.0.0.1:80/diesel-engine-3d/","robot":"http://127.0.0.1:80/robot-3d/","ox":"http://127.0.0.1:80/ox-movie-3d/"}
class H(http.server.BaseHTTPRequestHandler):
    def _j(self,o,c=200):
        b=json.dumps(o,ensure_ascii=False).encode()
        self.send_response(c);self.send_header("Content-Type","application/json; charset=utf-8");self.send_header("Access-Control-Allow-Origin","*");self.end_headers();self.wfile.write(b)
    def do_GET(self):
        if self.path in ("/","/api"):
            self._j({"service":"mini-worker","routes":["/api/status","/api/echo?msg=hi"],"sites":list(SITES)})
        elif self.path.startswith("/api/status"):
            out={}
            for k,u in SITES.items():
                try:
                    r=urllib.request.urlopen(u,timeout=3);out[k]="up" if r.status==200 else "down"
                except Exception as e:out[k]="down:"+str(e)[:40]
            self._j({"status":out})
        elif self.path.startswith("/api/echo"):
            q=urllib.parse.urlparse(self.path).query;m=urllib.parse.parse_qs(q).get("msg",[""])[0]
            self._j({"echo":m})
        else:self._j({"error":"not found"},404)
    def log_message(self,*a):pass
socketserver.TCPServer.allow_reuse_address=True
http.server.HTTPServer(("0.0.0.0",8080),H).serve_forever()
