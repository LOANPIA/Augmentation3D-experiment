from vedo import load, Volume, show
import vedo
from vedo.applications import FreeHandCutPlotter

vedo.settings.use_parallel_projection = True

path_nifti_vol = "./FinalizeDulieuDr/Augmented/Intensity/TrainSet/Image/PHANHOANGDINHKIEM_2_registered_motion.nii.gz"
# path_nifti_mask = "./data/images/BraTS20_Training_001_t1ce_1.nii.gz"
# mesh = Volume(path_nifti_vol).c('white').lighting('glossy')
mask = Volume(path_nifti_vol).isosurface().color("blue5")
plt = FreeHandCutPlotter(mask).add_hover_legend() #Thêm bộ công cụ cắt mảnh label thủ công
plt.start(axes=0, interactive=1).close()
# show(mask).close()


# import vedo
# from vedo.applications import IsosurfaceBrowser
# path_nifti_vol = "./data/images/ID_e566ef9b_ID_439ce9720b.nii.gz"
# vol = Volume(path_nifti_vol)
# # IsosurfaceBrowser(Plotter) instance:
# # plt = IsosurfaceBrowser(vol, use_gpu=True, c='gold')
# # plt.show(axes=7, bg2='lb').close()
# from vedo.applications import Slicer2DPlotter
# path_nifti_vol = "./data/images/ID_e566ef9b_ID_439ce9720b.nii.gz"
# vol = Volume(path_nifti_vol)
# # plt = Slicer2DPlotter(vol)
# # plt.show().close()