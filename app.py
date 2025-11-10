# fichier: app.py
import streamlit as st

st.set_page_config(layout="wide")
st.title("🚀 Copilote Projet MVP - Arborescence fluide")
st.markdown("Clique sur les options à chaque étape pour affiner automatiquement les ressources les plus pertinentes.")

# --- Base de ressources multi-axes ---
RESOURCES = [
    # Financement
    {"name":"Guide bourse et aides", "url":"https://exemple.com/bourse", 
     "tags":["Financement","Bourse/Aide","<1 mois","Budget limité"],
     "purpose":"Pour obtenir un financement non dilutif", "outcome":"Identifier et postuler aux aides adaptées"},
    {"name":"Template Business Model", "url":"https://exemple.com/bm",
     "tags":["Financement","Valider Business Model","Seul"],
     "purpose":"Pour tester la viabilité de ton business model", "outcome":"Savoir si ton projet est rentable sur papier"},
    {"name":"Guide levée de fonds", "url":"https://exemple.com/levée",
     "tags":["Financement","Lever Fonds","Scalabilité"],
     "purpose":"Pour structurer une levée de fonds", "outcome":"Préparer un pitch et identifier investisseurs potentiels"},
    # Validation marché
    {"name":"Checklist MVP","url":"https://exemple.com/mvp",
     "tags":["Validation marché","Tester MVP","<1 mois","Seul"],
     "purpose":"Pour tester ton MVP rapidement", "outcome":"Collecter des feedbacks concrets"},
    # Stratégie
    {"name":"Template Business Plan","url":"https://exemple.com/bp",
     "tags":["Stratégie","Structurer Plan","Budget limité"],
     "purpose":"Pour formaliser ta stratégie","outcome":"Avoir un business plan structuré"},
    # Compétences
    {"name":"Bootcamp entrepreneuriat","url":"https://exemple.com/bootcamp",
     "tags":["Compétences","Acquérir compétence clé"], "purpose":"Pour accélérer tes compétences entrepreneuriales",
     "outcome":"Maîtriser les fondamentaux pour lancer ton projet"}
]

# --- Session state ---
for key in ["category", "intent", "context", "selected_contexts"]:
    if key not in st.session_state:
        st.session_state[key] = None if key!="selected_contexts" else []

# --- Etape 1 : Catégorie ---
if not st.session_state.category:
    st.markdown("### 🔹 Choisis la catégorie principale de ton besoin")
    cols = st.columns(4)
    for i, cat in enumerate(["Financement","Validation marché","Stratégie","Compétences"]):
        if cols[i%4].button(cat):
            st.session_state.category = cat

# --- Etape 2 : Sous-intention ---
elif not st.session_state.intent:
    st.markdown(f"### 🔹 Tu as choisi : {st.session_state.category}. Choisis ton intention précise")
    intents = sorted({r["tags"][1] for r in RESOURCES if r["tags"][0]==st.session_state.category})
    cols = st.columns(len(intents))
    for i, it in enumerate(intents):
        if cols[i].button(it):
            st.session_state.intent = it

# --- Etape 3 : Contexte (optionnel) ---
elif st.session_state.intent and not st.session_state.context:
    st.markdown(f"### 🔹 Tu as choisi : {st.session_state.intent}. Optionnel : affiner par contexte / contrainte")
    # récupérer tags de contexte disponibles
    context_tags = sorted({t for r in RESOURCES if r["tags"][0]==st.session_state.category and r["tags"][1]==st.session_state.intent for t in r["tags"][2:]})
    if context_tags:
        cols = st.columns(len(context_tags))
        for i, c in enumerate(context_tags):
            if cols[i].button(c):
                if c not in st.session_state.selected_contexts:
                    st.session_state.selected_contexts.append(c)
        if st.button("Passer sans contexte"):
            st.session_state.context = "none"
    else:
        st.session_state.context = "none"

# --- Etape 4 : Affichage ressources filtrées + pondération ---
if st.session_state.intent and (st.session_state.context or st.session_state.context=="none"):
    st.markdown("### ✅ Actions recommandées (triées par pertinence)")

    def score_resource(r):
        score = 0
        if r["tags"][0]==st.session_state.category:
            score += 1
        if r["tags"][1]==st.session_state.intent:
            score += 1
        score += sum(1 for t in st.session_state.selected_contexts if t in r["tags"])
        return score

    scored = [(score_resource(r), r) for r in RESOURCES]
    scored = [x for x in scored if x[0]>0]
    scored.sort(reverse=True, key=lambda x:x[0])

    for score,r in scored:
        st.markdown(f"- [{r['name']}]({r['url']})  *(score pertinence : {score})*")
        st.markdown(f"  - **Pour** : {r['purpose']}")
        st.markdown(f"  - **Résultat attendu** : {r['outcome']}")

# --- Bouton Recommencer ---
if st.button("🔄 Recommencer"):
    for key in ["category", "intent", "context", "selected_contexts"]:
        st.session_state[key] = None if key!="selected_contexts" else []

st.markdown("---")
st.markdown("MVP fluide – arborescence progressive, pondération automatique, 2-3 clics suffisent pour accéder aux ressources pertinentes")
