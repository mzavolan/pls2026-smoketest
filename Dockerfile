FROM continuumio/miniconda3:24.9.2-0
WORKDIR /project
ENV PYTHONHASHSEED=0
COPY environment.yml .
RUN conda env create -f environment.yml && conda clean --all --yes
COPY src/ src/
COPY run.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "pls2026", "python", "run.py"]
