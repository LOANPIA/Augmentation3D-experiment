"""
  Visualize multiple nifti files detail like that:
  Mesh + Mask at 3D formatting
  """
from pycad.visualization import NIFTIVisualizer

path_nifti_vol = "./Finalize10/Augmented/Case1-Raw/Intensity/TrainSet/Image/2400064682_gaussianNoise.nii.gz"
path_nifti_mask = "./Finalize10/Augmented/Case1-Raw/Intensity/TrainSet/Label/2400064682-label_gaussianNoise.nii.gz"
paths = [path_nifti_vol, path_nifti_mask]

# imgregistered = "./data/Registered/registered_ID_0b10cbee_ID_f91d6a7cd2_final.nii.gz"
# labelregistered = "./data/RegisteredMask/_groundtruth_registered_ID_0b10cbee_ID_f91d6a7cd2.nii.gz"
# pathregistered = [imgregistered, labelregistered]

# imgaugmented = "./FinalizeData/Augmented/Geometric/TrainSet/Image/registered_ID_0b10cbee_ID_f91d6a7cd2_final_affine.nii.gz"
# labelaugmented = "./FinalizeData/Augmented/Geometric/TrainSet/Label/_groundtruth_registered_ID_0b10cbee_ID_f91d6a7cd2_affine.nii.gz"

#Show flip -> Orientation: Up
# imgaugmented = "./FinalizeData/Augmented/Geometric/TrainSet/Image/registered_ID_0b10cbee_ID_f91d6a7cd2_final_flip.nii.gz"
# labelaugmented = "./FinalizeData/Augmented/Geometric/TrainSet/Label/_groundtruth_registered_ID_0b10cbee_ID_f91d6a7cd2_flip.nii.gz"

#Show before flip -> Orientation: Down
# imgaugmented = "./FinalizeData/TrainData/registered_ID_0b10cbee_ID_f91d6a7cd2_final.nii.gz"
# labelaugmented = "./FinalizeData/TrainLabel/_groundtruth_registered_ID_0b10cbee_ID_f91d6a7cd2.nii.gz"

# pathaugmented = [imgaugmented, labelaugmented]

colors = ['viridis', 'inferno']
visualizer = NIFTIVisualizer(paths, mesh_colors=colors)
visualizer.visualize()