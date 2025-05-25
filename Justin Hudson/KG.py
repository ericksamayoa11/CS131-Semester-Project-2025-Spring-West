import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = {
    'source': ["cats", "dogs", "cats","mice", "dogs","mice", "cats", "dogs", "mice"],
    'target': ["mice", "water", "water", "water", "cats", "cats", "animals", "animals", "animals"],
    'relation': ["eat", "drink", "drink", "drink", "like", "hate", "are", "are", "are"],
}

dataframe = pd.DataFrame(data)

G = nx.MultiDiGraph()

for _, row in dataframe.iterrows():
    source = row['source']
    target = row['target']
    relation = row['relation']

    G.add_node(source)
    G.add_node(target)
    G.add_edge(source, target, relation=relation)

# Adjust the layout for better spacing
pos = nx.spring_layout(G, seed=42, k=3)

labels = nx.get_edge_attributes(G, 'relation')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, font_size=15, arrowsize=25, connectionstyle='arc3, rad = 0.05')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.75, font_size=12)

plt.show()
