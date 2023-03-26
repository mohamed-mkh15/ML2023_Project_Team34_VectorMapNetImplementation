import mmcv
import numpy as np
from os import path as osp
from pyquaternion import Quaternion
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Data converter arg parser')
    parser.add_argument(
        '--data-root',
        type=str,
        help='specify the root path of dataset')
    
    args = parser.parse_args()
    return args

def create_kia_infos_map(root_path,
                            dest_path=None,
                            info_prefix='kia'):
    """Create info file for map learning task on nuscene dataset.

    Given the raw data, generate its related info file in pkl format.

    Args:
        root_path (str): Path of the data root.
        info_prefix (str): Prefix of the info file to be generated.
        version (str): Version of the data.
            Default: 'v1.0-trainval'
    """
    
    train_samples, val_samples, test_samples = [], [], []

    lidar_path = root_path + '/samples/LIDAR_TOP/000000.bin'
    mmcv.check_file_exist(lidar_path)
    info = {
        'lidar_path': lidar_path,
        'token': 000000,
        'cams': {},
    }
    train_samples.append(info)
    val_samples.append(info)
    test_samples.append(info)            
    
    if dest_path is None:
        dest_path = root_path
    
    # for training set
    info_path = osp.join(dest_path, f'{info_prefix}_map_infos_train.pkl')
    print(f'saving training set to {info_path}')
    mmcv.dump(train_samples, info_path)

    # for val set
    info_path = osp.join(dest_path, f'{info_prefix}_map_infos_val.pkl')
    print(f'saving validation set to {info_path}')
    mmcv.dump(val_samples, info_path)


if __name__ == '__main__':
    args = parse_args()

    create_kia_infos_map(root_path=args.data_root)