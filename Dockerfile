FROM jupyter/base-notebook:latest as dev
RUN pip install solara==1.19.0
RUN pip install plotly
RUN pip install pandas