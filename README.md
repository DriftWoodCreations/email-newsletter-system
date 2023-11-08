# Email Newsletter System

This project provides an automated way to send newsletters to a list of customers using the [Surenotify API](https://newsleopard.com/surenotify/api/v1/). The newsletters are personalized and sent out based on the customer details provided in an Excel file. The content of the newsletter is defined in an HTML template.

## Prerequisites

Before starting with this project, you need to have the following:

- An active Surenotify API key.
- An installation of Conda on your machine.
- A `list.xlsx` file with your customers' names and emails.
- The HTML template `content.html` for the newsletter.

## Setup Instructions

### 1. Environment Setup

To set up the project environment, follow these steps:

#### Clone the repository

```bash
git clone <repository-url>
```
Replace `<repository-url>` with the actual URL of this repository.

#### Create the Conda environment
Navigate to the project directory and create the environment using the provided `environment.yml` file:
```bash
conda env create -f environment.yml
```
This will install all necessary dependencies in an environment named `email`.
#### Activate the environment
Activate the Conda environment with the following command:
```bash
conda activate email
```
### 2. Configuration

Modify the `main.py` script with your actual details:
- Replace `YOUR-API-KEY-HERE` with your Surenotify API key.
- Replace `YOUR-COMPANY` with your company's name.
- Replace `YOUR-EMAIL-ADDRESS` with your email address.
- All instances of `YOUR-LINK` should be replaced with your actual unsubscribe link.
- Replace `YOUR-EMAIL-TITLE` with the subject line of your email.
- Put `list.xlsx` with columns "Name" and "Email" in this directory.
- Put your `logo.png` in this directory.

### 3. Usage

Run the script with the following command:
```bash
python main.py
```
The script will read from `list.xlsx`, fill out the `content.html` template with customer-specific information, and send out the emails.

### 4. Output

The script will output the status of each email sent to the console. It will indicate whether the email was successfully sent or if it failed to send.

## Customizing the Email Template

You can customize the email template by editing the `content.html` file. Use Jinja2 template syntax to include customer-specific data in the newsletter.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).

## Contact

For support or queries, reach out to [My Email](driftwoodcreations.tw@gmail.com).