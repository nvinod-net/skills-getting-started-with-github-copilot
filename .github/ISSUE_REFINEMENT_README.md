# Issue Refinement Resources

This directory contains resources and documentation for using the Refine Issue agent to enhance GitHub issues with comprehensive, structured details.

## 📚 Documentation

### [REFINE_ISSUE_GUIDE.md](REFINE_ISSUE_GUIDE.md)
Complete guide on how to use the Refine Issue agent, including:
- When and why to use issue refinement
- Step-by-step usage instructions
- Best practices for authors, reviewers, and implementers
- Quality checklist and common pitfalls
- Integration with development workflow

### [ISSUE_REFINEMENT_TEMPLATE.md](ISSUE_REFINEMENT_TEMPLATE.md)
Ready-to-use template for refining issues, including:
- All required sections with placeholders
- Detailed instructions for each section
- Usage guidelines
- Definition of Done checklist

### [ISSUE_REFINEMENT_EXAMPLE.md](ISSUE_REFINEMENT_EXAMPLE.md)
Complete example showing:
- Original basic issue
- Fully refined issue with all sections
- Real-world context from the Mergington High School API

## 🛠️ Tools

### [refine_issue_utility.py](../refine_issue_utility.py)
Python utility for programmatic issue refinement:
- Data classes for all refinement components
- Markdown generation
- Example usage demonstration

```bash
# Run the example
python refine_issue_utility.py
```

## 🚀 Quick Start

### Option 1: Use the Agent Directly

```
@refine-issue refine https://github.com/owner/repo/issues/NUMBER
```

### Option 2: Use the Template

1. Copy content from [ISSUE_REFINEMENT_TEMPLATE.md](ISSUE_REFINEMENT_TEMPLATE.md)
2. Fill in all sections
3. Update your GitHub issue

### Option 3: Use the Python Utility

```python
from refine_issue_utility import RefinedIssue, AcceptanceCriterion

# Create refinement
refined = RefinedIssue(
    title="Your Issue Title",
    original_description="Original description",
    # ... fill in other fields
)

# Generate markdown
print(refined.to_markdown())
```

## 📋 What Gets Added to Issues

When you refine an issue, it gets enriched with:

- ✅ **Detailed Description**
  - Context and background
  - User impact analysis
  
- ✅ **Acceptance Criteria**
  - Testable Given/When/Then format
  - Multiple specific scenarios
  
- ✅ **Technical Considerations**
  - Implementation approach
  - Dependencies
  - Files to modify
  - API changes
  
- ✅ **Edge Cases and Risks**
  - Potential edge scenarios
  - Risk assessment with mitigation
  
- ✅ **Non-Functional Requirements**
  - Performance expectations
  - Security considerations
  - Scalability requirements
  - Maintainability standards
  
- ✅ **Effort Estimation**
  - Story points
  - Time breakdown
  - Complexity assessment

## 🎯 Benefits

### For Development Teams
- 📝 **Clearer requirements**: Less ambiguity, fewer questions
- ⏱️ **Better estimates**: Detailed breakdown enables accurate planning
- 🎯 **Testable criteria**: Clear definition of done
- 🔍 **Risk awareness**: Proactive identification of issues

### For Stakeholders
- 👁️ **Transparency**: Understand what's being built
- 📊 **Better planning**: Realistic timelines and priorities
- 🤝 **Alignment**: Ensure everyone understands the goal

### For Quality
- ✅ **Comprehensive testing**: Edge cases identified upfront
- 🏗️ **Better architecture**: Technical considerations thought through
- 📚 **Documentation**: Requirements serve as documentation

## 📖 Reference

### Agent Configuration
The refine-issue agent is configured in:
```
.github/agents/refine-issue.agent.md
```

### Template Sections

| Section | Purpose | Required |
|---------|---------|----------|
| Context & Background | Explain the why | Yes |
| User Impact | Show who's affected | Yes |
| Acceptance Criteria | Define success | Yes |
| Technical Approach | Guide implementation | Yes |
| Dependencies | Identify prerequisites | If applicable |
| Edge Cases | Handle special scenarios | Recommended |
| Risks | Assess and mitigate | Recommended |
| NFRs | Set quality standards | Yes |
| Effort Estimation | Plan resources | Yes |
| Testing Strategy | Ensure quality | Yes |
| Documentation | Keep current | If applicable |

## 🤝 Contributing

To improve these resources:

1. **Share feedback**: Open an issue with suggestions
2. **Provide examples**: Submit refined issues that worked well
3. **Enhance templates**: Propose new sections or improvements
4. **Add domain-specific guides**: Create specialized templates for different types of work

## 📞 Support

If you have questions or need help:

1. Check the [Guide](REFINE_ISSUE_GUIDE.md) for detailed instructions
2. Review the [Example](ISSUE_REFINEMENT_EXAMPLE.md) for reference
3. Use the [Template](ISSUE_REFINEMENT_TEMPLATE.md) as a starting point
4. Open an issue if you find problems or have suggestions

## 📄 License

These resources are part of the Mergington High School API project and follow the same license.

---

**Last Updated**: 2026-02-19  
**Version**: 1.0
