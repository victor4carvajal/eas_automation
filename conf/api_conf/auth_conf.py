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