class User {
  constructor (domainOrigin) {
    this.domainOrigin = domainOrigin
    this.id = ''
    this.name = ''
    this.username = ''
    this.loggedIn = false
    this.sessionJwt = ''
    this.latitude = ''
    this.longitude = ''
  }

  async apiRegister (payload) {
    console.log('In apiRegister')
    const new_user_credentials = {
      name: payload.name,
      username: payload.username,
      password: payload.password
    }

    console.log(new_user_credentials)

    const request_options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
        // Authorization: `Bearer ${this.user.session_jwt}`
      },
      body: JSON.stringify(new_user_credentials)
    }

    const url = this.domainOrigin + '/api/users/'

    try {
      const response = await fetch(url, request_options)
      if (!response.ok) {
        const errorData = await response.json() // Throw an error object containing both the status code and the error message
        throw {
          status: response.status,
          message: errorData.message || 'Network response was not ok'
        }
      }
      const apiObject = await response.json()
      return apiObject.new_user
    } catch (error) {
      // If the error object contains a status code, return it along with the error message
      if (error.status) {
        throw { status: error.status }
      } else {
        // Otherwise, just return the error message
        throw new Error('Failed to add user: ' + error.message)
      }
    }
  }

  async apiLogin (username, password) {
    console.log('In api_login')
    const payload = {
      username: username,
      password: password
    }

    const request_options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
        // Authorization: `Bearer ${this.user.session_jwt}`
      },
      body: JSON.stringify(payload)
    }

    const url = this.domainOrigin + '/api/auth/login'

    try {
      const response = await fetch(url, request_options)
      if (!response.ok) {
        const errorData = await response.json()
        // Throw an error object containing both the status code and the error message
        throw {
          status: response.status,
          message: errorData.message || 'Network response was not ok'
        }
      }
      const apiObject = await response.json()
      // update user details
      console.log(apiObject)
      this.id = apiObject.package.id
      this.name = apiObject.package.name
      this.username = apiObject.package.username
      this.loggedIn = true
      this.sessionJwt = apiObject.package.session_jwt

      const responsePackage = {
        status: response.status,
        message: apiObject.message
      }

      return responsePackage
    } catch (error) {
      // If the error object contains a status code, return it along with the error message
      if (error.status) {
        throw { status: error.status }
      } else {
        // Otherwise, just return the error message
        throw new Error('Failed to login')
      }
    }
  }

  async apiEditUser (editedName) {
    console.log('In api_edit_user')

    const payload = {
      edited_name: editedName
    }

    const request_options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.sessionJwt}`
      },
      body: JSON.stringify(payload)
    }

    const url = this.domainOrigin + '/api/users/'

    try {
      const response = await fetch(url, request_options)
      if (!response.ok) {
        const errorData = await response.json() // Throw an error object containing both the status code and the error message
        throw {
          status: response.status,
          message: errorData.message || 'Network response was not ok'
        }
      }
      const apiObject = await response.json()
      this.name = apiObject.user.name
      return apiObject.user
    } catch (error) {
      // If the error object contains a status code, return it along with the error message
      if (error.status) {
        throw { status: error.status }
      } else {
        // Otherwise, just return the error message
        throw new Error('Failed to edit user: ' + error.message)
      }
    }
  }

  async apiSubmitForm (category, payload) {
    console.log('In apiSubmitForm')

    const request_options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.sessionJwt}`
      },
      body: JSON.stringify(payload)
    }

    const url = this.domainOrigin + `/api/forms/${category}`

    try {
      const response = await fetch(url, request_options)
      if (!response.ok) {
        const errorData = await response.json() // Throw an error object containing both the status code and the error message
        throw {
          status: response.status,
          message: errorData.message || 'Network response was not ok'
        }
      }
      const apiObject = await response.json()
      return apiObject.form
    } catch (error) {
      // If the error object contains a status code, return it along with the error message
      if (error.status) {
        throw { status: error.status }
      } else {
        // Otherwise, just return the error message
        throw new Error('Failed to submit form: ' + error.message)
      }
    }
  }
}

export default User
