#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image
import os
import numpy
import sys



cwd = os.getcwd()
path_dir1 = cwd +"/IND"
path_dir2 = cwd +"/IND_cropped"
for filename in os.listdir(path_dir1):
    img = Image.open(os.path.join(path_dir1, filename))
    
left = 0
top = 96
right = 1216
bottom = 352

img_res = img.crop((left, top, right, bottom))

img_res.save(path_dir2+'/'+filename, img)


# In[ ]:





# In[ ]:




