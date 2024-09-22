# Streamlit and Docker Data Science Project: Bike Counts Prediction in Paris

## Project Overview
This project demonstrates the use of Streamlit and Docker in a data science context by predicting bike counts in Paris. It builds on a prior project by integrating an interactive Streamlit app that visualizes the exploratory data analysis (EDA) results. The project is fully dockerized, making sure that the setup and deployment are streamlined and reproducible.

## Objectives
- Learn and apply Streamlit for interactive data visualizations.
- Utilize Docker to create a consistent and isolated environment for the application.
- Predict and analyze bike counts in Paris based on historical data.

## Installation and Setup

### Prerequisites
- Docker installed on your machine. 
- Basic knowledge of Docker and Streamlit.

### Running the Application

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alexbohane/docker-streamlit-app.git
   cd docker-streamlit-app

2. **Build Docker Container**
   ```bash
   docker build -t bike-count-app .

3. **RUN Docker Container**
   ```bash
   docker run -dp 127.0.0.1:8540:8540 bike-count-app

This command runs the container and maps port 8540 of the container to port 8540 on your host, allowing you to access the Streamlit app by navigating to http://localhost:8540 in your browser (recommended not to use Safari).

###  Technologies Used
Python: Main programming language.
Streamlit: For creating the app.
Docker: For containerizing the application.
Pandas, Numpy: For data manipulation and calculations.
Matplotlib, Folium: For data visualization.

###  Project Structure

/docker-streamlit-app

    ├── Dockerfile
    
    ├── requirements.txt
    
    ├── streamlit-app.py
    
    ├── graph_generation.ipynb
    
    └── data/
    
        └── train.parquet
        
        └── test.parquet
        
    └── graphs/
    
        └── colorbar.png
        
        └── month_count.png

        └── saved_map.html
        
        └── week_count.png

### Contributors
Alex Bohane, GitHub username: alexbohane
Nacer Hadni (my partner for the previous DS project which this project aims to visualise)

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Data provided by Open Data Paris.


