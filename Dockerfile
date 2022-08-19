FROM python:3.8.7 AS base

# install oracle client, library to cx-Oracle dependencies and pandoc with latex package
RUN apt-get update \
    && apt-get install nano 

ENV PYTHONPATH="/work"
WORKDIR "${PYTHONPATH}"

COPY . .

RUN pip install -r requirements.txt 

FROM base as one

CMD ["python", "/work/server.py"]

FROM base as two

# RUN ls
# CMD ["python", "/work/client.py"]

# RUN addgroup --gid 1002 user
# RUN adduser --disabled-password --gecos '' --uid 1002 --gid 1002 user
# USER user

# CMD ["bash"]