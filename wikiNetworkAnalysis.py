import networkx as nx
import wikipedia as wiki

originPage = wiki.random()

todoList = [(0, originPage)]
todoSet = set(originPage)
doneSet = set()

graph = nx.DiGraph()
layer,page = todoList[0]

while layer < 2:
    doneSet.add(todoList.pop(0))
    try:
        linkPage = wiki.page(page)
    except:
        layer, page = todoList[0]
        print("Cannot load", page)
    
    for link in linkPage.links[:100]:
        link = link.title()
        if link not in todoSet and link not in doneSet:
            todoList.append((layer + 1, link))
            todoSet.add(link)
        graph.add_edge(page, link)
    layer, page = todoList[0]

core = [node for node, deg in dict(graph.degree()).items() if deg >= 2]
gsub = nx.subgraph(graph, core)
nx.write_graphml(gsub, "core.graphml")
nx.write_gexf(graph, "test.gexf")
