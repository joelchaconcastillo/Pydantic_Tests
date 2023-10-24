# Pydantic

Pydantic is a Python library that provides data validation and parsing using Python data classes. It's particularly useful for data validation and serialization, commonly used in the context of data transfer, such as parsing data from the web, APIs, or configuration files.

  

Key features and use cases of Pydantic include:

  

1. Data Validation: Pydantic allows you to define data models using Python data classes, specifying the types and validation rules for each field. When you create an instance of the data class, Pydantic automatically validates the data, ensuring that it matches the specified structure and constraints.

  

2. Data Serialization: You can easily serialize data objects into JSON or other formats and deserialize data from these formats into Python objects. This is useful when working with web APIs, reading configuration files, or saving data to a database.

  

3. Type Hinting: Pydantic leverages Python's type hinting system to define the expected data types for each field. This not only helps with validation but also makes code more self-documenting and can assist with code analysis tools.

  

4. Default Values: Pydantic allows you to specify default values for fields, so if a value is not provided during object creation, it will fall back to the default value.

  

5. Parsing and Transformation: You can define custom parsing and transformation functions to preprocess or modify the data during validation or serialization.

  
  
  

## Comparison between Pydantic V1 and Pydantic V2 alpha

![](https://lh7-us.googleusercontent.com/tZzpzEir8EggZyApiUc7RPGEwUuGN3F-l2v7mwq6NDzDLGjOgT9q9nhfg0ejLDGZmOr3Fku_jQNzhcA0rLVKVXJJHjZ76I5buupk8_MKjKGEatszvOUGrrJRnOnfbZheVEESPNe4RB9WMhwqhtEpcUk)

  
  
  

(Figure taken from [https://2pointers.medium.com/an-introduction-to-pydantic-v2-alpha-pre-release-a-massive-improvement-over-previous-version-748a1f1118ba](https://2pointers.medium.com/an-introduction-to-pydantic-v2-alpha-pre-release-a-massive-improvement-over-previous-version-748a1f1118ba) )

  

![](https://lh7-us.googleusercontent.com/hQREvRwlN485uVPaEDiwu2q2HYdoE8_6hOfOmWIOSgKVKinJ7kTwGTOJwMko1_1nSgkRggfGJSFtmb34zDZ2-kb15R-T0cw3CDNTyLxmTlP5l81n06o2HfVwa2G4lHeAzb4bHsyfKjDMuZSKdJp97rg)

(Performance comparison taken from https://janhendrikewers.uk/pydantic-1-vs-2-a-benchmark-test.html#:~:text=In%20this%20blog%20post%20I,put%20it%20to%20the%20test.)

  

# Data types with Pydantic

Pydantic uses a wide range of Python data types and Pydantic-specific types for defining the structure of data classes, specifying the types of fields, and enforcing data validation. Here are some common Pydantic types and Python data types used in Pydantic data classes:

  

## Pydantic Data Types

-   `conint`: Represents a constrained integer.
    
-   `confloat`: Represents a constrained float.
    
-   `constr`: Represents a constrained string.
    
-   `conlist`: Represents a constrained list.
    
-   `conset`: Represents a constrained set.
    
-   `conbytes`: Represents constrained bytes.
    
-   `condecimal`: Represents a constrained decimal.
    
-   `conbool`: Represents a constrained boolean.
    
-   `constr_bytes`: Represents a constrained bytes-like object.
    
-   `constr_regex`: Represents a string that must match a regular expression pattern.
    

## Common Python Data Types

-   `int`: Integer data type.
    
-   `float`: Floating-point data type.
    
-   `str`: String data type.
    
-   `bool`: Boolean data type.
    
-   `list`: List data type.
    
-   `tuple`: Tuple data type.
    
-   `set`: Set data type.
    
-   `dict`: Dictionary data type.
    
-   `datetime.datetime`: Date and time data type.
    
-   `datetime.date`: Date data type.
    
-   `datetime.time`: Time data type.
    
-   `Enum`: Enumeration data type.
    

## Custom Data Classes

  

-   Pydantic data classes can be used as types. For example, you can have a data class `User` and use it as a field type in another data class:
  
```python
from pydantic import BaseModel
class User(BaseModel):
username: str
email: str
class Comment(BaseModel):
user: User
content: str
```
## Union Types

Python's `Union` can be used to specify that a field can accept values of different types. For example, to indicate that a field can be either an integer or a string:
```python
from pydantic import BaseModel
from typing import Union
class Item(BaseModel):
id: Union[int, str]
```
## Optional Types

The `Optional` type from the `typing` module can be used to indicate that a field is optional, meaning it can be either a value of a specified type or `None`.
```python
from pydantic import BaseModel
from typing import Optional
class Person(BaseModel):
name: str
age: Optional[int]
```
These are some of the commonly used Pydantic types and Python data types that you can use to define the structure of your Pydantic data classes. Pydantic's type system allows you to create data models that enforce strong typing and data validation while providing flexibility to handle a wide variety of data structures and data types.
  


| Feature / Tool | Pydantic | Marshmallow | attrs | dataclasses |
|----------------------------|----------------|----------------|----------------|----------------|
| Data Validation | ✔️ Yes | ✔️ Yes | ✖️ No | ✖️ No |
| Serialization/Deserialization | ✔️ Yes | ✔️ Yes | ✖️ No | ✖️ No |
| Type Hinting | ✔️ Yes | ✖️ No | ✖️ No | ✖️ No |
| Default Values | ✔️ Yes | ✔️ Yes | ✔️ Yes | ✔️ Yes |
| Custom Validation | ✔️ Yes | ✔️ Yes | ✔️ Yes | ✖️ No |
| Support for Nested Data | ✔️ Yes | ✔️ Yes | ✔️ Yes | ✖️ No |
| Extensibility | ✔️ Yes | ✔️ Yes | ✔️ Yes | ✔️ Yes |
| Type Conversion | ✔️ Yes | ✔️ Yes | ✖️ No | ✖️ No |
| Speed/Performance | Good | Good | Very Good | Very Good |
| Community Support | Strong | Good | Good | Good |
| Active Development | ✔️ Yes | ✔️ Yes | ✖️ No (Stable) | ✖️ No (Stable) |
| Dependencies | Few | Few | Few | Standard Library |
| License | MIT | MIT | MIT | MIT |

**Key:**

- ✔️ Yes: The tool/library supports the feature.

- ✖️ No: The tool/library does not support the feature.

- Good/Very Good: Indicates the relative speed and performance. Performance may vary depending on specific use cases.

## Validation libraries Comparison: A Detailed Analysis

| Feature / Tool | Pydantic | Marshmallow | Cerberus | dataclasses | attrs |
|--------------------------|------------------------------|------------------------------|------------------------------|--------------------------|------------------------------|
| License | MIT License | MIT License | MIT License | Python Standard Library | MIT License |
| Main Use Case | Data Validation, Parsing | Data Validation, Serialization | Data Validation | Data Classes Definition | Class Attribute Management |
| Type Annotations | Yes (Python data classes) | No | No | No | No |
| Default Values | Yes | Yes | Yes | No | No |
| Custom Validation | Yes | Yes | Yes | No | No |
| Serialization Formats | JSON, Custom Formats | JSON, Custom Formats | JSON, Custom Formats | N/A | N/A |
| Nesting Support | Yes | Yes | Yes | Limited | No |
| Complex Data Models | Yes | Yes | Yes | Limited | No |
| Integration with ORM | Yes (e.g., SQLAlchemy) | Yes (e.g., SQLAlchemy) | Limited | No | Limited |
| Data Transformation | Yes | Yes | Limited | No | No |
| Performance | Fast | Moderate | Fast | N/A | N/A |
| Active Development | Yes | Yes | Yes | Yes | Yes |
| Official Documentation | [Pydantic Docs](https://pydantic-docs.helpmanual.io/) | [Marshmallow Docs](https://marshmallow.readthedocs.io/en/stable/) | [Cerberus Docs](http://docs.python-cerberus.org/en/stable/) | [Dataclasses Docs](https://docs.python.org/3/library/dataclasses.html) | [attrs Docs](http://www.attrs.org/en/stable/) |

| Feature / Tool | Pydantic | Marshmallow | Cerberus | dataclasses |
|------------------------|--------------------------|--------------------------|--------------------------|------------------------|
| License | MIT | MIT | MIT | Python Standard Library |
| Main Use Case | Data Validation, Parsing | Data Validation, Parsing | Data Validation | Data Classes Definition |
| Type Annotations | Yes | No | No | Yes |
| Default Values | Yes | Yes | Yes | No |
| Custom Validation | Yes | Yes | Yes | No |
| Serialization Formats | JSON, custom formats | JSON, custom formats | JSON | N/A |
| Nesting Support | Yes | Yes | Yes | No |
| Complex Data Models | Yes | Yes | Yes | Limited |
| Integration with ORM | Yes (e.g., SQLAlchemy) | Yes (e.g., SQLAlchemy) | Limited | No |
| Performance | Fast | Moderate | Fast | N/A |
| Active Development | Yes | Yes | Yes | Yes |
  

1. **Pydantic**:

- Pydantic is a data validation and parsing library that works well with Python 3.6 and later.

- It leverages Python data classes and type hints for data modeling.

- Pydantic is known for its simplicity and extensive features, including data validation, default values, custom validation, and serialization support.

2. **Marshmallow**:

- Marshmallow is a library for object serialization/deserialization, validation, and parsing.

- It's well-suited for data validation and serialization, often used in web applications.

- Marshmallow doesn't rely on Python data classes and type hints but instead uses schema objects.

3. **Cerberus**:

- Cerberus is a lightweight data validation library primarily designed for dictionaries and JSON-like data structures.

- It focuses on validating and transforming dictionaries against defined schemas.

- Cerberus is particularly useful when working with configuration files and external data sources.

4. **dataclasses**:

- Data classes are not a separate library, but a built-in feature introduced in Python 3.7 (PEP 557).

- They are used for defining classes primarily as simple containers for data.

- Data classes provide basic default values and are used for creating simple data objects.

 
For complex data models, Pydantic and Marshmallow are often preferred. Cerberus is a good choice for working with dictionaries and configuration files. Dataclasses are ideal for simple data storage objects, but they lack many of the features found in the other libraries. Additionally, Pydantic and Marshmallow offer strong support for integration with popular ORMs like SQLAlchemy when working with databases.

 

## References

-   [https://pypi.org/project/pydantic/](https://pypi.org/project/pydantic/)
-   [https://docs.pydantic.dev/latest/examples/secrets/](https://docs.pydantic.dev/latest/examples/secrets/)
-   [https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties](https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties)
-   [https://janhendrikewers.uk/pydantic-1-vs-2-a-benchmark-test.html#:~:text=In%20this%20blog%20post%20I,put%20it%20to%20the%20test](https://janhendrikewers.uk/pydantic-1-vs-2-a-benchmark-test.html#:~:text=In%20this%20blog%20post%20I,put%20it%20to%20the%20test).



