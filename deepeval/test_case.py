"""Investigate test case.
"""
import hashlib
from dataclasses import dataclass
from typing import Any, List, Optional

from .metrics.metric import Metric


@dataclass
class TestCase:
    id: Optional[str] = None

    def __post_init__(self):
        if self.id is None:
            id_string = "".join(str(value) for value in self.__dict__.values())
            self.id = hashlib.md5(id_string.encode()).hexdigest()


@dataclass
class LLMTestCase(TestCase):
    query: Optional[str] = None
    expected_output: Optional[str] = None
    context: Optional[str] = None
    metrics: Optional[List[Metric]] = None
    output: Optional[str] = None

    def dict(self):
        data = {
            "metrics": self.metrics,
            "id": self.id,
        }
        if self.query:
            data["query"] = self.query
        if self.expected_output:
            data["expected_output"] = self.expected_output
        if self.context:
            data["context"] = self.context
        if self.output:
            data["output"] = self.output
        return data


@dataclass
class SearchTestCase(TestCase):
    output_list: List[Any]
    golden_list: List[Any]


class AgentTestCase(TestCase):
    """Test Case For Agents"""

    pass
