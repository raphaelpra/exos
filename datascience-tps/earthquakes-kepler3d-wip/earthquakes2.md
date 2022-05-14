---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
---

> inspired from https://medium.com/nightingale/how-to-create-eye-catching-maps-with-python-and-kepler-gl-e7e897eff8ac

+++

# earthquakes

```{code-cell} ipython3
import pandas as pd
import keplergl 
```

## data acquisition

```{code-cell} ipython3
# could not spot a direct URL to this data...
dataset_url = "https://catalog.data.gov/dataset/global-significant-earthquake-database-2150-bc-to-present"

# so I copied it in this repo instead
dataset_filename = "Worldwide-Earthquake-database.csv"
```

```{code-cell} ipython3
%cd raw-tps/keplergl
```

```{code-cell} ipython3
df = pd.read_csv(dataset_filename)
df.describe()
```

## clean up

```{code-cell} ipython3
# lat and lon to numeric, errors converted to nan
df['LONGITUDE'] = pd.to_numeric(df.LONGITUDE, errors='coerce')
df['LATITUDE'] = pd.to_numeric(df.LATITUDE, errors='coerce')
```

```{code-cell} ipython3
# drop rows with missing lat, lon, and intensity
df.dropna(subset=['LONGITUDE', 'LATITUDE', 'INTENSITY'], inplace=True)
```

```{code-cell} ipython3
# convert tsunami flag from string to int
df['FLAG_TSUNAMI'] = [1 if i=='Yes' else 0 for i in df.FLAG_TSUNAMI.values]
```

## draw map

```{code-cell} ipython3
kepler_map = keplergl.KeplerGl(height=600)
kepler_map
```

```{code-cell} ipython3
kepler_map.add_data(data=df, name="earthquakes")
```

## config

```{code-cell} ipython3
manual_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "o2783kd",
          "type": "point",
          "config": {
            "dataId": "earthquakes",
            "label": "earthquakes",
            "color": [
              23,
              184,
              190
            ],
            "columns": {
              "lat": "LATITUDE",
              "lng": "LONGITUDE",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 10,
              "fixedRadius": False,
              "opacity": 0.8,
              "outline": False,
              "thickness": 2,
              "strokeColor": None,
              "colorRange": {
                "name": "Uber Viz Diverging 0",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#C22E00",
                  "#FEEEE8",
                  "#00939C"
                ],
                "reversed": True
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radiusRange": [
                2,
                12
              ],
              "filled": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "FLAG_TSUNAMI",
              "type": "integer"
            },
            "colorScale": "quantize",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": {
              "name": "INTENSITY",
              "type": "integer"
            },
            "sizeScale": "sqrt"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "earthquakes": [
              "I_D",
              "FLAG_TSUNAMI",
              "YEAR",
              "MONTH",
              "DAY"
            ]
          },
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 37.48434368318514,
      "longitude": -122.11886458964356,
      "pitch": 0,
      "zoom": 8.198674684017652,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
```

# graffiti

+++

***this part needs more work***

```{code-cell} ipython3
import pandas as pd
import geopandas as gpd
import keplergl 
```

```{code-cell} ipython3
block_url = "https://opendata.vancouver.ca/explore/dataset/block-outlines/download/?format=geojson&timezone=Europe/Berlin&lang=en"
block_filename = "block.geojson"
```

```{code-cell} ipython3
graffiti_url = "https://opendata.vancouver.ca/explore/dataset/graffiti/download/?format=geojson&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
graffiti_filename = "graffiti.geojson"
```

```{code-cell} ipython3
import requests
def store_url_as_filename(url, filename, force=False):
    from pathlib import Path
    if force or not Path(filename).exists():
        req = requests.get(url)
        text = req.text
        with open(filename, 'w') as writer:
            writer.write(text)
```

```{code-cell} ipython3
store_url_as_filename(block_url, block_filename)
store_url_as_filename(graffiti_url, graffiti_filename)
```

```{code-cell} ipython3
:cell_style: split

df_block = gpd.read_file(block_filename)
df_block.dropna(inplace=True)
df_block.head()
```

```{code-cell} ipython3
:cell_style: split

df_graffiti = gpd.read_file(graffiti_filename)
df_graffiti.dropna(inplace=True)
df_graffiti.head()
```

```{code-cell} ipython3
# join datasets
df = gpd.sjoin(df_block, df_graffiti, how='inner', predicate='contains')
```

```{code-cell} ipython3
# create new indexes
df.reset_index(inplace=True)
df.head()
```
