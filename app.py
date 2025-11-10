# fichier: app.py
import streamlit as st

st.set_page_config(layout="wide")
st.title("🚀 Copilote Projet MVP - Flow fluide 2 niveaux")
st.markdown("Clique sur la catégorie puis sur l’intention précise pour obtenir des actions concrètes.")

# --- Base de ressources enrichie ---
RESOURCES = [
    # Financement
    {"name": "Guide bourse et aides", "url":"https://exemple.com/bourse", "tags":["Financement","Bourse/Aide"], 
     "purpose":"Pour obtenir un financement non dilutif", "outcome":"Identifier et postuler aux aides adaptées"},
    {"name": "Template Business Model", "url":"https://exemple.com/bm", "tags":["Financement","Valider Business Model"],
     "purpose":"Pour tester la viabilité de ton business model", "outcome":"Savoir si ton projet est rentable sur papier"},
    {"name": "Guide levée de fonds", "url":"https://exemple.com/levée", "tags":["Financement","Lever Fonds"],
     "purpose":"Pour structurer une levée de fonds", "outcome":"Préparer un pitch et identifier investisseurs potentiels"},
    # Validation marché
    {"name": "Checklist MVP", "url":"https://exemple.com/mvp", "tags":["Validation marché","Tester MVP"],
     "purpose":"Pour tester ton MVP rapidement", "outcome":"Collecter des feedbacks concrets"},
    {"name": "Mentor produit", "url":"https://exemple.com/mentor", "tags":["Validation marché","Itérer produit"],
     "purpose":"Pour améliorer ton produit selon des conseils d’experts", "outcome":"Optimiser ton MVP selon feedback"},
    # Stratégie
    {"name": "Template Business Plan", "url":"https://exemple.com/bp", "tags":["Stratégie","Structurer Plan"],
     "purpose":"Pour formaliser ta stratégie", "outcome":"Avoir un business plan structuré"},
    {"name": "Guide Go-to-market", "url":"https://exemple.com/gotm", "tags":["Stratégie","Go-to-market"],
     "purpose":"Pour définir ta stratégie de lancement", "outcome":"Plan d’action concret pour le lancement"},
    # Compétences
    {"name": "Bootcamp entrepreneuriat", "url":"https://exemple.com/bootcamp", "tags":["Compétences","Acquérir compétence clé"],
     "purpose":"Pour accélérer tes compétences entrepreneuriales", "outcome":"Maîtriser les fondamentaux pour lancer ton projet"},
    {"name": "Réseau mentor", "url":"https://exemple.com/mentor-reseau", "tags":["Compétences","Trouver mentor"],
     "purpose":"Pour trouver un mentor adapté à ton projet", "outcome":"Accompagnement personnalisé"}
]

# --- Session state ---
if "category" not in st.session_state:
    st.session_state.category = None
if "intent" not in st.session_state:
    st.session_state.intent = None

# --- Etape 1 : Catégorie ---
if not st.session_state.category:
    st.markdown("### 🔹 Choisis la catégorie principale de ton besoin")
    cols = st.columns(4)
    for i, cat in enumerate(["Financement", "Validation marché", "Stratégie", "Compétences"]):
        if cols[i%4].button(cat):
            st.session_state.category = cat

# --- Etape 2 : Sous-intention ---
elif not st.session_state.intent:
    st.markdown(f"### 🔹 Tu as choisi : {st.session_state.category}. Choisis ton intention précise")
    # récupérer toutes les sous-intentions possibles
    intents = sorted({r["tags"][1] for r in RESOURCES if r["tags"][0]==st.session_state.category})
    cols = st.columns(len(intents))
    for i, it in enumerate(intents):
        if cols[i].button(it):
            st.session_state.intent = it

# --- Etape 3 : Affichage ressources ---
else:
    st.markdown(f"### ✅ Actions recommandées pour : {st.session_state.category} → {st.session_state.intent}")
    filtered = [r for r in RESOURCES if r["tags"][0]==st.session_state.category and r["tags"][1]==st.session_state.intent]
    for r in filtered:
        st.markdown(f"- [{r['name']}]({r['url']})")
        st.markdown(f"  - **Pour** : {r['purpose']}")
        st.markdown(f"  - **Résultat attendu** : {r['outcome']}")

    if st.button("🔄 Recommencer"):
        st.session_state.category = None
        st.session_state.intent = None

st.markdown("---")
st.markdown("MVP fluide – 2 clics suffisent pour accéder à des ressources précises avec raison et résultat attendu")
