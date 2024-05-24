class Maps {
  constructor (domainOrigin, user) {
    this.domainOrigin = domainOrigin
    this.user = user
  }

  async apiGetMapsSearchRequest (data) {
    console.log('In apiGetSearchRequest')

    // Iterate through categories and pull out those that have been selected
    const selectedCategories = []

    console.log(data['categories'])
    for (const category in data['categories']) {
      console.log('printing')
      console.log(category)
      if (data['categories'][category]) {
        selectedCategories.push(category.toLowerCase())
      }
    }
    console.log(selectedCategories)

    const payload = {
      categories: selectedCategories,
      dateFrom: data['dateFrom'],
      dateTo: data['dateTo'],
      searchRadiusKm: data['searchRadiusKm'],
      searchLatitude: data['latitude'],
      searchLongitude: data['longitude']
    }

    const request_options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.user.sessionJwt}`
      },
      body: JSON.stringify(payload)
    }

    const url = this.domainOrigin + '/api/maps/'

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
      return apiObject.results
    } catch (error) {
      // If the error object contains a status code, return it along with the error message
      if (error.status) {
        throw { status: error.status }
      } else {
        // Otherwise, just return the error message
        throw new Error('Failed to get search results: ' + error.message)
      }
    }
  }
}

export default Maps
