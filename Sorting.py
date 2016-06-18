# Written in Python 3.5.1 by Kurtis Mackey
"""
O(n^2) sorting algorithms
  Insertion Sort
  Selection Sort
  Bubble Sort

O(nlogn) sorting algorithms
  Merge Sort
  Quick Sort
"""
import unittest

# =================================================================

def insertion(array):
  """Insertion Sort for an array of numbers"""
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j-1] > array[j]:
      array[j], array[j-1] = array[j-1], array[j]
      j -= 1
  return array

# =================================================================

def selectionsort(array):
  """Selection Sort for an array of numbers"""
  for i in range(len(array)):
    min_index = i
    for j in range(i, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    if i != min_index:
      array[i], array[min_index] = array[min_index], array[i]
  return array


# ==================================================================

def bubblesort(array):
  """Bubble Sort for an array of numbers"""
  j = len(array)
  while j > 0:
    swapped = False
    for i in range(1, j):
      if array[i-1] > array[i]:
        array[i-1], array[i] = array[i], array[i-1]
        swapped = True
    j -= 1
    if swapped == False:
      return array
  return array

# ==================================================================

def _subsort(left, right):
  merged_array = list()
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged_array.append(left[i])
      i += 1
    else:
      merged_array.append(right[j])
      j += 1
  merged_array.extend(left[i:])
  merged_array.extend(right[j:])
  return merged_array

def mergesort(array):
  """Merge Sort for an array of numbers"""
  if len(array) == 1:
    return array
  else:
    mid = len(array) // 2
    return _subsort(mergesort(array[mid:]), mergesort(array[:mid]))

# ==================================================================

def _partition(array, low, high):
  pivot_index = (low + high) // 2
  pivot_value = array[pivot_index]
  array[low], array[pivot_index] = array[pivot_index], array[low]
  j = low
  for i in range(low, high+1):
    if array[i] < pivot_value:
      j += 1
      array[i], array[j] = array[j], array[i]
  array[low], array[j] = array[j], array[low]
  return j

def quicksort(array, low=0, high=None):
  """Quick Sort for an array of numbers"""
  if high == None:
    high = len(array)-1
  if low < high:
    p = _partition(array, low, high)
    quicksort(array, low, p - 1)
    quicksort(array, p + 1, high)
  return array

# ==================================================================
# =========================== TESTING ==============================

class SortingTests(unittest.TestCase):

  def setUp(self):
    self.rev_array_20 = list(reversed(range(20)))
    self.sorted_array_20 = list(range(20))
    self.rev_array_50 = list(reversed(range(50)))
    self.sorted_array_50 = list(range(50))

  def test_insertionEqual(self):
    self.assertEqual(insertion(self.rev_array_20), self.sorted_array_20)
    self.assertEqual(insertion(self.rev_array_50), self.sorted_array_50)
    self.assertEqual(insertion([4, 5, 1, 1, 5, 6, 1]), [1, 1, 1, 4, 5, 5, 6])
    self.assertEqual(insertion([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

  def test_selectionsortEqual(self):
    self.assertEqual(selectionsort(self.rev_array_20), self.sorted_array_20)
    self.assertEqual(selectionsort(self.rev_array_50), self.sorted_array_50)
    self.assertEqual(selectionsort([4, 5, 1, 1, 5, 6, 1]), [1, 1, 1, 4, 5, 5, 6])
    self.assertEqual(selectionsort([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

  def test_bubblesortEqual(self):
    self.assertEqual(bubblesort(self.rev_array_20), self.sorted_array_20)
    self.assertEqual(bubblesort(self.rev_array_50), self.sorted_array_50)
    self.assertEqual(bubblesort([4, 5, 1, 1, 5, 6, 1]), [1, 1, 1, 4, 5, 5, 6])
    self.assertEqual(bubblesort([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

  def test_mergesortEqual(self):
    self.assertEqual(mergesort(self.rev_array_20), self.sorted_array_20)
    self.assertEqual(mergesort(self.rev_array_50), self.sorted_array_50)
    self.assertEqual(mergesort([4, 5, 1, 1, 5, 6, 1]), [1, 1, 1, 4, 5, 5, 6])
    self.assertEqual(mergesort([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

  def test_quicksortEqual(self):
    self.assertEqual(quicksort(self.rev_array_20), self.sorted_array_20)
    self.assertEqual(quicksort(self.rev_array_50), self.sorted_array_50)
    self.assertEqual(quicksort([4, 5, 1, 1, 5, 6, 1]), [1, 1, 1, 4, 5, 5, 6])
    self.assertEqual(quicksort([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

  def tearDown(self):
    del self.rev_array_20
    del self.sorted_array_20
    del self.rev_array_50
    del self.sorted_array_50

if __name__ == '__main__':
  unittest.main()
