import streamlit as st
import requests
import time
import random
from datetime import datetime

# Configuration Streamlit
st.set_page_config(
    page_title="kzSINT - OSINT Tool 🎃",
    page_icon="🎃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Thème Halloween
st.markdown("""
<style>
    :root {
        --primary-color: #ff6600;
        --background-color: #0a0000;
        --text-color: #ffaa66;
    }
    .stApp {
        background-color: #0a0000;
    }
    .stButton>button {
        background-color: #ff6600;
        color: white;
        border: 2px solid #ff6600;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #cc4400;
        border-color: #cc4400;
    }
    .stTextInput>div>div>input {
        background-color: #0d0202;
        color: #ffaa66;
        border: 2px solid #ff6600;
        border-radius: 10px;
    }
    .stSelectbox>div>div>select {
        background-color: #0d0202;
        color: #ffaa66;
        border: 2px solid #ff6600;
        border-radius: 10px;
    }
    .stMarkdown {
        color: #ffaa66;
    }
    h1, h2, h3 {
        color: #ff6600 !important;
    }
    .chat-message {
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 80%;
    }
    .user-message {
        background-color: #ff6600;
        color: white;
        margin-left: auto;
    }
    .bot-message {
        background-color: #330000;
        color: #ffaa66;
        border: 2px solid #ff6600;
    }
</style>
""", unsafe_allow_html=True)

# Configuration API
API_KEY = "69db89a6e2048c4d485e35b4b25fd2e1"
API_URL_GENERAL = "https://api.lookup2bz.xyz/api/v1/query"
API_URL_SNAPCHAT = "https://api.lookup2bz.xyz/api/v1/snapchat"

# Variables de session
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'scan_results' not in st.session_state:
    st.session_state.scan_results = []

# Navigation
page = st.sidebar.radio(
    "🎃 kzSINT Navigation",
    ["🔍 SEARCH", "🛒 BUY", "❓ HELP"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👤 Utilisateur")
st.sidebar.markdown("kz-7686")
st.sidebar.markdown("🟢 En ligne")

# ============== PAGE SEARCH ==============
if page == "🔍 SEARCH":
    st.markdown("# 🔍 SEARCH")
    st.markdown("Recherche de renseignements en sources ouvertes — moteur d'analyse kzSINT")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        search_type = st.selectbox(
            "Type de recherche",
            ["TÉLÉPHONE", "EMAIL", "SNAPCHAT", "NOM/PRENOM"],
            label_visibility="collapsed"
        )
    
    with col2:
        target = st.text_input(
            "Cible : pseudo, email, domaine...",
            placeholder="Entre ta cible ici...",
            label_visibility="collapsed"
        )
    
    with col3:
        scan_clicked = st.button("🎃 SCANNER", use_container_width=True, type="primary")
    
    # Zone de résultats
    st.markdown("### 📊 Terminal kzSINT")
    results_container = st.container()
    
    if scan_clicked and target:
        with st.spinner("🎃 Scan en cours..."):
            try:
                headers = {"X-API-Key": API_KEY}
                
                if search_type == "SNAPCHAT":
                    params = {"query": target}
                    response = requests.get(API_URL_SNAPCHAT, params=params, headers=headers, timeout=30)
                    
                    if response.status_code == 200:
                        data = response.json()
                        st.success(f"✅ Scan Snapchat terminé - {data.get('time_ms', 0)}ms")
                        
                        result = data.get("result", {})
                        if result:
                            # Profil
                            profile = result.get("profile", {})
                            if profile:
                                st.markdown("#### 👤 PROFIL")
                                st.json(profile)
                            
                            # Anciens pseudos
                            prevnames = result.get("prevname_result", [])
                            if prevnames:
                                st.markdown("#### 📝 ANCIENS PSEUDOS")
                                for i, prev in enumerate(prevnames):
                                    st.write(f"**{i+1}.** {prev.get('username', 'N/A')}")
                    else:
                        st.error(f"❌ Erreur: {response.status_code}")
                else:
                    params = {"query": target, "limit": 150}
                    response = requests.get(API_URL_GENERAL, params=params, headers=headers, timeout=30)
                    
                    if response.status_code == 200:
                        data = response.json()
                        count = data.get("count", 0)
                        results = data.get("results", [])
                        
                        st.success(f"✅ {count} résultats trouvés - {data.get('time_ms', 0)}ms")
                        
                        # Affichage structuré
                        for i, result in enumerate(results):
                            source = result.get("source", "inconnu")
                            result_data = result.get("data", {})
                            
                            with st.expander(f"📁 Résultat #{i+1} - {source}"):
                                st.json(result_data)
                    else:
                        st.error(f"❌ Erreur: {response.status_code}")
                        
            except Exception as e:
                st.error(f"❌ Erreur: {str(e)}")
    else:
        st.info("🎃 En attente d'une cible...")

# ============== PAGE BUY ==============
elif page == "🛒 BUY":
    st.markdown("# 🛒 NOS OFFRES")
    st.markdown("Boutique officielle kzSINT — accès, outils et abonnements")
    
    # Produits
    products = [
        {
            "name": "kzSINT BASIC",
            "price": "9.99€",
            "features": ["10 scans / jour", "2 modules", "Support communautaire"],
            "color": "#2ecc71"
        },
        {
            "name": "kzSINT PRO",
            "price": "29.99€",
            "features": ["Scans illimités", "Tous les modules", "Alertes temps réel"],
            "color": "#3498db"
        },
        {
            "name": "kzSINT ELITE",
            "price": "99.99€",
            "features": ["Accès API", "Scans prioritaires", "Support dédié 24/7"],
            "color": "#e74c3c"
        },
        {
            "name": "SCAN DEEP-WEB",
            "price": "4.99€",
            "features": ["Analyse ponctuelle des fuites", "Scan des forums fermés"],
            "color": "#f39c12"
        },
        {
            "name": "RAPPORT OSINT",
            "price": "19.99€",
            "features": ["Dossier complet PDF", "Analyse experte"],
            "color": "#9b59b6"
        },
    ]
    
    col1, col2, col3 = st.columns(3)
    
    for i, product in enumerate(products):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f"""
            <div style="background-color: #0d0202; border: 2px solid {product['color']}; 
                        border-radius: 15px; padding: 20px; margin: 10px 0;">
                <h3 style="color: {product['color']};">{product['name']}</h3>
                <h2 style="color: #ffaa66;">{product['price']}</h2>
                <ul>
                    {"".join([f"<li style='color: #ffaa66;'>✓ {feat}</li>" for feat in product['features']])}
                </ul>
                <button style="background-color: {product['color']}; color: white; 
                        border: none; padding: 10px 20px; border-radius: 8px; 
                        cursor: pointer; width: 100%; font-weight: bold;">
                    ACHETER
                </button>
            </div>
            """, unsafe_allow_html=True)

# ============== PAGE HELP ==============
elif page == "❓ HELP":
    st.markdown("# ❓ HELP")
    st.markdown("Support kzSINT — assistance en direct et communauté")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💬 Chat Support")
        
        # Zone de chat
        for msg in st.session_state.chat_history:
            if msg['role'] == 'user':
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>Vous:</strong> {msg['content']}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message bot-message">
                    <strong>kzBot:</strong> {msg['content']}
                </div>
                """, unsafe_allow_html=True)
        
        # Input utilisateur
        user_input = st.text_input("Écris ton message...", key="chat_input")
        
        col_send1, col_send2 = st.columns([4, 1])
        with col_send1:
            pass
        with col_send2:
            send_clicked = st.button("📤 ENVOYER")
        
        # Questions rapides
        st.markdown("### 🔥 Questions rapides")
        col_q1, col_q2, col_q3, col_q4 = st.columns(4)
        
        with col_q1:
            if st.button("💰 Prix et offres?"):
                st.session_state.chat_history.append({'role': 'user', 'content': 'Prix et offres?'})
                st.session_state.chat_history.append({'role': 'bot', 'content': get_smart_response('prix')})
                st.rerun()
        
        with col_q2:
            if st.button("🎮 Discord?"):
                st.session_state.chat_history.append({'role': 'user', 'content': 'Discord?'})
                st.session_state.chat_history.append({'role': 'bot', 'content': get_smart_response('discord')})
                st.rerun()
        
        with col_q3:
            if st.button("👤 Créer compte?"):
                st.session_state.chat_history.append({'role': 'user', 'content': 'Créer compte?'})
                st.session_state.chat_history.append({'role': 'bot', 'content': get_smart_response('compte')})
                st.rerun()
        
        with col_q4:
            if st.button("🐛 Signaler bug"):
                st.session_state.chat_history.append({'role': 'user', 'content': 'Signaler bug'})
                st.session_state.chat_history.append({'role': 'bot', 'content': get_smart_response('bug')})
                st.rerun()
        
        # Traitement du message
        if send_clicked and user_input:
            st.session_state.chat_history.append({'role': 'user', 'content': user_input})
            response = get_smart_response(user_input.lower())
            st.session_state.chat_history.append({'role': 'bot', 'content': response})
            st.rerun()
    
    with col2:
        st.markdown("### 🎮 Discord")
        st.markdown("""
        <div style="background-color: #0d0202; border: 2px solid #ff6600; 
                    border-radius: 20px; padding: 30px; text-align: center;">
            <h3 style="color: #ff6600;">Rejoins notre Discord</h3>
            <p style="color: #ffaa66;">
            📢 Annonces exclusives<br>
            💬 Entraide OSINT<br>
            🆘 Support communautaire<br>
            ⚡ Accès anticipé
            </p>
            <a href="https://discord.gg/kzsint" target="_blank">
            <button style="background-color: #5865F2; color: white; 
                    border: none; padding: 15px 30px; border-radius: 10px; 
                    cursor: pointer; font-weight: bold; font-size: 16px;">
                OUVRIR LE DISCORD
            </button>
            </a>
            <p style="color: #994400; margin-top: 15px;">discord.gg/kzsint</p>
        </div>
        """, unsafe_allow_html=True)

# Message de bienvenue initial
if not st.session_state.chat_history:
    st.session_state.chat_history.append({
        'role': 'bot',
        'content': "🎃 Bienvenue sur le support kzSINT ! Comment pouvons-nous t'aider ?"
    })

def get_smart_response(message):
    """Génère une réponse intelligente basée sur les informations du panel"""
    
    if "prix" in message or "offre" in message or "tarif" in message:
        return """📦 NOS OFFRES

Voici nos plans disponibles :

🟢 kzSINT BASIC - 9.99€
• 10 scans / jour
• 2 modules
• Support communautaire

🔵 kzSINT PRO - 29.99€
• Scans illimités
• Tous les modules
• Alertes temps réel

🔴 kzSINT ELITE - 99.99€
• Accès API complet
• Scans prioritaires
• Support dédié 24/7

🟠 SCAN DEEP-WEB - 4.99€
• Analyse ponctuelle des fuites
• Scan des forums fermés

🟣 RAPPORT OSINT - 19.99€
• Dossier complet PDF
• Analyse experte sur une cible"""
    
    elif "discord" in message:
        return """🎮 DISCORD

Rejoins notre communauté Discord !

Avantages :
• 📢 Annonces exclusives
• 💬 Entraide OSINT
• 🆘 Support communautaire
• ⚡ Accès anticipé aux mises à jour

Clique sur le bouton "OUVRIR LE DISCORD" pour nous rejoindre !
discord.gg/kzsint"""
    
    elif "compte" in message or "créer" in message or "inscription" in message:
        return """👤 CRÉER UN COMPTE

Pour créer un compte kzSINT :

1️⃣ Va sur la page de connexion
2️⃣ Clique sur "CRÉER UN COMPTE"
3️⃣ Choisis un pseudo (3-20 caractères)
4️⃣ Choisis un mot de passe (min. 6 caractères)
5️⃣ Confirme ton mot de passe
6️⃣ Clique sur "CRÉER LE COMPTE"

💡 Une fois inscrit, tu pourras :
• Activer une clé de licence
• Effectuer des scans OSINT
• Accéder à toutes les fonctionnalités"""
    
    elif "bug" in message or "problème" in message or "erreur" in message:
        return """🐛 SIGNALER UN BUG

Tu as rencontré un problème ? Voici comment nous aider :

1️⃣ Décris le bug en détail
2️⃣ Indique la page où ça s'est produit
3️⃣ Explique ce que tu faisais quand le bug est survenu
4️⃣ Envoie-nous une capture d'écran si possible

📧 Contacte-nous sur Discord pour un support plus rapide !"""
    
    elif "licence" in message or "clé" in message or "cle" in message:
        return """🔑 ACTIVER UNE LICENCE

Pour activer une clé de licence :

1️⃣ Connecte-toi à ton compte
2️⃣ Va dans la section SEARCH
3️⃣ Entre ta clé dans le champ
4️⃣ Clique sur "ACTIVER LA CLÉ"

💡 Où trouver une clé ?
• Achète un plan dans la section BUY
• Après paiement, tu recevras ta clé par email"""
    
    elif "scan" in message or "recherche" in message or "osint" in message:
        return """🔍 FONCTIONNEMENT DU SCAN

Notre moteur de recherche OSINT permet de :

📞 Téléphone : Informations liées au numéro
✉️ Email : Comptes et données associés
👻 Snapchat : Profil et anciens pseudos
👤 Nom/Prénom : Informations personnelles

Comment scanner :
1️⃣ Choisis le type de recherche
2️⃣ Entre ta cible
3️⃣ Clique sur "SCANNER"
4️⃣ Attends les résultats"""
    
    else:
        return random.choice([
            "Je n'ai pas compris ta question. Essaie de reformuler ou choisis une des suggestions !",
            "Je peux t'aider avec les prix, le Discord, la création de compte ou signaler un bug.",
            "Pour une meilleure réponse, essaie les boutons rapides !",
        ])

# Footer
st.markdown("---")
st.markdown("### 🎃 kzSINT v1.0 - OSINT Tool")
st.markdown("© 2024 - Tous droits réservés")
