import pandas as pd
import numpy as np
import json
import folium
import branca.colormap as cm

df_all = pd.read_csv("../dati/insieme_with_votes.csv")
df_liste = pd.read_csv("../dati/liste.csv")
df_liste = df_liste[df_liste["pos"] == 8]
df_all = df_all.merge(df_liste, on="codice", how="left", suffixes=("", "_liste"))
df = df_all[
    [
        "codice",
        "CODICE ISTAT",
        "cod_com",
        "cod_prov",
        "desc_com",
        "desc_prov",
        "ele_t",
        "pref_marcello",
        "pref_silvia",
        "vot_t",
        "voti",
    ]]

df["voti_pd"] = df["voti"]
df["pref_totale"] = df["pref_marcello"] + df["pref_silvia"]

df["ele_t_10000_totale"] = round((df["pref_totale"] / df["ele_t"]) * 10000, 1)
df["vot_t_10000_totale"] = round((df["pref_totale"] / df["vot_t"]) * 10000, 1)
df["voti_pd_10000_totale"] = round((df["pref_totale"] / df["voti_pd"]) * 10000, 1)
df["ele_t_10000_silvia"] = round((df["pref_silvia"] / df["ele_t"]) * 10000, 1)
df["vot_t_10000_silvia"] = round((df["pref_silvia"] / df["vot_t"]) * 10000, 1)
df["voti_pd_10000_silvia"] = round((df["pref_silvia"] / df["voti_pd"]) * 10000, 1)
df["ele_t_10000_marcello"] = round((df["pref_marcello"] / df["ele_t"]) * 10000, 1)
df["vot_t_10000_marcello"] = round((df["pref_marcello"] / df["vot_t"]) * 10000, 1)
df["voti_pd_10000_marcello"] = round((df["pref_marcello"] / df["voti_pd"]) * 10000, 1)

topojson_comuni = json.loads(open("limits_IT_all.topo.json", 'r', encoding='utf-8').read())

filtered_geometries = [
    geom for geom in topojson_comuni["objects"]["municipalities"]["geometries"]
    if geom["properties"]["reg_name"] in [
        "Emilia-Romagna",
        "Veneto",
        "Trentino-Alto Adige/Südtirol",
        "Friuli-Venezia Giulia"
    ] 
]

topojson_comuni["objects"]["municipalities"]["geometries"] = filtered_geometries

df["com_istat_code_num"] = df["CODICE ISTAT"]

df = df.astype({
    "ele_t_10000_totale": float,
    "vot_t_10000_totale": float,
    "voti_pd_10000_totale": float,
    "ele_t_10000_silvia": float,
    "vot_t_10000_silvia": float,
    "voti_pd_10000_silvia": float,
    "ele_t_10000_marcello": float,
    "vot_t_10000_marcello": float,
    "voti_pd_10000_marcello": float,
    "pref_totale": float,
    "pref_silvia": float,
    "pref_marcello": float,
    "ele_t": float,
    "vot_t": float,
    "voti_pd": float
})

for geom in topojson_comuni['objects']['municipalities']["geometries"]:
    codice_istat = geom['properties']['com_istat_code_num']
    if codice_istat == None or codice_istat == False:
        print("codice istat none")
        
    row = df[df["com_istat_code_num"] == codice_istat]
    
    if not row.empty:
        geom['properties']['ele_t_10000_totale'] = row.iloc[0]['ele_t_10000_totale']
        geom['properties']['vot_t_10000_totale'] = row.iloc[0]['vot_t_10000_totale']
        geom['properties']['voti_pd_10000_totale'] = row.iloc[0]['voti_pd_10000_totale']
        geom['properties']['ele_t_10000_silvia'] = row.iloc[0]['ele_t_10000_silvia']
        geom['properties']['vot_t_10000_silvia'] = row.iloc[0]['vot_t_10000_silvia']
        geom['properties']['voti_pd_10000_silvia'] = row.iloc[0]['voti_pd_10000_silvia']
        geom['properties']['ele_t_10000_marcello'] = row.iloc[0]['ele_t_10000_marcello']
        geom['properties']['vot_t_10000_marcello'] = row.iloc[0]['vot_t_10000_marcello']
        geom['properties']['voti_pd_10000_marcello'] = row.iloc[0]['voti_pd_10000_marcello']
        geom['properties']['pref_totale'] = row.iloc[0]['pref_totale']
        geom['properties']['pref_silvia'] = row.iloc[0]['pref_silvia']
        geom['properties']['pref_marcello'] = row.iloc[0]['pref_marcello']
        geom['properties']['ele_t'] = row.iloc[0]['ele_t']
        geom['properties']['vot_t'] = row.iloc[0]['vot_t']
        geom['properties']['voti_pd'] = row.iloc[0]['voti_pd']
        
    if row.empty:
        new_row = pd.DataFrame({
            "com_istat_code_num" : [codice_istat],
            'ele_t_10000_totale': [0],
            'vot_t_10000_totale': [0],
            'voti_pd_10000_totale': [0],
            'ele_t_10000_silvia': [0],
            'vot_t_10000_silvia': [0],
            'voti_pd_10000_silvia': [0],
            'ele_t_10000_marcello': [0],
            'vot_t_10000_marcello': [0],
            'voti_pd_10000_marcello': [0],
            'pref_totale': [0],
            'pref_silvia': [0],
            'pref_marcello': [0],
            'ele_t': [0],
            'vot_t': [0],
            'voti_pd': [0]
        })
        df = pd.concat([df, new_row], ignore_index=True)
        geom['properties']['ele_t_10000_totale'] = 0
        geom['properties']['vot_t_10000_totale'] = 0
        geom['properties']['voti_pd_10000_totale'] = 0
        geom['properties']['ele_t_10000_silvia'] = 0
        geom['properties']['vot_t_10000_silvia'] = 0
        geom['properties']['voti_pd_10000_silvia'] = 0
        geom['properties']['ele_t_10000_marcello'] = 0
        geom['properties']['vot_t_10000_marcello'] = 0
        geom['properties']['voti_pd_10000_marcello'] = 0
        geom['properties']['pref_totale'] = 0
        geom['properties']['pref_silvia'] = 0
        geom['properties']['pref_marcello'] = 0
        geom['properties']['ele_t'] = 0
        geom['properties']['vot_t'] = 0
        geom['properties']['voti_pd'] = 0
        
for data_type in ["ele_t_10000", "vot_t_10000", "voti_pd_10000"]:
    for candidate in ["totale", "silvia", "marcello"]:
        lower_clip = np.percentile(df[f'{data_type}_{candidate}'], 1)
        upper_clip = np.percentile(df[f'{data_type}_{candidate}'], 99)
        colormap = cm.LinearColormap(
            colors=['white', '#502379', 'black'],
            vmin=lower_clip,
            vmax=upper_clip
        ).to_step(n=30)  # Optionally, convert to a stepped colormap

        def styler_function(feature):
            municipality_code = feature['properties']['com_istat_code_num']
            votes_per_10000 = df.loc[
                df['com_istat_code_num'] == municipality_code, f'{data_type}_{candidate}'
            ].values[0]
            return {
                'fillOpacity': 0.7,
                'weight': 0.2,
                'fillColor': colormap(votes_per_10000)
            }
        
        m = folium.Map(location=[44.494887, 11.342616], zoom_start=8, tiles=None)
        folium.TileLayer('openstreetmap', name='OpenStreetMap', overlay=True).add_to(m)
        
        tooltip =  [
            value for key, value in 
            {
                "ele_t_10000" : "elettori", 
                "vot_t_10000" : "votanti effettivi", 
                "voti_pd_10000" : "elettori PD"
            }.items() 
            if data_type == key
        ][0]
        
        folium.TopoJson(
            topojson_comuni,
            name='Layer preferenze',
            style_function=styler_function,
            tooltip=folium.GeoJsonTooltip(
                fields=['name', 'prov_name', f'pref_{candidate}', data_type[:-6], f'{data_type}_{candidate}'],
                aliases=['Comune:', 'Provincia:', 'Preferenze:', tooltip[0].upper() + tooltip[1:], f'Preferenze ogni 10000 {tooltip}'],
                localize=True
            ),
            object_path='objects.municipalities'
        ).add_to(m)

        folium.LayerControl().add_to(m)

        m.save(f'../webapp/templates/maps/{data_type}_{candidate}.html')
