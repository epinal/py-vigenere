# py-vigenere
Vigenere Cypher implementation in python 3.5

Example usage:

```python
    >>> vig = VigenereCypher()
    >>> cypher = vig.encrypt('secret', 'this is a sample text')
    >>> print(cypher)
    'LLKJ BK C WTETNV MWBV'
    >>> plain_text = vig.decrypt('secret', cypher)
    >>> print(plain_text)
    'THIS IS A SAMPLE TEXT'
    
```
