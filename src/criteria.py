import torch
import torch.nn as nn


loss_names = ['l1', 'l2']


class MaskedMSELoss(nn.Module):
    def __init__(self):
        super(MaskedMSELoss, self).__init__()

    def forward(self, pred, target):
        assert pred.dim() == target.dim(), "inconsistent dimensions"
        valid_mask = (target > 0).detach()
        diff = target - pred
        diff = diff[valid_mask]
        self.loss = (diff**2).mean()
        return self.loss


class MaskedL1Loss(nn.Module):
    def __init__(self):
        super(MaskedL1Loss, self).__init__()

    def forward(self, pred, target, weight=None):
        assert pred.dim() == target.dim(), "inconsistent dimensions"
        valid_mask = (target > 0).detach()
        diff = target - pred
        diff = diff[valid_mask]
        self.loss = diff.abs().mean()
        return self.loss

class MaskedRuberLoss(nn.Module):
    def __init__(self, c=1):
        super(MaskedRuberLoss, self).__init__()
        self.c = c



    def forward(self, pred, target, weight=None):
        assert pred.dim() == target.dim(), "inconsistent dimensions"
        valid_mask = (target > 0).detach()
        e = (target - pred).abs()
        diff1 = e*e
        diff2 = 2*self.c*e - self.c*self.c
        diff = torch.sqrt(torch.where(diff<=self.c, diff1, diff2))
        diff = diff[valid_mask]
        self.loss = diff.mean()
        return self.loss
