# not python syntax

def DFS(G):
    for each vertex u in G.V:
        u.color = white
        u.pi = None
    t = 0
    for each u in G.V:
        if u.color == white:
            DFS_visit(G, u)


def DFS_visit(G, u):
    t = t+1
    u.d = t
    u.color = gray
    for each v in G.adj[u]:
        if v.color == white:
            v.pi = u
            DFS_visit(G, v)
    u.color = black
    t = t+1
    u.f = t
