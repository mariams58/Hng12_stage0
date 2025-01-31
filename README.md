# HNG12 STAGE ZERO SUBMISSION

## DESCRIPTION

This is a submission to the HNG Stage 0 task submission.It is a simple public API built with Flask that returns JSON-formatted information including an email, the current datetime in UTC (ISO format with Z), and a GitHub repository URL. The API handles Cross-Origin Resource Sharing (CORS).

## SETUP INSTRUCTIONS
### Prerequisites

Ensure you have the following installed
- **Python 3.10+**
- **pip**(Python package manager)
- **Vercel CLI**(for deployment optional)

### Installation Steps
1. **Clone the repository:**
```sh
    git clone https://github.com/mariams58/Hng12_stage0
    cd Hng12_stage0
```
2. **Create and activate a virtual environment**
```sh
    python -m venv .venv
    source .venv/bin/activate
```
3. **Install dependencies**
```sh
    pip install -r requirements.txt
```
4. **Create a .env file and add the required variables:**
```
EMAIL=your-email@example.com
GITHUB_URL=https://github.com/yourusername/your-repo
```
5. **Run the application locally:**
```
cd api
flask run
```
The API will be available at
```
http://127.0.0.1:5000/
```

## API Documentation
#### Endpoint: GET ``` / ```
**Response format:** JSON
**Example Request:**
```
curl http://127.0.0.1:5000/
```

#### Example Response:
`
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-31T09:51:42Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
`
## Resources
For more information on hiring python developers, visit: [Hire a Python Developer](https://hng.tech/hire/python-developers)