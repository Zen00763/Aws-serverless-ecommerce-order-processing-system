# AWS Serverless E-Commerce Order Processing System

## Overview

This project demonstrates a fully serverless e-commerce order processing application built using Amazon Web Services (AWS). The application allows users to place orders through a web interface hosted on Amazon S3. Orders are processed using an event-driven architecture involving Amazon API Gateway, AWS Lambda, Amazon DynamoDB, Amazon SQS, and Amazon SNS.

The solution eliminates server management while providing scalability, reliability, and automated order processing capabilities.

---

## Project Objectives

* Build a fully serverless application using AWS services.
* Implement an event-driven architecture.
* Automate order processing workflows.
* Store customer orders using DynamoDB.
* Process orders asynchronously using Amazon SQS.
* Send automated email notifications using Amazon SNS.
* Host a frontend application using Amazon S3.

---

## AWS Services Used

### Amazon S3

* Static website hosting
* Frontend application deployment

### Amazon API Gateway

* REST API endpoint creation
* Request routing to AWS Lambda

### AWS Lambda

* Backend business logic execution
* Order creation and processing

### Amazon DynamoDB

* NoSQL database for storing customer orders

### Amazon SQS

* Queue-based asynchronous order processing

### Amazon SNS

* Automated email notifications

---

## Architecture Workflow

```text
Frontend Website (Amazon S3)
            │
            ▼
Amazon API Gateway
            │
            ▼
Lambda Function 1 (CreateOrder)
            │
            ├── Store Order → DynamoDB
            │
            └── Send Message → Amazon SQS
                                  │
                                  ▼
                     Lambda Function 2 (ProcessOrder)
                                  │
                                  ▼
                            Amazon SNS
                                  │
                                  ▼
                        Email Notification
```

---

## Features

✔ Static Website Hosting using Amazon S3

✔ REST API Development using API Gateway

✔ Serverless Backend using AWS Lambda

✔ NoSQL Database using DynamoDB

✔ Asynchronous Processing using Amazon SQS

✔ Automated Email Notifications using Amazon SNS

✔ Event-Driven Architecture

✔ Scalable Cloud-Native Design

---

## Frontend Features

* Customer Order Form
* Product Information Entry
* Quantity Selection
* API Integration using JavaScript Fetch API
* Responsive User Interface

---

## Project Workflow

1. User accesses the website hosted on Amazon S3.
2. User enters order details.
3. API Gateway receives the request.
4. Lambda Function (CreateOrder) processes the request.
5. Order details are stored in DynamoDB.
6. Order information is sent to Amazon SQS.
7. SQS triggers Lambda Function (ProcessOrder).
8. Lambda Function processes the order.
9. Amazon SNS publishes a notification.
10. Email notification is delivered to subscribers.

---



## Challenges Solved

### API Gateway CORS Configuration

* Enabled CORS to allow browser communication with backend APIs.

### SNS Subscription Issue

* Reconfigured and confirmed SNS email subscriptions.

### API Endpoint Configuration

* Updated frontend application with correct API Gateway endpoint.

---

## Skills Demonstrated

### Cloud Computing

* Amazon Web Services (AWS)
* Serverless Architecture
* Event-Driven Design
* Cloud-Native Development

### AWS Services

* Amazon S3
* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* Amazon SQS
* Amazon SNS

### Programming

* HTML
* CSS
* JavaScript
* Python
* Boto3

---

## Key Outcomes

* Developed a complete serverless application on AWS.
* Integrated six AWS services into a single workflow.
* Automated order processing and notifications.
* Eliminated infrastructure management.
* Improved scalability through serverless architecture.
* Implemented event-driven application design.

---

## Project Files

* Project Documentation (PDF)
* Frontend Source Code
* AWS Lambda Source Code
* Architecture Screenshots

---

## Author

Rogith Zen
