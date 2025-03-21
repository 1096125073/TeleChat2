# Copyright 2020-2024 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""
MindFormers tensor_parallel API.
"""
from .layers import RowParallelLinear, ColumnParallelLinear, VocabParallelEmbedding
from .lora_layers import LoRARowParallelLinear, LoRAColumnParallelLinear

__all__ = []
__all__.extend(layers.__all__)
__all__.extend(lora_layers.__all__)
