

# import plotly.graph_objects as go

# # Define the roadmap data (technology -> course link)
# roadmap_data = {
#     "Python": "https://www.learnpython.org/",
#     "Java": "https://www.java.com/en/",
#     "HTML": "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics",
#     "Django": "https://www.djangoproject.com/start/",
#     "TensorFlow": "https://www.tensorflow.org/tutorials",
#     "Machine Learning": "https://www.coursera.org/learn/machine-learning",
# }

# # Simulate AI selecting relevant technologies for a specific roadmap type
# roadmap_type = "Web Development"
# if roadmap_type == "Web Development":
#     selected_technologies = ["HTML", "CSS", "JavaScript", "Django"]
# elif roadmap_type == "Machine Learning":
#     selected_technologies = ["Python", "TensorFlow", "Machine Learning"]
# else:
#     selected_technologies = []

# # Create a flowchart using Plotly
# nodes = []
# links = []

# # Add nodes for each selected technology
# for i, tech in enumerate(selected_technologies):
#     # Each node has a clickable link
#     link = roadmap_data.get(tech, "#")
#     nodes.append({
#         "id": i,
#         "label": f"{tech}<br><a href='{link}' target='_blank'>Course Link</a>",
#         "url": link,
#     })

# # Create links (edges) between the technologies
# for i in range(len(selected_technologies) - 1):
#     links.append({
#         "source": i,
#         "target": i + 1
#     })

# # Create a Plotly flowchart with clickable links
# fig = go.Figure()

# # Add nodes to the figure (text boxes with links)
# for node in nodes:
#     fig.add_trace(go.Scatter(
#         x=[0], y=[0],  # Positions can be customized
#         text=[f"{node['label']}<br><a href='{node['url']}' target='_blank'>Click here</a>"],
#         mode="text",
#         hoverinfo="text",
#         name=node["label"]
#     ))

# # Add edges (links between steps)
# for link in links:
#     fig.add_trace(go.Scatter(
#         x=[0], y=[0],  # Customize edge positioning
#         text=[f"Linking {selected_technologies[link['source']]} to {selected_technologies[link['target']]}"],
#         mode="lines",
#         line=dict(width=1, color='black'),
#         showlegend=False
#     ))

# # Customize the layout for the flowchart
# fig.update_layout(
#     title="Project Roadmap Flowchart with Clickable Links",
#     showlegend=True
# )

# # Display the flowchart
# fig.write_html("roadmap_flowchart.html")

# fig.show()
