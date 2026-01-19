# ⏱️ Time Complexity (Yadav Ji DSA)

Time Complexity tells us **how fast an algorithm grows** as input size increases.

## Types Covered
- O(1) Constant Time   --> same time , no matter input size (n)
- O(log n) Logerathmic --> very fast , (Binary search)
- O(n) Linear Time.    --> Time Growth with input size
- O(n log n) Linerathmic --> Efficient sorting
- O(n²) Quadratic Time --> Nested loop 
- O( 2^n) Exponential Time  --> vey slow

## Golden Rule
- One loop → O(n)
- Loop inside loop → O(n²)
- Divide input by 2 → O(log n)

## 💼 Time & Space Complexity
Interview Questions & Answers (Yadav Ji DSA)
Q1️⃣ What is Time Complexity?

Answer (Interview-Ready):

Time Complexity measures how the number of operations in an algorithm grows with respect to input size n. It is expressed using Big-O notation and focuses on the worst-case scenario.

Q2️⃣ Why don’t we calculate time in seconds?

Answer:

Actual execution time depends on hardware, language, and compiler. Time complexity provides a machine-independent way to compare algorithm efficiency.

Q3️⃣ What is Big-O Notation?

Answer:

Big-O notation describes the upper bound of an algorithm’s time or space complexity, representing the worst-case growth rate as input size increases.

Q4️⃣ Why do we consider the worst case?

Answer:

Worst-case analysis guarantees that the algorithm will perform within acceptable limits even under maximum input or load conditions.

Q5️⃣ What is Space Complexity?

Answer:

Space Complexity measures the amount of extra memory used by an algorithm excluding the input, including variables, data structures, and recursion stack.

Q6️⃣ Does recursion affect space complexity?

Answer:

Yes. Each recursive call is stored in the call stack, so space complexity depends on the maximum recursion depth.

Q7️⃣ What is O(1) time complexity?

Answer:

O(1) means the algorithm takes constant time regardless of input size, such as accessing an array element by index.

Q8️⃣ What is O(log n) time complexity?

Answer:

O(log n) occurs when the input size is reduced by a constant factor, usually by half, in each step. Binary Search is a common example.

Q9️⃣ Explain O(n) time complexity.

Answer:

O(n) means the execution time grows linearly with input size, such as iterating through an array once.

Q1️⃣0️⃣ Why is Merge Sort O(n log n)?

Answer:

Merge Sort divides the array into halves log n times and processes all n elements during merging at each level.

Q1️⃣1️⃣ Difference between O(n²) and O(n log n)?

Answer:

O(n²) involves nested loops and becomes slow for large inputs, while O(n log n) is more efficient and is the best possible time complexity for comparison-based sorting.

Q1️⃣2️⃣ What is Exponential Time Complexity?

Answer:

Exponential complexity O(2ⁿ) occurs when each step doubles the number of operations, commonly seen in recursive problems like naive Fibonacci.

Q1️⃣3️⃣ What is Amortized Time Complexity?

Answer:

Amortized time complexity is the average cost per operation over a sequence of operations, even if some individual operations are expensive, such as dynamic array resizing.

Q1️⃣4️⃣ What is In-Place Algorithm?

Answer:

An in-place algorithm uses constant extra space O(1) and modifies the input directly, like Bubble Sort or Selection Sort.

Q1️⃣5️⃣ What is Time–Space Tradeoff?

Answer:

Time–Space tradeoff means using more memory to reduce execution time or using less memory at the cost of slower execution.

Q1️⃣6️⃣ What is the space complexity of Merge Sort?

Answer:

Merge Sort uses extra arrays during merging, so its space complexity is O(n).

Q1️⃣7️⃣ What is the space complexity of Quick Sort?

Answer:

Quick Sort is in-place but uses recursion. Average space complexity is O(log n) due to recursion stack, worst case is O(n).

Q1️⃣8️⃣ How do you calculate time complexity of nested loops?

Answer:

Multiply the number of iterations of each loop. For two nested loops running n times, time complexity is O(n²).

Q1️⃣9️⃣ What is the difference between best, average, and worst case?

Answer:

Best case is minimum time, average case is expected time, and worst case is maximum time. Interviews mostly focus on the worst case.

Q2️⃣0️⃣ How do you explain time complexity in interviews?

Answer:

First, identify loops or recursion. Then describe how operations scale with input size and conclude with the worst-case Big-O notation.