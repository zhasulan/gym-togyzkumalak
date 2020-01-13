import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Toguzkumalak-v0',
    entry_point='gym_toguzkumalak.envs:ToguzkumalakEnv',
)
