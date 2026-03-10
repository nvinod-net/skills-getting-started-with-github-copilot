# Refined Issue #4: Create a Login Page with Microsoft Entra ID Authentication

## Overview

Implement a secure authentication layer for the Mergington High School Activities Management System using Microsoft Entra ID (formerly Azure Active Directory). This will ensure that only authorized students and staff can access the application and manage extracurricular activity registrations.

## Context and Background

The current application is a High School Management System that allows students to view and sign up for extracurricular activities at Mergington High School. Currently, the application has no authentication mechanism - anyone can access the system and sign up for activities using any email address.

**Current Application Stack:**
- Backend: FastAPI (Python)
- Frontend: Vanilla JavaScript, HTML, CSS
- Deployment: Single-page application with static file serving
- Data Storage: In-memory (no database currently)

**Business Need:**
- Secure the application to ensure only authorized students/staff can access it
- Validate user identities before allowing activity signups
- Provide a professional, enterprise-grade authentication experience
- Enable future features like personalized dashboards and role-based access control

## Acceptance Criteria

### Must Have (P0)
1. **Login Page Creation**
   - [ ] Create a dedicated login page at `/login` route
   - [ ] Login page displays Mergington High School branding
   - [ ] Login page includes a "Sign in with Microsoft" button
   - [ ] Unauthenticated users are redirected to login page when accessing protected routes

2. **Microsoft Entra ID Integration**
   - [ ] Application is registered in Microsoft Entra ID
   - [ ] OAuth 2.0 authorization code flow is implemented
   - [ ] Users can successfully authenticate using their Microsoft credentials
   - [ ] Access tokens are obtained and validated

3. **Session Management**
   - [ ] Authenticated sessions are maintained using secure cookies or JWT tokens
   - [ ] Session expiration is handled gracefully (redirect to login with message)
   - [ ] Logout functionality is available and properly clears the session

4. **Route Protection**
   - [ ] All existing routes (/, /activities, /activities/*/signup, /activities/*/unregister) are protected
   - [ ] Unauthenticated requests to protected routes return 401/redirect to login
   - [ ] API endpoints validate authentication before processing requests

5. **User Context**
   - [ ] Authenticated user's email is extracted from the token
   - [ ] Email domain validation ensures only @mergington.edu emails are allowed
   - [ ] User's email is automatically used for activity signups (no manual email entry needed)

### Should Have (P1)
6. **Error Handling**
   - [ ] Clear error messages for authentication failures
   - [ ] Proper error handling for token expiration
   - [ ] Network error handling with user-friendly messages

7. **UI Updates**
   - [ ] Display logged-in user's name/email in the header
   - [ ] Remove email input field from signup form (use authenticated user's email)
   - [ ] Add logout button in the navigation/header

### Could Have (P2)
8. **Enhanced Security**
   - [ ] Implement CSRF protection
   - [ ] Add security headers (X-Frame-Options, CSP, etc.)
   - [ ] Rate limiting on authentication endpoints

9. **User Experience**
   - [ ] Remember user preference for "keep me signed in"
   - [ ] Single Sign-On (SSO) experience if user is already logged into Microsoft
   - [ ] Loading indicators during authentication flow

## Technical Considerations

### Dependencies Required
```python
# requirements.txt additions
msal==1.24.0  # Microsoft Authentication Library
python-jose[cryptography]>=3.3.0  # JWT token handling
python-multipart>=0.0.6  # Form data parsing
pydantic-settings>=2.0.0  # Configuration management
```

### Configuration
- **Entra ID Application Registration**: Requires Azure AD tenant, client ID, client secret, and redirect URI
- **Environment Variables**:
  - `AZURE_CLIENT_ID`: Application (client) ID from Entra ID
  - `AZURE_CLIENT_SECRET`: Client secret value
  - `AZURE_TENANT_ID`: Directory (tenant) ID
  - `AZURE_REDIRECT_URI`: OAuth redirect URI (e.g., `http://localhost:8000/auth/callback`)
  - `SESSION_SECRET_KEY`: Secret key for session encryption

### Architecture Changes
1. **Backend (FastAPI)**:
   - Add authentication middleware to validate sessions on all requests
   - Create new auth routes: `/login`, `/auth/callback`, `/logout`
   - Modify existing endpoints to use authenticated user's email
   - Add dependency injection for current user context

2. **Frontend**:
   - Create new `login.html` page
   - Update `index.html` to display user info and logout button
   - Modify `app.js` to handle authentication state and auto-redirect
   - Remove email input field from signup form

3. **Session Storage**:
   - Consider using server-side session storage (e.g., in-memory with timeout)
   - Or stateless JWT tokens stored in httpOnly cookies

### Integration Points
- **Microsoft Entra ID**: OAuth 2.0 endpoints for authentication
- **Existing API Endpoints**: Must be updated to accept authenticated user context
- **Frontend JavaScript**: Must handle redirect flows and session state

## Edge Cases and Risks

### Edge Cases to Handle
1. **User not in Entra ID tenant**: Show clear error message, don't allow access
2. **Email domain mismatch**: User authenticates but email is not @mergington.edu
3. **Token expiration during active session**: Gracefully handle and re-authenticate
4. **Multiple tabs/windows**: Ensure consistent auth state across browser tabs
5. **Browser back button after logout**: Prevent access to cached authenticated pages
6. **Concurrent signups**: Handle race conditions if same user signs up twice simultaneously
7. **Network interruptions during auth flow**: Provide retry mechanism

### Security Risks
1. **Token Leakage**: Ensure tokens are not exposed in URLs or logs
2. **Session Hijacking**: Use secure, httpOnly cookies with proper expiration
3. **CSRF Attacks**: Implement state parameter in OAuth flow and CSRF tokens
4. **XSS Attacks**: Sanitize user input, use Content Security Policy
5. **Insecure Redirect**: Validate redirect URIs to prevent open redirect vulnerabilities

### Technical Risks
1. **Entra ID Configuration Complexity**: Setup and debugging can be time-consuming
2. **Breaking Changes to Existing Users**: Current system has no auth, adding it will disrupt workflows
3. **Testing Challenges**: Requires Microsoft tenant for testing, mocking auth flows is complex
4. **Deployment Configuration**: Environment variables must be properly configured in production

### Mitigation Strategies
- Use MSAL library (Microsoft's official SDK) to reduce implementation errors
- Implement comprehensive error logging for debugging auth issues
- Create test accounts in development Entra ID tenant
- Document configuration steps thoroughly
- Add feature flag to enable/disable authentication during rollout

## Non-Functional Requirements (NFRs)

### Performance
- Authentication flow should complete within 3 seconds (excluding Microsoft's auth time)
- Token validation should add less than 100ms overhead to API requests
- Session lookups should be optimized (O(1) complexity with in-memory cache)

### Security
- All authentication tokens must be encrypted in transit (HTTPS required in production)
- Passwords/secrets must never be stored in code or version control
- Session tokens must expire within 8 hours of inactivity
- Implement proper logout that invalidates server-side sessions

### Scalability
- Session storage should support at least 1000 concurrent users
- Consider Redis or similar for session storage if scaling beyond in-memory

### Reliability
- Authentication failure should not crash the application
- Graceful degradation: If Entra ID is unavailable, show clear error message
- 99.9% authentication success rate for valid credentials

### Usability
- Login page should be mobile-responsive
- Clear instructions for first-time users
- Error messages should be actionable (e.g., "Contact IT support at...")

### Maintainability
- Authentication logic should be modular and testable
- Configuration should be externalized (environment variables)
- Comprehensive logging for troubleshooting
- Documentation for adding new protected routes

### Compliance
- GDPR: User data (email) must be handled according to privacy regulations
- Accessibility: Login page must meet WCAG 2.1 Level AA standards
- Audit Trail: Log all authentication events (success/failure) for security auditing

## Effort Estimation

### Complexity: Medium-High
**Rationale**: Integrating OAuth 2.0 with Microsoft Entra ID requires understanding authentication flows, token management, and security best practices. However, MSAL library simplifies much of the complexity.

### Estimated Effort
- **Backend Development**: 5-8 hours
  - Entra ID app registration: 1 hour
  - Auth endpoints and middleware: 3-4 hours
  - Update existing endpoints: 1-2 hours
  - Testing and debugging: 1-2 hours

- **Frontend Development**: 3-5 hours
  - Login page UI: 1-2 hours
  - JavaScript auth flow handling: 1-2 hours
  - UI updates (header, remove email field): 1 hour

- **Testing**: 4-6 hours
  - Unit tests for auth logic: 2-3 hours
  - Integration tests for protected routes: 1-2 hours
  - Manual testing of auth flows: 1 hour

- **Documentation and Configuration**: 2-3 hours
  - Setup guide for Entra ID: 1 hour
  - Developer documentation: 1-2 hours

**Total Estimated Effort**: 14-22 hours (approximately 2-3 days for one developer)

### Dependencies and Blockers
- **Critical**: Access to Microsoft Entra ID tenant with admin permissions to register applications
- **Important**: Decision on session storage mechanism (in-memory vs external)
- **Important**: HTTPS configuration for production deployment (required by OAuth 2.0)

### Suggested Breakdown
1. **Phase 1**: Entra ID setup and basic OAuth flow (4-6 hours)
2. **Phase 2**: Session management and route protection (4-6 hours)
3. **Phase 3**: Frontend integration and UI updates (3-5 hours)
4. **Phase 4**: Testing, refinement, and documentation (3-5 hours)

## Additional Notes

### Assumptions
- The application will be deployed with HTTPS in production
- An Azure subscription with Entra ID tenant is available
- All Mergington High School students have Microsoft accounts in the tenant
- Current in-memory data storage is acceptable (no database migration needed for this phase)

### Out of Scope
- Role-based access control (RBAC) - different permissions for students vs staff
- Multi-factor authentication (MFA) - can be enforced at Entra ID level
- Account recovery and password reset - handled by Microsoft
- Migration of existing data or user accounts
- Mobile app authentication (this is web-only)

### Follow-up Considerations
- After authentication is working, consider adding role-based permissions
- Implement persistent database to retain user sessions across server restarts
- Add admin panel for managing activities (requires role-based access)
- Consider SSO integration with other school systems

## References and Resources

- [Microsoft Entra ID Documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
- [MSAL Python Documentation](https://msal-python.readthedocs.io/)
- [FastAPI Security Documentation](https://fastapi.tiangolo.com/tutorial/security/)
- [OAuth 2.0 Authorization Code Flow](https://oauth.net/2/grant-types/authorization-code/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
