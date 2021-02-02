import torch
import torchvision
from PIL import Image

class StartingDataset(torch.utils.data.Dataset):
    def __init__(self, images, truth, base):
        self.images = images
        self.truth = truth
        self.base = base

    def __getitem__(self, index):
        path = self.images[index]
        label = self.truth[index]

        img = Image.open(f'{self.base}/{path}')
        tensor = torchvision.transforms.ToTensor()(img).unsqueeze_(0)
        return tensor, int(label)

    def __len__(self):
        return len(self.truth)
