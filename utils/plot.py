import os
import matplotlib.pyplot as plt
from torchvision.utils import make_grid


def show_tensor_images(image_tensor, num_images=25, size=(1, 28, 28), current_step=500, real=True):
    image_tensor = (image_tensor + 1) / 2
    image_shifted = image_tensor
    image_unflat = image_tensor.detach().cpu().view(-1, *size)
    image_grid = make_grid(image_unflat[:num_images], nrow=5)
    plt.imshow(image_grid.permute(1, 2, 0).squeeze())
    state = "fake"
    if real:
        state = "real"
    plt.axis('off')
    fig_name = "step_{}_{}".format(current_step, state)
    plt.title(fig_name)
    work_dir = os.getcwd()
    save_dir = f"{work_dir}/runs"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    plt.savefig(f"{save_dir}/{fig_name}.jpg")