# coding: utf-8
from alphazero.train import TrainModel

train_config = {
    'lr': 0.005,
    'c_puct': 3,
    'gamma': 0.8,
    'board_len': 7,
    'batch_size': 200,  # 500 previously
    'is_use_gpu': True,
    'n_test_games': 10,
    'n_mcts_iters': 500,
    'n_self_plays': 4000,
    'is_save_game': True,
    'n_feature_planes': 13,
    'policy_output_dim': 100,
    'check_frequency': 100,
    'start_train_size': 1000,  # 500 previously
}
train_model = TrainModel(**train_config)
train_model.train()
