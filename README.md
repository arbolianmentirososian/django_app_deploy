# Django Pipeline Test

Sample application that is used for testing purposes.
It is written in Python 3 and Django web framework.

There are 5 endpoints to play with:

* **URL**

    /add/{num1}/{num2}

* **Method**

    `GET`

* **URL Params**

    **Required:**

    `num1=[integer]`

    `num2=[integer]`

* **Sample call**

    `curl -X GET http://localhost:55555/add/50/5`

* **Success Response**

    * **Code:** 200 <br />
    * **Content:** `{"num1": 50, "num2": 5, "num1 + num2": 55}`

<br/><br/>
  
* **URL**

    /subtract/{num1}/{num2}

* **Method**

    `GET`

* **URL Params**

    **Required:**

    `num1=[integer]`

    `num2=[integer]`

* **Sample call**

    `curl -X GET http://localhost:55555/subtract/50/5`

* **Success Response**

    * **Code:** 200 <br />
    * **Content:** `{"num1": 50, "num2": 5, "num1 - num2": 45}`

<br/><br/>

* **URL**

    /multiply/{num1}/{num2}

* **Method**

    `GET`

* **URL Params**

    **Required:**

    `num1=[integer]`

    `num2=[integer]`

* **Sample call**

    `curl -X GET http://localhost:55555/multiply/50/5`

* **Success Response**

    * **Code:** 200 <br/>
    * **Content:** `{"num1": 50, "num2": 5, "num1 * num2": 250}`
  
<br/><br/>

* **URL**

    /divide/{num1}/{num2}

* **Method**

    `GET`

* **URL Params**

    **Required:**

    `num1=[integer]`

    `num2=[integer]`

* **Sample call**

    `curl -X GET http://localhost:55555/divide/50/5`

* **Success Response**

    * **Code:** 200 <br />
    * **Content:** `{"num1": 50, "num2": 5, "num1 / num2": 10}`
  
<br/><br/>

* **URL**

    /modulo/{num1}/{num2}

* **Method**

    `GET`

* **URL Params**

    **Required:**

    `num1=[integer]`

    `num2=[integer]`

* **Sample call**

    `curl -X GET http://localhost:55555/modulo/50/5`

* **Success Response**

    * **Code:** 200 <br />
    * **Content:** `{"num1": 50, "num2": 5, "num1 % num2": 0}`