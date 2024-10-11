## BE Capstone Project: Habit Tracker API

### Project Overview:
As a backend developer, your task is to design and implement a **Habit Tracker API** using Django and Django REST Framework. This API will allow users to create, track, and manage their habits by logging, updating, deleting, and viewing their progress. You will be responsible for building a fully functional API that tracks habits, manages users, and provides insights into habit-building success. This project simulates real-world development tasks, focusing on database management, user authentication, habit tracking, and progress analysis.

### Functional Requirements:

#### Habit Management (CRUD):
- Implement the ability to **Create, Read, Update, and Delete (CRUD)** user habits.
- Each habit should have the following attributes:
  - **Habit Name** (e.g., Meditation, Reading, Exercise)
  - **Description** (optional)
  - **Frequency** (e.g., Daily, Weekly, Monthly)
  - **Target Days** (e.g., every day, specific days of the week)
  - **Start Date** and **End Date** (optional)
  - **User ID** (to associate each habit with the user)
- Ensure validation for required fields such as Habit Name and Frequency.
- Provide endpoints for users to **log their progress** for a specific habit on any given day (e.g., mark a habit as completed or not completed).
  
#### User Management (CRUD):
- Implement CRUD operations for users.
- Each user should have a unique **Username**, **Email**, and **Password**.
- Ensure that users can only manage their own habits.
- Implement permission checks to ensure users cannot modify or delete habits logged by other users.

#### View Habit Progress:
- Create an endpoint for users to **view their habit progress** over time.
- The endpoint should display all habits the user is tracking, including details such as Habit Name, Frequency, Completion Status (per day or week), and Dates.
- Add optional filters to view habit progress by:
  - **Date Range** (e.g., show progress from last week, last month)
  - **Habit Name** (e.g., view only habits for "Exercise").

#### Habit Metrics and Insights:
- Provide an endpoint to allow users to **see a summary** of their habit-building activities, such as:
  - Total days the habit was completed within a given time period.
  - Success rate (e.g., percentage of days the habit was completed vs. the goal).
- Optionally, show trends (e.g., streaks of consecutive days with habit completion, weekly/monthly progress charts).

### Technical Requirements:

#### Database:
- Use Django ORM to interact with the database.
- Define models for **Habit** and **User**.
- Ensure that each habit is associated with the user who created it, and users can only access their own habit records.

#### Authentication:
- Implement user authentication using Django’s built-in authentication system.
- Users must be logged in to create, update, or delete their habits.
- Optionally, implement token-based authentication (JWT) to secure the API.

#### API Design:
- Use Django REST Framework (DRF) to design and expose the necessary API endpoints.
- Follow RESTful principles, using appropriate HTTP methods (GET, POST, PUT, DELETE).
- Ensure proper error handling with relevant HTTP status codes (e.g., 404 for not found, 400 for bad request).

#### Deployment:
- Deploy the API on **Heroku** or **PythonAnywhere**.
- Ensure the API is accessible, secure, and performs well in the deployed environment.

#### Pagination and Sorting:
- Add pagination to the list of habits for users with many habits.
- Provide sorting options such as sorting habits by **Name**, **Frequency**, or **Creation Date**.

### Stretch Goals (Optional):

#### Habit Reminders and Notifications:
- Add a feature to allow users to **set reminders** for their habits (e.g., daily or weekly notifications to remind users to complete a habit).
- Send notifications when users hit specific milestones (e.g., completing a habit 7 days in a row).

#### Habit Goals and Challenges:
- Allow users to set **goals** for their habits (e.g., "Read for 30 minutes every day for 30 days") and track progress toward those goals.
- Implement a system for users to create or join **challenges** (e.g., "Meditate every day for a month") and compare their progress with others in the challenge.

#### Social Sharing and Habit Groups:
- Create endpoints to allow users to **share** their habit achievements with other users or on social media platforms.
- Implement a feature for users to create or join **habit groups**, where multiple users can track their progress on similar habits together (e.g., a group for fitness habits).

#### Leaderboards:
- Add a leaderboard feature to allow users to see how they rank in terms of completing their habits. For example:
  - Who has the longest streak?
  - Who has completed the most habits this week?

#### Habit Streaks:
- Track **streaks** for each habit (e.g., how many consecutive days a user has successfully completed a habit) and provide insights on maintaining streaks.

#### Integration with Wearables or Other Apps:
- Optionally, provide an endpoint to **integrate with habit-tracking apps** or fitness wearables (e.g., smartwatches), allowing users to log habits automatically.

### Deliverables:
- **Code Files**: Models, views, and serializers for habits and users.
- **API Endpoint Documentation**: Detailed descriptions and usage instructions for all endpoints.
- **Deployment Documentation**: Steps and configuration for deploying the project to a production environment.
- **Testing Results**: Documentation of the testing procedures, cases, and outcomes.
