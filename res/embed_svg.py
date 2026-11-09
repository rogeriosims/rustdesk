import base64
from pathlib import Path

root = Path(__file__).resolve().parent.parent
source_png = root / "res" / "logo-source.png"

with open(source_png, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <image href="data:image/png;base64,{b64}" width="1024" height="1024"/>
</svg>'''

target_svg = root / "flutter" / "assets" / "icon.svg"
target_svg.write_text(svg_content, encoding="utf-8")
print(f"[+] Updated {target_svg} with RocketDesk logo!")

res_logo_svg = root / "res" / "logo.svg"
res_logo_svg.write_text(svg_content, encoding="utf-8")
print(f"[+] Updated {res_logo_svg} with RocketDesk logo!")
