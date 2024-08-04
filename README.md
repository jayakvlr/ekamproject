# Project Documentation

## Overview

This document outlines the functionality and API endpoints for the project. The system is divided into three main modules: Main, User, and Admin.



## User Module

### 1. Register

**Method**: POST  
**Endpoint**: `/signup/{event_id}`  
**Input Parameters**:
- `whatsapp_number` (string): The user's WhatsApp number.
- `country_code` (string): The country code for the WhatsApp number.
- `name` (string): User's name.
- `age` (integer): User's age.
- `gender` (string): User's gender.
- `place` (string): User's place.
- `state` (string): User's state.
- `country` (string): User's country.

**Functionality**:
- Adds the user to the log for tracking purposes.
- Triggers the wati api to send a message to the user
- wait for their response
- Once response recieved 
    - Save user to our DB
    - Saves the user's event registration.
    - Save contacts in wati
    - redirect to dashboard
    - send QRcode and ticket to whatsapp
    - Send introduction video to whatsapp


### 1. Login

**Method**: POST  
**Endpoint**: `/login/{event_id}`  
**Input Parameters**:
- `whatsapp_number` (string): The user's WhatsApp number.
- `country_code` (string): The country code for the WhatsApp number.

**Functionality**:
- Authenticates the user with an interactive whatsapp message
- Upon their reply login to dashboard

### 2. Referral Link

**Method**: GET  
**Endpoint**: `/referral_link`  
**Parameters**:
- `username` (string): The username of the person generating the referral link.
- `event_id` (integer): The ID of the event for which the referral link is generated.

**Functionality**:
- Generates a referral link for the specified username and event ID.

### 3. Get Referrals

**Method**: GET  
**Endpoint**: `/get_referrals`  

**Functionality**:
- Retrieves the list of referrals for the logged-in user.

### 4. Get E2 Ticket

**Method**: GET  
**Endpoint**: `/get_e2_ticket`  

**Functionality**:
- Loads the E2 ticket to the homepage for the user.

### 5. Get Profile

**Method**: GET  
**Endpoint**: `/get_profile`  

**Functionality**:
- Retrieves the user's profile details.

### 6. Update Profile

**Method**: POST/UPDATE  
**Endpoint**: `/update_profile`  
**Input Parameters**:
- `name` (string, optional): User's name.
- `age` (integer, optional): User's age.
- `gender` (string, optional): User's gender.
- `place` (string, optional): User's place.
- `state` (string, optional): User's state.
- `country` (string, optional): User's country.

**Functionality**:
- Updates the user's profile details (excluding WhatsApp number).

### 7. Get Posts

**Method**: GET  
**Endpoint**: `/get_posts`  

**Functionality**:
- Retrieves available posts.

### 8. Get Events

**Method**: GET  
**Endpoint**: `/get_events`  

**Functionality**:
- Retrieves details of upcoming events.

## Admin Module

### 1. Get Users

**Method**: GET  
**Endpoint**: `/get_users`  

**Functionality**:
- Retrieves a list of all registered users.

### 2. Get Users Registered for E2 Event

**Method**: GET  
**Endpoint**: `/get_e2_users`  

**Functionality**:
- Retrieves a list of users registered for the E2 event.

### 3. Add Events

**Method**: POST  
**Endpoint**: `/add_event`  
**Input Parameters**:
- `event_name` (string): The name of the event.
- `event_date` (datetime): The date and time of the event.
- `event_details` (string): Details about the event.

**Functionality**:
- Adds a new event to the system.

### 4. Get User Details by WhatsApp

**Method**: GET  
**Endpoint**: `/get_user_by_whatsapp`  
**Parameters**:
- `whatsapp_number` (string): The WhatsApp number of the user.

**Functionality**:
- Retrieves details of a particular user based on their WhatsApp number.




