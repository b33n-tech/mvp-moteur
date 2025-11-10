# fichier: app.py
import streamlit as st

st.set_page_config(layout="wide")
st.title("🚀 Copilote Projet MVP - Flow fluide")
st.markdown("Clique simplement sur ce qui résonne avec ton projet, et le copilote ajuste les recommandations automatiquement.")

# --- Base de ressources avec tags multi-axes ---
RESOURCES = [
    {"name": "Modèle campagne crowdfunding", "url": "https://exemple.com/campagne", "tags": ["financement", "crowdfunding"]},
    {"name": "Plateformes adaptées", "url": "https://exemple.com/plateformes", "tags": ["financement", "crowdfunding"]},
    {"name": "Checklist communication", "url": "https://exemple.com/checklist", "tags": ["financement", "crowdfunding"]},

    {"name": "Checklist MVP", "url": "https://exemple.com/mvp", "tags": ["validation marché", "prototype"]},
    {"name": "Plateforme test utilisateurs", "url": "https://exemple.com/test", "tags": ["validation marché", "prototype"]},
    {"name": "Mentor produit", "url": "https://exemple.com/mentor", "tags": ["validation marché", "prototype"]},

    {"name": "Formations en ligne", "url": "https://exemple.com/formations", "tags": ["compétences", "formation"]},
    {"name": "Bootcamp entrepreneuriat", "url": "https://exemple.com/bootcamp", "tags": ["compétences", "formation"]},
    {"name": "Réseau mentor", "url": "https://exemple.com/mentor-reseau", "tags": ["compétences", "formation"]},

    {"name": "Template Business Plan", "url": "https://exemple.com/bp", "tags": ["stratégie", "business plan"]},
    {"name": "Guide Go-to-market", "url": "https://exemple.com/gotm", "tags": ["stratégie", "business plan"]},
    {"name": "Atelier stratégie", "url": "https://exemple.com/atelier", "tags": ["stratégie", "business plan"]},
]

# --- Etapes fluides ---
if "selected_tags" not in st.session_state:
    st.session_state.selected_tags = []

st.markdown("### 🔹 Sélectionne ce qui correspond le mieux à ton projet")

# Afficher les options sous forme de cartes interactives (boutons)
all_tags = sorted({tag for r in RESOURCES for tag in r["tags"]})
cols = st.columns(4)
for i, tag in enumerate(all_tags):
    if cols[i % 4].button(tag):
        if tag not in st.session_state.selected_tags:
            st.session_state.selected_tags.append(tag)

# Afficher les tags sélectionnés
if st.session_state.selected_tags:
    st.markdown(f"**Sélections actuelles :** {', '.join(st.session_state.selected_tags)}")

# --- Filtrer ressources automatiquement selon tags sélectionnés ---
if st.session_state.selected_tags:
    filtered = []
    for r in RESOURCES:
        if any(tag in r["tags"] for tag in st.session_state.selected_tags):
            filtered.append(r)

    st.markdown("### ✅ Actions recommandées")
    for r in filtered:
        st.markdown(f"- [{r['name']}]({r['url']})")

# Bouton pour recommencer
if st.button("🔄 Recommencer"):
    st.session_state.selected_tags = []

st.markdown("---")
st.markdown("MVP fluide – le copilote s’adapte à ton flux de pensée")
