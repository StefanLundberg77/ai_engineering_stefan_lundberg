# python will be installed in our container
FROM python:3.11-slim

# speca your workdir of choice
WORKDIR /app

# copies everithing in this folder in host into working dir container
COPY . .

# install requrements
RUN pip install -r requirements.txt

# define streamlit port
EXPOSE 8501

# run 
CMD [ "streamlit", "run", "dashboard.py" ]

# docker run --name dashboard cool_dashboard -p