import { reactive } from 'vue'

class User {
  constructor () {
    this.domain_origin = window.location.origin
    if (this.domain_origin.slice(-5) == ':5173') {
      this.domain_origin = this.domain_origin.replace(':5173', ':5000')
    }
    this.id = ''
    this.name = ''
    this.username = ''
    this.password = ''
    this.password_authorised = false
    this.logged_in = false
    this.session_jwt = ''
  }

  async api_register (name, username, password) {
    const new_user_credentials = {
      name: name,
      username: username,
      password: password
    }

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
        throw new Error(errorData.message || 'Network response was not ok')
      }
      const api_object = await response.json()
      return api_object.new_user
    } catch (error) {
      throw new Error('Failed to add user: ' + error.message)
    }
  }
}

export const user = reactive(new User())
