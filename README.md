# DineWise


![0_s0_g_f0OUuc1blVC](https://user-images.githubusercontent.com/114544202/235055460-06eb1bc9-4a2d-4d49-96e5-e0caeae8f6fb.jpg)


[![PyPI](https://img.shields.io/pypi/pyversions/locust.svg)](https://pypi.org/project/locust/)
![Tests](https://github.com/kshitijzutshi/DAMG7245-Final-Project/actions/workflows/testing_workflow.yml/badge.svg)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)







# Overview 📝

The main problem faced by restaurent owner is to get a feeback from the customer using his services and  provide restaurant owners with insights into their business by analyzing the reviews they receive on social sites or any other Internet platform. Yelp is a popular platform where customers can leave reviews and ratings for businesses, including restaurants. However, analyzing these reviews manually can be time-consuming and may not provide the insights that restaurant owners need to improve their business.

# Goals 🎯
The goal of this project is to provide restaurant owners with a dashboard that displays the sentiment and topics of their Yelp reviews, as well as recommendations on how to improve their business based on the analysis. This can help restaurant owners make data-driven decisions that can lead to increased customer satisfaction and business success. We are trying to use data engineering techniques to automatically collect, preprocess, and analyze Yelp reviews for restaurants
By visualizing this data, we tend to provide restaurant owners with actionable insights that can help them improve their business.


# Dataset Source 🔦

The source of data for this project we used is Yelp's API (Application Programming Interface). The Yelp API provides access to a wealth of data, including business information, reviews, ratings, photos, and more. With the Yelp API, we have access to  collect data for specific restaurants based on their Yelp business ID, location, or other criteria. A brief preview of data is as below


![image](https://user-images.githubusercontent.com/114544202/235063605-c99417bb-9205-4b04-bf83-c22a838af154.png)


# Process Outline

1. Data gathering from he yelp API and dataging in Database
2. Data Preprocessing   
3. Understanding the Dataset - Exploratory Data Analysis(EDA)
4. Building a pipeline system using Airflow to scrape data on regular basis and also using various tools/softwares(AWS Cloudwatch , Streamlit, GCP)
5. Using OpenAi Api to suggest the steps of action that can be used to improve the business based on the reviews provided
6. Build a web application using streamlit for showcasing the results.


# Project overall Architecture

Project Architecture Diagram and technologies used


Project Requirements and Technology dependencies

### Requirements and dependencies

```

fastapi==0.95.1
frozenlist==1.3.3
gitdb==4.0.10
GitPython==3.1.31
🐍 Python ➡ 3.9.7
altair==4.1.0
📊 matplotlib==3.5.0
🔢 numpy==1.19.5
google-api-core==2.11.0
google-auth==2.17.3
google-auth-oauthlib==1.0.0
google-cloud==0.34.0
google-cloud-core==2.3.2
google-cloud-storage==2.8.0
google-crc32c==1.5.0
google-resumable-media==2.5.0
googleapis-common-protos==1.59.0
streamlit==1.21.0
toml==0.10.2
watchfiles==0.19.0
uvicorn==0.21.1
uvloop==0.17.0
validators==0.20.0
watchfiles==0.19.0
wcwidth==0.2.6
websockets==11.0.2
yarl==1.9.1
zipp==3.15.0
```













