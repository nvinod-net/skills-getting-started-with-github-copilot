# Refine Issue Agent Guide

This guide explains how to use the Refine Issue agent to enrich GitHub issues with comprehensive, structured details.

## Overview

The Refine Issue agent is a specialized GitHub Copilot agent that transforms basic issue descriptions into comprehensive, actionable requirements documents. It enriches issues with:

- **Detailed descriptions** with context and background
- **Acceptance criteria** in testable format
- **Technical considerations** and dependencies
- **Edge cases** and potential risks
- **Non-Functional Requirements** (NFRs)
- **Effort estimation** suggestions

## When to Use the Refine Issue Agent

Use this agent when you have:

✅ **Basic issue descriptions** that need more detail  
✅ **User stories** that lack acceptance criteria  
✅ **Feature requests** without technical specifications  
✅ **Bug reports** that need structured analysis  
✅ **Requirements** that need standardization  

## How to Use

### Method 1: Direct Issue Refinement

1. Navigate to the GitHub issue you want to refine
2. In GitHub Copilot Chat, activate the refine-issue agent:
   ```
   @refine-issue refine https://github.com/owner/repo/issues/NUMBER
   ```
3. Review the refined content
4. Update the issue with the enriched details

### Method 2: Using the Template

1. Open the [Issue Refinement Template](.github/ISSUE_REFINEMENT_TEMPLATE.md)
2. Copy the template content
3. Fill in each section with relevant details for your issue
4. Update the GitHub issue with the completed template

## Refinement Process

The agent follows these steps:

### 1. Read and Understand
- Analyzes the original issue description
- Identifies the core problem or feature request
- Gathers context from related code and documentation

### 2. Enrich Context
Adds detailed background including:
- Current state analysis
- Problem statement clarity
- User impact assessment
- Business value proposition

### 3. Define Acceptance Criteria
Creates testable criteria using Given/When/Then format:
```
GIVEN [initial state]
WHEN [action occurs]
THEN [expected outcome]
AND [additional requirements]
```

### 4. Technical Analysis
Identifies:
- Implementation approach
- Dependencies and prerequisites
- Files and components to modify
- API/interface changes

### 5. Risk Assessment
Documents:
- Potential edge cases
- Technical risks
- Mitigation strategies
- Known limitations

### 6. Non-Functional Requirements
Defines NFRs for:
- Performance expectations
- Security considerations
- Scalability requirements
- Maintainability standards
- Reliability targets
- Accessibility needs

### 7. Effort Estimation
Provides:
- Story point estimate
- Time breakdown
- Complexity assessment
- Resource requirements

## Best Practices

### For Issue Authors

1. **Provide context**: Include as much relevant information as possible in the original issue
2. **Be specific**: Clearly state what you want to achieve
3. **Include examples**: Screenshots, error messages, or use cases help
4. **Link related issues**: Help the agent understand dependencies

### For Reviewers

1. **Validate acceptance criteria**: Ensure they are testable and complete
2. **Check technical feasibility**: Review implementation approach
3. **Assess estimates**: Confirm effort estimates are realistic
4. **Verify completeness**: Ensure all relevant sections are filled

### For Implementers

1. **Use acceptance criteria**: As a checklist for development
2. **Follow technical approach**: Unless you have a better solution
3. **Handle edge cases**: Test all documented scenarios
4. **Meet NFRs**: Don't skip non-functional requirements

## Example Workflow

### Original Issue
```markdown
Title: Add capacity validation

Description:
Users should not be able to register for activities that are full.
```

### After Refinement
The issue now includes:
- ✅ Detailed context about why this matters
- ✅ 4 specific acceptance criteria
- ✅ Technical implementation approach
- ✅ 4 identified edge cases
- ✅ NFRs for performance, security, and maintainability
- ✅ 2-4 hour effort estimate with breakdown
- ✅ Testing strategy and documentation requirements

See [ISSUE_REFINEMENT_EXAMPLE.md](ISSUE_REFINEMENT_EXAMPLE.md) for the complete example.

## Customization

You can customize the refinement process by:

### Adjusting Agent Configuration

Edit `.github/agents/refine-issue.agent.md` to:
- Add domain-specific sections
- Modify the refinement steps
- Include custom validation rules
- Add team-specific standards

### Creating Custom Templates

Modify `ISSUE_REFINEMENT_TEMPLATE.md` to:
- Add project-specific sections
- Include regulatory requirements
- Add team workflows
- Incorporate company standards

## Quality Checklist

Before finalizing a refined issue, ensure:

- [ ] **Context is clear**: Anyone can understand the problem/feature
- [ ] **Acceptance criteria are testable**: Can verify when complete
- [ ] **Technical approach is sound**: Feasible and appropriate
- [ ] **Edge cases are identified**: Nothing obvious is missing
- [ ] **NFRs are defined**: Performance, security, etc. are considered
- [ ] **Estimate is realistic**: Time and complexity make sense
- [ ] **All sections are complete**: No TBD or placeholder text

## Common Pitfalls to Avoid

❌ **Vague acceptance criteria**: "System should work well"  
✅ **Specific criteria**: "API responds in < 200ms for 95% of requests"

❌ **Missing edge cases**: Only considering happy path  
✅ **Comprehensive scenarios**: Happy path + error cases + boundaries

❌ **Ignoring NFRs**: Only focusing on functionality  
✅ **Balanced requirements**: Functionality + performance + security + UX

❌ **Unrealistic estimates**: Not accounting for testing/review  
✅ **Complete estimates**: Implementation + testing + review + documentation

## Integration with Development Workflow

### Planning Phase
1. Create basic issue
2. Refine with agent
3. Review in planning meeting
4. Adjust based on team feedback
5. Approve and assign

### Development Phase
- Use acceptance criteria as development checklist
- Follow technical approach outlined
- Handle all identified edge cases
- Meet NFR targets

### Review Phase
- Verify all acceptance criteria met
- Check NFRs are satisfied
- Validate edge cases handled
- Confirm documentation updated

### Completion Phase
- Update issue with results
- Link to PR
- Note any deviations from plan
- Document lessons learned

## Support and Resources

- **Template**: [ISSUE_REFINEMENT_TEMPLATE.md](ISSUE_REFINEMENT_TEMPLATE.md)
- **Example**: [ISSUE_REFINEMENT_EXAMPLE.md](ISSUE_REFINEMENT_EXAMPLE.md)
- **Agent Config**: `.github/agents/refine-issue.agent.md`

## Feedback

To improve the Refine Issue agent:
1. Open an issue with your suggestions
2. Share examples of good/bad refinements
3. Propose template improvements
4. Contribute custom sections for specific domains

---

**Last Updated**: 2026-02-19  
**Version**: 1.0  
**Maintained By**: Development Team
