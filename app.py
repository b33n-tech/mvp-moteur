# fichier: app.py
import streamlit as st

st.set_page_config(layout="wide")
st.title("🚀 Copilote Projet MVP - Flow fluide et actionnable")
st.markdown("Clique sur ce qui résonne avec ton projet. Chaque ressource indique pourquoi elle est utile et le résultat attendu.")

# --- Base de ressources enrichie ---
RESOURCES = [
    {
        "name": "Modèle campagne crowdfunding",
        "url": "https://exemple.com/campagne",
        "tags": ["financement", "crowdfunding"],
        "purpose": "Pour structurer ta campagne de crowdfunding",
        "outcome": "Avoir un modèle prêt à remplir et publier"
    },
    {
        "name": "Plateformes adaptées",
        "url": "https://exemple.com/plateformes",
        "tags": ["financement", "crowdfunding"],
        "purpose": "Pour trouver la plateforme la plus adaptée à ton projet",
        "outcome": "Sélectionner la plateforme idéale pour lancer ta campagne"
    },
    {
        "name": "Checklist communication",
        "url": "https://exemple.com/checklist",
        "tags": ["financement", "crowdfunding"],
        "purpose": "Pour préparer la communication autour de ta campagne",
        "outcome": "Avoir une checklist complète prête à exécuter"
    },
    {
        "name": "Checklist MVP",
        "url": "https://exemple.com/mvp",
        "tags": ["validation marché", "prototype"],
        "purpose": "Pour valider rapidement ton MVP",
        "outcome": "Recevoir un feedback concret de 10 utilisateurs"
    },
    {
        "name": "Plateforme test utilisateurs",
        "url": "https://exemple.com/test",
        "tags": ["validation marché", "prototype"],
        "purpose": "Pour tester ton prototype avec de vrais utilisateurs",
        "outcome": "Identifier rapidement les points forts et points faibles de ton MVP"
    },
    {
        "name": "Mentor produit",
        "url": "https://exemple.com/mentor",
        "tags": ["validation marché", "prototype"],
        "purpose": "Pour obtenir un retour expert sur ton produit",
        "outcome": "Améliorer ton MVP selon des conseils personnalisés"
    },
    {
        "name": "Formations en ligne",
        "url": "https://exemple.com/formations",
        "tags": ["compétences", "formation"],
        "purpose": "Pour acquérir rapidement une compétence clé",
        "outcome": "Être capable de réaliser une tâche spécifique liée au projet"
    },
    {
        "name": "Bootcamp entrepreneuriat",
        "url": "https://exemple.com/bootcamp",
        "tags": ["compétences", "formation"],
        "purpose": "Pour accélérer tes compétences entrepreneuriales",
        "outcome": "Maîtriser les fondamentaux pour structurer et lancer ton projet"
    },
    {
        "name": "Réseau mentor",
        "url": "https://exemple.com/mentor-reseau",
        "tags": ["compétences", "formation"],
        "purpose": "Pour trouver un mentor adapté à ton projet",
        "outcome": "Avoir un accompagnement personnalisé pour progresser plus vite"
    },
    {
        "name": "Template Business Plan",
        "url": "https://exemple.com/bp",
        "tags": ["stratégie", "business plan"],
        "purpose": "Pour formaliser ta stratégie",
        "outcome": "Avoir un business plan structuré prêt à présenter"
    },
    {
        "name": "Guide Go-to-market",
        "url": "https://exemple.com/gotm",
        "tags": ["stratégie", "business plan"],
        "purpose": "Pour définir ta stratégie de lancement",
        "outcome": "Construire un plan d’action concret pour ton go-to-market"
    },
    {
        "name": "Atelier stratégie",
        "url": "https://exemple.com/atelier",
        "tags": ["stratégie", "business plan"],
        "purpose": "Pour travailler ta stratégie avec un expert",
        "outcome": "Clarifier tes prochaines étapes stratégiques"
    }
]

# --- Flow fluide ---
if "selected_tags" not in st.session_state:
    st.session_state.selected_tags = []

st.markdown("### 🔹 Sélectionne ce qui correspond le mieux à ton projet")

# Afficher les tags sous forme de boutons
all_tags = sorted({tag for r in RESOURCES for tag in r["tags"]})
cols = st.columns(4)
for i, tag in enumerate(all_tags):
    if cols[i % 4].button(tag):
        if tag not in st.session_state.selected_tags:
            st.session_state.selected_tags.append(tag)

# Afficher les tags sélectionnés
if st.session_state.selected_tags:
    st.markdown(f"**Sélections actuelles :** {', '.join(st.session_state.selected_tags)}")

# --- Filtrer et afficher les ressources ---
if st.session_state.selected_tags:
    filtered = []
    for r in RESOURCES:
        if any(tag in r["tags"] for tag in st.session_state.selected_tags):
            filtered.append(r)

    st.markdown("### ✅ Actions recommandées")
    for r in filtered:
        st.markdown(f"- [{r['name']}]({r['url']})")
        st.markdown(f"  - **Pour** : {r['purpose']}")
        st.markdown(f"  - **Résultat attendu** : {r['outcome']}")

# Bouton pour recommencer
if st.button("🔄 Recommencer"):
    st.session_state.selected_tags = []

st.markdown("---")
st.markdown("MVP fluide – chaque ressource indique pourquoi et ce que tu progresses en l'utilisant")
