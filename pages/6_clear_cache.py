import streamlit as st

st.runtime.legacy_caching.clear_cache()
st.cache_data.clear()
st.cache_resource.clear()
