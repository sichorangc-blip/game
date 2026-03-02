from typing import Callable, List, Optional

from .agents import AgentRole, default_roles
from .models import OrchestrationReport, WorkItem, WorkResult


class TeamOrchestrator:
    def __init__(self) -> None:
        self.roles = default_roles()
        self.pipeline: List[str] = [
            "market_research",
            "branding_manager",
            "product_reviewer",
            "sns_manager",
            "ads_manager",
            "store_manager",
            "designer",
        ]

    def run(
        self,
        goal: str,
        progress_callback: Optional[Callable[[str], None]] = None,
    ) -> OrchestrationReport:
        shared_context = {"goal": goal}
        results: List[WorkResult] = []

        for role_key in self.pipeline:
            agent: AgentRole = self.roles[role_key]
            if progress_callback is not None:
                progress_callback(f"[{agent.name}] 작업을 시작합니다.")
            work_item = WorkItem(
                role=agent.name,
                objective=f"{goal}에 대한 {agent.name} 실행안 작성",
                inputs=shared_context,
            )
            result = agent.run(work_item)
            results.append(result)
            shared_context[role_key] = result.summary
            if progress_callback is not None:
                progress_callback(f"[{agent.name}] 완료: {result.summary}")

        return OrchestrationReport(goal=goal, results=results)
