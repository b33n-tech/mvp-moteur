# fichier: app.py
import streamlit as st

st.title("🚀 Copilote Projet MVP - Boutons")
st.markdown("Clique sur ton blocage puis sur ton stade pour recevoir des actions concrètes.")

# --- Base de ressources structurée ---
RESOURCES = [
    {"blocage": "Financement", "stade": "Crowdfunding", "name": "Modèle campagne crowdfunding", "url": "https://exemple.com/campagne"},
    {"blocage": "Financement", "stade": "Crowdfunding", "name": "Plateformes adaptées", "url": "https://exemple.com/plateformes"},
    {"blocage": "Financement", "stade": "Crowdfunding", "name": "Checklist communication", "url": "https://exemple.com/checklist"},

    {"blocage": "Validation marché", "stade": "Prototype", "name": "Checklist MVP", "url": "https://exemple.com/mvp"},
    {"blocage": "Validation marché", "stade": "Prototype", "name": "Plateforme test utilisateurs", "url": "https://exemple.com/test"},
    {"blocage": "Validation marché", "stade": "Prototype", "name": "Mentor produit", "url": "https://exemple.com/mentor"},

    {"blocage": "Compétences", "stade": "Formation", "name": "Formations en ligne", "url": "https://exemple.com/formations"},
    {"blocage": "Compétences", "stade": "Formation", "name": "Bootcamp entrepreneuriat", "url": "https://exemple.com/bootcamp"},
    {"blocage": "Compétences", "stade": "Formation", "name": "Réseau mentor", "url": "https://exemple.com/mentor-reseau"},

    {"blocage": "Stratégie", "stade": "Business Plan", "name": "Template Business Plan", "url": "https://exemple.com/bp"},
    {"blocage": "Stratégie", "stade": "Business Plan", "name": "Guide Go-to-market", "url": "https://exemple.com/gotm"},
    {"blocage": "Stratégie", "stade": "Business Plan", "name": "Atelier stratégie", "url": "https://exemple.com/atelier"},
]

# --- Etape 1 : Choix du blocage ---
if "blocage" not in st.session_state:
    st.session_state.blocage = None
if "stade" not in st.session_state:
    st.session_state.stade = None

def select_blocage(b):
    st.session_state.blocage = b

if not st.session_state.blocage:
    st.markdown("### 🔹 Quel est ton blocage principal ?")
    cols = st.columns(4)
    for i, b in enumerate(["Financement", "Validation marché", "Compétences", "Stratégie"]):
        if cols[i%4].button(b):
            select_blocage(b)

# --- Etape 2 : Choix du stade ---
elif not st.session_state.stade:
    st.markdown(f"### 🔹 Tu as choisi : {st.session_state.blocage}. Quel est ton stade / solution ?")
    # Récupérer les stades possibles pour ce blocage
    stades = list({r['stade'] for r in RESOURCES if r['blocage']==st.session_state.blocage})
    cols = st.columns(len(stades))
    for i, s in enumerate(stades):
        if cols[i].button(s):
            st.session_state.stade = s

# --- Etape 3 : Affichage des ressources ---
else:
    st.markdown(f"### ✅ Actions recommandées pour : {st.session_state.blocage} → {st.session_state.stade}")
    filtered = [r for r in RESOURCES if r['blocage']==st.session_state.blocage and r['stade']==st.session_state.stade]
    for r in filtered:
        st.markdown(f"- [{r['name']}]({r['url']})")

    if st.button("🔄 Recommencer"):
        st.session_state.blocage = None
        st.session_state.stade = None

# Footer
st.markdown("---")
st.markdown("MVP sans LLM – expérience fluide en 2-3 clics")
