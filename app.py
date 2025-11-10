# fichier: app.py
import streamlit as st

# --- Base de données simplifiée ---
RESOURCES = {
    "Financement": [
        {"name": "Guide crowdfunding", "url": "https://exemple.com/crowdfunding"},
        {"name": "Aides régionales", "url": "https://exemple.com/aides"},
        {"name": "Prêt d'honneur", "url": "https://exemple.com/pret"}
    ],
    "Validation marché": [
        {"name": "Checklist MVP", "url": "https://exemple.com/mvp"},
        {"name": "Plateforme test utilisateurs", "url": "https://exemple.com/test"},
        {"name": "Mentor produit", "url": "https://exemple.com/mentor"}
    ],
    "Compétences": [
        {"name": "Formations en ligne", "url": "https://exemple.com/formations"},
        {"name": "Bootcamp entrepreneuriat", "url": "https://exemple.com/bootcamp"},
        {"name": "Réseau mentor", "url": "https://exemple.com/mentor-reseau"}
    ],
    "Stratégie": [
        {"name": "Template Business Plan", "url": "https://exemple.com/bp"},
        {"name": "Guide Go-to-market", "url": "https://exemple.com/gotm"},
        {"name": "Atelier stratégie", "url": "https://exemple.com/atelier"}
    ]
}

# --- Streamlit UI ---
st.title("🚀 Copilote Projet MVP")
st.markdown("En 2 minutes, identifie ton blocage et trouve 2-3 actions concrètes pour avancer.")

# Étape 1 : Choix du blocage
blocage = st.selectbox(
    "Quel est ton blocage principal ?", 
    ["Financement", "Validation marché", "Compétences", "Stratégie"]
)

# Étape 2 : Affiner (optionnel, ici simple pour MVP)
if blocage:
    st.markdown(f"### 🔹 Actions pour le blocage : {blocage}")
    actions = RESOURCES.get(blocage, [])
    for action in actions:
        st.markdown(f"- [{action['name']}]({action['url']})")

# Footer
st.markdown("---")
st.markdown("MVP sans LLM - Base de ressources simplifiée")
