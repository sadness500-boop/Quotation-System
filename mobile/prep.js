// 웹 앱(../index.html)과 아이콘을 앱 폴더(www)로 복사합니다.
const fs = require("fs"), path = require("path");
const root = path.join(__dirname, ".."), www = path.join(__dirname, "www");
fs.mkdirSync(www, { recursive: true });
for (const f of ["index.html", "icon-192.png", "icon-512.png", "manifest.webmanifest", "app-config.json"]) fs.copyFileSync(path.join(root, f), path.join(www, f));
console.log("www 준비 완료");
