from adjancyView import AdjacencyView


class Graph(object):
    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict

    def __init__(self, **attr):
        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory

        self.graph = self.graph_attr_dict_factory()  # dictionary for graph attributes
        self._node = self.node_dict_factory()  # dictionary for node attr
        # We store two adjacency lists:
        # the  predecessors of node n are stored in the dict self._pred
        # the successors of node n are stored in the dict self._succ=self._adj
        self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict
        self._pred = self.adjlist_outer_dict_factory()  # predecessor
        self._succ = self._adj  # successor

        # attempt to load graph with data
        # load graph attributes (must be after convert)
        self.graph.update(attr)

    def __iter__(self):
        return iter(self._node)

    def __contains__(self, n):
        try:
            return n in self._node
        except TypeError:
            return False

    def __len__(self):
        return len(self._node)

    def __getitem__(self, n):
        return self.adj[n]

    @property
    def adj(self):
        return AdjacencyView(self._succ)

    @property
    def succ(self):
        return AdjacencyView(self._succ)

    @property
    def pred(self):
        return AdjacencyView(self._pred)

    def add_node(self, node_for_adding, **attr):
        if node_for_adding not in self._succ:
            self._succ[node_for_adding] = self.adjlist_inner_dict_factory()
            self._pred[node_for_adding] = self.adjlist_inner_dict_factory()
            attr_dict = self._node[node_for_adding] = self.node_attr_dict_factory()
            attr_dict.update(attr)
        else:  # update attr even if node already exists
            self._node[node_for_adding].update(attr)

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            # keep all this inside try/except because
            # CPython throws TypeError on n not in self._succ,
            # while pre-2.7.5 ironpython throws on self._succ[n]
            try:
                if n not in self._succ:
                    self._succ[n] = self.adjlist_inner_dict_factory()
                    self._pred[n] = self.adjlist_inner_dict_factory()
                    attr_dict = self._node[n] = self.node_attr_dict_factory()
                    attr_dict.update(attr)
                else:
                    self._node[n].update(attr)
            except TypeError:
                nn, ndict = n
                if nn not in self._succ:
                    self._succ[nn] = self.adjlist_inner_dict_factory()
                    self._pred[nn] = self.adjlist_inner_dict_factory()
                    newdict = attr.copy()
                    newdict.update(ndict)
                    attr_dict = self._node[nn] = self.node_attr_dict_factory()
                    attr_dict.update(newdict)
                else:
                    olddict = self._node[nn]
                    olddict.update(attr)
                    olddict.update(ndict)

    def remove_node(self, n):
        try:
            nbrs = self._succ[n]
            del self._node[n]
        except KeyError:
            raise ("The node %s is not in the digraph." % (n,))
        for u in nbrs:
            del self._pred[u][n]  # remove all edges n-u in graph
        del self._succ[n]  # remove node from succ
        for u in self._pred[n]:
            del self._succ[u][n]  # remove all edges n-u in graph
        del self._pred[n]  # remove node from pred

    def remove_nodes_from(self, nodes):
        for n in nodes:
            try:
                succs = self._succ[n]
                del self._node[n]
                for u in succs:
                    del self._pred[u][n]  # remove all edges n-u in digraph
                del self._succ[n]  # now remove node
                for u in self._pred[n]:
                    del self._succ[u][n]  # remove all edges n-u in digraph
                del self._pred[n]  # now remove node
            except KeyError:
                pass  # silent failure on remove

    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        # add nodes
        if u not in self._succ:
            self._succ[u] = self.adjlist_inner_dict_factory()
            self._pred[u] = self.adjlist_inner_dict_factory()
            self._node[u] = self.node_attr_dict_factory()
        if v not in self._succ:
            self._succ[v] = self.adjlist_inner_dict_factory()
            self._pred[v] = self.adjlist_inner_dict_factory()
            self._node[v] = self.node_attr_dict_factory()
        # add the edge
        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._succ[u][v] = datadict
        self._pred[v][u] = datadict

    def add_edges_from(self, ebunch_to_add, **attr):
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}
            else:
                raise ("Edge tuple %s must be a 2-tuple or 3-tuple." % (e,))
            if u not in self._succ:
                self._succ[u] = self.adjlist_inner_dict_factory()
                self._pred[u] = self.adjlist_inner_dict_factory()
                self._node[u] = self.node_attr_dict_factory()
            if v not in self._succ:
                self._succ[v] = self.adjlist_inner_dict_factory()
                self._pred[v] = self.adjlist_inner_dict_factory()
                self._node[v] = self.node_attr_dict_factory()
            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
            datadict.update(attr)
            datadict.update(dd)
            self._succ[u][v] = datadict
            self._pred[v][u] = datadict

    def remove_edge(self, u, v):
        try:
            del self._succ[u][v]
            del self._pred[v][u]
        except KeyError:
            raise ("The edge %s-%s not in graph." % (u, v))

    def remove_edges_from(self, ebunch):
        for e in ebunch:
            u, v = e[:2]  # ignore edge data
            if u in self._succ and v in self._succ[u]:
                del self._succ[u][v]
                del self._pred[v][u]

    def has_successor(self, u, v):
        return u in self._succ and v in self._succ[u]

    def has_predecessor(self, u, v):
        return u in self._pred and v in self._pred[u]

    def successors(self, n):
        try:
            return iter(self._succ[n])
        except KeyError:
            raise ("The node %s is not in the digraph." % (n,))

    # graph definitions
    neighbors = successors

    def predecessors(self, n):
        try:
            return iter(self._pred[n])
        except KeyError:
            raise ("The node %s is not in the digraph." % (n,))

    def clear(self):
        self._succ.clear()
        self._pred.clear()
        self._node.clear()
        self.graph.clear()

    # def reverse(self, copy=True):
    #     if copy:
    #         H = self.__class__()
    #         H.graph.update(deepcopy(self.graph))
    #         H.add_nodes_from((n, deepcopy(d)) for n, d in self._node.items())
    #         H.add_edges_from((v, u, deepcopy(d)) for u, v, d
    #                          in self.edges(data=True))
    #         return H
    #     return nx.graphviews.reverse_view(self)


def from_pandas_edgelist(df, source='source', target='target'):
    g = Graph()
    g.add_edges_from(zip(df[source], df[target]))
    return g


def bidirectional_shortest_path(G, source, target):
    if source not in G or target not in G:
        msg = 'Either source {} or target {} is not in G'
        raise msg.format(source, target)

    # call helper to do the real work
    results = _bidirectional_pred_succ(G, source, target)
    pred, succ, w = results

    # build path from pred+w+succ
    path = []
    # from source to w
    while w is not None:
        path.append(w)
        w = pred[w]
    path.reverse()
    # from w to target
    w = succ[path[-1]]
    while w is not None:
        path.append(w)
        w = succ[w]

    return path


def _bidirectional_pred_succ(G, source, target):
    # does BFS from both source and target and meets in the middle
    if target == source:
        return ({target: None}, {source: None}, source)

    Gpred = G.pred
    Gsucc = G.succ

    # predecesssor and successors in search
    pred = {source: None}
    succ = {target: None}

    # initialize fringes, start with forward
    forward_fringe = [source]
    reverse_fringe = [target]

    while forward_fringe and reverse_fringe:
        if len(forward_fringe) <= len(reverse_fringe):
            this_level = forward_fringe
            forward_fringe = []
            for v in this_level:
                for w in Gsucc[v]:
                    if w not in pred:
                        forward_fringe.append(w)
                        pred[w] = v
                    if w in succ:  # path found
                        return pred, succ, w
        else:
            this_level = reverse_fringe
            reverse_fringe = []
            for v in this_level:
                for w in Gpred[v]:
                    if w not in succ:
                        succ[w] = v
                        reverse_fringe.append(w)
                    if w in pred:  # found path
                        return pred, succ, w

    raise ("No path between %s and %s." % (source, target))


def has_path(G, source, target):
    try:
        bidirectional_shortest_path(G, source, target)
    except:
        return False
    return True
