"""
Issue Refinement Utility

This script demonstrates how to refine GitHub issues programmatically
by adding structured details including acceptance criteria, technical
considerations, edge cases, and NFRs.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AcceptanceCriterion:
    """Represents a single acceptance criterion in Given/When/Then format"""
    name: str
    given: str
    when: str
    then: str
    additional: List[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        """Convert to markdown format"""
        lines = [
            f"**{self.name}**",
            f"   - GIVEN {self.given}",
            f"   - WHEN {self.when}",
            f"   - THEN {self.then}"
        ]
        for item in self.additional:
            lines.append(f"   - AND {item}")
        return "\n".join(lines)


@dataclass
class EdgeCase:
    """Represents an edge case to handle"""
    name: str
    description: str
    handling: str

    def to_markdown(self) -> str:
        """Convert to markdown format"""
        return f"**{self.name}**: {self.description}\n   - {self.handling}"


@dataclass
class Risk:
    """Represents a potential risk"""
    category: str
    description: str
    impact: str  # High, Medium, Low
    probability: str  # High, Medium, Low
    mitigation: str

    def to_markdown(self) -> str:
        """Convert to markdown format"""
        return (
            f"**{self.category}**: {self.description}\n"
            f"  - Impact: {self.impact}\n"
            f"  - Probability: {self.probability}\n"
            f"  - Mitigation: {self.mitigation}"
        )


@dataclass
class NonFunctionalRequirement:
    """Represents a non-functional requirement"""
    category: str  # Performance, Security, Scalability, etc.
    requirements: List[str]

    def to_markdown(self) -> str:
        """Convert to markdown format"""
        lines = [f"#### {self.category}"]
        for req in self.requirements:
            lines.append(f"- {req}")
        return "\n".join(lines)


@dataclass
class RefinedIssue:
    """Represents a fully refined GitHub issue"""
    title: str
    original_description: str
    
    # Context
    context_background: str
    user_impact: Dict[str, str]
    
    # Acceptance Criteria
    acceptance_criteria: List[AcceptanceCriterion]
    
    # Technical
    implementation_approach: List[str]
    dependencies: List[str]
    files_to_modify: Dict[str, str]
    api_changes: Optional[str] = None
    
    # Risks
    edge_cases: List[EdgeCase] = field(default_factory=list)
    risks: List[Risk] = field(default_factory=list)
    
    # NFRs
    nfrs: List[NonFunctionalRequirement] = field(default_factory=list)
    
    # Estimation
    story_points: int = 0
    estimated_hours: str = ""
    time_breakdown: Dict[str, str] = field(default_factory=dict)
    complexity: str = "Medium"
    complexity_reasons: List[str] = field(default_factory=list)
    
    # Additional
    related_issues: List[str] = field(default_factory=list)
    testing_strategy: List[str] = field(default_factory=list)
    documentation_updates: List[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        """Generate complete markdown for the refined issue"""
        sections = []
        
        # Title
        sections.append(f"# {self.title}\n")
        
        # Original Issue
        sections.append("## Original Issue\n")
        sections.append(f"{self.original_description}\n")
        sections.append("---\n")
        
        # Detailed Description
        sections.append("### 📋 Detailed Description\n")
        sections.append("#### Context and Background")
        sections.append(f"{self.context_background}\n")
        
        if self.user_impact:
            sections.append("#### User Impact")
            for persona, impact in self.user_impact.items():
                sections.append(f"- **{persona}**: {impact}")
            sections.append("")
        
        # Acceptance Criteria
        sections.append("### ✅ Acceptance Criteria\n")
        for i, criterion in enumerate(self.acceptance_criteria, 1):
            sections.append(f"{i}. {criterion.to_markdown()}\n")
        
        # Technical Considerations
        sections.append("### 🔧 Technical Considerations\n")
        sections.append("#### Implementation Approach")
        for item in self.implementation_approach:
            sections.append(f"- {item}")
        sections.append("")
        
        if self.dependencies:
            sections.append("#### Dependencies")
            for dep in self.dependencies:
                sections.append(f"- {dep}")
            sections.append("")
        
        if self.files_to_modify:
            sections.append("#### Files to Modify")
            for file, change in self.files_to_modify.items():
                sections.append(f"- `{file}` - {change}")
            sections.append("")
        
        if self.api_changes:
            sections.append("#### API Contract Changes")
            sections.append(self.api_changes)
            sections.append("")
        
        # Edge Cases and Risks
        sections.append("### ⚠️ Edge Cases and Risks\n")
        if self.edge_cases:
            sections.append("#### Edge Cases to Handle")
            for i, edge_case in enumerate(self.edge_cases, 1):
                sections.append(f"{i}. {edge_case.to_markdown()}\n")
        
        if self.risks:
            sections.append("#### Potential Risks")
            for risk in self.risks:
                sections.append(f"- {risk.to_markdown()}\n")
        
        # NFRs
        if self.nfrs:
            sections.append("### 📊 Non-Functional Requirements (NFRs)\n")
            for nfr in self.nfrs:
                sections.append(nfr.to_markdown())
                sections.append("")
        
        # Effort Estimation
        sections.append("### 📈 Effort Estimation\n")
        sections.append(f"**Story Points:** {self.story_points}\n")
        sections.append(f"**Estimated Time:** {self.estimated_hours}\n")
        
        if self.time_breakdown:
            sections.append("**Breakdown:**")
            for category, time in self.time_breakdown.items():
                sections.append(f"- **{category}:** {time}")
            sections.append("")
        
        sections.append(f"**Complexity:** {self.complexity}")
        for reason in self.complexity_reasons:
            sections.append(f"- {reason}")
        sections.append("")
        
        # Additional Notes
        sections.append("### 📝 Additional Notes\n")
        
        if self.related_issues:
            sections.append("#### Related Issues")
            for issue in self.related_issues:
                sections.append(f"- {issue}")
            sections.append("")
        
        if self.testing_strategy:
            sections.append("#### Testing Strategy")
            for strategy in self.testing_strategy:
                sections.append(f"- {strategy}")
            sections.append("")
        
        if self.documentation_updates:
            sections.append("#### Documentation Updates Required")
            for doc in self.documentation_updates:
                sections.append(f"- {doc}")
            sections.append("")
        
        return "\n".join(sections)


def create_example_refinement() -> RefinedIssue:
    """Create an example refined issue for capacity validation"""
    return RefinedIssue(
        title="Add capacity validation for activity registration",
        original_description="Users should not be able to register for activities that are already full.",
        
        context_background=(
            "The Mergington High School Activities API currently allows unlimited participants "
            "to sign up for activities, even when the max_participants limit has been reached. "
            "This can lead to overcrowded activities that exceed safety limits and available resources."
        ),
        
        user_impact={
            "Students": "May register for activities that are actually full, leading to confusion",
            "Activity Coordinators": "Cannot rely on the system to enforce capacity limits",
            "School Administrators": "Risk safety and resource management issues from overcrowding"
        },
        
        acceptance_criteria=[
            AcceptanceCriterion(
                name="AC1: Reject signup when activity is at capacity",
                given="an activity has reached max_participants limit",
                when="a student attempts to sign up",
                then="the API returns HTTP 400 status code",
                additional=["an error message indicates the activity is full"]
            ),
            AcceptanceCriterion(
                name="AC2: Allow signup when activity has available capacity",
                given="an activity has not reached max_participants limit",
                when="a student attempts to sign up",
                then="the registration succeeds (HTTP 200)",
                additional=["the student is added to the participants list"]
            ),
        ],
        
        implementation_approach=[
            "Add validation logic in the signup_for_activity() function",
            "Check len(activity['participants']) against activity['max_participants']",
            "Implement before existing duplicate participant check"
        ],
        
        dependencies=[
            "No new dependencies required",
            "Uses existing FastAPI HTTPException for error handling"
        ],
        
        files_to_modify={
            "src/app.py": "Add capacity validation logic",
            "tests/test_api.py": "Add test cases for capacity validation"
        },
        
        edge_cases=[
            EdgeCase(
                name="Race condition",
                description="Multiple simultaneous signups when 1 spot remains",
                handling="Current in-memory storage is not thread-safe. Document as known limitation."
            ),
            EdgeCase(
                name="Activities with 0 max_participants",
                description="Edge case where activity allows 0 participants",
                handling="Should reject all signups"
            )
        ],
        
        risks=[
            Risk(
                category="Breaking change",
                description="Existing integrations expecting unlimited signups will fail",
                impact="Medium",
                probability="Low",
                mitigation="This is a bug fix, correct behavior is to enforce limits"
            )
        ],
        
        nfrs=[
            NonFunctionalRequirement(
                category="Performance",
                requirements=[
                    "Validation should add < 1ms overhead to signup endpoint",
                    "No additional database/external calls required"
                ]
            ),
            NonFunctionalRequirement(
                category="Security",
                requirements=[
                    "Prevents resource exhaustion by limiting participants"
                ]
            )
        ],
        
        story_points=2,
        estimated_hours="2-4 hours",
        time_breakdown={
            "Implementation": "30 minutes",
            "Testing": "1-2 hours",
            "Documentation": "30 minutes",
            "Code Review": "1 hour"
        },
        complexity="Low",
        complexity_reasons=[
            "Single function modification",
            "Clear requirements",
            "Existing test infrastructure"
        ],
        
        testing_strategy=[
            "Unit tests for validation logic",
            "Integration tests for complete signup flow",
            "Test both boundary conditions (exactly at capacity, one over)"
        ],
        
        documentation_updates=[
            "Update API documentation",
            "Update README.md API endpoints table"
        ]
    )


if __name__ == "__main__":
    # Create and print example refinement
    refined = create_example_refinement()
    print(refined.to_markdown())
