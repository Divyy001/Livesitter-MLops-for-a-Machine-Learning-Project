FROM python:3.10.4-slim-bullseye
WORKDIR / C:\Users\divyy\Desktop\github\Livesitter-MLops-for-a-Machine-Learning-Project
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY ./ C:\Users\divyy\Desktop\github\Livesitter-MLops-for-a-Machine-Learning-Project
ENTRYPOINT ["streamlit", "run"]
CMD ["interface.py"]
