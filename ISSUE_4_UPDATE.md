# Issue #4 Update - For GitHub Issue Description

> **Note**: This content should replace the current issue description in GitHub Issue #4

---

## 🎯 Create a Login Page with Microsoft Entra ID Authentication

### Overview
Implement secure authentication for the Mergington High School Activities Management System using Microsoft Entra ID (formerly Azure Active Directory) to ensure only authorized students and staff can access the application.

### Context
The current application allows anyone to access and sign up for activities without authentication. We need to add a login layer to:
- Validate user identities before allowing activity signups
- Ensure only @mergington.edu users can access the system
- Provide enterprise-grade security
- Enable future features like personalized dashboards

**Current Stack**: FastAPI (Python), Vanilla JavaScript/HTML/CSS, In-memory data storage

---

## ✅ Acceptance Criteria

### Core Requirements
- [ ] Create login page at `/login` with "Sign in with Microsoft" button
- [ ] Integrate Microsoft Entra ID OAuth 2.0 authentication
- [ ] Implement secure session management (cookies or JWT)
- [ ] Protect all routes - redirect unauthenticated users to login
- [ ] Extract and use authenticated user's email for signups
- [ ] Validate email domain (only @mergington.edu allowed)
- [ ] Add logout functionality
- [ ] Update UI to show logged-in user and remove email input field

### Error Handling
- [ ] Clear error messages for auth failures and token expiration
- [ ] Graceful handling of network errors

---

## 🛠️ Technical Considerations

### New Dependencies
```python
msal==1.24.0  # Microsoft Authentication Library
python-jose[cryptography]>=3.3.0  # JWT tokens
python-multipart>=0.0.6
pydantic-settings>=2.0.0
```

### Required Configuration
**Entra ID Setup**: Register application in Azure AD, obtain:
- Client ID
- Client Secret  
- Tenant ID
- Redirect URI

**Environment Variables**: `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID`, `AZURE_REDIRECT_URI`, `SESSION_SECRET_KEY`

### Architecture Changes
- **Backend**: Add auth middleware, create `/login`, `/auth/callback`, `/logout` routes
- **Frontend**: New login page, update header with user info, remove email input
- **Session**: Implement server-side session storage or stateless JWT

---

## ⚠️ Edge Cases & Risks

### Edge Cases
- User not in Entra ID tenant
- Email domain mismatch (@gmail.com instead of @mergington.edu)
- Token expiration during active session
- Multiple browser tabs/windows
- Browser back button after logout

### Security Risks
- Token leakage, session hijacking, CSRF/XSS attacks
- Insecure redirect vulnerabilities

**Mitigation**: Use MSAL library, httpOnly secure cookies, CSRF tokens, validate redirects, implement proper logging

---

## 📊 Non-Functional Requirements

- **Performance**: Auth flow < 3 sec, API overhead < 100ms
- **Security**: HTTPS required, tokens encrypted, 8-hour session timeout
- **Scalability**: Support 1000+ concurrent users
- **Reliability**: 99.9% auth success rate for valid credentials
- **Usability**: Mobile-responsive, clear error messages
- **Compliance**: GDPR, WCAG 2.1 Level AA accessibility

---

## ⏱️ Effort Estimation

**Complexity**: Medium-High  
**Total Effort**: 14-22 hours (2-3 days for one developer)

### Breakdown
- Backend Development: 5-8 hours
- Frontend Development: 3-5 hours  
- Testing: 4-6 hours
- Documentation: 2-3 hours

### Phases
1. Entra ID setup and OAuth flow (4-6 hrs)
2. Session management and route protection (4-6 hrs)
3. Frontend integration (3-5 hrs)
4. Testing and documentation (3-5 hrs)

### Critical Dependencies
- Access to Microsoft Entra ID tenant with admin permissions
- HTTPS configuration for production deployment

---

## 📝 Assumptions & Scope

### Assumptions
- Application will use HTTPS in production
- Azure subscription with Entra ID tenant is available
- All students have Microsoft accounts in tenant

### Out of Scope
- Role-based access control (RBAC)
- Multi-factor authentication (MFA) - enforced at Entra ID level
- Account recovery - handled by Microsoft
- Database migration

### Future Considerations
- Add role-based permissions (student vs staff)
- Implement persistent database for sessions
- Admin panel for activity management
- SSO with other school systems

---

## 📚 Resources
- [Microsoft Entra ID Documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
- [MSAL Python Documentation](https://msal-python.readthedocs.io/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [OAuth 2.0 Spec](https://oauth.net/2/grant-types/authorization-code/)
