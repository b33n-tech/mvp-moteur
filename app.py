# fichier: app.py
import streamlit as st

st.set_page_config(layout="wide")
st.title("🚀 Copilote Projet MVP - Triangulation fluide")
st.markdown("Clique sur ce qui résonne avec ton projet. Les ressources les plus pertinentes remontent automatiquement.")

# --- Base de ressources multi-axes ---
RESOURCES = [
    {
        "name": "Guide bourse et aides",
        "url": "https://exemple.com/bourse",
        "tags": ["Financement","Bourse/Aide","<1 mois","Budget limité"],
        "purpose":"Pour obtenir un financement non dilutif",
        "outcome":"Identifier et postuler aux aides adaptées"
    },
    {
        "name": "Template Business Model",
        "url":"https://exemple.com/bm",
        "tags":["Financement","Valider Business Model","Seul"],
        "purpose":"Pour tester la viabilité de ton business model",
        "outcome":"Savoir si ton projet est rentable sur papier"
    },
    {
        "name": "Guide levée de fonds",
        "url":"https://exemple.com/levée",
        "tags":["Financement","Lever Fonds","Scalabilité"],
        "purpose":"Pour structurer une levée de fonds",
        "outcome":"Préparer un pitch et identifier investisseurs potentiels"
    },
    {
        "name": "Checklist MVP",
        "url":"https://exemple.com/mvp",
        "tags":["Validation marché","Tester MVP","<1 mois","Seul"],
        "purpose":"Pour tester ton MVP rapidement",
        "outcome":"Collecter des feedbacks concrets"
    },
    {
        "name": "Template Business Plan",
        "url":"https://exemple.com/bp",
        "tags":["Stratégie","Structurer Plan","Budget limité"],
        "purpose":"Pour formaliser ta stratégie",
        "outcome":"Avoir un business plan structuré"
    },
]

# --- Session state ---
if "selections" not in st.session_state:
    st.session_state.selections = []

# --- Affichage boutons axes ---
st.markdown("### 🔹 Sélectionne ce qui correspond le mieux à ton projet")
all_tags = sorted({tag for r in RESOURCES for tag in r["tags"]})
cols = st.columns(4)
for i, tag in enumerate(all_tags):
    if cols[i % 4].button(tag):
        if tag not in st.session_state.selections:
            st.session_state.selections.append(tag)

# Afficher les tags sélectionnés
if st.session_state.selections:
    st.markdown(f"**Sélections actuelles :** {', '.join(st.session_state.selections)}")

# --- Filtrage + pondération automatique ---
def score_resource(r, selections):
    return sum(1 for t in r["tags"] if t in selections)

if st.session_state.selections:
    scored = []
    for r in RESOURCES:
        s = score_resource(r, st.session_state.selections)
        if s>0:
            scored.append((s,r))
    scored.sort(reverse=True, key=lambda x: x[0])  # tri par pertinence

    st.markdown("### ✅ Actions recommandées (les plus pertinentes en haut)")
    for score, r in scored:
        st.markdown(f"- [{r['name']}]({r['url']})  *(score pertinence : {score})*")
        st.markdown(f"  - **Pour** : {r['purpose']}")
        st.markdown(f"  - **Résultat attendu** : {r['outcome']}")

# Bouton recommencer
if st.button("🔄 Recommencer"):
    st.session_state.selections = []

st.markdown("---")
st.markdown("MVP ultra-fluide – la pertinence des ressources s’ajuste automatiquement selon tes clics")
