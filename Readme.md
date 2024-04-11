# Gas Utility Services

The Gas Utility Services Web Application is a platform that allows users to raise complaints related to gas utility services, track the status of their complaints, and pay charges by generating an invoice. Users are required to register or login to access the complaint submission, tracking, and payment functionalities.

## Features

- User authentication: Register, login, and logout functionality for users.
- Complaint submission: Users can submit complaints regarding gas utility services.
- Complaint tracking: Users can track the status of their complaints.
- Admin interface: Administrators can manage complaints and users through the Django admin panel.

## Installation

1. Clone the repository:

```
git clone https://github.com/tanujgupta18/Gas-Utility-Services.git
```

2. Run the development server:

```
python manage.py runserver
```

The application will be accessible at `http://localhost:8000`.

## Usage

- Visit `http://localhost:8000/register` to create a new user account.
- Visit `http://localhost:8000/login` to log in to an existing account.
- Once logged in, visit `http://localhost:8000/service_request` to submit a complaint.
- Visit `http://localhost:8000/track_status` to track the status of your complaints.
- Administrators can access the admin interface at `http://localhost:8000/admin` to manage complaints and users.

## Paying Service Charges

Users can now pay their service charges by downloading the invoice from the track request page. After logging in, users can navigate to the track request page (`http://localhost:8000/track_status`) to view the status of their complaints. For unpaid complaints, users can download the invoice by clicking on the "Download Bill PDF" button. Once the invoice is downloaded, users can proceed with the payment process according to the instructions provided in the invoice.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
