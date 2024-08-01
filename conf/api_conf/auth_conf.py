def token_payload(username, encriptedPassword):
    return {
        'userName': username,
        'password': encriptedPassword,
        'login_p': '',
        'eService': 2
    }

token_schema = {
  "type": "object",
  "properties": {
    "content": {},
    "errorList": {
      "type": "object",
      "properties": {
        "R2FA": {
          "type": "string"
        },
        "Error": {
          "type": "string"
        }
      },
      "required": [
        "R2FA",
        "Error"
      ]
    },
    "successList": {
      "type": "object",
      "properties": {},
      "required": []
    },
    "warningList": {
      "type": "object",
      "properties": {},
      "required": []
    },
    "success": {
      "type": "boolean"
    }
  },
  "required": [
    "content",
    "errorList",
    "successList",
    "warningList",
    "success"
  ]
}

token_data = {
    "content": None,
    "errorList": {
        "R2FA": "Authentication token has been sent to email",
        "Error": "2FA Required"
    },
    "successList": {},
    "warningList": {},
    "success": False
}

def verify_token_payload (token, userName):
    return {
    "token": token,
    "userName": userName,
    "rememberDevice": False,
    "eService": 2
    }

verify_token_schema = {
  "type": "object",
  "properties": {
    "content": {
      "type": "object",
      "properties": {
        "userName": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "firstName": {
          "type": "string"
        },
        "lastName": {
          "type": "string"
        },
        "lastLogon": {
          "type": "string"
        },
        "authToken": {
          "type": "string"
        },
        "simpleToken": {
          "type": "string"
        },
        "expiresIn": {
          "type": "number"
        },
        "changePassword": {
          "type": "boolean"
        },
        "firstLogin": {
          "type": "boolean"
        }
      },
      "required": [
        "userName",
        "email",
        "firstName",
        "lastName",
        "lastLogon",
        "authToken",
        "simpleToken",
        "expiresIn",
        "changePassword",
        "firstLogin"
      ]
    },
    "errorList": {
      "type": "object",
      "properties": {},
      "required": []
    },
    "successList": {
      "type": "object",
      "properties": {},
      "required": []
    },
    "warningList": {
      "type": "object",
      "properties": {},
      "required": []
    },
    "success": {
      "type": "boolean"
    }
  },
  "required": [
    "content",
    "errorList",
    "successList",
    "warningList",
    "success"
  ]
}

verify_token_schema = {
  "type": "object",
  "properties": {
    "content": {
      "type": "object",
      "properties": {
        "userName": { "type": "string" },
        "email": { "type": "string" },
        "firstName": { "type": "string" },
        "lastName": { "type": "string" },
        "lastLogon": { "type": "string" },
        "authToken": { "type": "string" },
        "simpleToken": { "type": "string" },
        "expiresIn": { "type": "integer" },
        "changePassword": { "type": "boolean" },
        "firstLogin": { "type": "boolean" }
      },
      "required": [
        "userName",
        "email",
        "firstName",
        "lastName",
        "lastLogon",
        "authToken",
        "simpleToken",
        "expiresIn",
        "changePassword",
        "firstLogin"
      ]
    },
    "errorList": { "type": "object" },
    "successList": { "type": "object" },
    "warningList": { "type": "object" },
    "success": { "type": "boolean" }
  },
  "required": ["content", "errorList", "successList", "warningList", "success"]
}

resend_validation_code_data = {
    "content": "The code was sent to your email.",
    "errorList": {},
    "successList": {},
    "warningList": {},
    "success": True
}

resend_validation_code_schema = {
  "type": "object",
  "properties": {
    "content": { "type": "string" },
    "errorList": { "type": "object" },
    "successList": { "type": "object" },
    "warningList": { "type": "object" },
    "success": { "type": "boolean" }
  },
  "required": ["content", "errorList", "successList", "warningList", "success"]
}

send_password_reset_email_data = None
send_password_reset_email_schema = {}

def verify_token_reset_password_payload(email,token): 
  return{
    "email": email,
    "token": token,
    "tokenProvider": "reset_password"
}

verify_token_reset_password_data = True

verify_token_reset_password_schema = {
  "type": "boolean"
}

def password_reset_payload(answer,email,password,securityQuestion,token,userFirstName,userLastName): 
   return {
	  "token": token,
	  "email": email,
	  "userFirstName": userFirstName,
	  "userLastname": userLastName,
	  "password": password,
	  "answer": answer,
	  "securityQuestion": securityQuestion
}

password_reset_schema = {}

def refresh_token_payload(token):
  return{
    "token": token
  }

refresh_token_schema = {
  "type": "object",
  "properties": {
    "content": {
      "type": "object",
      "properties": {
        "userName": {
          "type": "string",
          "description": "Nombre de usuario asociado a la cuenta."
        },
        "email": {
          "type": "string",
          "description": "Dirección de correo electrónico asociada a la cuenta."
        },
        "firstName": {
          "type": "string",
          "description": "Primer nombre del usuario."
        },
        "lastName": {
          "type": "string",
          "description": "Apellido del usuario."
        },
        "lastLogon": {
          "type": "string",
          "format": "date-time",
          "description": "Fecha y hora del último inicio de sesión en formato 'MM/DD/YYYY HH:mm:ss AM/PM'."
        },
        "authToken": {
          "type": "string",
          "description": "Token de autenticación en formato JWT (JSON Web Token)."
        },
        "simpleToken": {
          "type": "string",
          "description": "Token simplificado en formato JWT (JSON Web Token)."
        },
        "expiresIn": {
          "type": "integer",
          "description": "Tiempo en segundos hasta que el token expire."
        },
        "changePassword": {
          "type": "boolean",
          "description": "Indica si se requiere cambiar la contraseña."
        },
        "firstLogin": {
          "type": "boolean",
          "description": "Indica si es el primer inicio de sesión del usuario."
        }
      },
      "required": ["userName", "email", "firstName", "lastName", "lastLogon", "authToken", "simpleToken", "expiresIn", "changePassword", "firstLogin"]
    },
    "errorList": {
      "type": "object",
      "properties": {},
      "description": "Lista de errores, vacía si no hay errores."
    },
    "successList": {
      "type": "object",
      "properties": {},
      "description": "Lista de éxitos, vacía si no hay éxitos."
    },
    "warningList": {
      "type": "object",
      "properties": {},
      "description": "Lista de advertencias, vacía si no hay advertencias."
    },
    "success": {
      "type": "boolean",
      "description": "Indica si la operación fue exitosa."
    }
  },
  "required": ["content", "errorList", "successList", "warningList", "success"]
}

def check_password_payload(username,password): 
   return{ 
    "userName": username,
    "password": password,
    "login_p": "",
    "eService": 2
  }

check_password_data = {
    "content": True,
    "errorList": {},
    "successList": {},
    "warningList": {},
    "success": True
}  

check_password_schema = {
  "type": "object",
  "properties": {
    "content": {
      "type": "boolean"
    },
    "errorList": {
      "type": "object",
      "properties": {}
    },
    "successList": {
      "type": "object",
      "properties": {}
    },
    "warningList": {
      "type": "object",
      "properties": {}
    },
    "success": {
      "type": "boolean"
    }
  },
  "required": ["content", "errorList", "successList", "warningList", "success"]
}
