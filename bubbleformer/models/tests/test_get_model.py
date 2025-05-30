import pytest
import torch
from bubbleformer.models import get_model

@pytest.mark.parametrize("input_fields", [1, 2])
@pytest.mark.parametrize("output_fields", [1, 2])
@pytest.mark.parametrize("patch_size", [8, 16])
@pytest.mark.parametrize("embed_dim", [192, 384])
@pytest.mark.parametrize("attn_scale", [True, False])
@pytest.mark.parametrize("feat_scale", [True, False])
def test_avit(input_fields, output_fields, patch_size, embed_dim, attn_scale, feat_scale):
    """
    Test AViT model with random configs
    """
    model_params = {
        "input_fields": input_fields,
        "output_fields": output_fields,
        "time_window": 3,
        "patch_size": patch_size,
        "embed_dim": embed_dim,
        "num_heads": 4,
        "processor_blocks": 4,
        "drop_path": 0.1,
        "attn_scale": attn_scale,
        "feat_scale": feat_scale,
    }
    spatial_dims = 64, 64
    model = get_model("avit", **model_params)
    x = torch.randn(2, 3, input_fields, *spatial_dims) # (B, T, C, H, W)
    y = model(x) # (B, T, C, H, W)

    assert y.shape == (2, 3, output_fields, *spatial_dims)

@pytest.mark.parametrize("time_window", [1, 3])
@pytest.mark.parametrize("input_fields", [1, 2])
@pytest.mark.parametrize("output_fields", [1, 2])
@pytest.mark.parametrize("hidden_channels", [16, 32])
def test_unet_classic(time_window, input_fields, output_fields, hidden_channels):
    """
    Test UNet model with random configs
    """
    model_params = {
        "time_window": time_window,
        "input_fields": input_fields,
        "output_fields": output_fields,
        "hidden_channels": hidden_channels
    }
    spatial_dims = 64, 64
    model = get_model("unet_classic", **model_params)
    x = torch.randn(2, time_window, input_fields, *spatial_dims)
    y = model(x)

    assert y.shape == (2, time_window, output_fields, *spatial_dims)

@pytest.mark.parametrize("time_window", [1, 3])
@pytest.mark.parametrize("input_fields", [1, 2])
@pytest.mark.parametrize("output_fields", [1, 2])
@pytest.mark.parametrize("hidden_channels", [16, 32])
def test_unet_modern(time_window, input_fields, output_fields, hidden_channels):
    """
    Test UNet model with random configs
    """
    model_params = {
        "time_window": time_window,
        "input_fields": input_fields,
        "output_fields": output_fields,
        "hidden_channels": hidden_channels,
        "ch_mults": [1, 2, 2],
        "norm": True,
    }
    spatial_dims = 64, 64
    model = get_model("unet_modern", **model_params)
    x = torch.randn(2, time_window, input_fields, *spatial_dims)
    y = model(x)

    assert y.shape == (2, time_window, output_fields, *spatial_dims)
