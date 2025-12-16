import streamlit as st

# Tytuł aplikacji
st.title("📦 Prosty Magazyn")

# 1. Inicjalizacja stanu (Session State)
# Streamlit odświeża kod przy każdym kliknięciu. 
# Aby lista produktów nie znikała, musimy ją trzymać w 'session_state'.
if 'produkty' not in st.session_state:
    st.session_state.produkty = []

# --- SEKCJA DODAWANIA ---
st.subheader("Dodaj nowy produkt")
nowy_produkt = st.text_input("Nazwa produktu:", key="nowy_input")

if st.button("Dodaj produkt"):
    if nowy_produkt:
        if nowy_produkt not in st.session_state.produkty:
            st.session_state.produkty.append(nowy_produkt)
            st.success(f"Dodano: {nowy_produkt}")
        else:
            st.warning("Ten produkt jest już na liście!")
    else:
        st.error("Wpisz nazwę produktu.")

st.divider() # Linia oddzielająca

# --- SEKCJA USUWANIA ---
st.subheader("Usuń produkt")

if st.session_state.produkty:
    # Wybór produktu z listy rozwijanej
    produkt_do_usuniecia = st.selectbox(
        "Wybierz produkt do usunięcia:", 
        st.session_state.produkty
    )
    
    if st.button("Usuń wybrany"):
        st.session_state.produkty.remove(produkt_do_usuniecia)
        st.rerun() # Odświeżamy aplikację natychmiast po usunięciu
else:
    st.info("Brak produktów do usunięcia.")

st.divider()

# --- SEKCJA WYŚWIETLANIA ---
st.subheader("Aktualny stan magazynu")

if st.session_state.produkty:
    for i, produkt in enumerate(st.session_state.produkty, 1):
        st.text(f"{i}. {produkt}")
else:
    st.write("Magazyn jest pusty.")
