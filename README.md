# Rental Platform

A rental platform where users can browse, book, and manage rental services. Built using **HTML, CSS, MySQL**, and **Docker**.

## Features
- User authentication (login/signup)
- Browse available rentals
- Book and manage reservations
- Admin dashboard for managing rentals
- Responsive UI

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python) / PHP / Node.js *(mention the one you used)*
- **Database**: MySQL
- **Containerization**: Docker

## Installation
### Prerequisites
- Install [Docker](https://www.docker.com/get-started)
- Install MySQL *(if running without Docker)*

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rental-platform.git
   cd rental-platform
   ```
2. Setup database:
   - If using Docker, skip to the Docker section below.
   - If using MySQL locally:
     ```sql
     CREATE DATABASE rental_db;
     ```
3. Configure `.env` file (if applicable) with database credentials.

## Running with Docker
1. Build and start the container:
   ```bash
   docker-compose up --build -d
   ```
2. Access the platform at `http://localhost:5000` (or the port you configured).

## Deployment
- Can be deployed using AWS/GCP/Azure
- Use `docker-compose up` for production setup

## Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Added new feature'`)
4. Push to your branch (`git push origin feature-name`)
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Need Help?
Feel free to raise an issue or contact me!

