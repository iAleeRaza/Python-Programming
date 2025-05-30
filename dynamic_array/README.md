<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

  <h1>Dynamic Array Implementation in Python using <code>ctypes</code></h1>

  <p>This project demonstrates the creation of a <strong>dynamic array (similar to Python's built-in list)</strong> using the <code>ctypes</code> module. It mimics low-level array management in C, providing better understanding of how dynamic arrays work under the hood.</p>

  <h2>📦 Features</h2>
  <p>The custom dynamic array supports the following operations:</p>
  <ul>
    <li><strong>len</strong> – Returns the number of elements in the array.</li>
    <li><strong>append</strong> – Adds an element at the end of the array.</li>
    <li><strong>remove</strong> – Removes the first occurrence of a specified element.</li>
    <li><strong>insert</strong> – Inserts an element at a specified index.</li>
    <li><strong>delete</strong> – Deletes an element at a specified index.</li>
    <li><strong>Extend</strong> – Extends the array with another ietratable .</li>
    <li><strong>clear</strong> – Removes all elements from the array.</li>
    <li><strong>print</strong> – Displays all the elements in the array.</li>
    <li><strong>pop</strong> – Removes and returns the last element.</li>
    <li><strong>find</strong> – Returns the index of the first occurrence of a specified element.</li>
    <li><strong>Sum</strong> – Returns the sum of all the elements in the array.</li>
    <li><strong>Min</strong> – Returns the minimum value in the array.</li>
    <li><strong>Max</strong> – Returns the maximum value in the array.</li>
  </ul>

  <h2>🧰 What is <code>ctypes</code>?</h2>
  <p><a href="https://docs.python.org/3/library/ctypes.html" target="_blank"><code>ctypes</code></a> is a built-in Python library for calling functions and using data types from C libraries. It allows you to create fixed-type, contiguous memory buffers—ideal for understanding how arrays work in low-level languages like C.</p>

  <h2>📁 File Structure</h2>
  <div class="code-block">
    📦 Python-Programming/<br>
    ┣ 📜 dynamic_array.py<br>
    ┗ 📜 practice.ipynb
    ┗ 📜 README.html
  </div>

  <h2>🧠 Learning Objective</h2>
  <p>This project is a hands-on practice for learning:</p>
  <ul>
    <li>How dynamic memory allocation works</li>
    <li>Manual array resizing and copying</li>
    <li>Building foundational data structures in Python using low-level techniques</li>
  </ul>

</body>
</html>
