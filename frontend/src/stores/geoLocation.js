function checkLocationPermission () {
  if ('permissions' in navigator && 'geolocation' in navigator) {
    return navigator.permissions.query({ name: 'geolocation' }).then(function (permissionStatus) {
      if (permissionStatus.state === 'granted') {
        // Permission already granted, return a Promise resolving to the user's location
        return getLocation()
      } else {
        // Permission not granted, ask the user for permission
        return new Promise((resolve, reject) => {
          navigator.geolocation.getCurrentPosition(resolve, reject)
        })
      }
    })
  } else if ('geolocation' in navigator) {
    // Geolocation is available but permissions API is not supported
    return getLocation()
  } else {
    // Geolocation is not available
    console.error('Geolocation is not supported by this browser.')
    return Promise.reject('Geolocation is not supported by this browser.')
  }
}

function getLocation () {
  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(resolve, reject)
  })
}

export { checkLocationPermission }
