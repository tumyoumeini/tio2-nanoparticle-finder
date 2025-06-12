
import streamlit as st

st.set_page_config(page_title="TiO₂ Nanoparticle Finder", layout="centered")
st.title("🔍 AI-Assisted TiO₂ Nanoparticle Finder")

st.markdown("""
Welcome to Schnaiffer's intelligent assistant. Select your application or enter technical specs to get a personalized TiO₂ recommendation.
""")

# Step 1: Choose Application or Custom Input
option = st.radio("How would you like to start?", ["Select by Application", "Enter Custom Technical Specs"])

if option == "Select by Application":
    app = st.selectbox("Select Your Application", [
        "Photocatalysis",
        "Antibacterial Coating",
        "Sunscreen / Cosmetics",
        "DSSC / Solar Cells",
        "Gas Sensors",
        "Functional Paints / Coatings"
    ])

    if st.button("Find My Match"):
        if app == "Photocatalysis":
            st.success("✅ Recommended: Anatase phase, 20–30 nm, >90 m²/g surface area. Available in aqueous dispersion or powder.")
        elif app == "Antibacterial Coating":
            st.success("✅ Recommended: Mixed phase (anatase + rutile), 30–50 nm, surface-modified with ROS optimization.")
        elif app == "Sunscreen / Cosmetics":
            st.success("✅ Recommended: Rutile phase, 25–50 nm, silica-coated, transparent dispersion available.")
        elif app == "DSSC / Solar Cells":
            st.success("✅ Recommended: Anatase phase, monodispersed, 15–20 nm, tailored for high electron mobility.")
        elif app == "Gas Sensors":
            st.success("✅ Recommended: Porous anatase, <20 nm, high-purity nanoparticles for sensor substrate coating.")
        elif app == "Functional Paints / Coatings":
            st.success("✅ Recommended: Rutile phase, 50–70 nm, dispersion-ready with UV protection and self-cleaning capability.")

elif option == "Enter Custom Technical Specs":
    size = st.slider("Desired Particle Size (nm)", 10, 100, (20, 30))
    phase = st.selectbox("Preferred Crystal Phase", ["Anatase", "Rutile", "Mixed"])
    medium = st.selectbox("Dispersion Medium", ["Powder", "Water", "Ethanol", "Oil / Resin"])

    if st.button("Get Recommendation"):
        st.success(f"✅ Recommended Spec: {phase} phase, {size[0]}–{size[1]} nm, available in {medium}. Custom surface treatment optional.")

st.markdown("---")
st.markdown("📩 Need a formal quote or sample? Email us at [support@schnaiffer.com](mailto:support@schnaiffer.com)")
st.markdown("🌐 Visit: [www.schnaiffer.com](http://www.schnaiffer.com)")
