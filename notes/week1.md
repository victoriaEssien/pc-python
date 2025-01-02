learnt about “f strings” (f ” ”} - allows you to insert a variable anywhere in the print statement - different from concatenation with “+”. f string is more convenient

```python
# With f string
full_name = "CodeBreaker"
print(f"Hello {full_name}, how are you?")

# Output
# Hello CodeBreaker, how are you?

# Without f string
full_name = "CodeBreaker"
print("Hello" + " " + full_name + " " + "how are you?")

# Output
# Hello CodeBreaker how are you?
```

## Keywords

- Typecasting - the process of converting a variable from one data type to another. This is useful in converting user input.
```python
age= 18
age = float(age)
print(age)

# Output
# 18.0
```