questions_data = {
    "content": [
        {
            "id": 1,
            "code": "SecurityQuestion",
            "description": "What was your first school?",
            "type": "string"
        },
        {
            "id": 4,
            "code": "SecurityQuestion",
            "description": "What's your favorite song?",
            "type": "string"
        },
        {
            "id": 5,
            "code": "SecurityQuestion",
            "description": "Which is your favorite historical figure?",
            "type": "string"
        },
        {
            "id": 6,
            "code": "SecurityQuestion",
            "description": "Where would you like to be?",
            "type": "string"
        },
        {
            "id": 7,
            "code": "SecurityQuestion",
            "description": "Name of a friend from your childhood?",
            "type": "string"
        },
        {
            "id": 8,
            "code": "SecurityQuestion",
            "description": "What city did your parents meet in?",
            "type": "string"
        },
        {
            "id": 9,
            "code": "SecurityQuestion",
            "description": "What year did you finish high school?",
            "type": "string"
        }
    ],
    "errorList": {},
    "successList": {},
    "warningList": {},
    "success": True
}
questions_schema = {
  "type": "object",
  "properties": {
    "content": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "code": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "required": ["id", "code", "description", "type"]
      }
    },
    "errorList": {
      "type": "object"
    },
    "successList": {
      "type": "object"
    },
    "warningList": {
      "type": "object"
    },
    "success": {
      "type": "boolean"
    }
  },
  "required": ["content", "errorList", "successList", "warningList", "success"]
}