import os

Images_folder = "/images/arc_turkey"

with open("arc_turkey.html", "r") as f:
    html_file = f.read()

print(html_file)

Images = ""

for filename in os.listdir(Images_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        Image_path = os.path.join(Images_folder, filename)
        Images += f'''
          <div class="col-sm-6 col-md-4 col-lg-3 col-xl-3 item" data-aos="fade" data-src="{Image_path}" data-sub-html="<h4></h4><p></p>">
            <a href="#"><img src="{Image_path}" alt="Image" class="img-fluid"></a>
          </div>
        '''

print(Images)

html_file = html_file.replace("<!-- Placeholder for Images -->", Images)

with open("arc_turkey.html", "w") as f:
    f.write(html_file)






with open("arc_turkey.html", "r") as f:
    html_file = f.read()

print(html_file)

Images = ""

for filename in os.listdir(Images_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        Image_path = os.path.join(Images_folder, filename)
        Images += f'''
          <div class="col-sm-6 col-md-4 col-lg-3 col-xl-3 item" data-aos="fade" data-src="{Image_path}" data-sub-html="<h4></h4><p></p>">
            <a href="#"><img src="{Image_path}" alt="Image" class="img-fluid"></a>
          </div>
        '''

print(Images)

html_file = html_file.replace("<!-- Placeholder for Images -->", Images)

with open("arc_turkey.html", "w") as f:
    f.write(html_file)


