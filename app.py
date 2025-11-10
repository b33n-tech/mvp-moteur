# fichier: app.py
import streamlit as st

# --- Base de ressources simplifiée ---
RESOURCES = {
    "crowdfunding": [
        {"name": "Modèle campagne crowdfunding", "url": "https://exemple.com/campagne"},
        {"name": "Plateformes adaptées", "url": "https://exemple.com/plateformes"},
        {"name": "Checklist communication", "url": "https://exemple.com/checklist"}
    ],
    "validation marché": [
        {"name": "Checklist MVP", "url": "https://exemple.com/mvp"},
        {"name": "Plateforme test utilisateurs", "url": "https://exemple.com/test"},
        {"name": "Mentor produit", "url": "https://exemple.com/mentor"}
    ],
    "compétences": [
        {"name": "Formations en ligne", "url": "https://exemple.com/formations"},
        {"name": "Bootcamp entrepreneuriat", "url": "https://exemple.com/bootcamp"},
        {"name": "Réseau mentor", "url": "https://exemple.com/mentor-reseau"}
    ],
    "stratégie": [
        {"name": "Template Business Plan", "url": "https://exemple.com/bp"},
        {"name": "Guide Go-to-market", "url": "https://exemple.com/gotm"},
        {"name": "Atelier stratégie", "url": "https://exemple.com/atelier"}
    ]
}

# --- Mapping mots-clés vers ressources ---
KEYWORDS = {
    "crowdfunding": "crowdfunding",
    "financement": "crowdfunding",
    "investisseur": "crowdfunding",
    "mvp": "validation marché",
    "prototype": "validation marché",
    "test utilisateur": "validation marché",
    "compétence": "compétences",
    "formation": "compétences",
    "stratégie": "stratégie",
    "business plan": "stratégie",
    "go to market": "stratégie"
}

# --- Streamlit UI ---
st.title("🚀 Copilote Projet MVP Smooth")
st.markdown("Décris rapidement ta solution ou ton idée, et reçois des actions concrètes pour avancer.")

# Input libre
user_input = st.text_area("Décris ta solution ou ton blocage (1-2 phrases)", height=100)

def detect_need(text):
    text_lower = text.lower()
    for keyword, category in KEYWORDS.items():
        if keyword in text_lower:
            return category
    return None

if user_input:
    category = detect_need(user_input)
    if category:
        st.markdown(f"### 🔹 Actions recommandées pour : {category}")
        actions = RESOURCES.get(category, [])
        for action in actions:
            st.markdown(f"- [{action['name']}]({action['url']})")
    else:
        st.markdown("⚠️ Désolé, je n'ai pas identifié de besoin précis. Essaie d'être plus concret (financement, MVP, stratégie, compétences…).")

# Footer
st.markdown("---")
st.markdown("MVP sans LLM – expérience ultra-rapide et directe")
