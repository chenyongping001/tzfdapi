FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Required to install mysqlclient with Pip
RUN apt-get update \
  && apt-get install python3-dev default-libmysqlclient-dev gcc -y

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install oracle client
RUN apt-get install libaio1 -y
RUN mkdir -p /usr/lib/oracle && cd /usr/lib/oracle \
  && wget -O client.zip "https://box.zjenergy.com.cn:10081/v2/delivery/data/c4105d5fe858483e94001910bc78efbc/?token=&dup_t=1680101380880" \
  && unzip client.zip && rm client.zip \
  && cd /usr/lib/oracle/instantclient_11_2/ \
  && ln -s libclntsh.so.11.1 libclntsh.so \
  && ln -s libocci.so.11.1 libocci.so \
  && chmod 755 ./*.so 
ENV ORACLE_HOME=/usr/lib/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH
ENV PATH=$PATH:$ORACLE_HOME
ENV NLS_LANG="american_america.ZHS16GBK"

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
# 开发环境
RUN pipenv install --system --dev

# 生产环境
# RUN pipenv install --system


# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container
EXPOSE 8000