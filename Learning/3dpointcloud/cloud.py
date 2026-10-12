import matplotlib
matplotlib.use('tkAgg')
from matplotlib import pyplot as plt
from PIL import Image
import torch
from transformers import GLPNImageProcessor, GLPNForDepthEstimation
import numpy as np
import open3d as o3d

feature_extractor = GLPNImageProcessor.from_pretrained("vinvino02/glpn-nyu")
model = GLPNForDepthEstimation.from_pretrained("vinvino02/glpn-nyu")

pythonopy codeimage = Image.open('data/Midi.jpeg')
new_height = 480 if image.height > 480 else image.height
new_height -= (new_height % 32)
new_width = int(new_height * image.width / image.height)
diff = new_width % 32
new_width = new_width - diff if diff < 16 else new_width + 32 - diff
new_size = (new_height, new_width)
image = image.resize(new_size)

inputs = feature_extractor(images=image, return_tensors='pt')
with torch.no_grad():
    outputs = model(**inputs)
    predicted_depth = outputs.predicted_depth

pad = 16
output = predicted_depth.squeeze().cpu().numpy() * 1000.0
output = output[pad:-pad, pad:-pad]
image = image.crop((pad, pad, image.width - pad, image.height - pad))

fig, ax = plt.subplots(1, 2)
ax[0].imshow(image)
ax[0].tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
ax[1].imshow(output, cmap='plasma')
ax[1].tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.tight_layout()
plt.pause(5)

def create_point_cloud_from_depth_image(depth_image, intrinsic, scale=1.0):
    """
    Create a point cloud from a depth image using Open3D.
Parameters:
    - depth_image: A numpy array containing the depth image.
    - intrinsic: An Open3D camera intrinsic object.
    - scale: A scaling factor to adjust the depth values.
Returns:
    - A point cloud object.
    """

height, width = depth_image.shape
    depth_image = o3d.geometry.Image((depth_image / scale).astype(np.float32))    # Create an RGBD image
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color=o3d.geometry.Image(np.zeros((height, width, 3), dtype=np.uint8)),
        depth=depth_image,
        convert_rgb_to_intensity=False
    )

# Create the point cloud from the RGBD image
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        intrinsic
    )    return pcd
    fx = 1000  # Focal length in the x axis
    fy = 1000  # Focal length in the y axis
    cx = output.shape[1] / 2  # Principal point in the x axis
    cy = output.shape[0] / 2  # Principal point in the y axis
    intrinsic = o3d.camera.PinholeCameraIntrinsic(
        width=output.shape[1],
        height=output.shape[0],
        fx=fx,
        fy=fy,
        cx=cx,
        cy=cy
)

# Create the point cloud from the depth image
pcd = create_point_cloud_from_depth_image(output, intrinsic, scale=1.0)
# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])


