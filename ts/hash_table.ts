

const HashTable = new Map<string , number>();

console.log(typeof HashTable); // object


HashTable.set("apple", 1);
HashTable.set("banana", 2);
HashTable.set("cherry", 3);

console.log(HashTable.get("banana")); // Output: 2
// console.log(HashTable.has("grape"));