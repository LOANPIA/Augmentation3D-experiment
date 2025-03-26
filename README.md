# Augmentation3D-experiment
This is my experiment for augmentation 3D Dicom image (particularly: Brain-BloodVolume), Segmented by Slicer3D tool


- Folder 10: data from scratch (https://drive.google.com/file/d/1w21_F5YxCppL1vDAd3HbawhKuoGynC1J/view?usp=sharing) 
- Folder Finalize10: data after augmentation 
- Preprocessing-2: Folder contains code of augmentation
++++++++++++++++++ Augmentation
+++++++++++++++++++++++++++++++ 1/ Augmentation in geometric 
+++++++++++++++++++++++++++++++ 2/ Augmentation in intensity
- pycadNifti and vedo: file (.py) for visualize 3D (pycadNifti: visual Brain&SegmentTumour, vedo: just visual one thing)
- split-data: file split dataset before augmentation
- dicomtonifti: file convert (could use or none)
- requirements: some library name attach to this file for install one time.

Code run into Python 3.11.8

**Notice: Dataset very heavy! You can use dataset through Cloud  (Google, Azure, etc.)
