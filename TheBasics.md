# Data Structures & Algoritms
## Intro
This is a study guide to relearning the bascics of Data Structures and Algorithms for interview prep.

## What are Data Strucutres?
- Specific ways of orginizing and storing data in computer memory
- Defined layouts and organization of Data elements
- The enablement of efficent manipulation, retrevial and mangement of data
- Provides a layer of abstraction to work with data in a structured and orginized manner

## What are Basic Data Structures?
- **[Arrays](#arrays)**: Fixed size , Block of memory to store Data
- **[Linked Lists](#linked_list)** : A list of nodes that contain data and refrence link (pointer) to the next node
- **[Trees](#trees)** : a collection of nodes that contain children nodes connected to Root. Heirachical Structure
- **[Stacks](#stacks)** : LiFo. Insertion and Deletion only happens from the top.
- **[Queues](#queues)** : FiFo. Insertion from bottom/end and Deletion from front/top
- **[Graphs](#graphs)** : Set of vertecies (nodes) connected by edges. Represents various relationships
 

 # [Arrays](#arrays)

|Action | Time Complexity|
| --- | --- |
|Access Element| O(1) |
|Insert Front | O(1) |
|Insert Middle/End | O(N) |
|Delete End |O(1) |
|Delete Front/Middle | O(N) |
|Search |O(N) |
|Update Element |O(1) |

# [Linked Lists](#linked_list)
|Action | Time Complexity|
| --- | --- |
|Access Element | O(N) |
|Insertion Front | O(1) |
|Insertion Middle | O(N) |
|Insertion End |O(N) |
|Deletion Front |O(1) |
|Deletion Middle |O(N) |
|Deletion End |O(N) |

# [Trees](#trees)
|Action | Time Complexity|
| --- | --- |
|Traversal |O(N) |
|Insertion |O(N) |
|Deletion |O(log N) or O(N) |
|Searching |O(log N)  or O(N)|
|Height and Depth |O(N) |
|Balancedness Checking|O(N) |

# [Stacks](#stacks)
|Action | Time Complexity|
| --- | --- |
|Push | O(1)|
|Pop |O(1) |
|Peek |O(1) |
|Search |O(N) |
|Size |O(1) |


# [Queues](#queues)
|Action | Time Complexity|
| --- | --- |
|Enqueue |O(1) |
|Dequeue |O(1) |
|Peek |O(1) |
|Search |O(N) |
|Size |O(1) |


# [Graphs](#graphs)
|Action | Time Complexity|
| --- | --- |
|Representation: |  |
|- Adjacency Matrix |O(N<Sup>2</Sup>) |
|- Adjacency List |O(N+M) |
|Traversal: | |
|- DFS |O(N+M) |
|- BFS |O(N+M) |
|Shortest Path: | |
|- Dijikstra's Algorithm | O((N+M)Log N) |
|- Bellman-Ford Algorithm |O(N+M) |
|Connectivity Checking |O(N+M) |
|Cycle Detection |O(N+M) |
|Topological |O(N+M) |
