# IFRC Award Allocator
This code simulates allocating funds to grant applications in a random order, as Wellcome used for its IFRC scheme. It deducts the requested amounts from the total budget until it is exhausted. After each deduction, the application reference, bid amount and remaining budget are recorded.
 
When the budget becomes negative, the final application is recorded, and the process stops.
