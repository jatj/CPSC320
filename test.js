// ####################################################################################################################################
// Graph

var GraphNode = function(data = null){
	this.Value = data;
	this.adjacent = [];
	this.Marked = false;
}
GraphNode.prototype.directedEdge = function(node) {
	this.adjacent.push(node);	
};
GraphNode.prototype.undirectedEdge = function(node) {
    this.adjacent.push(node);
    node.adjacent.push(this);
};
// ####################################################################################################################################
// Stack
var Stack = function(){
	this.top = null;
	this.size = 0;
}
Stack.prototype.makeNode = function(data=null) {
	return {'Value':data,'Next':null};
};
Stack.prototype.push = function(data) {
	var node = this.makeNode(data);
	node.Next = this.top;
	this.top = node;
	this.size++;
};
Stack.prototype.pop = function() {
	if(this.top != null){
		var data = this.top.Value;
		this.top = this.top.Next;
		this.size--;
		return data;
	}else{
		return null;
	}
};
Stack.prototype.peek = function() {
	if(this.top != null){
		return this.top.Value;
	}else{
		return null;
	}
};
Stack.prototype.isEmpty = function() {
	return this.top==null;
};

// ####################################################################################################################################
// Queue
var Queue = function(){
	this.first = null;
	this.last = null;

}
Queue.prototype.makeNode = function(data=null) {
	return {'Value':data,'Next':null};
};
Queue.prototype.enqueue = function(data) {
	var node = this.makeNode(data);
	if(this.first ==null){
		this.first = node;
		this.last = node;
	}else{
		this.last.Next = node;
		this.last = node; 
	}
};
Queue.prototype.dequeue = function() {
	if(this.first == null){
		return null;
	}
	var data = this.first.Value;
	this.first = this.first.Next;
	if(this.first == null){
		this.last = null;
	}
	return data;
};
Queue.prototype.peek = function() {
	if(this.first==null){
		return null
	}else{
		return this.first.Value;
	}
};
Queue.prototype.isEmpty = function() {
	return this.first == null;
};
// ####################################################################################################################################
// Depth-First Search

function DFS(root,visit){
	if(root == null) return;
	var result = visit(root);
	if(result != undefined){
		return result;
	}
	root.Marked = true;
	for(n in root.adjacent){
		var node = root.adjacent[n];
		if(node.Marked == false){
			DFS(node,visit);
		}
	}
}

// ####################################################################################################################################
// Breath-First Search

function BFS(root,visit){
	var queue = new Queue();
    root.Marked = true;
	queue.enqueue(root);
	iterations = 0;

	while(!queue.isEmpty()){
		var r = queue.dequeue();
		var result = visit(r);
		if(result != undefined){
			return result;
		}
		for(n in r.adjacent){
			var node = r.adjacent[n];
			if(node.Marked == false){
                node.Marked = true;
				queue.enqueue(node);
			}
		}
	}
}

// ####################################################################################################################################
// 1.3 Triangle in graph
// var n = 5
// var V = Array(n);
// for(var i = 0; i < n; i++){
//     V[i] = new GraphNode(i);
// }
// V[0].undirectedEdge(V[1]);
// V[1].undirectedEdge(V[2]);
// V[1].undirectedEdge(V[3]);
// V[2].undirectedEdge(V[3]);
// V[2].undirectedEdge(V[4]);
// var triangle = 0;

// function DFSTriangle(root,searchNode, depth = 0){
// 	if(root == null) return;
// 	if(depth == 3){
// 		return root.Value == searchNode.Value
// 	}
// 	root.Marked = true;
// 	for(n in root.adjacent){
// 		var node = root.adjacent[n];
// 		return DFSTriangle(node,searchNode,depth+1);
// 	}
// }

// for(var i = 0; i < n; i++){
//     res = DFSTriangle(V[i],V[i]);
//     if(res != undefined){
//         triangle++;
//         break;
//     }
// }
// console.log((triangle == 0) ? "No" : "Yes")

// ####################################################################################################################################
// 4.2 Triangle in graph

var N = 6;
var V = Array(N);
for(var i = 0; i < N; i++){
    V[i] = new GraphNode(i);
}
// V[0].undirectedEdge(V[1]);
// V[1].undirectedEdge(V[3]);
// V[2].undirectedEdge(V[0]);
// V[3].undirectedEdge(V[2]);
// V[3].undirectedEdge(V[4]);

V[0].undirectedEdge(V[1]);
V[1].undirectedEdge(V[2]);
V[0].undirectedEdge(V[3]);
V[3].undirectedEdge(V[2]);
V[0].undirectedEdge(V[4]);
V[5].undirectedEdge(V[4]);

function FindVulnerability(root){
	var queue = new Queue();
    root.Marked = true;
    root.depth = 0;
	queue.enqueue(root);

	while(!queue.isEmpty()){
		var r = queue.dequeue();
		for(n in r.adjacent){
			var node = r.adjacent[n];
			if(node.Marked == false){
				if((r.depth + 1) > N/2) return r;
				node.Marked = true;
				node.depth = r.depth + 1
				queue.enqueue(node);
			}
		}
	}
	return null;
}

console.log("Vulnerability:", FindVulnerability(V[2]));