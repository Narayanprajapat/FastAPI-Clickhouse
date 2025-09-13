# FastAPI-Clickhouse

## Key Features & Benefits

- **Created two endpoints:** Latest data and historical data
- **Health Check Endpoint:** Provides a health check endpoint for monitoring application status.
- **Dockerized Deployment:** Easy deployment using Docker.
## Prerequisites & Dependencies


## Tech Stack / Key Dependencies

-   **Python** Version 3.12 or higher.
-   **FastAPI** RestAPI python framework
-   **Poetry:** A tool for dependency management and packaging.
-   **Clickhouse** Database to store stock data
-   **Docker:** For containerization.


## File Structure Overview

```text
.
├── .gitignore
├── README.md
├── clickhouse/
├── docker-compose.yml
├── fastapi_service/
└── ingestion_services/
```


## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Narayanprajapat/FastAPI-CRUD
    cd FastAPI-CRUD
    ```

2.  **Run Docker Compose:**

    ```bash
    docker-compose up --build
    ```

## Usage Examples & API Documentation

### API Endpoints:

#### Health Check

-   **Endpoint:** `http://localhost:8080/api/v1/health`
-   **Method:** `GET`
-   **Description:** Checks the health status of the application.
-   **Example Response:**

    ```json
    {
        "status_code": 200,
        "message": "Server is running"
    }
    ```

#### Latest data

-   **Base URL:** ``http://localhost:8080/api/v1`

##### Create a Book

-   **Endpoint:** `/latest/{symbol}`
-   **Method:** `GET`
-   **Description:** Latest data for stock
-   **Example Response:**

    ```json
    {
        "symbol": "TCS",
        "close": 3133.39990234375,
        "open": 3144,
        "last_updated": "2025-09-13T14:40:56"
    }
    ```


##### Get all historical data by symbol

-   **Endpoint:** `/history/{symbol}`
-   **Method:** `GET`
-   **Description:** Get all history based on symbol.


-   **Example Response:**

    ```json
    [
        {
            "symbol": "TCS",
            "close": 3133.39990234375,
            "open": 3144,
            "date": "2025-09-13",
            "high": 3148.699951171875,
            "low": 3121,
            "volume": 428361432
        }
    ]
    ```

## Contributing Guidelines

We welcome contributions! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write tests for your changes.
5.  Submit a pull request.
