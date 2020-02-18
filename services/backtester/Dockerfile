FROM tiangolo/meinheld-gunicorn-flask
RUN pip install pipenv
WORKDIR /app/
COPY backtester/Pipfile .
COPY backtester/Pipfile.lock .
RUN pipenv install --system --dev
CMD ["/start-reload.sh"]
COPY ./common /app/common
COPY backtester/ /app