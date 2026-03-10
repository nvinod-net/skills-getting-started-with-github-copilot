# User Authentication Implementation Plan
## Mergington High School Activities Management System

---

## Overview

### Problem Statement
The Mergington High School Activities Management System currently allows anyone to sign up for activities using any email address without verification. This creates several issues:
- No validation that users are actual students
- No way to prevent unauthorized access to activity management
- No protection against malicious activity registrations
- No ability to track user history or preferences
- No administrative controls for managing activities

### Success Criteria
A successful implementation of user authentication will achieve the following:
- **Security**: Only authenticated students can sign up for activities
- **Identity Verification**: Users must verify their email addresses
- **Session Management**: Secure, token-based authentication with automatic expiry
- **User Experience**: Simple, intuitive login/signup flow with minimal friction
- **Administrative Access**: Role-based access control for administrators
- **Data Protection**: Passwords stored securely using industry-standard hashing
- **API Security**: All sensitive endpoints protected with authentication middleware

### Target Users
1. **Students**: High school students at Mergington High School who want to browse and sign up for extracurricular activities
2. **Administrators**: School staff who need to manage activities, view registrations, and moderate content
3. **System Administrators**: Technical staff who maintain the system and user accounts

---

## Technical Approach

### Architecture Overview
We will implement a **JWT (JSON Web Token) based authentication system** with the following components:

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (HTML/JS)                       │
│  - Login/Signup Forms                                        │
│  - JWT Token Storage (localStorage)                          │
│  - Authenticated API Requests                                │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  FastAPI Backend                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Authentication Middleware                               ││
│  │  - Token Validation                                      ││
│  │  - User Session Management                               ││
│  └─────────────────────────────────────────────────────────┘│
│  ┌─────────────────────────────────────────────────────────┐│
│  │  User Management Module                                  ││
│  │  - Registration                                          ││
│  │  - Login/Logout                                          ││
│  │  - Password Reset                                        ││
│  │  - Email Verification                                    ││
│  └─────────────────────────────────────────────────────────┘│
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Protected Endpoints                                     ││
│  │  - Activity Signup (requires auth)                       ││
│  │  - Activity Management (admin only)                      ││
│  │  - User Profile                                          ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Database Layer                             │
│  - User Table (id, email, hashed_password, role, verified)  │
│  - Session Table (token, user_id, expires_at)               │
│  - Activity Signup Table (user_id, activity_id, timestamp)  │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

#### Core Dependencies
- **FastAPI**: Web framework (already in use)
- **python-jose[cryptography]**: JWT token generation and validation
- **passlib[bcrypt]**: Password hashing using bcrypt algorithm
- **python-multipart**: Form data parsing for login endpoints
- **pydantic[email]**: Email validation
- **SQLAlchemy**: ORM for database operations
- **alembic**: Database migrations

#### Optional/Future Dependencies
- **fastapi-mail**: Email verification and password reset emails
- **redis**: Session storage and rate limiting (for production)
- **python-dotenv**: Environment variable management

### Key Technical Decisions

#### 1. Database Choice
**Decision**: Use SQLite for development, with easy migration path to PostgreSQL for production

**Rationale**: 
- Current system uses in-memory storage
- SQLite requires no additional setup for development
- SQLAlchemy provides database-agnostic code
- Can upgrade to PostgreSQL without code changes

**Trade-offs**:
- SQLite is file-based and not suitable for high-concurrency production use
- Will need migration plan for production deployment

#### 2. Authentication Strategy
**Decision**: JWT (JSON Web Tokens) with Bearer token authentication

**Rationale**:
- Stateless authentication scales better than session cookies
- Works well with REST APIs
- Easy to implement in both backend and frontend
- Industry standard for modern web applications

**Trade-offs**:
- Cannot invalidate tokens before expiry (need token blacklist for logout)
- Requires secure token storage on client side
- Need to implement token refresh mechanism

#### 3. Password Security
**Decision**: Use bcrypt with cost factor of 12 for password hashing

**Rationale**:
- Bcrypt is specifically designed for password hashing
- Automatically handles salt generation
- Configurable cost factor allows future-proofing
- Industry standard with no known vulnerabilities

**Trade-offs**:
- Slower than generic hash functions (this is intentional for security)
- Higher CPU usage during authentication

#### 4. Email Verification
**Decision**: Phase 1 will skip email verification; Phase 2 will add it

**Rationale**:
- Allows faster initial implementation
- Email verification requires SMTP configuration
- Can validate implementation with manual verification first

**Trade-offs**:
- Initial version will trust email addresses
- Need to restrict signups to @mergington.edu domain

### Data Models

#### User Model
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, default="student")  # "student" or "admin"
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

#### Activity Signup Model
```python
class ActivitySignup(Base):
    __tablename__ = "activity_signups"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    activity_name = Column(String, nullable=False)
    signed_up_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="signups")
```

### API Design

#### Authentication Endpoints

```
POST /api/auth/register
Request:
{
  "email": "student@mergington.edu",
  "password": "SecurePassword123!",
  "full_name": "John Doe"
}
Response: 
{
  "id": 1,
  "email": "student@mergington.edu",
  "full_name": "John Doe",
  "role": "student"
}

POST /api/auth/login
Request (form-data):
  username: student@mergington.edu
  password: SecurePassword123!
Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600
}

GET /api/auth/me
Headers: Authorization: Bearer <token>
Response:
{
  "id": 1,
  "email": "student@mergington.edu",
  "full_name": "John Doe",
  "role": "student"
}

POST /api/auth/logout
Headers: Authorization: Bearer <token>
Response:
{
  "message": "Successfully logged out"
}
```

#### Protected Endpoints (Modified)

```
POST /api/activities/{activity_name}/signup
Headers: Authorization: Bearer <token>
Response:
{
  "message": "Signed up for Chess Club",
  "activity": "Chess Club"
}

DELETE /api/activities/{activity_name}/unregister
Headers: Authorization: Bearer <token>
Response:
{
  "message": "Unregistered from Chess Club"
}
```

### Security Measures

1. **Password Requirements**:
   - Minimum 8 characters
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one number
   - At least one special character

2. **Email Domain Validation**:
   - Only allow @mergington.edu email addresses
   - Case-insensitive email matching

3. **Rate Limiting**:
   - Login attempts: 5 per 15 minutes per IP
   - Registration: 3 per hour per IP
   - Password reset: 3 per hour per email

4. **Token Security**:
   - Access tokens expire after 1 hour
   - Refresh tokens expire after 7 days
   - Tokens include user ID and role claims
   - Signature verification on every request

5. **CORS Configuration**:
   - Restrict origins to school domain
   - Credentials allowed for authenticated requests

---

## Implementation Plan

### Phase 1: Foundation (Week 1)
**Goal**: Set up database, user model, and basic authentication infrastructure

#### Tasks:

**1.1 Database Setup** (Medium)
- [ ] Add SQLAlchemy and Alembic to requirements.txt
- [ ] Create database configuration module
- [ ] Set up SQLAlchemy Base and session management
- [ ] Initialize Alembic for migrations
- [ ] Create initial migration for users table

**1.2 User Model and Schema** (Medium)
- [ ] Create User database model
- [ ] Create Pydantic schemas for User (UserCreate, UserResponse, UserInDB)
- [ ] Add password validation utility functions
- [ ] Add email domain validation (@mergington.edu only)

**1.3 Password Security** (Small)
- [ ] Add passlib to requirements.txt
- [ ] Create password hashing utility functions
- [ ] Create password verification functions
- [ ] Add password strength validation

**1.4 JWT Token Management** (Medium)
- [ ] Add python-jose to requirements.txt
- [ ] Create JWT token generation function
- [ ] Create token verification function
- [ ] Add token expiration handling
- [ ] Create environment configuration for SECRET_KEY

**Dependencies**: None
**Testing**: Unit tests for password hashing, token generation/validation, email validation

---

### Phase 2: Core Authentication (Week 2)
**Goal**: Implement registration, login, and authentication middleware

#### Tasks:

**2.1 User Registration** (Large)
- [ ] Create POST /api/auth/register endpoint
- [ ] Validate email uniqueness
- [ ] Validate email domain (@mergington.edu)
- [ ] Hash password before storage
- [ ] Create user record in database
- [ ] Return user information (excluding password)
- [ ] Add error handling for duplicate emails

**2.2 User Login** (Large)
- [ ] Create POST /api/auth/login endpoint
- [ ] Validate credentials against database
- [ ] Generate JWT access token on success
- [ ] Generate refresh token
- [ ] Return tokens and user information
- [ ] Add error handling for invalid credentials
- [ ] Add rate limiting for failed attempts

**2.3 Authentication Middleware** (Medium)
- [ ] Create dependency for token validation
- [ ] Extract and verify JWT from Authorization header
- [ ] Load user from database based on token claims
- [ ] Handle expired or invalid tokens
- [ ] Create role-based authorization dependencies

**2.4 Current User Endpoint** (Small)
- [ ] Create GET /api/auth/me endpoint
- [ ] Return current user's information
- [ ] Require authentication

**Dependencies**: Phase 1 must be complete
**Testing**: Integration tests for registration, login, protected endpoints

---

### Phase 3: Frontend Integration (Week 3)
**Goal**: Update UI to support authentication and protect activity signups

#### Tasks:

**3.1 Login/Signup Forms** (Large)
- [ ] Create login.html page with form
- [ ] Create signup.html page with form
- [ ] Add CSS styling for auth pages
- [ ] Add client-side validation for email and password
- [ ] Add error message display

**3.2 Token Management** (Medium)
- [ ] Implement token storage in localStorage
- [ ] Add token to all API requests via fetch interceptor
- [ ] Implement token expiry handling
- [ ] Add automatic redirect to login on 401 responses

**3.3 UI Updates** (Medium)
- [ ] Add navigation menu with Login/Signup links
- [ ] Add "Logout" button when authenticated
- [ ] Display current user information in header
- [ ] Show/hide features based on authentication state
- [ ] Update signup form to use authenticated endpoint

**3.4 User Experience** (Small)
- [ ] Add loading states for authentication actions
- [ ] Add success/error notifications
- [ ] Implement remember me functionality
- [ ] Add password visibility toggle

**Dependencies**: Phase 2 must be complete
**Testing**: Manual UI testing, E2E tests for user flows

---

### Phase 4: Protected Endpoints (Week 4)
**Goal**: Secure existing endpoints and migrate data model

#### Tasks:

**4.1 Database Migration** (Large)
- [ ] Create ActivitySignup model
- [ ] Create migration to add activity_signups table
- [ ] Create migration script to convert in-memory data to database
- [ ] Update activities to reference ActivitySignup table
- [ ] Remove in-memory activities dictionary

**4.2 Protect Activity Endpoints** (Medium)
- [ ] Add authentication requirement to POST /activities/{activity_name}/signup
- [ ] Update signup logic to use current user's ID instead of email parameter
- [ ] Add authentication to DELETE /activities/{activity_name}/unregister
- [ ] Update unregister logic to verify user owns the signup
- [ ] Add authorization checks (user can only modify their own signups)

**4.3 User Activity Management** (Medium)
- [ ] Create GET /api/user/activities endpoint (my activities)
- [ ] Create GET /api/user/profile endpoint
- [ ] Create PUT /api/user/profile endpoint (update profile)
- [ ] Add activity history tracking

**4.4 API Documentation** (Small)
- [ ] Update OpenAPI/Swagger documentation
- [ ] Add authentication examples to docs
- [ ] Document all new endpoints
- [ ] Update existing endpoint documentation

**Dependencies**: Phase 3 must be complete
**Testing**: Integration tests for protected endpoints, authorization tests

---

### Phase 5: Administration & Polish (Week 5)
**Goal**: Add admin features, improve security, and polish the implementation

#### Tasks:

**5.1 Admin Endpoints** (Large)
- [ ] Create GET /api/admin/users endpoint (list all users)
- [ ] Create PUT /api/admin/users/{user_id}/role endpoint (change user role)
- [ ] Create DELETE /api/admin/users/{user_id} endpoint (deactivate user)
- [ ] Create GET /api/admin/activities/{activity_name}/participants endpoint
- [ ] Add admin-only authorization checks

**5.2 Token Refresh** (Medium)
- [ ] Implement refresh token storage in database
- [ ] Create POST /api/auth/refresh endpoint
- [ ] Add automatic token refresh in frontend
- [ ] Implement token rotation for security

**5.3 Enhanced Security** (Large)
- [ ] Implement rate limiting using middleware
- [ ] Add CORS configuration
- [ ] Add request logging for security events
- [ ] Implement token blacklist for logout
- [ ] Add brute force protection for login
- [ ] Add input sanitization

**5.4 Error Handling & Validation** (Medium)
- [ ] Standardize error response format
- [ ] Add comprehensive validation error messages
- [ ] Improve HTTP status code usage
- [ ] Add request/response logging
- [ ] Create custom exception handlers

**5.5 Testing & Documentation** (Large)
- [ ] Write comprehensive unit tests (target: 80% coverage)
- [ ] Write integration tests for all auth flows
- [ ] Create API usage guide
- [ ] Create deployment guide
- [ ] Document environment variables
- [ ] Add inline code documentation

**Dependencies**: Phase 4 must be complete
**Testing**: Full regression testing, security testing, load testing

---

### Phase 6: Email Verification (Optional - Week 6)
**Goal**: Add email verification for enhanced security

#### Tasks:

**6.1 Email Infrastructure** (Medium)
- [ ] Add fastapi-mail to requirements.txt
- [ ] Configure SMTP settings
- [ ] Create email templates for verification
- [ ] Create email sending utility

**6.2 Verification Flow** (Large)
- [ ] Generate verification tokens on registration
- [ ] Send verification email after signup
- [ ] Create GET /api/auth/verify/{token} endpoint
- [ ] Update login to check verification status
- [ ] Create POST /api/auth/resend-verification endpoint
- [ ] Add verification status to user profile

**6.3 Password Reset** (Large)
- [ ] Create POST /api/auth/forgot-password endpoint
- [ ] Generate password reset tokens
- [ ] Send password reset email
- [ ] Create POST /api/auth/reset-password endpoint
- [ ] Add password reset flow to frontend
- [ ] Add rate limiting for reset requests

**Dependencies**: Phase 5 must be complete
**Testing**: Email flow testing, integration tests

---

## Implementation Timeline

| Phase | Duration | Start | End |
|-------|----------|-------|-----|
| Phase 1: Foundation | 1 week | Week 1 | Week 1 |
| Phase 2: Core Authentication | 1 week | Week 2 | Week 2 |
| Phase 3: Frontend Integration | 1 week | Week 3 | Week 3 |
| Phase 4: Protected Endpoints | 1 week | Week 4 | Week 4 |
| Phase 5: Administration & Polish | 1 week | Week 5 | Week 5 |
| Phase 6: Email Verification (Optional) | 1 week | Week 6 | Week 6 |

**Total Duration**: 5-6 weeks (depending on whether email verification is included)

---

## Considerations

### Assumptions

1. **User Base**: The system is for a single high school with <5,000 students
2. **Deployment**: Will be deployed in a controlled school environment
3. **Support**: School has IT staff who can manage user accounts
4. **Email System**: School can provide SMTP credentials for email verification (Phase 6)
5. **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge - latest versions)
6. **Database**: Can start with SQLite and migrate to PostgreSQL if needed
7. **Load**: Concurrent users will be <500 during peak hours
8. **Compliance**: No special regulatory requirements (FERPA compliance handled separately)

### Constraints

1. **Time**: 5-6 weeks for complete implementation
2. **Resources**: Single developer working part-time (20 hours/week)
3. **Infrastructure**: Must work with existing FastAPI setup
4. **Budget**: Open-source solutions only, no paid services
5. **Backwards Compatibility**: Must not break existing activity viewing functionality
6. **Data Migration**: Need to preserve existing activity signup data
7. **Learning Curve**: Developer is familiar with FastAPI but new to authentication

### Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| **Password Leakage** | Low | High | Use bcrypt, enforce strong passwords, add rate limiting, monitor for breaches |
| **XSS Attacks** | Medium | High | Sanitize all inputs, use HTTP-only cookies for sensitive data, implement CSP headers |
| **CSRF Attacks** | Medium | Medium | Use JWT tokens (inherently CSRF-resistant), add CSRF tokens for cookie-based auth |
| **Token Theft** | Medium | High | Use HTTPS only, short token expiry, implement token refresh rotation |
| **SQL Injection** | Low | High | Use SQLAlchemy ORM (parameterized queries), validate all inputs |
| **Database Corruption** | Low | High | Regular backups, use transactions, implement database migrations properly |
| **Email Spoofing** | Medium | Medium | Verify email domain, add SPF/DKIM checks, implement rate limiting |
| **Brute Force Attacks** | High | Medium | Rate limiting, account lockout after failed attempts, CAPTCHA after 3 failures |
| **Session Hijacking** | Low | High | Use secure tokens, implement IP validation, add user agent verification |
| **Scope Creep** | High | Medium | Stick to defined phases, defer nice-to-have features to Phase 6+ |
| **Integration Issues** | Medium | Medium | Write integration tests early, test frequently, maintain backwards compatibility |
| **Performance Degradation** | Low | Medium | Index database properly, implement caching, monitor query performance |
| **Third-party Dependency Vulnerabilities** | Medium | Medium | Use dependency scanning tools, keep dependencies updated, pin versions |

### Technical Debt

The following technical debt items are acceptable for MVP but should be addressed in future iterations:

1. **Token Revocation**: Phase 1-4 won't have true token revocation (tokens valid until expiry)
   - *Future*: Implement Redis-based token blacklist

2. **Email Verification**: Deferred to Phase 6
   - *Impact*: Users can register with fake emails initially
   - *Mitigation*: Restrict to @mergington.edu domain

3. **Rate Limiting**: Basic implementation in Phase 5
   - *Future*: Implement distributed rate limiting with Redis for multi-server deployment

4. **Session Management**: No persistent session storage initially
   - *Future*: Add Redis for session management in production

5. **Logging**: Basic logging in Phase 5
   - *Future*: Implement structured logging, log aggregation, and monitoring

6. **Password Complexity**: Basic validation
   - *Future*: Add password strength meter, prevent common passwords, check against breach databases

---

## Not Included (Future Enhancements)

The following features are out of scope for the initial authentication implementation:

### Authentication Features
- **OAuth/SSO Integration**: Google, Microsoft, or other identity providers
- **Multi-factor Authentication (MFA)**: SMS or authenticator app-based 2FA
- **Biometric Authentication**: Fingerprint or face recognition
- **Anonymous Access**: Guest users with limited permissions
- **Social Login**: Facebook, Twitter, etc.

### User Management
- **Self-service Password Change**: Users changing their own passwords (not reset)
- **Account Deletion**: GDPR-compliant account deletion
- **User Profiles**: Profile pictures, bio, preferences beyond basic info
- **Account Linking**: Linking multiple email addresses to one account
- **User Directory**: Searchable directory of students

### Advanced Security
- **Advanced Threat Detection**: Anomaly detection, behavioral analysis
- **Compliance Reporting**: FERPA, GDPR compliance reports
- **Security Audit Logs**: Detailed audit trail for all user actions
- **IP Whitelisting**: Restrict access to school network
- **Device Management**: Trust/untrust specific devices

### Administrative Features
- **Bulk User Import**: CSV upload for user creation
- **User Analytics**: Login patterns, activity trends, dashboards
- **Custom Roles**: Beyond student/admin roles
- **Permission Management**: Granular permissions system
- **Activity Moderation**: Approve/reject activity signups

### Performance & Scalability
- **Caching Layer**: Redis for session and data caching
- **CDN Integration**: For static assets
- **Database Replication**: Read replicas for scalability
- **Horizontal Scaling**: Multi-server deployment support
- **WebSocket Support**: Real-time notifications

### User Experience
- **Progressive Web App (PWA)**: Offline support, push notifications
- **Mobile App**: Native iOS/Android apps
- **Accessibility**: WCAG 2.1 AA compliance
- **Internationalization**: Multi-language support
- **Dark Mode**: UI theme switching

---

## Success Metrics

How we'll measure the success of the authentication implementation:

### Security Metrics
- Zero authentication-related security incidents in first 3 months
- 100% of passwords stored with bcrypt hashing
- 100% of sensitive endpoints protected with authentication
- <0.1% rate of failed authentication attempts (indication of attack attempts)

### Performance Metrics
- Login response time <500ms (p95)
- Registration response time <1s (p95)
- Token validation overhead <50ms per request
- Database query time <100ms (p95)

### User Experience Metrics
- >90% successful login rate (excluding wrong password)
- <5% support tickets related to authentication in first month
- Average time to complete registration <2 minutes
- <10% password reset requests in first month

### Development Metrics
- >80% code coverage with automated tests
- <5 critical bugs discovered post-deployment
- All phases completed within estimated timeline (±1 week)
- Zero data loss during migration

---

## Deployment Checklist

Before deploying authentication to production:

- [ ] All tests passing (unit, integration, E2E)
- [ ] Security review completed
- [ ] Code review completed by peer
- [ ] Documentation updated (API docs, user guide, admin guide)
- [ ] Environment variables configured securely
- [ ] Database backups configured
- [ ] HTTPS enabled and enforced
- [ ] CORS configured properly
- [ ] Rate limiting tested and configured
- [ ] Error monitoring configured (e.g., Sentry)
- [ ] Performance monitoring configured
- [ ] Rollback plan documented and tested
- [ ] User communication prepared (announcement, training materials)
- [ ] Support team briefed on new features
- [ ] Staging environment tested thoroughly

---

## Appendix

### A. Environment Variables

Required environment variables for authentication:

```bash
# Application
SECRET_KEY=<generate-random-32-character-string>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=7

# Database
DATABASE_URL=sqlite:///./school_activities.db  # Development
# DATABASE_URL=postgresql://user:pass@host:5432/dbname  # Production

# Email (Phase 6)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=noreply@mergington.edu
SMTP_PASSWORD=<app-specific-password>
SMTP_FROM=noreply@mergington.edu

# Security
ALLOWED_EMAIL_DOMAIN=mergington.edu
RATE_LIMIT_PER_MINUTE=60
FAILED_LOGIN_ATTEMPTS=5
LOCKOUT_DURATION_MINUTES=15

# CORS
ALLOWED_ORIGINS=https://activities.mergington.edu
ALLOW_CREDENTIALS=true
```

### B. Database Schema

```sql
-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'student',
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Activity signups table
CREATE TABLE activity_signups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    activity_name VARCHAR(255) NOT NULL,
    signed_up_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE(user_id, activity_name)
);

-- Refresh tokens table (Phase 5)
CREATE TABLE refresh_tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token VARCHAR(500) UNIQUE NOT NULL,
    user_id INTEGER NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Blacklisted tokens table (Phase 5)
CREATE TABLE blacklisted_tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token VARCHAR(500) UNIQUE NOT NULL,
    blacklisted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_activity_signups_user_id ON activity_signups(user_id);
CREATE INDEX idx_activity_signups_activity ON activity_signups(activity_name);
CREATE INDEX idx_refresh_tokens_user_id ON refresh_tokens(user_id);
CREATE INDEX idx_refresh_tokens_token ON refresh_tokens(token);
```

### C. Sample Code Snippets

#### Password Hashing Utility
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
```

#### JWT Token Generation
```python
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

#### Authentication Dependency
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        user = get_user_by_email(email)
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception
```

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-19 | Technical Planning Team | Initial implementation plan |

---

**Document Status**: Draft for Review  
**Next Review Date**: Before Phase 1 begins  
**Approvers**: Development Lead, Security Officer, Product Owner
