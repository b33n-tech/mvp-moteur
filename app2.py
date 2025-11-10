# fichier: app_multi_ecos.py
import streamlit as st

st.set_page_config(layout="wide")
st.title("🚀 Copilote Projet Multi-Écosystèmes")
st.markdown("Choisis un sujet, le moteur central t'oriente, puis chaque mini-copilote filtre les ressources les plus pertinentes.")

# --- Base des écosystèmes ---
ECOSYSTEMS = {
    "Financement": [
        {"name":"Guide bourse et aides","type":"Cours","tags":["Bourse/Aide","<1 mois"], 
         "purpose":"Obtenir un financement non dilutif","outcome":"Identifier et postuler aux aides"},
        {"name":"Template Business Model","type":"Framework","tags":["Valider Business Model","Seul"],
         "purpose":"Tester la viabilité de ton business model","outcome":"Savoir si ton projet est rentable"},
        {"name":"Podcast levée de fonds","type":"Podcast","tags":["Lever Fonds","Scalabilité"],
         "purpose":"Comprendre comment structurer une levée de fonds","outcome":"Préparer un pitch et identifier investisseurs"},
    ],
    "Stratégie": [
        {"name":"Template Business Plan","type":"Cours","tags":["Structurer Plan"],
         "purpose":"Formaliser ta stratégie","outcome":"Avoir un business plan structuré"},
        {"name":"Guide Go-to-market","type":"Méthode","tags":["Go-to-market"],
         "purpose":"Définir ta stratégie de lancement","outcome":"Plan d’action concret pour le lancement"},
    ],
    "Compétences": [
        {"name":"Bootcamp entrepreneuriat","type":"Programme","tags":["Acquérir compétence clé"],
         "purpose":"Accélérer tes compétences entrepreneuriales","outcome":"Maîtriser les fondamentaux pour lancer ton projet"},
        {"name":"Réseau mentor","type":"Réseau","tags":["Trouver mentor"],
         "purpose":"Trouver un mentor adapté","outcome":"Accompagnement personnalisé"},
    ]
}

# --- Session state ---
for key in ["subject","intent","context","selected_contexts"]:
    if key not in st.session_state:
        st.session_state[key] = None if key!="selected_contexts" else []

# --- Moteur central : choix du sujet ---
if not st.session_state.subject:
    st.markdown("### 🔹 Choisis le sujet principal")
    cols = st.columns(len(ECOSYSTEMS))
    for i, subj in enumerate(ECOSYSTEMS.keys()):
        if cols[i].button(subj):
            st.session_state.subject = subj

# --- Mini-copilote : sous-intention (arborescence) ---
elif not st.session_state.intent:
    st.markdown(f"### 🔹 Sujet : {st.session_state.subject}. Choisis ton intention")
    intents = sorted({r["tags"][0] for r in ECOSYSTEMS[st.session_state.subject]})
    cols = st.columns(len(intents))
    for i, it in enumerate(intents):
        if cols[i].button(it):
            st.session_state.intent = it

# --- Mini-copilote : contexte optionnel ---
elif st.session_state.intent and not st.session_state.context:
    st.markdown(f"### 🔹 Affiner par contexte / contrainte (optionnel)")
    context_tags = sorted({t for r in ECOSYSTEMS[st.session_state.subject] if r["tags"][0]==st.session_state.intent for t in r["tags"][1:]})
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

# --- Affichage ressources filtrées + pondération ---
if st.session_state.intent and (st.session_state.context or st.session_state.context=="none"):
    st.markdown("### ✅ Ressources recommandées")
    
    def score_resource(r):
        score = 0
        if r["tags"][0]==st.session_state.intent:
            score += 1
        score += sum(1 for t in st.session_state.selected_contexts if t in r["tags"])
        return score
    
    scored = [(score_resource(r), r) for r in ECOSYSTEMS[st.session_state.subject]]
    scored = [x for x in scored if x[0]>0]
    scored.sort(reverse=True, key=lambda x:x[0])

    for score,r in scored:
        st.markdown(f"- {r['type']}: [{r['name']}]({r.get('url','')}) *(score pertinence : {score})*")
        st.markdown(f"  - **Pour** : {r['purpose']}")
        st.markdown(f"  - **Résultat attendu** : {r['outcome']}")

# --- Recommencer ---
if st.button("🔄 Recommencer"):
    for key in ["subject","intent","context","selected_contexts"]:
        st.session_state[key] = None if key!="selected_contexts" else []

st.markdown("---")
st.markdown("MVP multi-écos – moteur central + mini-copilotes par sujet, arborescence progressive, pondération automatique")
