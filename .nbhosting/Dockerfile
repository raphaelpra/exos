# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/minimal-notebook

# NOTE
# we cannot use jupyter nbextension enable/disable
# because we provide our own nbconfig/notebook.json
# and that is where is stored the enabled/disabled extensions
RUN true \
 && pip install -U --pre jupyterlab notebook jupyterlab-myst jupytext \
 && pip install -U git+https://github.com/mwouts/jupyterlab-jupytext.git@jupyterlab4 \
 && pip install jupyterlab-courselevels jupyterlab-nbhosting \
 && pip install -U nbautoeval ipythontutor \
 && pip install numpy pandas matplotlib ipywidgets ipympl \
 && pip install mpld3 bokeh plotly folium vispy seaborn pygal networkx mypy autograd k3d \
 && apt-get install -y graphviz && pip install graphviz \
 && pip install geopandas keplergl \
 && pip install scikit-learn \
 && true
