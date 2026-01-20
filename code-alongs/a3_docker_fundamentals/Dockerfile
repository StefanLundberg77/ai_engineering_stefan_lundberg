# python will be installed in our container
FROM python:3.11-slim

# speca your workdir of choice
WORKDIR /app

# copies everithing in this folder in host into working dir container
COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "dashboard.py" ]

