# MBA Surgical Challenge · SOBACIR 2026

Aplicación Streamlit que sirve el juego completo de SOBACIR 2026 en un único despliegue web.

## Streamlit Community Cloud

- Repository: `dukvanmid/blank-app`
- Branch: `sobacir-streamlit`
- Main file path: `streamlit_app.py`
- App URL sugerida: `mba-sobacir-2026`

El juego se carga desde `app_payload/`, que contiene el HTML completo comprimido. Los logotipos de Hospital de Manacor y Grupo Juaneda se cargan desde recursos locales del repositorio y se integran como `data:` al abrir el juego, para no depender de URLs externas.
