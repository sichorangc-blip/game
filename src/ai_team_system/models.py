from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class WorkItem:
    role: str
    objective: str
    inputs: Dict[str, str]


@dataclass
class WorkResult:
    role: str
    summary: str
    outputs: Dict[str, str]
    next_actions: List[str] = field(default_factory=list)


@dataclass
class OrchestrationReport:
    goal: str
    results: List[WorkResult]

    def as_dict(self) -> Dict[str, object]:
        return {
            "goal": self.goal,
            "results": [
                {
                    "role": item.role,
                    "summary": item.summary,
                    "outputs": item.outputs,
                    "next_actions": item.next_actions,
                }
                for item in self.results
            ],
        }
