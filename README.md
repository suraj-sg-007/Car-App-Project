# Car Rental Platform

## Overview
A **Car Rental Platform** built using **HTML, CSS, MySQL**, and containerized with **Docker**. This project allows users to browse, book, and manage car rentals efficiently.

## Features
- User authentication (Sign up/Login)
- Search and filter cars by model, price, and availability
- Booking system with date selection
- Admin panel for managing cars and bookings
- Responsive UI with modern design

## Technologies Used
- **Frontend:** HTML, CSS
- **Backend:** MySQL (Database)
- **Containerization:** Docker

## Installation
### Prerequisites
Ensure you have the following installed:
- **Docker**
- **MySQL Server**

### Steps to Run Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/car-rental-platform.git
   cd car-rental-platform
   ```
2. Run the MySQL database server.
3. Set up the database:
   - Import the provided SQL file (`database.sql`) into MySQL.
4. Start the project using Docker:
   ```sh
   docker-compose up --build
   ```
5. Open your browser and go to:
   ```
   http://localhost:5000
   ```

## Docker Setup
A **Dockerfile** is included to containerize the application.

### Build and Run the Docker Container
```sh
docker build -t car-rental .
docker run -p 5000:5000 car-rental
```

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.




