# MP2: Fault-Tolerant Key-Value Store

## 📘 Overview

This project is part of the *Cloud Computing Specialization - Programming Assignment (C3 Part 2)* and focuses on implementing a **fault-tolerant distributed key-value store**. The system is built in C++ and runs on a virtual emulated network environment. Key features include consistent hashing, replication for fault-tolerance, quorum-based consistency, and stabilization on node failure.

---

## 💡 Features

- ✅ **CRUD Operations**: Full support for Create, Read, Update, and Delete operations.
- 🔁 **Consistent Hashing Ring**: Ensures uniform key distribution and simplifies node joining/leaving.
- 🔄 **Replication (3 copies)**: Every key is replicated on three successive nodes for fault tolerance.
- 💥 **Fault Tolerance**: Can tolerate up to two simultaneous node failures.
- ☑️ **Quorum-Based Consistency**: Write and read operations require a quorum (≥2/3 nodes) to succeed.
- 🔧 **Stabilization Protocol**: Automatically handles key re-replication after a node crash.

---

## 📂 Project Structure

├── MP1Node.cpp/.h # Membership Protocol (from Part 1)
├── MP2Node.cpp/.h # Key-Value Store Logic (implement here)
├── EmulNet.* # Emulated Network Layer (do not modify)
├── Log.* # Logging functions
├── HashTable.* # Provided hash table wrapper (C++11 map)
├── Application.cpp # Application layer test cases
├── KVStoreGrader.sh # Local grading script
├── dbg.log # Output log file for grading
└── submit.py # Submit to Coursera

yaml
Copy
Edit

---

## 🧱 Architecture

The system is composed of three logical layers:

1. **Application Layer** (Top)
2. **P2P Layer**:
   - `MP1Node` - Membership protocol (already implemented in C3 Part 1).
   - `MP2Node` - Key-value store logic (implemented in this project).
3. **EmulNet Layer** (Bottom) - Simulated network for message passing.

Each node is logically split into `MP1Node` and `MP2Node` components. Nodes communicate through a simulated single-threaded EmulNet engine.

---

## 🛠️ Files to Modify

You are only allowed to modify the following files:

- `MP1Node.cpp` / `MP1Node.h` – Import your working membership protocol.
- `MP2Node.cpp` / `MP2Node.h` – Implement the KV store logic here.

---

## 📌 Functions to Implement

### 🔄 Ring Management
- `MP2Node::updateRing()`

### 🧑‍💻 Client-side APIs
- `MP2Node::clientCreate()`
- `MP2Node::clientRead()`
- `MP2Node::clientUpdate()`
- `MP2Node::clientDelete()`

### 🖥️ Server-side APIs
- `MP2Node::createKeyValue()`
- `MP2Node::readKey()`
- `MP2Node::updateKeyValue()`
- `MP2Node::deleteKey()`

### 🛡️ Fault Tolerance
- `MP2Node::stabilizationProtocol()`

---

## 🧪 Testing

Use the provided grading script to test your implementation:

```bash
$ ./KVStoreGrader.sh
This script will run a set of test cases that check for:

✔️ Basic CRUD operations

🔁 Key replication under single node failures

❌ Quorum failure scenarios with multiple node crashes

🛠️ Stabilization and successful operations after failure recovery

A log file named dbg.log will be generated automatically and evaluated against expected log patterns.

To view or debug logs manually:
```bash
$ cat dbg.log