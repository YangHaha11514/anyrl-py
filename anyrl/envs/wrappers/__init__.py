"""
Environments that wrap and modify other environments.
"""

from .batched import BatchedWrapper, BatchedFrameStack
from .image import DownsampleEnv, FrameStackEnv, GrayscaleEnv
from .logs import LoggedEnv
from .meta import RL2Env, SwitchableEnv
from .padding import ObservationPadEnv, MultiBinaryPadEnv
