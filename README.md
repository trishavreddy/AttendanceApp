# Attendance Helper

## Overview

Attendance Helper is a facial recognition app designed to simplify the process of recording and managing student attendance. By leveraging machine learning and NoSQL databases, this application offers efficient and scalable attendance tracking for educational institutions.

## Features

- **Facial Recognition:**
  - Implements a facial recognition function using the K-Nearest Neighbors (KNN) algorithm to identify students and record their attendance.
  - Captures 100 frames of facial data for each student to ensure accurate recognition.
  - Generates serializable Python files (pickle) to store the facial data securely in the database.

- **Database Integration:**
  - Stores students' attendance data in a NoSQL format using MongoDB Atlas for fast and reliable access.

- **API Integration:**
  - Utilizes an API to make GET requests, fetching attendance data from the database.
  - Displays attendance data in a user-friendly table for easy monitoring and management.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning Algorithm:** K-Nearest Neighbors (KNN)
- **Database:** MongoDB Atlas (NoSQL)
- **API:** Custom-built API for database interaction

## How It Works

1. **Face Registration:**
   - Students' faces are registered by capturing 100 frames of facial data.
   - The data is processed and stored as serialized Python files (pickle) in the database.

2. **Attendance Recording:**
   - During attendance sessions, the app scans students' faces and matches them against the stored data using the KNN algorithm.

3. **Data Storage and Access:**
   - Attendance records are automatically uploaded to MongoDB Atlas in a NoSQL format.
   - The app's API fetches this data and displays it in a clear, organized table for administrators.

## Capstone Project

This project was developed as the capstone project for my senior year. It helped me explore:
- Machine learning and facial recognition techniques
- Database design and integration with MongoDB Atlas
- API development and data visualization


