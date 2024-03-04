# Instructions

1. Create and activate **venv**.
2. Install dependencies from requirements.txt or u can simply install pytest
3. start executing script using 
```python
python main.py <specify_path_and_json_name> --root <root_element_name>
```
4. *Optional:* To run unit tests run
```python
pytest
```

> **Note!** *Unit tests doesn't compare whole result string with expected one, because of indentation.*

# Task description

We have some json, for example this one:

```jsx
{
"result": {
"status": "active",
"name": {
"first": "Kaley",
"middle": "James",
"last": "Wilderman",
"kids": [
"X",
"Y"
]
},
"username": "Kaley-Wilderman",
"password": "0MN5UzpT6WJCPx_",
"emails": [
"[Kiel88@gmail.com](mailto:Kiel88@gmail.com)",
"[Javon84@gmail.com](mailto:Javon84@gmail.com)"
],
"phoneNumber": "790-274-3174 x842",
"location": {
"street": "4063 O'Keefe Road",
"city": "Bartlett",
"state": "New Jersey",
"country": "Singapore",
"zip": "38602",
"coordinates": {
"latitude": 39.0617,
"longitude": 64.7887
}
},
"website": "[https://striped-double.biz](https://striped-double.biz/)",
"uuid": "0e044067-e95c-4cb8-90fc-aa3427843ff7"
}
}
```

> Goal - write code using pure python which converts such json into xml


Expected xml:

```jsx
<?xml version="1.0" encoding="UTF-8"?>
<root>
<result>
<emails>
<element>Kiel88@gmail.com</element>
<element>Javon84@gmail.com</element>
</emails>
<location>
<city>Bartlett</city>
<coordinates>
<latitude>39.0617</latitude>
<longitude>64.7887</longitude>
</coordinates>
<country>Singapore</country>
<state>New Jersey</state>
<street>4063 O'Keefe Road</street>
<zip>38602</zip>
</location>
<name>
<first>Kaley</first>
<kids>
<element>X</element>
<element>Y</element>
</kids>
<last>Wilderman</last>
<middle>James</middle>
</name>
<password>0MN5UzpT6WJCPx_</password>
<phoneNumber>790-274-3174 x842</phoneNumber>
<status>active</status>
<username>Kaley-Wilderman</username>
<uuid>0e044067-e95c-4cb8-90fc-aa3427843ff7</uuid>
<website>https://striped-double.biz</website>
</result>
</root>
```

**Important** - no matter how much nested objects/arrays inside, it must return valid xml.

[To verify xml click there](https://www.freeformatter.com/json-to-xml-converter.html#before-output)

👉🏻  **Additionally** - code must be covered by tests