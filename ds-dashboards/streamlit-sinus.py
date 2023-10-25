# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
#     text_representation:
#       extension: .py
#       format_name: light
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
# ---

# # a simple streamlit dashboard

# ````{admonition} attention
# :class: warning
#
# this code won't work from a notebook, you need to kick it off from a terminal using (download as .py if needed)
#
# ```bash
# streamlit run streamlit-sinus.py
# ```
# ````

import numpy as np
import matplotlib.pyplot as plt

# +
import streamlit as st


# -

st.title("Sinusoidal with matplotlib")

freq = st.slider("frequency", value=1, min_value=1, max_value=10, step=1)

phase = 0

amplitude = st.selectbox(
     'Amplitude',
     (.1, 1, 3, 5),
     # the index in the tuple above
     # so that initial value is 3
     index=2)

# keep it simple and use a fixed domain
domain = 4


def sinus4(freq, phase, amplitude, domain):

    figure = plt.figure(figsize=(10, 5))
    X = np.linspace(0., domain*np.pi, 250)
    Y = amplitude * np.sin(freq*(X+phase))
    # because we are going to mess with amplitude
    # let us fix the Y scale
    plt.ylim(-5, 5)
    plt.plot(X, Y)
    plt.legend()
    return figure


# +
st.pyplot(fig=sinus4(freq, phase, amplitude, domain))
