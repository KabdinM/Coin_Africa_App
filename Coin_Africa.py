import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit.components.v1 as components
import re

# Configuration de la page
st.set_page_config(page_title="CoinAfrique Scraper", layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>COINAFRIQUE DATA SCRAPER APP</h1>", unsafe_allow_html=True)

st.markdown("""
Cette application permet de scraper des données de CoinAfrique sur plusieurs pages et d'analyser les données.
* **Bibliothèques Python:** pandas, streamlit, requests, beautifulsoup4, matplotlib, seaborn
* **Source des données:** [CoinAfrique Sénégal](https://sn.coinafrique.com/)
* **Catégories:** Vêtements homme, Vêtements enfants, Chaussures homme, Chaussures enfants
""")

# Fonction pour ajouter un arrière-plan
def add_bg_from_local(image_file):
    try:
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    except FileNotFoundError:
        pass

# Fonction pour convertir DataFrame en CSV
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Fonction pour charger et afficher les données
def load_data(dataframe, title, key, key1):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    st.subheader('Dimensions des données')
    st.write(f'Dimensions: {dataframe.shape[0]} lignes et {dataframe.shape[1]} colonnes.')
    st.dataframe(dataframe)

    csv = convert_df(dataframe)
    st.download_button(
        label="Télécharger les données en CSV",
        data=csv,
        file_name=f'{title.replace(" ", "_")}.csv',
        mime='text/csv',
        key=key
    )

# Fonction pour charger CSS local
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# Fonctions de scraping
def scrape_vetements_homme(pages):
    data = []
    for page in range(1, pages + 1):
        url = f"https://sn.coinafrique.com/categorie/vetements-homme?page={page}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            annonces = soup.find_all('div', class_='ad__card')
            
            for annonce in annonces:
                try:
                    type_habit = annonce.find('p', class_='ad__card-description').get_text(strip=True)
                    prix = annonce.find('p', class_='ad__card-price').get_text(strip=True)
                    adresse = annonce.find('p', class_='ad__card-location').find('span').get_text(strip=True)
                    image = annonce.find('img', class_='ad__card-img')['src']
                    
                    data.append({
                        "type": type_habit,
                        "prix": prix,
                        "adresse": adresse,
                        "image_lien": image
                    })
                except Exception:
                    continue
        except Exception:
            continue
    
    return pd.DataFrame(data)

def scrape_vetements_enfants(pages):
    data = []
    for page in range(1, pages + 1):
        url = f"https://sn.coinafrique.com/categorie/vetements-enfants?page={page}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            annonces = soup.find_all('div', class_='ad__card')
            
            for annonce in annonces:
                try:
                    type_habit = annonce.find('p', class_='ad__card-description').get_text(strip=True)
                    prix = annonce.find('p', class_='ad__card-price').get_text(strip=True)
                    adresse = annonce.find('p', class_='ad__card-location').find('span').get_text(strip=True)
                    image = annonce.find('img', class_='ad__card-img')['src']
                    
                    data.append({
                        "type": type_habit,
                        "prix": prix,
                        "adresse": adresse,
                        "image_lien": image
                    })
                except Exception:
                    continue
        except Exception:
            continue
    
    return pd.DataFrame(data)

def scrape_chaussures_homme(pages):
    data = []
    for page in range(1, pages + 1):
        url = f"https://sn.coinafrique.com/categorie/chaussures-homme?page={page}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            annonces = soup.find_all('div', class_='ad__card')
            
            for annonce in annonces:
                try:
                    type_chaussure = annonce.find('p', class_='ad__card-description').get_text(strip=True)
                    prix = annonce.find('p', class_='ad__card-price').get_text(strip=True)
                    adresse = annonce.find('p', class_='ad__card-location').find('span').get_text(strip=True)
                    image = annonce.find('img', class_='ad__card-img')['src']
                    
                    data.append({
                        "type": type_chaussure,
                        "prix": prix,
                        "adresse": adresse,
                        "image_lien": image
                    })
                except Exception:
                    continue
        except Exception:
            continue
    
    return pd.DataFrame(data)

def scrape_chaussures_enfants(pages):
    data = []
    for page in range(1, pages + 1):
        url = f"https://sn.coinafrique.com/categorie/chaussures-enfants?page={page}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            annonces = soup.find_all('div', class_='ad__card')
            
            for annonce in annonces:
                try:
                    type_chaussure = annonce.find('p', class_='ad__card-description').get_text(strip=True)
                    prix = annonce.find('p', class_='ad__card-price').get_text(strip=True)
                    adresse = annonce.find('p', class_='ad__card-location').find('span').get_text(strip=True)
                    image = annonce.find('img', class_='ad__card-img')['src']
                    
                    data.append({
                        "type": type_chaussure,
                        "prix": prix,
                        "adresse": adresse,
                        "image_lien": image
                    })
                except Exception:
                    continue
        except Exception:
            continue
    
    return pd.DataFrame(data)

# Fonctions de nettoyage des données
def clean_price(price_str):
    """Nettoie et convertit le prix en valeur numérique"""
    if pd.isna(price_str):
        return None
    
    # Supprimer les espaces et convertir en string
    price_str = str(price_str).strip()
    
    # Supprimer les caractères non numériques sauf les chiffres
    import re
    price_clean = re.sub(r'[^\d]', '', price_str)
    
    try:
        return int(price_clean) if price_clean else None
    except ValueError:
        return None

def clean_address(address_str):
    """Nettoie les adresses"""
    if pd.isna(address_str):
        return "Non spécifié"
    
    address_str = str(address_str).strip()
    # Supprimer les caractères spéciaux et normaliser
    address_clean = re.sub(r'[^\w\s-]', '', address_str)
    return address_clean.title() if address_clean else "Non spécifié"

def clean_type(type_str):
    """Nettoie les types de produits"""
    if pd.isna(type_str):
        return "Non spécifié"
    
    type_str = str(type_str).strip()
    # Limiter la longueur pour éviter les descriptions trop longues
    if len(type_str) > 50:
        type_str = type_str[:47] + "..."
    
    return type_str.title()

def clean_dataframe(df):
    """Nettoie un DataFrame complet"""
    if df.empty:
        return df
    
    df_clean = df.copy()
    
    # Nettoyer les colonnes si elles existent
    if 'prix' in df_clean.columns:
        df_clean['prix_clean'] = df_clean['prix'].apply(clean_price)
        df_clean['prix_range'] = df_clean['prix_clean'].apply(lambda x: 
            'Moins de 50k' if x and x < 50000 else
            '50k-100k' if x and x < 100000 else
            '100k-500k' if x and x < 500000 else
            'Plus de 500k' if x and x >= 500000 else
            'Non spécifié')
    
    if 'adresse' in df_clean.columns:
        df_clean['adresse_clean'] = df_clean['adresse'].apply(clean_address)
    
    if 'type' in df_clean.columns:
        df_clean['type_clean'] = df_clean['type'].apply(clean_type)
    
    # Supprimer les lignes avec des prix invalides
    if 'prix_clean' in df_clean.columns:
        df_clean = df_clean.dropna(subset=['prix_clean'])
    
    return df_clean

def get_price_stats(df):
    """Calcule les statistiques de prix"""
    if df.empty or 'prix_clean' not in df.columns:
        return {}
    
    prices = df['prix_clean'].dropna()
    if len(prices) == 0:
        return {}
    
    return {
        'min': prices.min(),
        'max': prices.max(),
        'mean': prices.mean(),
        'median': prices.median(),
        'count': len(prices)
    }
@st.cache_data
def load_vetements_homme_csv():
    try:
        return pd.read_csv('Data/CoinAfrique_Vetements_Homme.csv')
    except FileNotFoundError:
        st.error("Fichier 'vetements_homme.csv' non trouvé")
        return pd.DataFrame()

@st.cache_data
def load_vetements_enfants_csv():
    try:
        return pd.read_csv('Data/CoinAfrique_Vetements_Enfants.csv')
    except FileNotFoundError:
        st.error("Fichier 'vetements_enfants.csv' non trouvé")
        return pd.DataFrame()

@st.cache_data
def load_chaussures_homme_csv():
    try:
        return pd.read_csv('Data/CoinAfrique_Chaussures_Hommes.csv')
    except FileNotFoundError:
        st.error("Fichier 'chaussures_homme.csv' non trouvé")
        return pd.DataFrame()

@st.cache_data
def load_chaussures_enfants_csv():
    try:
        return pd.read_csv('Data/CoinAfrique_Chaussure_Enfant.csv')
    except FileNotFoundError:
        st.error("Fichier 'chaussures_enfants.csv' non trouvé")
        return pd.DataFrame()

# Interface utilisateur
st.sidebar.header('Options de l\'utilisateur')
pages = st.sidebar.selectbox('Nombre de pages', list(range(1, 51)))
choice = st.sidebar.selectbox('Choix', [
    'Scraper des données avec BeautifulSoup',
    'Télécharger des données déjà scrapées',
    'Dashboard des données',
    'Remplir le formulaire d\'évaluation'
])

# Ajout de l'arrière-plan et du CSS
add_bg_from_local('img_file3.jpg')
local_css('style.css')

if choice == 'Scraper des données avec BeautifulSoup':
    st.subheader("Scraping des données CoinAfrique")
    
    # Sélection de la catégorie à scraper
    categorie = st.selectbox('Choisissez la catégorie à scraper', [
        'Vêtements Homme',
        'Vêtements Enfants', 
        'Chaussures Homme',
        'Chaussures Enfants'
    ])
    
    # Bouton pour lancer le scraping
    if st.button('Lancer le scraping', key='scrape_btn'):
        with st.spinner(f'Scraping en cours pour {categorie}...'):
            if categorie == 'Vêtements Homme':
                data = scrape_vetements_homme(pages)
                load_data(data, 'Vêtements Homme', '1', '101')
            elif categorie == 'Vêtements Enfants':
                data = scrape_vetements_enfants(pages)
                load_data(data, 'Vêtements Enfants', '2', '102')
            elif categorie == 'Chaussures Homme':
                data = scrape_chaussures_homme(pages)
                load_data(data, 'Chaussures Homme', '3', '103')
            elif categorie == 'Chaussures Enfants':
                data = scrape_chaussures_enfants(pages)
                load_data(data, 'Chaussures Enfants', '4', '104')
    else:
        st.info(f"Cliquez sur 'Lancer le scraping' pour scraper les données de {categorie} sur {pages} page(s).")

elif choice == 'Télécharger des données déjà scrapées':
    st.subheader("Chargement des données déjà scrapées")
    
    # Sélection de la catégorie à charger
    categorie = st.selectbox('Choisissez la catégorie à charger', [
        'Vêtements Homme',
        'Vêtements Enfants',
        'Chaussures Homme', 
        'Chaussures Enfants'
    ], key='load_select')
    
    # Bouton pour charger les données
    if st.button('Charger les données', key='load_btn'):
        if categorie == 'Vêtements Homme':
            data = load_vetements_homme_csv()
            if not data.empty:
                load_data(data, 'Vêtements Homme', '1', '101')
        elif categorie == 'Vêtements Enfants':
            data = load_vetements_enfants_csv()
            if not data.empty:
                load_data(data, 'Vêtements Enfants', '2', '102')
        elif categorie == 'Chaussures Homme':
            data = load_chaussures_homme_csv()
            if not data.empty:
                load_data(data, 'Chaussures Homme', '3', '103')
        elif categorie == 'Chaussures Enfants':
            data = load_chaussures_enfants_csv()
            if not data.empty:
                load_data(data, 'Chaussures Enfants', '4', '104')
    else:
        st.info(f"Cliquez sur 'Charger les données' pour afficher les données de {categorie}.")

elif choice == 'Dashboard des données':
    st.subheader("Dashboard des données CoinAfrique")
    
    # Sélection de la catégorie à analyser
    categorie_dashboard = st.selectbox('Choisissez la catégorie à analyser', [
        'Vêtements Homme',
        'Vêtements Enfants',
        'Chaussures Homme',
        'Chaussures Enfants',
        'Toutes les catégories'
    ], key='dashboard_select')
    
    try:
        # Chargement et nettoyage des données
        if categorie_dashboard == 'Vêtements Homme':
            df_raw = load_vetements_homme_csv()
            df_clean = clean_dataframe(df_raw)
            title = "Vêtements Homme"
        elif categorie_dashboard == 'Vêtements Enfants':
            df_raw = load_vetements_enfants_csv()
            df_clean = clean_dataframe(df_raw)
            title = "Vêtements Enfants"
        elif categorie_dashboard == 'Chaussures Homme':
            df_raw = load_chaussures_homme_csv()
            df_clean = clean_dataframe(df_raw)
            title = "Chaussures Homme"
        elif categorie_dashboard == 'Chaussures Enfants':
            df_raw = load_chaussures_enfants_csv()
            df_clean = clean_dataframe(df_raw)
            title = "Chaussures Enfants"
        else:  # Toutes les catégories
            df_vh = clean_dataframe(load_vetements_homme_csv())
            df_ve = clean_dataframe(load_vetements_enfants_csv())
            df_ch = clean_dataframe(load_chaussures_homme_csv())
            df_ce = clean_dataframe(load_chaussures_enfants_csv())
            
            # Ajouter une colonne catégorie
            df_vh['categorie'] = 'Vêtements Homme'
            df_ve['categorie'] = 'Vêtements Enfants'
            df_ch['categorie'] = 'Chaussures Homme'
            df_ce['categorie'] = 'Chaussures Enfants'
            
            df_clean = pd.concat([df_vh, df_ve, df_ch, df_ce], ignore_index=True)
            title = "Toutes les catégories"
        
        if not df_clean.empty:
            # Statistiques générales
            st.subheader(f"Statistiques générales - {title}")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Nombre total d'annonces", len(df_clean))
            
            with col2:
                if 'prix_clean' in df_clean.columns:
                    prix_moyen = df_clean['prix_clean'].mean()
                    st.metric("Prix moyen", f"{prix_moyen:,.0f} F CFA")
                else:
                    st.metric("Prix moyen", "N/A")
            
            with col3:
                if 'adresse_clean' in df_clean.columns:
                    nb_villes = df_clean['adresse_clean'].nunique()
                    st.metric("Nombre de villes", nb_villes)
                else:
                    st.metric("Nombre de villes", "N/A")
            
            with col4:
                if 'type_clean' in df_clean.columns:
                    nb_types = df_clean['type_clean'].nunique()
                    st.metric("Types de produits", nb_types)
                else:
                    st.metric("Types de produits", "N/A")
            
            # Graphiques
            col1, col2 = st.columns(2)
            
            with col1:
                if 'type_clean' in df_clean.columns:
                    st.subheader("Top 10 des types de produits")
                    fig1, ax1 = plt.subplots(figsize=(10, 6))
                    top_types = df_clean['type_clean'].value_counts().head(10)
                    bars = ax1.bar(range(len(top_types)), top_types.values, color='skyblue')
                    ax1.set_title('Top 10 des types de produits les plus populaires')
                    ax1.set_xlabel('Types de produits')
                    ax1.set_ylabel('Nombre d\'annonces')
                    ax1.set_xticks(range(len(top_types)))
                    ax1.set_xticklabels(top_types.index, rotation=45, ha='right')
                    
                    # Ajouter les valeurs sur les barres
                    for bar in bars:
                        height = bar.get_height()
                        ax1.text(bar.get_x() + bar.get_width()/2., height,
                                f'{int(height)}', ha='center', va='bottom')
                    
                    plt.tight_layout()
                    st.pyplot(fig1)
            
            with col2:
                if 'prix_range' in df_clean.columns:
                    st.subheader("Répartition par gamme de prix")
                    fig2, ax2 = plt.subplots(figsize=(10, 6))
                    prix_counts = df_clean['prix_range'].value_counts()
                    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
                    wedges, texts, autotexts = ax2.pie(prix_counts.values, labels=prix_counts.index, 
                                                      autopct='%1.1f%%', colors=colors)
                    ax2.set_title('Répartition des annonces par gamme de prix')
                    
                    # Améliorer la lisibilité
                    for autotext in autotexts:
                        autotext.set_color('white')
                        autotext.set_fontweight('bold')
                    
                    st.pyplot(fig2)
            
            col3, col4 = st.columns(2)
            
            with col3:
                if 'adresse_clean' in df_clean.columns:
                    st.subheader("Top 10 des villes")
                    fig3, ax3 = plt.subplots(figsize=(10, 6))
                    top_villes = df_clean['adresse_clean'].value_counts().head(10)
                    bars = ax3.barh(range(len(top_villes)), top_villes.values, color='lightcoral')
                    ax3.set_title('Top 10 des villes avec le plus d\'annonces')
                    ax3.set_xlabel('Nombre d\'annonces')
                    ax3.set_ylabel('Villes')
                    ax3.set_yticks(range(len(top_villes)))
                    ax3.set_yticklabels(top_villes.index)
                    
                    # Ajouter les valeurs sur les barres
                    for i, bar in enumerate(bars):
                        width = bar.get_width()
                        ax3.text(width, bar.get_y() + bar.get_height()/2.,
                                f'{int(width)}', ha='left', va='center')
                    
                    plt.tight_layout()
                    st.pyplot(fig3)
            
            with col4:
                if categorie_dashboard == 'Toutes les catégories' and 'categorie' in df_clean.columns:
                    st.subheader("Répartition par catégorie")
                    fig4, ax4 = plt.subplots(figsize=(10, 6))
                    cat_counts = df_clean['categorie'].value_counts()
                    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f7b731']
                    bars = ax4.bar(cat_counts.index, cat_counts.values, color=colors)
                    ax4.set_title('Nombre d\'annonces par catégorie')
                    ax4.set_xlabel('Catégories')
                    ax4.set_ylabel('Nombre d\'annonces')
                    
                    # Ajouter les valeurs sur les barres
                    for bar in bars:
                        height = bar.get_height()
                        ax4.text(bar.get_x() + bar.get_width()/2., height,
                                f'{int(height)}', ha='center', va='bottom')
                    
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    st.pyplot(fig4)
                elif 'prix_clean' in df_clean.columns:
                    st.subheader("Distribution des prix")
                    fig4, ax4 = plt.subplots(figsize=(10, 6))
                    prices = df_clean['prix_clean'].dropna()
                    if len(prices) > 0:
                        ax4.hist(prices, bins=20, color='lightgreen', alpha=0.7, edgecolor='black')
                        ax4.set_title('Distribution des prix')
                        ax4.set_xlabel('Prix (F CFA)')
                        ax4.set_ylabel('Nombre d\'annonces')
                        
                        # Ajouter des statistiques
                        mean_price = prices.mean()
                        ax4.axvline(mean_price, color='red', linestyle='--', 
                                   label=f'Prix moyen: {mean_price:,.0f} F CFA')
                        ax4.legend()
                    
                    plt.tight_layout()
                    st.pyplot(fig4)
            
            # Tableau des statistiques détaillées
            if 'prix_clean' in df_clean.columns:
                st.subheader("Statistiques détaillées des prix")
                stats = get_price_stats(df_clean)
                if stats:
                    col1, col2, col3, col4, col5 = st.columns(5)
                    
                    with col1:
                        st.metric("Prix minimum", f"{stats['min']:,.0f} F CFA")
                    with col2:
                        st.metric("Prix maximum", f"{stats['max']:,.0f} F CFA")
                    with col3:
                        st.metric("Prix moyen", f"{stats['mean']:,.0f} F CFA")
                    with col4:
                        st.metric("Prix médian", f"{stats['median']:,.0f} F CFA")
                    with col5:
                        st.metric("Nombre d'annonces", stats['count'])
            
            # Option pour télécharger les données nettoyées
            st.subheader("Télécharger les données nettoyées")
            csv_clean = convert_df(df_clean)
            st.download_button(
                label="Télécharger les données nettoyées en CSV",
                data=csv_clean,
                file_name=f'{title.replace(" ", "_")}_clean.csv',
                mime='text/csv',
                key='download_clean'
            )
            
        else:
            st.error("Aucune donnée disponible pour cette catégorie. Veuillez d'abord scraper ou charger des données.")
            
    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {str(e)}")
        st.info("Assurez-vous que les fichiers CSV existent ou scrapez d'abord les données.")

else:  # Formulaire d'évaluation
    st.subheader("Formulaire d'évaluation de l'application")
    components.html("""
    <iframe src="https://ee.kobotoolbox.org/i/r5stuQBl" width="800" height="600"></iframe>
    """, height=1100, width=800)
