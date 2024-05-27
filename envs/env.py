from typing import Any

import gymnasium as gym
from gymnasium.core import ObsType

from util.config import EdgeEnvConfig

class EdgeEnv(gym.Env):
    def __init__(self, config: EdgeEnvConfig):
        self.config = config

        if self.config.render:
            pass

    def step(self, action):
        pass

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[ObsType, dict[str, Any]]:
        pass

    def render(self, mode: str = "human"):
        pass