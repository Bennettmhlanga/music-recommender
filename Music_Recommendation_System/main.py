import streamlit as st
import pandas as pd
import pickle

# Load data
df = pd.read_csv(cleaned.csv)

# Load cosine similarity matrix
with open('cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

# Function to recommend songs
def recommend_songs(song_name, cosine_sim=cosine_sim, df=df, top_n=5):
    try:
        index = df.loc[df['song_name'] == song_name].index[0]
        sim_scores = list(enumerate(cosine_sim[index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_indices = [i[0] for i in sim_scores[1:top_n + 1]]
        recommendations = df.iloc[top_indices]
        return recommendations
    except KeyError:
        return None

# Function to create song cards
def create_song_card(song_info):
    card = f"""
    <div style="width: 300px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin: 10px;
                background-color: rgba(40, 255, 160, 0.8);">
        <h3>{song_info['song_name']}</h3>
        <p>Artist: {song_info['artists']}</p>
        <p>Album: {song_info['album']}</p>
        <p>Album Number: {song_info['album_number']}</p>
        <p>Track Number: {song_info['track_number']}</p>
        <p>Duration (minutes): {song_info['duration_minutes']}</p>
        <p>Release Date: {song_info['release_date']}</p>
    </div>
    """
    return card

# Streamlit app
def main():
    st.title("Sportify Music Recommender")

    # Search bar
    search_query = st.text_input("Search for a song:")

    if search_query:
        # Retrieve suggestions
        suggestions = df[df['song_name'].str.contains(search_query, case=False, na=False)]['song_name'].tolist()
        st.markdown("### Suggestions:")
        for suggestion in suggestions[:4]:  # Limit suggestions to maximum 4 songs
            st.write(suggestion)

        # Retrieve selected song
        selected_song = st.selectbox("Select a song:", suggestions)

        # Retrieve song information
        if selected_song:
            song_info = df[df['song_name'] == selected_song].iloc[0]
            st.markdown("---")
            st.markdown("<h2 align='center'>Song Information</h2>", unsafe_allow_html=True)
            st.markdown(create_song_card(song_info), unsafe_allow_html=True)

            # Retrieve recommended songs
            recommendations = recommend_songs(selected_song)
            st.markdown("---")
            st.markdown("<h2 align='center'>Recommended Songs</h2>", unsafe_allow_html=True)

            # Check if recommendations are available
            if recommendations is not None:
                # Create song cards for the recommended songs in rows of three
                st.markdown('<div style="display: flex; flex-wrap: wrap;">', unsafe_allow_html=True)
                for i, (_, rec_song) in enumerate(recommendations.iterrows()):
                    rec_song_card = create_song_card(rec_song)
                    if i < 3:
                        st.markdown(rec_song_card, unsafe_allow_html=True)
                    else:
                        st.markdown('</div>', unsafe_allow_html=True)
                        st.markdown('<div style="display: flex; flex-wrap: wrap;">', unsafe_allow_html=True)
                        st.markdown(rec_song_card, unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown("No recommendations found.")

    # Add message at the end of the app
    st.markdown("---")
    st.markdown("<h3 align='center'>with ❤️ by Bennett Mhlanga</h3>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
