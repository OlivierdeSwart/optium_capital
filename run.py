import streamlit.web.bootstrap
import pathlib

app_path = pathlib.Path("app/main.py").resolve()

streamlit.web.bootstrap.run(str(app_path), "", [], None)
