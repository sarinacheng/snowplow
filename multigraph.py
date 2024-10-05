import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Parse the OSM XML file
def parse_osm(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Dictionary to store nodes: {node_id: (longitude, latitude)}
    nodes = {}
    
    # Extract all node elements
    for node in root.findall('node'):
        node_id = node.get('id')
        lon = float(node.get('lon'))
        lat = float(node.get('lat'))
        nodes[node_id] = (lon, lat)
    
    return nodes

# Step 2: Create a Multigraph
def create_multigraph(nodes):
    G = nx.MultiGraph()
    
    # Add each node to the graph
    for node_id, (lon, lat) in nodes.items():
        G.add_node(node_id, longitude=lon, latitude=lat)
    
    # Optional: Add edges between nodes (in this example, no edges are added yet)
    # You can add edges between nodes that are part of the same 'way', or based on proximity
    
    return G

# Main execution
file_path = '.\downtown small.osm'  # Path to the OSM XML file
nodes = parse_osm(file_path)
multigraph = create_multigraph(nodes)

# Print the multigraph nodes and edges
#print("Nodes:", multigraph.nodes(data=True))
#print("Edges:", multigraph.edges(data=True))

#idk
nodes = multigraph.nodes(data=True)
edges = multigraph.edges(data=True)

#create agraph
G = nx.Graph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)

#draw
nx.draw(G, with_labels=True)
plt.show()