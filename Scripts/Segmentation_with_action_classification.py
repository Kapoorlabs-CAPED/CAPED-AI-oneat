#!/usr/bin/env python
# coding: utf-8

# In[1]:



import sys
import os
import glob
from csbdeep.models import  CARE
from oneat.NEATModels import NEATDynamic
from oneat.NEATModels.config import dynamic_config
from oneat.NEATUtils import helpers
from oneat.NEATUtils.helpers import load_json
os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"
from pathlib import Path


# In[4]:


n_tiles = (4,8,8)
event_threshold = 0.999
event_confidence = 0.9
iou_threshold = 0.4
fidelity = 4
downsamplefactor = 1
#For a Z of 0 to 22 this setup takes the slices from 11 - 4 = 7 to 11 + 1 = 12
normalize = True
nms_function = 'iou'

# In[ ]:


imagedir = 'D:/TestDatasets/Oneat/Drosophila_oneat/'
segdir = 'D:/TestDatasets/Oneat/Drosophila_oneat/seg/'
model_dir = 'D:/TrainingModels/Oneat/'
savedir= 'D:/TestDatasets/Oneat/Drosophila_oneat/Results/'
model_name = 'Celldeathpredictordrosophila'


division_categories_json = model_dir + 'Cellsplitcategoriesdrosophila.json'
catconfig = load_json(division_categories_json)
division_cord_json = model_dir + 'Cellsplitcorddrosophila.json'
cordconfig = load_json(division_cord_json)
model = NEATDynamic(None, model_dir , model_name,catconfig, cordconfig)

Path(savedir).mkdir(exist_ok=True)

Raw_path = os.path.join(imagedir, '*tif')
X = glob.glob(Raw_path)
 
for imagename in X:
  
     marker_tree =  model.get_markers(imagename, segdir)

                                   
     model.predict(imagename,
                           savedir, 
                           n_tiles = n_tiles, 
                           event_threshold = event_threshold, 
                           event_confidence = event_confidence,
                           iou_threshold = iou_threshold,
                           fidelity = fidelity,
                           marker_tree = marker_tree, 
                           nms_function = nms_function,
                           downsamplefactor = downsamplefactor,
                           normalize = normalize)


# In[ ]:





# In[ ]:




