FROM tiangolo/meinheld-gunicorn-flask
RUN pip install pipenv
WORKDIR /app/
COPY data_processor/Pipfile .
COPY data_processor/Pipfile.lock .
RUN pipenv install --system --dev
CMD ["/start-reload.sh"]
COPY ./common /app/common
COPY data_processor/ /app