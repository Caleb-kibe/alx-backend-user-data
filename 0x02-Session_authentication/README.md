# 0x02. Session Authentication

## Description
This project is focused on implementing a **Session Authentication** system in a back-end API. Unlike token-based authentication, session authentication relies on storing user credentials in a server-side session, which is referenced by a cookie sent to the client. This project walks you through the steps of building your own session authentication system for learning purposes, though it is not recommended to implement such a system in production environments.

### Key Concepts Covered:
- Session Authentication
- Cookies and how they work
- How to send and parse Cookies using Flask

## Learning Objectives:
By the end of this project, you should be able to:
1. Explain what authentication means.
2. Define session authentication and how it differs from token-based approaches.
3. Understand the role of Cookies in session authentication.
4. Implement mechanisms to send and parse cookies.
5. Develop session authentication without using external frameworks like Flask-HTTPAuth.

## Project Structure:
The project builds on the previous `0x01. Basic Authentication` system. Make sure all tasks from that project are completed before proceeding.

**Folder structure:**
- `api/`: Contains the Flask API implementation and endpoints.
- `models/`: User and session models for handling authentication.

## Requirements:
- No additional modules should be installed.
- All authentication logic is implemented manually for educational purposes.

## Endpoints:
### New Endpoint:
- **GET /users/me**: Retrieves the authenticated user's details based on session authentication.

### Existing Endpoints (extended with session authentication):
- **GET /api/v1/users**
- **POST /api/v1/users**
- **GET /api/v1/users/<user_id>**
- **PUT /api/v1/users/<user_id>**
- **DELETE /api/v1/users/<user_id>**

## Tasks Overview:
1. **Session Creation**: Implement logic to create a session when a user logs in.
2. **Cookie Management**: Send and parse cookies for maintaining the session.
3. **Session Validation**: Implement session validation to authorize users based on stored session data.
4. **User Data Access**: Allow authenticated users to retrieve their own information.

## Instructions:
1. Copy all files from `0x01. Basic Authentication` into the current project folder.
2. Extend the authentication system to include session-based authentication.
3. Modify the `GET /api/v1/users/<user_id>` endpoint to support retrieving user data for the currently authenticated session.

## Conclusion:
This project provides hands-on experience in implementing session authentication. It helps reinforce understanding of the authentication process and the role of cookies in maintaining user sessions across requests.
