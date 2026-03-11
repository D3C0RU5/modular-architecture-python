FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm
WORKDIR /app
ENV PYTHONUNBUFFERED 1

USER root

RUN rm -f /etc/apt/sources.list.d/yarn.list \
    apt-get update && apt-get install -y \
    bash \
    git \
    curl \
    vim-tiny \
    unzip \
    && rm -rf /var/lib/apt/lists/*

USER vscode

ENV PATH="/home/vscode/.local/bin:${PATH}"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash"]

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



