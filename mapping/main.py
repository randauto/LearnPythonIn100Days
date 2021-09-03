import folium

# create a mapp with location and zoom
m = folium.Map(location=[20.924836112998882, 105.73852435448771], zoom_start=100, tiles="cartodb positron")
tool_tips = "Click me!"  # show tooltip on marker.
fg = folium.FeatureGroup(name="My Map")
# add marker in map.
folium.Marker(
    [20.924836112998882, 105.73852435448771], popup="<i>Mam non Dong Duong</i>", tooltip=tool_tips
).add_to(fg)

m.add_child(fg)
m.save("index.html")
