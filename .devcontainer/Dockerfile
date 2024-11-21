FROM python:3.12

RUN apt-get update && apt-get install -y git pv && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash vscode

USER vscode

WORKDIR /workspaces

RUN curl -s https://api.github.com/repos/njavilas2015/githooks/releases/latest | grep "browser_download_url" | cut -d '"' -f 4 | wget -i -

RUN chmod +x githooks

COPY . /workspaces

RUN python3 -m venv /workspaces/venv

RUN /workspaces/venv/bin/pip install --upgrade pip

RUN /workspaces/venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
