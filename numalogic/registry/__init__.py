# Copyright 2022 The Numaproj Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from numalogic.registry.artifact import ArtifactManager, ArtifactData, ArtifactCache
from numalogic.registry.localcache import LocalLRUCache

try:
    from numalogic.registry.mlflow_registry import MLflowRegistry
    from numalogic.registry.redis_registry import RedisRegistry
except ImportError:
    __all__ = ["ArtifactManager", "ArtifactData", "ArtifactCache", "LocalLRUCache"]
else:
    __all__ = [
        "ArtifactManager",
        "ArtifactData",
        "MLflowRegistry",
        "ArtifactCache",
        "LocalLRUCache",
        "RedisRegistry",
    ]
