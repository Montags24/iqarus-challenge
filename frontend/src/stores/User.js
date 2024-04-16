import { reactive } from 'vue'

class User {
  constructor () {
    this.domain_origin = window.location.origin
    if (this.domain_origin.slice(-5) == ':5173') {
      this.domain_origin = this.domain_origin.replace(':5173', ':5000')
    }
    this.id = ''
    this.name = ''
    this.email = ''
    this.password = ''
    this.password_authorised = false
    this.logged_in = false
    this.session_jwt = ''
  }

  login (form_email, form_password) {
    return new Promise((resolve, reject) => {
      const mfa_jwt = localStorage.getItem('mfa_' + form_email)

      const url = this.domain_origin + '/api/auth/login'
      console.log(url)

      const data = {
        email: form_email,
        password: form_password,
        mfa_jwt: mfa_jwt
      }

      if (this.logged_in) {
        // Push user to homepage if already logged in
        this.router.push('/')
      } else {
        const request_options = {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        }

        fetch(url, request_options)
          .then(response => response.json())
          .then(api_object => {
            this.session_jwt = api_object.session_jwt
            if (api_object.rc == 0) {
              this.vue_instance.$toast.add({
                severity: 'success',
                summary: 'Success!',
                detail: api_object.message['message'],
                life: 3000
              })

              const user = api_object.user
              if (user.mfa_authorised) {
                this.id = user.id
                this.logged_in = true
                this.mfa_authorised = true
                this.mfa_secret_confirmed = true
              } else {
                this.logged_in = false
                this.mfa_authorised = false
                this.mfa_secret_confirmed = user.mfa_secret_confirmed
                this.mfa_qr_code_base64 = api_object.mfa_qr_image
              }

              if (user.password_authorised) {
                this.password_authorised = true
                this.email = user.email
                this.cc_emails = user.cc_emails
                this.name = user.name
                this.session_jwt = user.session_jwt
                this.failed_login_streak = user.failed_login_streak
                this.set_globally_visible = user.set_globally_visible
                this.org_roles = user.organisation_role_list
                this.organisation_id_list = user.organisation_id_list
                this.populate_task_completer_orgs()
              } else {
                this.password_authorised = false
                this.logged_in = false
                this.email = ''
                this.cc_emails = ''
                this.name = ''
                this.id = ''
                this.failed_login_streak = ''
                this.logout()
                this.vue_instance.$toast.add({
                  severity: 'error',
                  summary: 'Error!',
                  detail: api_object.message['message'],
                  life: 3000
                })

                setTimeout(() => {
                  location.replace('/login')
                }, 5000)
              }
            } else {
              setTimeout(() => {
                location.replace('/login')
              }, 5000)
              this.vue_instance.$toast.add({
                severity: 'error',
                summary: 'Incorrect username or password',
                life: 3000
              })
            }
            resolve()
          })
          .catch(error => {
            console.log(error)
            reject(error)
          })
      }
      console.log('End of user.login()')
    })
  }

  logout () {
    // reinitialise constructor
    console.log('user is logging out...')
    this.id = ''
    this.name = ''
    this.email = ''
    this.password = ''
    this.password_authorised = false
    this.session_jwt = ''
    this.vue_instance.$router.push('/login')
  }

  api_update_user_details (user_id, user_name, user_cc_email) {
    return new Promise((resolve, reject) => {
      const payload = {
        cc_emails: user_cc_email,
        name: user_name
      }

      const request_options = {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.user.session_jwt}`
        },
        body: JSON.stringify(payload)
      }

      const url = this.domain_origin + `/api/users/${user_id}`
      fetch(url, request_options)
        .then(response => response.json())
        .then(api_object => {
          try {
            if (api_object.rc == 0) {
              resolve(api_object.message)
            } else {
              reject(new Error(api_object.message))
            }
          } catch (error) {
            reject(new Error('Failed to update user'))
          }
        })
        .catch(error => {
          reject(new Error('Failed to update user'))
        })
    })
  }
}

export const user = reactive(new User())
