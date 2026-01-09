#include <vector>
#include <queue>
using namespace std;

vector<int> getBfsTraversalOrder(const vector<vector<int>>& adjacency_list) {
    
    vector<bool> is_visited(adjacency_list.size(), false);
    
    vector<int> traversal_order; 
    
    queue<int> nodes_to_visit;

    // Push Start Node
    is_visited[0] = true;
    nodes_to_visit.push(0);

    while(!nodes_to_visit.empty()){

        int current_node = nodes_to_visit.front();
        nodes_to_visit.pop();

        traversal_order.push_back(current_node);

        for(int neighbor : adjacency_list[current_node]){
            if(!is_visited[neighbor]){
                is_visited[neighbor] = true;
                nodes_to_visit.push(neighbor);
            }
        }
    }
    return traversal_order;
}