from dataclasses import dataclass
from typing import Dict

from .models import WorkItem, WorkResult


@dataclass
class AgentRole:
    name: str
    kpi: str
    output_template: Dict[str, str]

    def run(self, work_item: WorkItem) -> WorkResult:
        synthesized_outputs = {
            key: f"[{self.name}] {value} | objective={work_item.objective}"
            for key, value in self.output_template.items()
        }
        return WorkResult(
            role=self.name,
            summary=f"{self.name} 역할 분석 완료",
            outputs=synthesized_outputs,
            next_actions=[
                "핵심 지표 재검증",
                "실행 전 승인 요청",
            ],
        )


def default_roles() -> Dict[str, AgentRole]:
    return {
        "market_research": AgentRole(
            name="시장조사 담당자",
            kpi="시장 기회 점수, 경쟁 강도, 수요 성장률",
            output_template={
                "market_map": "세그먼트별 TAM/SAM/SOM 요약",
                "competitor_snapshot": "상위 경쟁사 가격/리뷰/포지션",
            },
        ),
        "sns_manager": AgentRole(
            name="SNS 게시글 관리자",
            kpi="도달수, 참여율, 저장률",
            output_template={
                "content_calendar": "주간 채널별 게시 일정",
                "post_drafts": "숏폼/이미지 게시글 초안",
            },
        ),
        "store_manager": AgentRole(
            name="쇼핑스토어 운영 담당자",
            kpi="전환율, 객단가, 재구매율",
            output_template={
                "listing_plan": "상품 상세/옵션/FAQ 개선안",
                "promo_plan": "쿠폰, 번들, 타임딜 운영안",
            },
        ),
        "product_reviewer": AgentRole(
            name="신제품 개발 검토 담당자",
            kpi="출시 성공확률, 원가율, 차별화 점수",
            output_template={
                "product_risks": "원료/제조/규제 리스크",
                "mvp_scope": "MVP 스펙 및 검증 실험",
            },
        ),
        "branding_manager": AgentRole(
            name="브랜딩 담당자",
            kpi="브랜드 인지도, 선호도, 메시지 일관성",
            output_template={
                "brand_narrative": "브랜드 스토리/톤앤매너",
                "positioning_statement": "타깃별 포지셔닝 문장",
            },
        ),
        "ads_manager": AgentRole(
            name="광고 담당자",
            kpi="ROAS, CAC, CTR",
            output_template={
                "channel_mix": "예산 배분 및 채널 전략",
                "creative_test_plan": "크리에이티브 A/B 테스트 설계",
            },
        ),
        "designer": AgentRole(
            name="디자이너",
            kpi="제작 리드타임, 승인율, 성과 연계",
            output_template={
                "design_brief": "캠페인/상세페이지 디자인 브리프",
                "asset_list": "필요 시각 자산 체크리스트",
            },
        ),
    }
