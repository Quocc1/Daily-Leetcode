# Script to create Python files with specified filenames based on problem titles and dates
import os
from datetime import datetime

# List of problems with their titles and dates in the format 'dd/mm/yyyy: index. Title'
problems = [
    "02/11/2024: 50. Pow(x, n)",
    "03/11/2024: 53. Maximum Subarray",
    "04/11/2024: 54. Spiral Matrix",
    "05/11/2024: 55. Jump Game",
    "06/11/2024: 56. Merge Intervals",
    "07/11/2024: 57. Insert Interval",
    "08/11/2024: 59. Spiral Matrix II",
    "09/11/2024: 61. Rotate List",
    "10/11/2024: 62. Unique Paths",
    "11/11/2024: 71. Simplify Path",
    "12/11/2024: 72. Edit Distance",
    "13/11/2024: 73. Set Matrix Zeroes",
    "14/11/2024: 74. Search a 2D Matrix",
    "15/11/2024: 75. Sort Colors",
    "16/11/2024: 77. Combinations",
    "17/11/2024: 79. Word Search",
    "18/11/2024: 80. Remove Duplicates from Sorted Array II",
    "19/11/2024: 81. Search in Rotated Sorted Array II",
    "20/11/2024: 82. Remove Duplicates from Sorted List II",
    "21/11/2024: 86. Partition List",
    "22/11/2024: 89. Gray Code",
    "23/11/2024: 90. Subsets II",
    "24/11/2024: 91. Decode Ways",
    "25/11/2024: 92. Reverse Linked List II",
    "26/11/2024: 93. Restore IP Addresses",
    "27/11/2024: 95. Unique Binary Search Trees II",
    "28/11/2024: 96. Unique Binary Search Trees",
    "29/11/2024: 97. Interleaving String",
    "30/11/2024: 98. Validate Binary Search Tree",
    "01/12/2024: 99. Recover Binary Search Tree"
]

# Create a directory for the output if it does not exist
output_directory = "problem_scripts"
os.makedirs(output_directory, exist_ok=True)

# Create Python files based on problem names
for problem in problems:
    # Extract the date and title
    date_part, title_part = problem.split(": ")
    _, title = title_part.split(". ", 1)
    
    # Create a valid filename (remove spaces and use capitalization for the name)
    filename = title.replace(" ", "") + ".py"
    filepath = os.path.join(output_directory, filename)

    # Write a header to the file with the problem date and title
    with open(filepath, "w") as file:
        file.write(f"# {date_part}: {title_part}\n")
        file.write(f"# Solution for {title}\n\n")
        file.write("def main():\n")
        file.write("    pass\n\n")
        file.write("if __name__ == '__main__':\n")
        file.write("    main()\n")

# List created files for verification
created_files = os.listdir(output_directory)
created_files
