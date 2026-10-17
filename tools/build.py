#!/usr/bin/env python3
"""src/app.html 템플릿에 이미지·사업장·지도 데이터와 라이브러리를 넣어
단독 실행 파일(index.html)과 Claude 아티팩트용 본문(dist/artifact.html)을 만듭니다.
사용법: python3 tools/build.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = lambda *a: os.path.join(ROOT, *a)
rd = lambda f: open(p(f), encoding="utf-8").read()
t = rd("src/app.html")
img = json.load(open(p("assets/img.json"), encoding="utf-8"))
t = t.replace("/*__LEAFLET_CSS__*/", rd("src/leaflet.css"))
t = t.replace("__CUBE__", img["cube"]).replace("__LOGO__", img["logo"]).replace("__TEAM__", img["team"])
t = t.replace("/*__LEAFLET_JS__*/", rd("vendor/leaflet-1.9.4.min.js"))
t = t.replace("/*__EXCELJS__*/", rd("vendor/exceljs-4.4.0.min.js").replace("�", "\\ufffd"))
t = t.replace("/*__QRCODE__*/", rd("vendor/qrcode-generator-1.4.4.js"))
t = t.replace("/*__SHEETJS__*/", rd("vendor/xlsx-0.18.5.core.min.js").replace("\ufffd", "\\ufffd").replace("</script", "<\\/script"))
t = t.replace("/*__IMG__*/{}", json.dumps(img)).replace("/*__SITES__*/{}", rd("assets/sites.json")).replace("/*__ADM__*/{}", rd("assets/adm.json"))
os.makedirs(p("dist"), exist_ok=True)
open(p("dist/artifact.html"), "w", encoding="utf-8").write(t)
html = '<!doctype html>\n<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#1b2a86"><link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-192.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="에스텍 견적"></head><body>\n' + t + '\n</body></html>'
open(p("index.html"), "w", encoding="utf-8").write(html)
print(f"index.html {len(html)//1024} KB")
