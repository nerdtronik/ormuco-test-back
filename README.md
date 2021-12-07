# Ormuco test-back

## Routes

- #### /login

  **Method**: POST

  Login into the ormuco account

  **Body**: 

  ```json
  {
      "username":"email@email.com",
      "password":"hnasc89ashncjas"
  }
  ```

  **Response**:

  ```json
  {
      "success":true,
      "token":"asnd978ashgdiuashdb79asgdjashbjkasbn9f8dhsg98chbisa",
      "expires":"2021-12-12P12:35:442323423Z"
  }
  ```

For every next method, you need to send the next headers:

**Headers**:

```json
{
    "X-Auth-Token":"token"
}
```

- #### /servers

  **Method**: POST
  
  Create a server

  **Body**:

  ```json
  {
      "name":"Server name",
      "flavor":"Instance flavor id",
      "keypair":"Keypair to be used",
      "image":"Image id"
  }
  ```
  
  **Response**:
  
  ```json
  {
      "success":true,
      "data":{OpenStack detailed server info}
  }
  ```

  **Method**: GET
  
  Get Server list
  
  If you want the list with detailed information send ``/servers?detailed=true``
  
  **Response**:
  
  ```json
  {
      "success":true,
      "data":[ Server data list ]
  }
  ```

- #### /keypairs

  **Method**: POST

  Create a keypair

  **Body**:

  ```json
  {
      "name":"Keypair Name"
  }
  ```

  **Response**:

  ```json
  {
  "success":true,
  "data":{ OpenStack Keypair data }
  }
  ```

  **Method**: GET

  Get keypairs list

  **Response**:

  ```json
  {
   	"success":true,
      "data":[ Keypairs List ]
  }
  ```

- #### /flavors

  **Method**: GET

  Get Flavors list

  **Response**:

  ```json
  {
   	"success":true,
      "data":[ Flavors List ]
  }
  ```

- #### /networks

  **Method**: GET

  Obtain network list

  **Response**:

  ```json
  {
   	"success":true,
      "data":[ Network List ]
  }
  ```

- #### /images

  **Method**: GET

  Obtain images list

  **Response**:

  ```json
  {
   	"success":true,
      "data":[ Images List ]
  }
  ```

  



