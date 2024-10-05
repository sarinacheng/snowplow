import xml.etree.ElementTree as ET
import networkx as nx

# Step 1: Parse the OSM XML file
def parse_osm(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Dictionary to store nodes: {node_id: (longitude, latitude)}
    nodes = {}
    ways = []
    
    # Extract all node elements
    for node in root.findall('node'):
        node_id = node.get('id')
        lon = float(node.get('lon'))
        lat = float(node.get('lat'))
        nodes[node_id] = (lon, lat)
    
    # Extract all way elements
    for way in root.findall('way'):
        way_nodes = [nd.get('ref') for nd in way.findall('nd')]
        ways.append(way_nodes)
    
    return nodes, ways

# Step 2: Create a Multigraph and Add Edges from Ways
def create_multigraph(nodes, ways):
    G = nx.MultiGraph()
    
    # Add each node to the graph
    for node_id, (lon, lat) in nodes.items():
        G.add_node(node_id, longitude=lon, latitude=lat)
    
    # Add edges between consecutive nodes in each way
    for way in ways:
        for i in range(len(way) - 1):
            node1 = way[i]
            node2 = way[i + 1]
            
            if node1 in nodes and node2 in nodes:
                # Add an edge between node1 and node2
                G.add_edge(node1, node2)
    
    return G

# Main execution
file_path = './downtown small.osm' # Path to the OSM XML file
nodes, ways = parse_osm(file_path)
multigraph = create_multigraph(nodes, ways)

# Print the multigraph nodes and edges
print("Nodes:", multigraph.nodes(data=True))
print("Edges:", multigraph.edges(data=True))
