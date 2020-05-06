import * as React from 'react';

import {
  GraphView,
  type IEdgeType as IEdge,
  type INodeType as INode,
  type LayoutEngineType,
} from '../../';
import GraphConfig, {
  edgeTypes,
  EMPTY_EDGE_TYPE,
  EMPTY_TYPE,
  NODE_KEY,
  nodeTypes,
  COMPLEX_CIRCLE_TYPE,
  POLY_TYPE,
  SPECIAL_CHILD_SUBTYPE,
  SPECIAL_EDGE_TYPE,
  SPECIAL_TYPE,
  SKINNY_TYPE,
} from './graph-config'; // Configures node/edge types


// NOTE: Edges must have 'source' & 'target' attributes
// In a more realistic use case, the graph would probably originate
// elsewhere in the App or be generated from some other state upstream of this component.
const sample = {
  edges: [
  ],
  nodes: [
    {
      id: 'a7',
      title: 'Nod',
      type: SKINNY_TYPE,
      x: 0,
      y: 300,
    },
  ],
};


class Graph extends React.Component{
  GraphView;

  constructor(props) {
    super(props);

    this.state = {
      copiedNode: null,
      graph: sample,
      layoutEngineType: undefined,
      selected: null,
      totalNodes: sample.nodes.length,
    };

    this.GraphView = React.createRef();
  }

  // Helper to find the index of a given node
  getNodeIndex(searchNode) {
    return this.state.graph.nodes.findIndex(node => {
      return node[NODE_KEY] === searchNode[NODE_KEY];
    });
  }

  // Helper to find the index of a given edge
  getEdgeIndex(searchEdge) {
    return this.state.graph.edges.findIndex(edge => {
      return (
        edge.source === searchEdge.source && edge.target === searchEdge.target
      );
    });
  }

  // Given a nodeKey, return the corresponding node
  getViewNode(nodeKey) {
    const searchNode = {};

    searchNode[NODE_KEY] = nodeKey;
    const i = this.getNodeIndex(searchNode);

    return this.state.graph.nodes[i];
  }

  addStartNode = () => {
    const graph = this.state.graph;

    // using a new array like this creates a new memory reference
    // this will force a re-render
    graph.nodes = [
      {
        id: Date.now(),
        title: 'Node',
        type: SKINNY_TYPE,
        x: 0,
        y: 0,
      },
      ...this.state.graph.nodes,
    ];
    this.setState({
      graph,
    });
  };
  deleteStartNode = () => {
    const graph = this.state.graph;

    graph.nodes.splice(0, 1);
    // using a new array like this creates a new memory reference
    // this will force a re-render
    graph.nodes = [...this.state.graph.nodes];
    this.setState({
      graph,
    });
  };

  handleChange = (event) => {
    this.setState(
      {
        totalNodes: parseInt(event.target.value || '0', 10),
      },
      this.makeItLarge
    );
  };

  /*
   * Handlers/Interaction
   */

  // Called by 'drag' handler, etc..
  // to sync updates from D3 with the graph
  onUpdateNode = (viewNode) => {
    const graph = this.state.graph;
    const i = this.getNodeIndex(viewNode);

    graph.nodes[i] = viewNode;
    this.setState({ graph });
  };

  // Node 'mouseUp' handler
  onSelectNode = (viewNode) => {
    // Deselect events will send Null viewNode
    this.setState({ selected: viewNode });
  };

  // Edge 'mouseUp' handler
  onSelectEdge = (viewEdge) => {
    this.setState({ selected: viewEdge });
  };

  // Updates the graph with a new node
  onCreateNode = (x, y) => {
    const graph = this.state.graph;

    // This is just an example - any sort of logic
    // could be used here to determine node type
    // There is also support for subtypes. (see 'sample' above)
    // The subtype geometry will underlay the 'type' geometry for a node
    const type = Math.random() < 0.25 ? SPECIAL_TYPE : EMPTY_TYPE;

    const viewNode = {
      id: Date.now(),
      title: '',
      type,
      x,
      y,
    };

    graph.nodes = [...graph.nodes, viewNode];
    this.setState({ graph });
  };

  // Deletes a node from the graph
  onDeleteNode = () => {
    const graph = this.state.graph;

    const selectedNode = this.state.selected;
    

    graph.nodes = [...this.state.graph.nodes];

    const newNodes = graph.nodes.filter((node, i) => {
      return (
        node.id !== selectedNode.id 
      );
    });

    const newEdges = graph.edges.filter((edge, i) => {
      return (
        edge.source !== selectedNode[NODE_KEY] && edge.target !== selectedNode[NODE_KEY]
      );
    });

    graph.nodes = newNodes;
    graph.edges = newEdges;
    
    this.setState({ graph, selected: null });
  };

  // Creates a new node between two edges
  onCreateEdge = (sourceViewNode, targetViewNode) => {
    const graph = this.state.graph;
    // This is just an example - any sort of logic
    // could be used here to determine edge type
    const type =
      sourceViewNode.type === SPECIAL_TYPE
        ? SPECIAL_EDGE_TYPE
        : EMPTY_EDGE_TYPE;

    const viewEdge = {
      source: sourceViewNode[NODE_KEY],
      target: targetViewNode[NODE_KEY],
      type,
    };

    // Only add the edge when the source node is not the same as the target
    if (viewEdge.source !== viewEdge.target) {
      graph.edges = [...graph.edges, viewEdge];
      this.setState({
        graph,
        selected: viewEdge,
      });
    }
  };

  // Called when an edge is reattached to a different target.
  onSwapEdge = (
    sourceViewNode,
    targetViewNode,
    viewEdge
  ) => {
    const graph = this.state.graph;
    const i = this.getEdgeIndex(viewEdge);
    const edge = JSON.parse(JSON.stringify(graph.edges[i]));

    edge.source = sourceViewNode[NODE_KEY];
    edge.target = targetViewNode[NODE_KEY];
    graph.edges[i] = edge;
    // reassign the array reference if you want the graph to re-render a swapped edge
    graph.edges = [...graph.edges];

    this.setState({
      graph,
      selected: edge,
    });
  };

  // Called when an edge is deleted
  onDeleteEdge = (viewEdge , edges) => {
    const graph = this.state.graph;

    graph.edges = edges;
    this.setState({
      graph,
      selected: null,
    });
  };

  handleChangeLayoutEngineType = (event) => {
    this.setState({
      layoutEngineType: (event.target.value),
    });
  };

  onSelectPanNode = (event) => {
    if (this.GraphView) {
      this.GraphView.panToNode(event.target.value, true);
    }
  };

  /*
   * Render
   */

  render() {
    const { nodes, edges } = this.state.graph;
    const selected = this.state.selected;
    const { NodeTypes, NodeSubtypes, EdgeTypes } = GraphConfig;

    return (
      <div id="graph">
        <div className="graph-header">
          <button onClick={this.addStartNode}>Add Node</button>
          <button onClick={this.onDeleteNode}>Delete Node</button>
          <input
            className="total-nodes"
            type="number"
            onBlur={this.handleChange}
            placeholder={this.state.totalNodes.toString()}
          />
          <div className="layout-engine">
            <span>Layout Engine:</span>
            <select
              name="layout-engine-type"
              onChange={this.handleChangeLayoutEngineType}
            >
              <option value={undefined}>None</option>
              <option value={'SnapToGrid'}>Snap to Grid</option>
              <option value={'VerticalTree'}>Vertical Tree</option>
            </select>
          </div>
          <div className="pan-list">
            <span>Pan To:</span>
            <select onChange={this.onSelectPanNode}>
              {nodes.map(node => (
                <option key={node[NODE_KEY]} value={node[NODE_KEY]}>
                  {node.title}
                </option>
              ))}
            </select>
          </div>
        </div>
        <GraphView
          ref={el => (this.GraphView = el)}
          nodeKey={NODE_KEY}
          nodes={nodes}
          edges={edges}
          selected={selected}
          nodeTypes={NodeTypes}
          nodeSubtypes={NodeSubtypes}
          edgeTypes={EdgeTypes}
          onSelectNode={this.onSelectNode}
          onCreateNode={this.onCreateNode}
          onUpdateNode={this.onUpdateNode}
          onDeleteNode={this.onDeleteNode}
          onSelectEdge={this.onSelectEdge}
          onCreateEdge={this.onCreateEdge}
          onSwapEdge={this.onSwapEdge}
          onDeleteEdge={this.onDeleteEdge}
          onUndo={this.onUndo}
          onCopySelected={this.onCopySelected}
          onPasteSelected={this.onPasteSelected}
          layoutEngineType={this.state.layoutEngineType}
        />
      </div>
    );
  }
}

export default Graph;
