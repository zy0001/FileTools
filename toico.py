import base64
with open("icon.py","w") as f:
  f.write('class Icon(object):\n')
  f.write('\tdef __init__(self):\n')
  f.write("\t\tself.ig='")
with open("bat.ico","rb") as i:
  b64str = base64.b64encode(i.read())
  with open("icon.py","ab+") as f:
    f.write(b64str)
with open("icon.py","a") as f:
  f.write("'")