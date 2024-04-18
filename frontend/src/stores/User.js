class User {
  constructor (domainOrigin) {
    this.domain_origin = domainOrigin
    this.id = ''
    this.name = ''
    this.username = ''
    this.password = ''
    this.password_authorised = false
    this.logged_in = false
    this.session_jwt = ''
  }

  async api_register (payload) {
    console.log('In api_register')
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

    const url = this.domain_origin + '/api/users/'

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
      const api_object = await response.json()
      return api_object.new_user
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
}

export default User
