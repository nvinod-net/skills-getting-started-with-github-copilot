# Issue Refinement Template

Use this template when refining GitHub issues to ensure comprehensive and actionable requirements.

---

## Original Issue

**Title:** [Original Issue Title]

**Description:**
[Original brief description]

---

## Refined Issue Structure

### 📋 Detailed Description

#### Context and Background
[Provide comprehensive context about why this issue exists, what problem it solves, and relevant background information]

- What is the current state?
- What problem does this solve?
- Who is affected?
- What business value does this provide?

#### User Impact
[Describe the impact on different user personas]
- **[Persona 1]**: [Impact description]
- **[Persona 2]**: [Impact description]
- **[Persona 3]**: [Impact description]

### ✅ Acceptance Criteria

[List specific, testable criteria in Given/When/Then format]

1. **AC1: [Criterion Name]**
   - GIVEN [initial context/state]
   - WHEN [action taken]
   - THEN [expected outcome]
   - AND [additional expectations]

2. **AC2: [Criterion Name]**
   - GIVEN [initial context/state]
   - WHEN [action taken]
   - THEN [expected outcome]

3. **AC3: [Criterion Name]**
   - GIVEN [initial context/state]
   - WHEN [action taken]
   - THEN [expected outcome]

### 🔧 Technical Considerations

#### Implementation Approach
[High-level approach to implementing the solution]
- Key architectural decisions
- Recommended patterns or practices
- Integration points

#### Dependencies
[List any dependencies]
- External libraries or packages
- Internal modules or services
- Infrastructure requirements
- Third-party services

#### Files to Modify
[List specific files that will likely need changes]
- `path/to/file1.ext` - [What changes]
- `path/to/file2.ext` - [What changes]
- `path/to/file3.ext` - [What changes]

#### API/Interface Changes
[Document any changes to public APIs, interfaces, or contracts]
- New endpoints or methods
- Modified request/response formats
- Breaking changes (if any)
- Backward compatibility considerations

### ⚠️ Edge Cases and Risks

#### Edge Cases to Handle
[Identify potential edge cases that need explicit handling]

1. **[Edge Case 1]**: [Description]
   - [How it should be handled]
   - [Any specific considerations]

2. **[Edge Case 2]**: [Description]
   - [How it should be handled]

3. **[Edge Case 3]**: [Description]
   - [How it should be handled]

#### Potential Risks
[Identify and describe potential risks]

- **[Risk Category 1]**: [Description]
  - Impact: [High/Medium/Low]
  - Probability: [High/Medium/Low]
  - Mitigation: [How to mitigate]

- **[Risk Category 2]**: [Description]
  - Impact: [High/Medium/Low]
  - Probability: [High/Medium/Low]
  - Mitigation: [How to mitigate]

### 📊 Non-Functional Requirements (NFRs)

#### Performance
[Performance requirements and expectations]
- Response time targets
- Throughput requirements
- Resource utilization limits
- Performance testing approach

#### Security
[Security considerations and requirements]
- Authentication/Authorization changes
- Data protection requirements
- Security testing needed
- Compliance considerations

#### Scalability
[Scalability considerations]
- Expected load/volume
- Horizontal/vertical scaling implications
- Bottlenecks to avoid

#### Maintainability
[Code quality and maintainability standards]
- Code documentation requirements
- Naming conventions
- Testing coverage expectations
- Refactoring opportunities

#### Reliability
[Reliability and availability requirements]
- Error handling strategy
- Fault tolerance
- Recovery procedures
- Monitoring and alerting

#### Accessibility
[Accessibility requirements if applicable]
- WCAG compliance level
- Screen reader support
- Keyboard navigation
- Color contrast requirements

### 📈 Effort Estimation

**Story Points:** [Fibonacci number: 1, 2, 3, 5, 8, 13]

**Estimated Time:** [Hour/day range]

**Breakdown:**
- **Implementation:** [Time estimate]
  - [Sub-task 1] ([time])
  - [Sub-task 2] ([time])
- **Testing:** [Time estimate]
  - [Testing activity 1] ([time])
  - [Testing activity 2] ([time])
- **Documentation:** [Time estimate]
- **Code Review & Refinement:** [Time estimate]

**Complexity:** [Low/Medium/High]
- [Reason 1 for complexity level]
- [Reason 2 for complexity level]
- [Reason 3 for complexity level]

**Assumptions:**
- [Assumption 1]
- [Assumption 2]

### 📝 Additional Notes

#### Related Issues
[Link to related issues or future work]
- #[issue-number] - [Relationship description]
- #[issue-number] - [Relationship description]

#### Testing Strategy
[Outline the testing approach]
- Unit tests: [What to test]
- Integration tests: [What to test]
- Manual testing: [What to verify]
- Performance testing: [If needed]

#### Documentation Updates Required
[List documentation that needs updating]
- [ ] API documentation
- [ ] README.md
- [ ] User guides
- [ ] Architecture diagrams
- [ ] Inline code comments
- [ ] Changelog

#### Definition of Done
[Checklist for completion]
- [ ] Code implemented and reviewed
- [ ] All acceptance criteria met
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] No new security vulnerabilities
- [ ] Performance benchmarks met
- [ ] Deployed to staging environment
- [ ] Stakeholder approval obtained

---

## Refinement Metadata

**Refined By:** [Name/Username]  
**Refinement Date:** [YYYY-MM-DD]  
**Original Issue:** [Link to original issue]  
**Review Status:** [Draft/In Review/Approved]

---

## Usage Instructions

1. Copy this template
2. Fill in each section with relevant details
3. Remove sections that don't apply (mark with N/A if uncertain)
4. Ensure acceptance criteria are testable and specific
5. Have the refinement reviewed by at least one other team member
6. Update the original issue with the refined content
